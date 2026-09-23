#!/usr/bin/env python3
"""Print a PDF's metadata and, if pdftotext is available, its opening text.

Reads only. Prints JSON to stdout, diagnostics to stderr.

Usage:
  pdf_info.py FILE.pdf [--pages N] [--chars N]

Output keys: file, size_bytes, pages (if known), metadata (dict of the
PDF Info fields pdfinfo reports, or what the file's /Info dictionary
holds), text (first N pages via pdftotext, or null), tools (which of
pdfinfo and pdftotext were found).
Exit 0 on success, 2 on bad arguments, 3 if the file is unreadable.
"""

import argparse
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


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("file", help="the PDF to read")
    ap.add_argument("--pages", type=int, default=3, help="pages of text to extract (default 3)")
    ap.add_argument("--chars", type=int, default=12000, help="max characters of text (default 12000)")
    args = ap.parse_args()

    if not os.path.isfile(args.file):
        print(f"Error: not a file: {args.file}", file=sys.stderr)
        return 3
    tools = {"pdfinfo": shutil.which("pdfinfo") is not None,
             "pdftotext": shutil.which("pdftotext") is not None}
    result = {"file": os.path.basename(args.file),
              "size_bytes": os.path.getsize(args.file),
              "pages": None, "metadata": {}, "text": None, "tools": tools}

    meta, pages = (None, None)
    if tools["pdfinfo"]:
        meta, pages = info_from_pdfinfo(args.file)
    if meta is None:
        meta = info_from_bytes(args.file)
    result["metadata"], result["pages"] = meta, pages

    if tools["pdftotext"]:
        text = run(["pdftotext", "-f", "1", "-l", str(max(1, args.pages)), "-layout", args.file, "-"])
        if text is not None:
            result["text"] = text[: args.chars]
    else:
        print("pdftotext not found; text extraction skipped", file=sys.stderr)

    json.dump(result, sys.stdout, indent=1, ensure_ascii=False)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
