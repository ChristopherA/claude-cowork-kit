#!/usr/bin/env python3
"""Print a PDF's metadata and opening text, and optionally write a rendition.

Reads the PDF only. Prints JSON to stdout, diagnostics to stderr. With
--rendition, also writes a markdown copy of the whole text to the path
given, with a page marker (<!-- p. N -->) at the start of every page and
a header naming the source, so quotes can be found and located later.

Usage:
  pdf_info.py FILE.pdf [--pages N] [--chars N]
  pdf_info.py FILE.pdf --rendition OUT.md [--first-page N] [--title T]
      [--author A] [--link URL] [--original NAME] [--retrieved YYYY-MM-DD]

--first-page is the number printed on the PDF's first page (a journal
article starting at page 1561 passes 1561), so the markers carry the
page numbers a citation uses; it defaults to 1.

Output keys: file, size_bytes, pages (if known), metadata (dict of the
PDF Info fields pdfinfo reports, or what the file's /Info dictionary
holds), text (first N pages, or null), tools (which of pdfinfo,
pdftotext and pypdf were found), and with --rendition, rendition (the
path written, pages written, and how many pages had no text).
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


def page_texts(path, tools):
    """Every page's text, in order, or None when nothing can extract it."""
    if tools["pdftotext"]:
        text = run(["pdftotext", "-layout", path, "-"])
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


def write_rendition(args, meta, tools):
    pages = page_texts(args.file, tools)
    if not pages or not any(p.strip() for p in pages):
        print("no text could be extracted; the PDF may be scanned images", file=sys.stderr)
        return None
    title = args.title or meta.get("Title") or "[title from the title page]"
    author = args.author or meta.get("Author") or "[author from the title page]"
    original = args.original or os.path.basename(args.file)
    retrieved = args.retrieved or datetime.date.today().isoformat()
    head = [f"# {title}", "", f"author: {author}"]
    if args.link:
        head.append(f"link: {args.link}")
    head += [f"retrieved: {retrieved}",
             f"original: originals/{original}",
             "", "A lossy text copy of the original, for searching and checking quotes. "
             "Cite the original, not this file.", ""]
    body, empty = [], 0
    for i, text in enumerate(pages):
        if not text.strip():
            empty += 1
        body += [f"<!-- p. {args.first_page + i} -->", "", text.rstrip(), ""]
    with open(args.rendition, "w", encoding="utf-8") as f:
        f.write("\n".join(head + body))
    return {"path": args.rendition, "pages": len(pages), "pages_without_text": empty}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
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
        result["text"] = "\f".join(pages_text[: max(1, args.pages)])[: args.chars]
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
