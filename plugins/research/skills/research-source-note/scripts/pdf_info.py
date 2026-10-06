#!/usr/bin/env python3
"""Print a PDF's metadata and opening text, and optionally write a rendition.

Reads the PDF only. Prints JSON to stdout, diagnostics to stderr. With
--rendition, also writes a markdown copy of the whole text to the path
given, with a page marker (<!-- p. N -->) at the start of every page and
a header naming the source, so quotes can be found and located later.

Text is extracted in reading order, one column after another (never
pdftotext's -layout, which sets a two-column page's columns side by side
and splits every sentence across them). Ligatures such as "fi" are
written as plain letters, so a quote typed from the page matches.
Publisher download stamps ("Downloaded from ... by <IP address> on ...")
are removed from every page, since they are not the work and often name
the reader. A publisher's cover sheet, a first or last page carrying a
download notice rather than the article, is left out of the rendition and
out of the page numbering; --cover-pages names the cover pages when the
guess is wrong. The header's "made with" line names the script and the
kit release that wrote it, so a later upgrade can find renditions made
before a fix; --version prints the release alone.

Usage:
  pdf_info.py FILE.pdf [--pages N] [--chars N]
  pdf_info.py FILE.pdf --rendition OUT.md [--first-page N] [--title T]
      [--author A] [--link URL] [--original NAME] [--retrieved YYYY-MM-DD]
      [--link-style relative|wiki] [--cover-pages auto|none|N,N]

--first-page is the number printed on the article's first page (a journal
article starting at page 1561 passes 1561), so the markers carry the
page numbers a citation uses; it defaults to 1. A cover sheet left out
before the article does not use up a number.
--link-style follows map.md: relative (the default) writes the header's
original line as ../originals/NAME, wiki writes [[NAME]].
--cover-pages: auto (the default) guesses from the first and last page,
none keeps every page, and a list of PDF page positions (1 is the first
page in the file) names them.

Output keys: file, size_bytes, pages (if known), metadata (dict of the
PDF Info fields pdfinfo reports, or what the file's /Info dictionary
holds), text (first N pages, or null), tools (which of pdfinfo,
pdftotext and pypdf were found), and with --rendition, rendition (the
path written, pages written, how many pages had no text, the PDF page
positions left out as a cover sheet, and how many stamp lines were
removed).
Exit 0 on success, 2 on bad arguments, 3 if the file is unreadable,
4 if a rendition was asked for and no text could be extracted.
"""

import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys

__version__ = "0.1.0-rc.11"  # the kit release; build.py sets it from VERSION


def run(cmd):
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired) as e:
        print(f"{cmd[0]} failed: {e}", file=sys.stderr)
        return None
    if out.returncode != 0:
        print(f"{cmd[0]} exit {out.returncode}: {out.stderr.strip()[:200]}", file=sys.stderr)
        return None
    return out.stdout


def info_from_pdfinfo(path):
    text = run(["pdfinfo", path])
    if text is None:
        return None, None
    meta, pages = {}, None
    for line in text.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k, v = k.strip(), v.strip()
        if k == "Pages":
            try:
                pages = int(v)
            except ValueError:
                pass
        elif k in ("Title", "Author", "Subject", "Keywords", "Creator", "Producer", "CreationDate", "ModDate"):
            meta[k] = v
    return meta, pages


def info_from_bytes(path):
    """Fallback: scan the raw file for /Title, /Author and friends."""
    meta = {}
    try:
        with open(path, "rb") as f:
            raw = f.read(4_000_000)
    except OSError as e:
        print(f"read failed: {e}", file=sys.stderr)
        return meta
    for key in ("Title", "Author", "Subject", "Keywords", "CreationDate", "ModDate"):
        m = re.search(rb"/" + key.encode() + rb"\s*\((.*?)\)", raw, re.S)
        if m:
            val = m.group(1).decode("latin-1", errors="replace")
            if val and not val.startswith("\xfe\xff"):
                meta[key] = val.strip()
    return meta


LIGATURES = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi",
             "\ufb04": "ffl", "\ufb05": "ft", "\ufb06": "st"}
STAMP = re.compile(r"^[ \t]*(?:this content )?downloaded (?:from|by)\b.*$"
                   r"|^[ \t]*all use subject to\b.*$", re.I | re.M)
COVER = re.compile(r"this copy is for your personal|following resources related to this article"
                   r"|your use of the jstor archive|terms and conditions of use", re.I)


def clean(text):
    """Plain letters for ligatures and no stamp lines; returns (text, stamps removed)."""
    for lig, plain in LIGATURES.items():
        text = text.replace(lig, plain)
    text, stamps = STAMP.subn("", text)
    return re.sub(r"\n{3,}", "\n\n", text), stamps


def page_texts(path, tools):
    """Every page's raw text, in order, or None when nothing can extract it."""
    if tools["pdftotext"]:
        text = run(["pdftotext", path, "-"])
        if text is not None:
            pages = text.split("\f")
            if pages and not pages[-1].strip():
                pages = pages[:-1]
            return pages
    if tools["pypdf"]:
        try:
            import pypdf
            return [pg.extract_text() or "" for pg in pypdf.PdfReader(path).pages]
        except Exception as e:  # a damaged or encrypted file
            print(f"pypdf failed: {e}", file=sys.stderr)
    return None


def cover_pages(pages, choice):
    """PDF page positions (from 1) to leave out as a publisher's cover sheet."""
    if choice == "none":
        return []
    if choice != "auto":
        return sorted({int(n) for n in choice.split(",") if n.strip()})
    ends = {1, len(pages)} if len(pages) > 1 else set()
    return sorted(n for n in ends if COVER.search(pages[n - 1]))


def write_rendition(args, meta, tools):
    pages = page_texts(args.file, tools)
    if not pages or not any(p.strip() for p in pages):
        print("no text could be extracted; the PDF may be scanned images", file=sys.stderr)
        return None
    covers = cover_pages(pages, args.cover_pages)
    for n in covers:
        print(f"PDF page {n} left out as a publisher's cover sheet; pass --cover-pages to change that",
              file=sys.stderr)
    title = args.title or meta.get("Title") or "[title from the title page]"
    author = args.author or meta.get("Author") or "[author from the title page]"
    original = args.original or os.path.basename(args.file)
    retrieved = args.retrieved or datetime.date.today().isoformat()
    head = [f"# {title}", "", f"author: {author}"]
    if args.link:
        head.append(f"link: {args.link}")
    link = f"[[{original}]]" if args.link_style == "wiki" else f"../originals/{original}"
    body, empty, stamps, number = [], 0, 0, args.first_page
    for i, raw in enumerate(pages, 1):
        if i in covers:
            continue
        text, removed = clean(raw)
        stamps += removed
        if not text.strip():
            empty += 1
        body += [f"<!-- p. {number} -->", "", text.strip(), ""]
        number += 1
    notes = ["A lossy text copy of the original, for searching and checking quotes. "
             "Cite the original, not this file. Extracted in reading order, column by column"]
    if covers:
        notes.append("the publisher's cover sheet (PDF page " + ", ".join(map(str, covers)) + ") is left out")
    if stamps:
        notes.append("publisher download stamps are removed")
    head += [f"retrieved: {retrieved}", f"original: {link}", f"made with: research pdf_info {__version__}",
             "", "; ".join(notes) + ".", ""]
    with open(args.rendition, "w", encoding="utf-8") as f:
        f.write("\n".join(head + body))
    return {"path": args.rendition, "pages": len(pages) - len(covers), "pages_without_text": empty,
            "cover_pages": covers, "stamps_removed": stamps}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    ap.add_argument("file", help="the PDF to read")
    ap.add_argument("--pages", type=int, default=3, help="pages of text to extract (default 3)")
    ap.add_argument("--chars", type=int, default=12000, help="max characters of text (default 12000)")
    ap.add_argument("--rendition", help="write a markdown rendition of the whole text here")
    ap.add_argument("--first-page", type=int, default=1, help="the page number printed on the PDF's first page")
    ap.add_argument("--title", help="the title for the rendition's header")
    ap.add_argument("--author", help="the author(s) for the rendition's header")
    ap.add_argument("--link", help="where the original came from")
    ap.add_argument("--original", help="the original's file name in originals/")
    ap.add_argument("--retrieved", help="the date the original was retrieved (default today)")
    ap.add_argument("--link-style", choices=("relative", "wiki"), default="relative",
                    help="map.md's link style, for the header's original line")
    ap.add_argument("--cover-pages", default="auto",
                    help="auto, none, or PDF page positions to leave out as a cover sheet")
    args = ap.parse_args()

    if not os.path.isfile(args.file):
        print(f"Error: not a file: {args.file}", file=sys.stderr)
        return 3
    try:
        import pypdf  # noqa: F401
        has_pypdf = True
    except ImportError:
        has_pypdf = False
    tools = {"pdfinfo": shutil.which("pdfinfo") is not None,
             "pdftotext": shutil.which("pdftotext") is not None,
             "pypdf": has_pypdf}
    result = {"file": os.path.basename(args.file),
              "size_bytes": os.path.getsize(args.file),
              "pages": None, "metadata": {}, "text": None, "tools": tools}

    meta, pages = (None, None)
    if tools["pdfinfo"]:
        meta, pages = info_from_pdfinfo(args.file)
    if meta is None:
        meta = info_from_bytes(args.file)
    result["metadata"], result["pages"] = meta, pages

    pages_text = page_texts(args.file, tools) if (tools["pdftotext"] or tools["pypdf"]) else None
    if pages_text is not None:
        result["text"] = "\f".join(clean(t)[0] for t in pages_text[: max(1, args.pages)])[: args.chars]
        if result["pages"] is None:
            result["pages"] = len(pages_text)
    else:
        print("neither pdftotext nor pypdf found; text extraction skipped", file=sys.stderr)

    status = 0
    if args.rendition:
        result["rendition"] = write_rendition(args, meta, tools)
        if result["rendition"] is None:
            status = 4

    json.dump(result, sys.stdout, indent=1, ensure_ascii=False)
    print()
    return status


if __name__ == "__main__":
    sys.exit(main())
