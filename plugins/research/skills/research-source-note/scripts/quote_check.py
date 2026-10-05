#!/usr/bin/env python3
"""Check that every quote in a source note is in the source's rendition, on the page cited.

Reads only. Prints JSON to stdout, diagnostics to stderr.

Usage:
  quote_check.py --note NOTE.md --rendition RENDITION.md [--min-words N]

A quote is any span in double quotes (straight or curly) of at least
--min-words words (default 4) anywhere in the note. A quote may itself
quote something: inside straight quotes, curly ones are part of the
quote ("we might add “natural cooperation” as a third"), and inside
curly quotes, a balanced inner pair of curly ones is. A page cited for it
is a "(p. N)", "(pp. N-M)", "p. N" or "page N" within a few characters
after the closing quote. The rendition is the markdown copy of the
source, with a page marker <!-- p. N --> at the start of each page.

Matching forgives what extraction and typing change and nothing else:
whitespace and line breaks, a hyphen at a line break, curly against
straight quotes and apostrophes, dash forms, and an ellipsis or a
bracketed insertion in the quote, which stand for text left out or
added by the quoter. Each quote gets one status:

  ok              found word for word, and on the page cited (or no
                  page markers to check against and none cited)
  page_mismatch   found word for word, on a different page than cited
  no_page_cited   found word for word; the note cites no page though
                  the rendition has page markers
  punctuation     the words are in the rendition in this order, but the
                  punctuation, case or spelling of a word differs;
                  "found" holds the rendition's text to copy instead
  not_found       not in the rendition; "nearest" holds the closest
                  passage, which may be unrelated

Exit 0 when every quote is ok, 1 when any is not, 2 on bad arguments,
3 if a file is unreadable.
"""

import argparse
import difflib
import json
import re
import sys
import unicodedata

QUOTE = re.compile(r'"([^"\n]+?)"'                       # straight, curly quotes inside allowed
                   r'|“((?:[^“”"\n]|“[^“”\n]*”)+?)”'       # curly, a balanced curly pair inside
                   r'|[“”]([^"“”\n]+?)[“”"]')                # mismatched marks, as typed
PAGE_AFTER = re.compile(r'^[\s,.;:)]{0,3}\(?(?:pp?\.|pages?)\s*(\d+)(?:\s*[-–]\s*(\d+))?', re.I)
MARKER = re.compile(r'<!--\s*p\.\s*(\d+)\s*-->')
GAP = re.compile(r'\s*(?:\.\s?\.\s?\.|…|\[[^\]]*\])\s*')

TRANSLATE = str.maketrans({
    "‘": "'", "’": "'", "‚": "'", "‛": "'", "′": "'",
    "“": '"', "”": '"', "„": '"', "″": '"',
    "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "−": "-",
    " ": " ", "­": "", "ﬁ": "fi", "ﬂ": "fl",
})


def norm(text):
    return unicodedata.normalize("NFKC", text).translate(TRANSLATE)


def exact_form(text):
    """Whitespace collapsed; a hyphen at a line break joined."""
    text = re.sub(r"(\w)-[ \t]*\n\s*(\w)", r"\1\2", text)
    return re.sub(r"\s+", " ", text).strip()


def skeleton(text):
    """Lowercase letters and digits only, with each one's index in text."""
    chars, where = [], []
    for i, ch in enumerate(text):
        if ch.isalnum():
            chars.append(ch.lower())
            where.append(i)
    return "".join(chars), where


def page_at(markers, pos):
    page = None
    for mpos, num in markers:
        if mpos > pos:
            break
        page = num
    return page


def find_in_order(haystack, parts, start=0):
    """Find each part in order; return (first start, last end) or None."""
    first, pos = None, start
    for part in parts:
        i = haystack.find(part, pos)
        if i < 0:
            return None
        if first is None:
            first = i
        pos = i + len(part)
    return first, pos


def check(quote, cited, rendition, markers):
    q = norm(quote)
    parts_exact = [exact_form(p) for p in GAP.split(q) if exact_form(p)]
    parts_skel = [skeleton(p)[0] for p in GAP.split(q) if skeleton(p)[0]]
    r_exact = exact_form(rendition)
    r_skel, r_where = skeleton(rendition)
    loc = find_in_order(r_skel, parts_skel)
    if loc is None:
        best = difflib.SequenceMatcher(None, r_exact, exact_form(q), autojunk=False).find_longest_match(0, len(r_exact), 0, len(exact_form(q)))
        lo = max(0, best.a - 80)
        return {"status": "not_found", "nearest": r_exact[lo: best.a + best.size + 80]}
    start, end = r_where[loc[0]], r_where[loc[1] - 1] + 1
    pages = sorted({p for p in (page_at(markers, start), page_at(markers, end - 1)) if p is not None})
    found = exact_form(rendition[start:end])
    result = {"found_pages": pages}
    if find_in_order(r_exact, parts_exact) is None:
        result.update(status="punctuation", found=found)
        return result
    if not markers:
        result["status"] = "ok"
    elif cited is None:
        result["status"] = "no_page_cited"
    elif set(range(cited[0], cited[1] + 1)) & set(pages):
        result["status"] = "ok"
    else:
        result["status"] = "page_mismatch"
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--note", required=True, help="the source note")
    ap.add_argument("--rendition", required=True, help="the source's markdown rendition, with page markers")
    ap.add_argument("--min-words", type=int, default=4, help="shortest quoted span to check (default 4 words)")
    args = ap.parse_args()
    try:
        with open(args.note, encoding="utf-8") as f:
            note = f.read()
        with open(args.rendition, encoding="utf-8") as f:
            raw = f.read()
    except OSError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 3

    rendition = norm(raw)
    markers = [(m.start(), int(m.group(1))) for m in MARKER.finditer(rendition)]
    # Blank the markers in place, so a quote running across a page break
    # still matches and every position still points into the same text.
    rendition = MARKER.sub(lambda m: " " * len(m.group(0)), rendition)
    if not markers:
        print("the rendition has no page markers; pages cannot be checked", file=sys.stderr)

    results = []
    for m in QUOTE.finditer(note):
        quote = next(g for g in m.groups() if g is not None).strip()
        if len(quote.split()) < args.min_words:
            continue
        pm = PAGE_AFTER.match(note[m.end(): m.end() + 30])
        cited = None
        if pm:
            lo = int(pm.group(1))
            cited = (lo, int(pm.group(2)) if pm.group(2) else lo)
        line = note.count("\n", 0, m.start()) + 1
        entry = {"line": line, "quote": quote, "cited_page": None if cited is None else (cited[0] if cited[0] == cited[1] else list(cited))}
        entry.update(check(quote, cited, rendition, markers))
        results.append(entry)

    failed = [r for r in results if r["status"] != "ok"]
    json.dump({"quotes": len(results), "ok": len(results) - len(failed), "failed": len(failed),
               "page_markers": len(markers), "results": results}, sys.stdout, indent=1, ensure_ascii=False)
    print()
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
