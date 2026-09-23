#!/usr/bin/env python3
"""Census of a notes folder, for comparing against its description.

Reads only. Prints JSON to stdout, diagnostics to stderr.

Usage:
  census.py --folder PATH [--limit N] [--ext .md]

Output keys:
  folders: {relative folder: {"files": N, "md": N}}
  naming: {relative folder: {"pattern": "kebab|spaces|mixed|other", "sample": [...]}}
  metadata: {"with_created": N, "with_source": N, "without_created": [...]}
  wrapping: {"hard_wrapped": N, "unwrapped": N, "hard_wrapped_files": [...]}
  links: {"relative_markdown": N, "wikilinks": N, "urls": N}
  newest, oldest: [{"path", "mtime", "created"}] by modification time
    (mtime is unreliable on a mounted folder; prefer created)
  created_range: {"earliest", "latest"} from created lines
Exit 0 on success, 2 on bad arguments, 3 if the folder is unreadable.
"""

import argparse
import datetime
import json
import os
import re
import sys

KEYLINE = re.compile(r"^[A-Za-z][A-Za-z _-]{0,30}:\s")  # a metadata line, not prose
CREATED = re.compile(r"^\s*created:\s*(\d{4}-\d{2}-\d{2})", re.I | re.M)
SOURCE = re.compile(r"^\s*source:", re.I | re.M)
WIKI = re.compile(r"\[\[[^\]]+\]\]")
RELMD = re.compile(r"\]\((?!https?://)[^)]+\.md\)")
URL = re.compile(r"\]\(https?://[^)]+\)")


def name_pattern(names):
    stems = [os.path.splitext(n)[0] for n in names]
    if not stems:
        return "none"
    kebab = sum(1 for s in stems if re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", s))
    spaces = sum(1 for s in stems if " " in s)
    if kebab == len(stems):
        return "kebab"
    if spaces == len(stems):
        return "spaces"
    if kebab or spaces:
        return "mixed"
    return "other"


def is_hard_wrapped(text):
    """True when a paragraph runs over several short lines that do not each end a sentence.

    One paragraph is enough: a short note wrapped by hand has only one or two.
    Sentence-per-line prose is not flagged, since every line there ends with
    punctuation; that is a different convention, not a wrap.
    """
    paragraphs, run = [], []
    for line in text.splitlines() + [""]:
        s = line.strip()
        if not s or s.startswith(("#", "-", "*", ">", "|", "```")) or s[:2].isdigit() or KEYLINE.match(s):
            if run:
                paragraphs.append(run)
            run = []
            continue
        run.append(line)
    ends = (".", "!", "?", ":", ";", ")", '"')
    for para in paragraphs:
        if len(para) >= 2 and all(len(l) < 100 for l in para) and any(not l.rstrip().endswith(ends) for l in para[:-1]):
            return True
    return False


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--folder", required=True)
    ap.add_argument("--limit", type=int, default=10, help="items per list (default 10)")
    ap.add_argument("--ext", default=".md")
    args = ap.parse_args()
    root = args.folder
    if not os.path.isdir(root):
        print(f"Error: not a folder: {root}", file=sys.stderr)
        return 3

    folders, naming, files_seen = {}, {}, []
    meta = {"with_created": 0, "with_source": 0, "without_created": []}
    wrap = {"hard_wrapped": 0, "unwrapped": 0, "hard_wrapped_files": []}
    links = {"relative_markdown": 0, "wikilinks": 0, "urls": 0}
    created_dates = []

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        rel = os.path.relpath(dirpath, root)
        rel = "." if rel == "." else rel
        md = [f for f in filenames if f.endswith(args.ext) and not f.startswith(".")]
        if rel == ".":
            md = [f for f in md if f not in ("CLAUDE.md", "README.md")]  # instructions and a readme are not notes
        folders[rel] = {"files": len([f for f in filenames if not f.startswith(".")]), "md": len(md)}
        naming[rel] = {"pattern": name_pattern(md), "sample": sorted(md)[: args.limit]}
        for name in md:
            path = os.path.join(dirpath, name)
            try:
                with open(path, "r", encoding="utf-8", errors="replace") as f:
                    text = f.read()
                mtime = os.path.getmtime(path)
            except OSError as e:
                print(f"skip {path}: {e}", file=sys.stderr)
                continue
            relpath = os.path.relpath(path, root)
            head = text[:600]
            m = CREATED.search(head)
            created = m.group(1) if m else None
            if created:
                meta["with_created"] += 1
                created_dates.append(created)
            else:
                meta["without_created"].append(relpath)
            if SOURCE.search(head):
                meta["with_source"] += 1
            if is_hard_wrapped(text):
                wrap["hard_wrapped"] += 1
                wrap["hard_wrapped_files"].append(relpath)
            else:
                wrap["unwrapped"] += 1
            links["relative_markdown"] += len(RELMD.findall(text))
            links["wikilinks"] += len(WIKI.findall(text))
            links["urls"] += len(URL.findall(text))
            files_seen.append({"path": relpath,
                               "mtime": datetime.date.fromtimestamp(mtime).isoformat(),
                               "created": created, "_m": mtime})

    files_seen.sort(key=lambda r: r["_m"])
    strip = lambda rows: [{k: v for k, v in r.items() if k != "_m"} for r in rows]
    meta["without_created"] = meta["without_created"][: args.limit]
    wrap["hard_wrapped_files"] = wrap["hard_wrapped_files"][: args.limit]
    out = {
        "folder": root,
        "notes": len(files_seen),
        "folders": folders,
        "naming": naming,
        "metadata": meta,
        "wrapping": wrap,
        "links": links,
        "newest": strip(list(reversed(files_seen[-args.limit:]))),
        "oldest": strip(files_seen[: args.limit]),
        "created_range": {"earliest": min(created_dates) if created_dates else None,
                          "latest": max(created_dates) if created_dates else None},
    }
    print(f"scanned {len(files_seen)} notes in {len(folders)} folders", file=sys.stderr)
    json.dump(out, sys.stdout, indent=1)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
