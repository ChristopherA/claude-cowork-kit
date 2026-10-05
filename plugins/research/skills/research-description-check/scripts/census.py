#!/usr/bin/env python3
"""Census of a notes folder, for comparing against its description.

Reads only. Prints JSON to stdout, diagnostics to stderr.

Usage:
  census.py --folder PATH [--limit N] [--ext .md] [--sources sources] [--topics topics]
      [--works works] [--folders inbox,sources,topics,...]

--folders is the list of top-level folders map.md names; the census then
reports which of them are missing and which top-level folders it does
not name (such as a "Claude outputs" folder the app made). map.md is a
Context document, not a file in the folder, so the script cannot read
it; whoever runs the script passes the list.

Output keys:
  folders: {relative folder: {"files": N, "md": N}}
  naming: {relative folder: {"pattern": "kebab|spaces|mixed|other", "sample": [...]}}
  metadata: {"with_created": N, "with_source": N, "without_created": [...]}
    (with_source counts a source line, or a source note's level line)
  wrapping: {"hard_wrapped": N, "unwrapped": N, "hard_wrapped_files": [...]}
  links: {"relative_markdown": N, "wikilinks": N, "urls": N}
  newest, oldest: [{"path", "mtime", "created"}] by modification time
    (mtime is unreliable on a mounted folder; prefer created)
  created_range: {"earliest", "latest"} from created lines
  sources: the source notes, checked against the binder's conventions:
    flat, compound: how many source notes are one file, how many a folder
    no_lead: source folders without a lead file of the folder's name
    lead_only: source folders holding nothing but their lead file
    no_rendition: originals (PDF or saved web page) with no rendition
    loose_files: files in the sources folder that are not notes and sit
      outside an originals/ or renditions/ folder (a PDF beside its note)
    levels: {"citation": N, "minimal": N, "read": N, "none": N}
    level_mismatch: [{"path", "level", "problem"}] where a note's
      labeled blocks do not match its level
    uncited: source notes no note outside the sources folder links to
  topics: {"notes": N, "cite_nothing": [...]}, topic notes with no link
    to a source note or a works note (empty when the topics folder does
    not exist)
  works: {"notes": N}, the reader's own works, citable like sources
  awaiting_confirmation: {"count": N, "items": [{"path", "what"}]}, lines
    Claude drafted for the reader to confirm: a WHY SAVED inferred from
    their writing, and in a topic or works note, a passage marked
    "(Drafted by Claude from ...)"
  folders_check: {"missing": [...], "unknown": [...]} against --folders,
    or null when no list was given
Files under originals/ and renditions/ are counted in "sources", not as notes.
Exit 0 on success, 2 on bad arguments, 3 if the folder is unreadable.
"""

import argparse
import datetime
import json
import os
import re
import sys

__version__ = "0.1.0-rc.10"  # the kit release; build.py sets it from VERSION

KEYLINE = re.compile(r"^[A-Za-z][A-Za-z _-]{0,30}:\s")  # a metadata line, not prose
CREATED = re.compile(r"^\s*created:\s*(\d{4}-\d{2}-\d{2})", re.I | re.M)
SOURCE = re.compile(r"^\s*source:", re.I | re.M)
WIKI = re.compile(r"\[\[[^\]]+\]\]")
RELMD = re.compile(r"\]\((?!https?://)[^)]+\.md\)")
RELMD_TARGET = re.compile(r"\]\((?!https?://)([^)#]+\.md)(?:#[^)]*)?\)")
WIKI_TARGET = re.compile(r"\[\[([^\]|#]+)")
LEVEL = re.compile(r"^\s*level:\s*(\w+)", re.I | re.M)
LABEL = re.compile(r"^\W*(BRIEF|SHORT ABSTRACT|EVIDENCE|KEY POINTS|KEY QUOTES|INFLUENCE|WHY SAVED)\b", re.M)
ORIGINAL_EXT = (".pdf", ".html", ".htm", ".webarchive", ".mhtml")
SIDECARS = ("originals", "renditions")
INFERRED = re.compile(r"^\W*WHY SAVED\s*\(inferred", re.I | re.M)
DRAFTED = re.compile(r"\(Drafted by Claude from", re.I)
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


def level_problem(level, labels):
    """What is wrong with a source note's blocks for its level, or None."""
    summary = {"BRIEF", "SHORT ABSTRACT"}
    deep = {"KEY POINTS", "KEY QUOTES", "INFLUENCE"}
    if level == "citation" and labels - {"WHY SAVED"}:
        return "citation level but carries " + ", ".join(sorted(labels - {"WHY SAVED"}))
    if level == "minimal":
        if not summary <= labels:
            return "minimal level but lacks " + ", ".join(sorted(summary - labels))
        if labels & deep:
            return "minimal level but carries " + ", ".join(sorted(labels & deep))
    if level == "read" and not labels & deep:
        return "read level but has no KEY POINTS or KEY QUOTES"
    if level not in ("citation", "minimal", "read"):
        return f"unknown level {level!r}"
    return None


def source_census(root, sources_dir, topics_dir, works_dir, texts, limit):
    """Check the sources folder's shape and how the notes cite it."""
    out = {"flat": 0, "compound": 0, "no_lead": [], "lead_only": [], "no_rendition": [], "loose_files": [],
           "levels": {"citation": 0, "minimal": 0, "read": 0, "none": 0},
           "level_mismatch": [], "uncited": []}
    base = os.path.join(root, sources_dir)
    notes = {}  # stem -> relative path of the source note
    if os.path.isdir(base):
        for entry in sorted(os.listdir(base)):
            if entry.startswith("."):
                continue
            path = os.path.join(base, entry)
            if os.path.isfile(path) and entry.endswith(".md"):
                out["flat"] += 1
                notes[entry[:-3]] = os.path.relpath(path, root)
            elif os.path.isfile(path):
                out["loose_files"].append(os.path.relpath(path, root))
            elif os.path.isdir(path):
                out["compound"] += 1
                lead = os.path.join(path, entry + ".md")
                rel = os.path.relpath(path, root)
                if not os.path.isfile(lead):
                    out["no_lead"].append(rel)
                    continue
                notes[entry] = os.path.relpath(lead, root)
                others = [f for f in os.listdir(path) if not f.startswith(".") and f != entry + ".md"]
                out["loose_files"] += [os.path.join(rel, f) for f in sorted(others)
                                       if os.path.isfile(os.path.join(path, f)) and not f.endswith(".md")]
                beside = [f for d in SIDECARS if os.path.isdir(os.path.join(path, d))
                          for f in os.listdir(os.path.join(path, d)) if not f.startswith(".")]
                if not [o for o in others if o not in SIDECARS] and not beside:
                    out["lead_only"].append(rel)
                originals = os.path.join(path, "originals")
                if os.path.isdir(originals):
                    for f in sorted(os.listdir(originals)):
                        if f.lower().endswith(ORIGINAL_EXT):
                            stem = os.path.splitext(f)[0]
                            if not os.path.isfile(os.path.join(path, "renditions", stem + ".md")):
                                out["no_rendition"].append(os.path.join(rel, "originals", f))
    for stem, rel in notes.items():
        text = texts.get(rel, "")
        m = LEVEL.search(text[:600])
        if not m:
            out["levels"]["none"] += 1
            continue
        level = m.group(1).lower()
        out["levels"][level] = out["levels"].get(level, 0) + 1
        problem = level_problem(level, set(LABEL.findall(text)))
        if problem:
            out["level_mismatch"].append({"path": rel, "level": level, "problem": problem})

    # Works are the reader's own writing, citable like a source note.
    works = {os.path.splitext(os.path.basename(rel))[0]: rel for rel in texts
             if rel.startswith(works_dir + os.sep)}
    # Who links to which source note, from outside the sources folder.
    by_path = {os.path.normpath(rel): stem for stem, rel in notes.items()}
    by_path.update({os.path.normpath(rel): stem for stem, rel in works.items()})
    cited, topic_links = set(), {}
    for rel, text in texts.items():
        if rel.startswith(sources_dir + os.sep):
            continue
        found = set()
        for target in RELMD_TARGET.findall(text):
            resolved = os.path.normpath(os.path.join(os.path.dirname(rel), target))
            if resolved in by_path:
                found.add(by_path[resolved])
        for target in WIKI_TARGET.findall(text):
            stem = os.path.basename(target.strip())
            if stem.endswith(".md"):
                stem = stem[:-3]
            if stem in notes or stem in works:
                found.add(stem)
        cited |= found
        if rel.startswith(topics_dir + os.sep):
            topic_links[rel] = found
    out["uncited"] = sorted(notes[s] for s in notes if s not in cited)[:limit]
    topics = {"notes": len(topic_links), "cite_nothing": sorted(r for r, f in topic_links.items() if not f)[:limit]}
    for key in ("no_lead", "lead_only", "no_rendition", "loose_files", "level_mismatch"):
        out[key] = out[key][:limit]
    return out, topics, {"notes": len(works)}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    ap.add_argument("--folder", required=True)
    ap.add_argument("--limit", type=int, default=10, help="items per list (default 10)")
    ap.add_argument("--ext", default=".md")
    ap.add_argument("--sources", default="sources", help="the sources folder, relative to --folder")
    ap.add_argument("--topics", default="topics", help="the topic notes' folder, relative to --folder")
    ap.add_argument("--works", default="works", help="the reader's own works, relative to --folder")
    ap.add_argument("--folders", help="the top-level folders map.md names, comma-separated")
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
    texts = {}

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d not in SIDECARS]
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
            texts[relpath] = text
            head = text[:600]
            m = CREATED.search(head)
            created = m.group(1) if m else None
            if created:
                meta["with_created"] += 1
                created_dates.append(created)
            else:
                meta["without_created"].append(relpath)
            if SOURCE.search(head) or LEVEL.search(head):
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
    out["sources"], out["topics"], out["works"] = source_census(root, args.sources, args.topics, args.works,
                                                                texts, args.limit)
    waiting = []
    for rel, text in sorted(texts.items()):
        if INFERRED.search(text):
            waiting.append({"path": rel, "what": "WHY SAVED inferred, not yet confirmed"})
        if DRAFTED.search(text) and rel.startswith((args.topics + os.sep, args.works + os.sep)):
            waiting.append({"path": rel, "what": "drafted by Claude, not yet corrected"})
    out["awaiting_confirmation"] = {"count": len(waiting), "items": waiting[: args.limit]}
    out["folders_check"] = None
    if args.folders is not None:
        named = [f.strip().strip("/") for f in args.folders.split(",") if f.strip()]
        present = sorted(d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)) and not d.startswith("."))
        out["folders_check"] = {"missing": [f for f in named if f not in present],
                                "unknown": [d for d in present if d not in named]}
    print(f"scanned {len(files_seen)} notes in {len(folders)} folders", file=sys.stderr)
    json.dump(out, sys.stdout, indent=1)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
