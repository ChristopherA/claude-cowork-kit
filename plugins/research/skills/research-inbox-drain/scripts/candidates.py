#!/usr/bin/env python3
"""Find notes that share distinctive words with a captured item.

Reads the notes folder, prints JSON to stdout, changes nothing.

Usage:
  candidates.py --folder PATH --text "captured item" [--limit N]
                [--skip inbox,archive]

Matches whole words, treating a plural and its singular as one word, and
ranks by how distinctive the shared words are: a word found in few files
counts for more than one found in most, and a word in a file's name counts
twice. The inbox and archive folders, hidden folders and CLAUDE.md are not
searched, so a capture never matches itself.

Output: a JSON list of {"path": ..., "matches": N, "words": [...],
"score": S}, best first. Diagnostics go to stderr. Exit 0 on success,
2 on bad arguments, 3 if the folder is unreadable.
"""

import argparse
import json
import math
import os
import re
import sys

STOP = set("""
a an the and or but if then of to in on at by for from with without into onto
is are was were be been being am do does did have has had not no yes it its
this that these those i me my we our you your he she they them his her their
as so than too very can could should would will just also about over under
what which who whom whose when where why how all any some more most other
there here out up down off again each every both such own same may might must
one two get got make made like want need really much many well still even back
now only way going thing things lot per via let
""".split())

SKIP_FILES = {"claude.md"}


def norm(w):
    """One form for a word and its plural: notes -> note, stories -> story."""
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
        return w[:-1]
    return w


def tokens(text):
    return [norm(w.strip("'-")) for w in re.findall(r"[a-z][a-z'-]{2,}", text.lower())]


def terms_of(text):
    seen = []
    for w in tokens(text):
        if w in STOP or w in seen or len(w) < 3:
            continue
        seen.append(w)
    return seen


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--folder", required=True, help="notes folder to search")
    ap.add_argument("--text", required=True, help="the captured item")
    ap.add_argument("--limit", type=int, default=5, help="max results (default 5)")
    ap.add_argument("--ext", default=".md", help="file extension to read (default .md)")
    ap.add_argument("--skip", default="inbox,archive",
                    help="top-level folders not searched (default inbox,archive)")
    args = ap.parse_args()

    if not os.path.isdir(args.folder):
        print(f"Error: not a folder: {args.folder}", file=sys.stderr)
        return 3
    terms = terms_of(args.text)
    if not terms:
        print("Error: no distinctive words in --text", file=sys.stderr)
        return 2
    skip = {s.strip().lower() for s in args.skip.split(",") if s.strip()}

    files = []
    for root, dirs, names in os.walk(args.folder):
        if os.path.relpath(root, args.folder) == ".":
            dirs[:] = [d for d in dirs if not d.startswith(".") and d.lower() not in skip]
        else:
            dirs[:] = [d for d in dirs if not d.startswith(".")]
        for name in names:
            if not name.endswith(args.ext) or name.lower() in SKIP_FILES:
                continue
            path = os.path.join(root, name)
            try:
                with open(path, "r", encoding="utf-8", errors="replace") as f:
                    body = set(tokens(f.read()))
            except OSError as e:
                print(f"skip {path}: {e}", file=sys.stderr)
                continue
            title = set(tokens(os.path.splitext(name)[0].replace("-", " ")))
            files.append((os.path.relpath(path, args.folder), body, title))

    n = len(files)
    df = {t: sum(1 for _p, body, title in files if t in body or t in title) for t in terms}
    results = []
    for rel, body, title in files:
        hit = [t for t in terms if t in body or t in title]
        if not hit:
            continue
        score = sum(math.log((n + 1) / df[t]) * (2 if t in title else 1) for t in hit)
        results.append({"path": rel, "matches": len(hit), "words": hit, "score": round(score, 2)})
    results.sort(key=lambda r: (-r["score"], -r["matches"], r["path"]))
    print(f"scanned {n} files for {len(terms)} words", file=sys.stderr)
    json.dump(results[: args.limit], sys.stdout, indent=1)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
