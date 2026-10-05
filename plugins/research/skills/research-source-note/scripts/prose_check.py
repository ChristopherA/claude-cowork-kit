#!/usr/bin/env python3
"""Check the prose in a source note, block by block, before it is shown.

Reads only. Prints JSON to stdout, diagnostics to stderr.

Usage:
  prose_check.py NOTE.md

A source note is written in labeled blocks (BRIEF, SHORT ABSTRACT,
KEY POINTS, INFLUENCE, WHY SAVED and the rest), and each kind of block
has its own reader, length and voice, so a pattern is judged by the
block it sits in: an achievement verb opening a brief is expected, a
"we" in a short abstract is an error, and nothing inside a quote is
checked at all. Blockquotes, the KEY QUOTES block and any text in
double quotes are skipped.

Each finding has a severity: ERROR (fix before the note is filed),
WARNING (should fix) or SUGGESTION. Whether evidence beside a strong
word actually supports it, and whether a summary leads with substance
rather than framing, are judgments this script only flags for a
reader to make.

Exit 0 when there are no errors, 1 when there are, 2 on bad
arguments, 3 if the note is unreadable.
"""

import argparse
import json
import re
import sys

__version__ = "0.1.0-rc.10"  # the kit release; build.py sets it from VERSION

LABELS = ["SHORT ABSTRACT", "ABSTRACT", "BRIEF", "EVIDENCE", "KEY POINTS", "KEY QUOTES", "INFLUENCE",
          "METHODOLOGY", "WHY SAVED", "WHY THIS MATTERS", "CONTRIBUTED BY", "CURRENT THINKING",
          "SOURCES", "OPEN QUESTIONS", "WRITTEN UP"]
LABEL_LINE = re.compile(r"^\W*(" + "|".join(re.escape(l) for l in LABELS) + r")\b(\s*\([^)]*\))?\W*(.*)$")

# Words that claim weight: each needs evidence in the same note (G1).
STRONG = {
    "highly cited": "about 200 or more citations",
    "frequently cited": "tens of documented citations, with their date and source",
    "influential": "about 200 or more citations, or adoption across more than one community",
    "widely cited": "about 200 or more citations",
    "foundational": "500 or more citations and an origin point; 201 to 500 allows only 'foundational for <subdomain>'",
    "seminal": "500 or more citations and a named concept the field now uses",
    "landmark": "500 or more citations and an origin point the field recognises",
    "groundbreaking": "a documented change in the field",
    "revolutionary": "a documented change in the field",
    "revolutionized": "a documented change in the field",
    "essential": "being literally required, on a syllabus or by a standard",
}
AI_WORDS = ["delve", "delves", "crucial", "pivotal", "vital", "underscore", "underscores", "foster", "fosters",
            "tapestry", "intricate", "vibrant", "showcase", "showcases", "garner", "garners", "testament",
            "interplay", "landscape"]
AI_SOFT = ["align", "aligns", "enhance", "enhances", "emphasize", "emphasizes"]
PHRASES = [
    (r"\bnot only\b.*\bbut also\b", "'not only X but also Y': write 'X and Y'"),
    (r"\bit is (important|worth) (to note|noting) that\b", "delete 'it is important to note that' and state the point"),
    (r"\bplays an? (crucial|key|vital|pivotal|important|central) role\b", "say what the thing actually does"),
    (r"\bserves as a testament\b", "describe the evidence instead"),
    (r"\b(could|might|may) potentially\b|\barguably perhaps\b|\bperhaps arguably\b|\bmay possibly\b", "stacked hedges: one hedge or none"),
    (r"^\s*(in summary|in conclusion|overall|despite these challenges)\b", "template ending: end on the last substantive point"),
]
FIRST_PERSON = re.compile(r"\bI\b|(?i:\b(me|my|mine|we|us|our|ours)\b)")
NO_FIRST_PERSON = {"BRIEF", "SHORT ABSTRACT", "KEY POINTS", "INFLUENCE", "METHODOLOGY", "EVIDENCE"}
LENGTHS = {"BRIEF": (20, 30), "SHORT ABSTRACT": (50, 75), "INFLUENCE": (60, 80), "METHODOLOGY": (60, 80), "ABSTRACT": (200, 250)}
SENTENCES = {"BRIEF": (1, 1), "SHORT ABSTRACT": (3, 4), "INFLUENCE": (2, 3)}
SIGNIFICANCE_OPENER = re.compile(r"^(this|the)\s+(\w+\s+){0,2}(paper|article|book|work|study|essay|report|post)\s+(is|was|provides|offers|presents|represents)\b", re.I)
DATED_COUNT = re.compile(r"\b\d[\d,]*\s+citations?\b.*\b(19|20)\d\d\b|\b(19|20)\d\d\b.*\b\d[\d,]*\s+citations?\b", re.I | re.S)


def blocks(text):
    """Split a note into (label, start line, lines); text before the first label is 'HEAD'."""
    out, label, start, lines = [], "HEAD", 1, []
    for n, line in enumerate(text.splitlines(), 1):
        m = LABEL_LINE.match(line)
        if m:
            out.append((label, start, lines))
            label, start, lines = m.group(1), n, []
            rest = m.group(3).strip()
            if rest:
                lines.append((n, rest))
            continue
        lines.append((n, line))
    out.append((label, start, lines))
    return out


def unquoted(line):
    """The line with blockquotes and double-quoted spans removed."""
    if line.lstrip().startswith(">"):
        return ""
    return re.sub(r'["“][^"”]*["”]', " ", line)


def words(text):
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9'’-]*", text)


def sentence_count(text):
    return len([s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"“])", text.strip()) if s.strip()])


def check(text):
    findings = []

    def add(sev, code, line, msg):
        findings.append({"severity": sev, "check": code, "line": line, "message": msg})

    whole = "\n".join(unquoted(l) for l in text.splitlines())
    has_dated_count = bool(DATED_COUNT.search(whole))
    adoption = bool(re.search(r"\badopted by\b|\badoption\b|\bused by\b|\bstandard(ised|ized)? (by|in)\b", whole, re.I))
    for label, start, lines in blocks(text):
        if label in ("KEY QUOTES", "SOURCES", "WRITTEN UP"):
            continue
        body_lines = [(n, unquoted(l)) for n, l in lines]
        body = " ".join(l.strip() for _, l in body_lines if l.strip())
        for n, line in body_lines:
            low = line.lower()
            if not line.strip() or (label == "HEAD" and re.match(r"^\s*[A-Za-z][\w -]*:\s", line)):
                continue
            if label == "HEAD" and line.lstrip().startswith("* _**"):
                if re.search(r"\b(important|influential|seminal|foundational|groundbreaking|excellent|key)\b", low):
                    add("ERROR", "C1", n, "the citation line carries an evaluation; it is data only")
                continue
            for word, need in STRONG.items():
                if re.search(r"\b" + re.escape(word) + r"\b", low):
                    if word == "foundational" and re.search(r"foundational for\b", low):
                        need = "201 to 500 citations in that subdomain"
                    if not (has_dated_count or (adoption and word in ("influential", "essential"))):
                        add("ERROR", "G1", n, f"'{word}' needs {need}, stated with its date and source in this note; otherwise describe what the work does")
                    else:
                        add("SUGGESTION", "G1", n, f"'{word}' has evidence nearby; confirm it meets {need}")
            if re.search(r"\bcomprehensive\b", low):
                add("ERROR", "G1", n, "'comprehensive' as an adjective: state the scope instead")
            for w in AI_WORDS:
                if re.search(r"\b" + w + r"\b", low):
                    sev = "ERROR" if label == "SHORT ABSTRACT" else "WARNING"
                    add(sev, "G2", n, f"'{w}': use a plain word (show, enable, examine, complex)")
            for w in AI_SOFT:
                if re.search(r"\b" + w + r"\b", low):
                    add("SUGGESTION", "G2", n, f"'{w}' is on the lower tier of AI vocabulary")
            for pat, msg in PHRASES:
                if re.search(pat, low):
                    add("WARNING", "G3", n, msg)
            if label in NO_FIRST_PERSON and FIRST_PERSON.search(line):
                add("ERROR", "voice", n, f"first person in {label}, which is our neutral summary; the reader's judgment goes in WHY SAVED or the topic note")
            if label == "BRIEF" and re.search(r'["\u201c\u201d]', dict(lines).get(n, "")):
                add("ERROR", "C2", n, "quotation marks in BRIEF, which is our summary, not the source's words")
            if label == "KEY POINTS" and re.search(r'["“][^"”]{3,}["”]', dict(lines).get(n, "")):
                add("ERROR", "C5", n, "a quoted phrase in KEY POINTS; quotes belong in KEY QUOTES")
            if label == "KEY POINTS" and line.strip().startswith(("-", "*")) and not re.match(r"^\s*[-*]\s+\*\*[^*]+(\*\*:|:\*\*)", line):
                add("WARNING", "C5", n, "a key point opens with a bold concept name and a colon")
        openers = [l.strip().split()[0].strip(",").lower() for _, l in body_lines if l.strip() and l.strip().split()]
        for w in ("furthermore", "moreover", "additionally"):
            if label not in ("ABSTRACT",) and openers.count(w) >= 2:
                add("WARNING", "G3", start, f"'{w.capitalize()}' opens several lines in {label}")
        dashes = len(re.findall(r"—| -- ", body))
        if dashes >= 3:
            add("WARNING", "G3", start, f"{dashes} dash-joined clauses in {label}; rewrite the structure, not the glyph")
        if label in LENGTHS and body:
            lo, hi = LENGTHS[label]
            count = len(words(body))
            if not lo <= count <= hi:
                add("WARNING", "length", start, f"{label} is {count} words; it should be {lo} to {hi}")
        if label in SENTENCES and body:
            lo, hi = SENTENCES[label]
            count = sentence_count(body)
            if not lo <= count <= hi:
                add("WARNING", "length", start, f"{label} is {count} sentences; it should be {lo}" + (f" to {hi}" if hi != lo else ""))
        if label in ("BRIEF", "SHORT ABSTRACT") and body and SIGNIFICANCE_OPENER.search(body):
            add("WARNING", "G4", start, f"{label} opens on framing; lead with what the work does")
        if label == "INFLUENCE" and body and not (has_dated_count or adoption):
            add("WARNING", "C7", start, "INFLUENCE has no dated citation count or named adoption")
    order = {"ERROR": 0, "WARNING": 1, "SUGGESTION": 2}
    findings.sort(key=lambda f: (order[f["severity"]], f["line"]))
    return findings


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    ap.add_argument("note", help="the source note to check")
    args = ap.parse_args()
    try:
        with open(args.note, encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 3
    findings = check(text)
    counts = {s: sum(1 for f in findings if f["severity"] == s) for s in ("ERROR", "WARNING", "SUGGESTION")}
    json.dump({"note": args.note, **{k.lower() + "s": v for k, v in counts.items()}, "findings": findings},
              sys.stdout, indent=1, ensure_ascii=False)
    print()
    return 1 if counts["ERROR"] else 0


if __name__ == "__main__":
    sys.exit(main())
