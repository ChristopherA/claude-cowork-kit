#!/usr/bin/env python3
"""Find notes that share distinctive words with a captured item.

Reads the notes folder, prints JSON to stdout, changes nothing.

Usage:
  candidates.py --folder PATH --text "captured item" [--limit N]

Output: a JSON list of {"path": ..., "matches": N, "words": [...]},
most matches first. Diagnostics go to stderr. Exit 0 on success,
2 on bad arguments, 3 if the folder is unreadable.
"""

import argparse
import json
import os
import re
import sys

STOP = set("""
a an the and or but if then of to in on at by for from with without into onto
is are was were be been being am do does did have has had not no yes it its
this that these those i me my we our you your he she they them his her their
as so than too very can could should would will just also about over under
what which who whom whose when where why how all any some more most other
""".split())


def words(text):
    seen = []
    for w in re.findall(r"[A-Za-z][A-Za-z'-]{2,}", text.lower()):
        if w in STOP or w in seen:
            continue
        seen.append(w)
    return seen


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--folder", required=True, help="notes folder to search")
    ap.add_argument("--text", required=True, help="the captured item")
    ap.add_argument("--limit", type=int, default=5, help="max results (default 5)")
    ap.add_argument("--ext", default=".md", help="file extension to read (default .md)")
    args = ap.parse_args()

    if not os.path.isdir(args.folder):
        print(f"Error: not a folder: {args.folder}", file=sys.stderr)
        return 3
    terms = words(args.text)
    if not terms:
        print("Error: no distinctive words in --text", file=sys.stderr)
        return 2

    results = []
    scanned = 0
    for root, _dirs, files in os.walk(args.folder):
        for name in files:
            if not name.endswith(args.ext):
                continue
            path = os.path.join(root, name)
            try:
                with open(path, "r", encoding="utf-8", errors="replace") as f:
                    body = f.read().lower()
            except OSError as e:
                print(f"skip {path}: {e}", file=sys.stderr)
                continue
            scanned += 1
            hit = [t for t in terms if t in body]
            if hit:
                results.append({
                    "path": os.path.relpath(path, args.folder),
                    "matches": len(hit),
                    "words": hit,
                })
    results.sort(key=lambda r: (-r["matches"], r["path"]))
    print(f"scanned {scanned} files for {len(terms)} words", file=sys.stderr)
    json.dump(results[: args.limit], sys.stdout, indent=1)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
