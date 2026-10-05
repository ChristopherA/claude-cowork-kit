#!/usr/bin/env python3
"""Write the fixture's invented paper as a PDF shaped like a journal article.

Real articles defeated the first rendition script in ways a plain
one-column fixture could not show, so this one carries each of them:
two columns per page, a publisher's cover sheet as the last page, a
download stamp naming an IP address on every article page (192.0.2.10,
from the range reserved for documentation), and a sentence quoting a
phrase in curly quotes. Ligatures are not here: pdftotext expands a
standard font's fi glyph itself, so build.py tests that normalisation
directly. Standard library only, so the
PDF can be rebuilt anywhere.

Usage: make-fixture-pdf.py OUT.pdf
"""

import sys

STAMP = "Downloaded from https://example.org by 192.0.2.10 on October 4, 2026."
LQ, RQ = "\\252", "\\272"  # curly double quotes

# Each page: a list of (x, y, size, text) runs, already broken into lines.
COL_L, COL_R, TOP, LEAD = 56, 316, 640, 13


def column(x, lines, top=TOP):
    return [(x, top - i * LEAD, 10, s) for i, s in enumerate(lines)]


PAGE1 = [(56, 720, 18, "Notes That Last"), (56, 698, 11, "Ada Example")] + column(COL_L, [
    "This short paper is invented for the",
    "Claude Cowork Kit's test fixture. It",
    "argues that a note survives only when a",
    "later piece of writing needs it. Notes",
    "kept for their own sake are rarely opened",
    "again, and a collection that grows",
    "without being written from becomes",
    "harder to trust with every addition.",
]) + column(COL_R, [
    "The first claim is about use. A note that",
    "no topic note cites has no reader but its",
    "author, and its author has moved on. The",
    "second claim is about cost: every note",
    "added to a pile raises the price of",
    "finding any one of them.",
]) + [(56, 40, 7, STAMP)]

PAGE2 = column(COL_L, [
    "The remedy the paper proposes is to",
    "write the synthesis first. Keep one",
    "living note for each topic, stating what",
    "you currently think, and let sources",
    "earn a fuller note only when that topic",
    "note cites them. Call this practice",
    f"{LQ}writing from{RQ} a collection rather than",
    f"{LQ}writing to{RQ} it.",
]) + column(COL_R, [
    "The paper closes with a test any reader",
    "can run: open a topic you care about",
    "and ask whether one note says what you",
    "think. If the answer is a folder of",
    "sources, the collection has been",
    "gathering rather than thinking.",
]) + [(56, 40, 7, STAMP)]

COVER = column(56, [
    "Notes That Last",
    "Ada Example, et al.",
    "Invented Journal 1, 1 (2024)",
    "This copy is for your personal, non-commercial use only.",
    "The following resources related to this article are available online.",
], top=700)


def esc(s):
    return s.replace("(", "\\(").replace(")", "\\)")


def stream(runs):
    ops = [f"BT /F1 {size} Tf {x} {y} Td ({esc(text)}) Tj ET" for x, y, size, text in runs]
    return "\n".join(ops).encode("latin-1")


def build(pages):
    objs = [b"<< /Type /Catalog /Pages 2 0 R >>", None,
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"]
    kids = []
    for runs in pages:
        body = stream(runs)
        objs.append(b"<< /Length %d >>\nstream\n" % len(body) + body + b"\nendstream")
        content = len(objs)
        objs.append(b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
                    b"/Resources << /Font << /F1 3 0 R >> >> /Contents %d 0 R >>" % content)
        kids.append(len(objs))
    objs[1] = b"<< /Type /Pages /Kids [%s] /Count %d >>" % (
        b" ".join(b"%d 0 R" % k for k in kids), len(kids))
    out, offsets = bytearray(b"%PDF-1.4\n"), []
    for n, obj in enumerate(objs, 1):
        offsets.append(len(out))
        out += b"%d 0 obj\n" % n + obj + b"\nendobj\n"
    xref = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objs) + 1)
    out += b"".join(b"%010d 00000 n \n" % o for o in offsets)
    out += b"trailer\n<< /Size %d /Root 1 0 R /Info << /Title (Notes That Last) /Author (Ada Example) >> >>\n" % (len(objs) + 1)
    out += b"startxref\n%d\n%%%%EOF\n" % xref
    return bytes(out)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__.strip().splitlines()[-1])
    with open(sys.argv[1], "wb") as f:
        f.write(build([PAGE1, PAGE2, COVER]))
