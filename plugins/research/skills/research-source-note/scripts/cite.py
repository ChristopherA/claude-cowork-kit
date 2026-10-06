#!/usr/bin/env python3
"""Write citations from the structured fields at the top of source notes.

Reads only. Prints to stdout, or writes to --out; diagnostics to stderr.

Usage:
  cite.py NOTE.md [NOTE.md ...] [--style kit|apa|chicago|ieee|bibtex|csl] [--out FILE]
  cite.py NOTE.md [NOTE.md ...] --check

A source note's metadata is the run of "key: value" lines at its top,
before the first blank line. The citation fields are:

  kind       web article, blog post, journal article, review article,
             preprint, book, book chapter, report, software, microcontent
             (a social post), conference paper, working paper,
             dissertation, news article, magazine article, encyclopedia
             entry, standard (an RFC, an ISO standard), white paper,
             documentation, discussion (a forum thread), licence, talk,
             presentation, event page, fact sheet, government guidance,
             or another plain word, which the published styles treat as
             a document
  authors    "Family, Given" each, separated by semicolons; an
             organisation, or a name whose family name comes first by
             culture, is written as it is shown, without a comma
  year       YYYY, ~YYYY for an approximate year, or n.d.
  title      the work's title, in its own language
  container  the journal, site, or book a chapter appears in
  editors    for a book chapter, as authors
  volume, issue, pages, publisher, doi, isbn (the ISBN-13), url
  retrieved  YYYY-MM-DD, for an open link
  available  YYYY-MM-DD, for a paywalled link
  apa-title  optional: the title in sentence case with its proper nouns
             capitalised, when the APA style's guess is wrong

A Wikipedia article is an encyclopedia entry whose authors field is
"Wikipedia contributors", whose container is Wikipedia, whose year is
the year it was retrieved, and which carries its retrieved date, since
the page changes; APA then prints "Retrieved <date>, from <url>".

Styles: kit is the binder's own reference line; apa is APA 7, with
titles in sentence case (the first word, the first word after a colon,
acronyms and words with an inner capital keep their capitals; every
other word is lowercased, so a proper noun needs a hand check, and the
script says so on stderr whenever it changed a title); chicago
is Chicago author-date; ieee numbers the references in the order the
notes are given; bibtex and csl write a file a reference manager reads.
--check compares each note's own citation line (the first line after
the metadata that starts with "* _**") with the kit line its fields
produce, and lists the fields a note lacks.

Exit 0 on success, 1 when --check finds a difference or a note has no
fields, 2 on bad arguments, 3 if a note is unreadable.
"""

import argparse
import json
import os
import re
import sys

__version__ = "0.1.0-rc.11"  # the kit release; build.py sets it from VERSION

FIELDS = ("kind", "authors", "year", "title", "container", "editors", "volume", "issue",
          "pages", "publisher", "doi", "isbn", "url", "retrieved", "available", "apa-title")
# Kinds printed "In <container>", a part of a larger work.
IN_KINDS = {"book chapter", "chapter", "conference paper", "encyclopedia entry"}
# Kinds whose container is printed after the title as a periodical or site.
CONTAINED = {"web article", "blog post", "microcontent", "journal article", "review article", "article",
             "news article", "magazine article", "discussion", "event page"} | IN_KINDS
CSL_TYPE = {"web article": "webpage", "journal article": "article-journal", "review article": "article-journal",
            "article": "article-journal", "preprint": "article", "book": "book", "book chapter": "chapter",
            "chapter": "chapter", "report": "report", "software": "software", "blog post": "post-weblog",
            "microcontent": "post", "conference paper": "paper-conference", "working paper": "report",
            "dissertation": "thesis", "news article": "article-newspaper", "magazine article": "article-magazine",
            "encyclopedia entry": "entry-encyclopedia", "standard": "standard", "white paper": "report",
            "documentation": "document", "discussion": "post", "licence": "document", "talk": "speech",
            "presentation": "speech", "event page": "webpage", "fact sheet": "report",
            "government guidance": "report"}
BIB_TYPE = {"journal article": "article", "review article": "article", "article": "article", "book": "book",
            "book chapter": "incollection", "chapter": "incollection", "report": "techreport",
            "web article": "online", "blog post": "online", "microcontent": "online", "preprint": "unpublished",
            "software": "software", "conference paper": "inproceedings", "working paper": "techreport",
            "dissertation": "phdthesis", "news article": "article", "magazine article": "article",
            "encyclopedia entry": "incollection", "standard": "techreport", "white paper": "techreport",
            "documentation": "manual", "discussion": "online", "licence": "misc", "talk": "misc",
            "presentation": "misc", "event page": "online", "fact sheet": "techreport",
            "government guidance": "techreport"}
# The bracketed description APA 7 puts after the title of grey literature,
# and the genre or type a reference manager shows for it.
DESCRIBED = {"dissertation": "Doctoral dissertation", "working paper": "Working paper", "white paper": "White paper",
             "fact sheet": "Fact sheet", "government guidance": "Guidance", "standard": "Standard",
             "talk": "Talk", "presentation": "Presentation", "licence": "Licence", "documentation": "Documentation"}
# Kinds that carry a report number in the issue field ("24-038", "RFC 8259").
NUMBERED = {"report", "working paper", "white paper", "fact sheet", "government guidance", "standard"}
SMALL_AFTER = re.compile(r"([:?!—–]\s*)(\w)")


def read_fields(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    meta, rest = {}, text
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not line.strip():
            rest = "\n".join(lines[i:])
            break
        m = re.match(r"^([A-Za-z][A-Za-z _-]*):\s*(.*)$", line)
        if m:
            meta[m.group(1).strip().lower()] = m.group(2).strip()
    line = next((l.strip() for l in rest.splitlines() if l.strip().startswith("* _**")), None)
    meta["_line"] = line
    meta["_slug"] = os.path.splitext(os.path.basename(path))[0]
    return meta


def people(value):
    """A list of (family, given) pairs; given is None for a name kept as written."""
    out = []
    for name in (value or "").split(";"):
        name = name.strip()
        if not name:
            continue
        if "," in name:
            family, given = name.split(",", 1)
            out.append((family.strip(), given.strip()))
        else:
            out.append((name, None))
    return out


def initials(given):
    parts = re.split(r"[\s]+", given.strip())
    return " ".join("-".join(p[0] + "." for p in part.split("-") if p) for part in parts if part)


def doi_url(f):
    if f.get("doi"):
        return "https://doi.org/" + re.sub(r"^https?://(dx\.)?doi\.org/", "", f["doi"])
    return f.get("url")


def locator(f, sep_pages=", "):
    bits = []
    if f.get("volume"):
        bits.append(f["volume"] + (f"({f['issue']})" if f.get("issue") else ""))
    elif f.get("issue"):
        bits.append(f"({f['issue']})")
    if f.get("pages"):
        bits.append(f["pages"])
    return sep_pages.join(bits)


def kit(f):
    authors = people(f.get("authors"))
    names = ["; ".join((fa + ", " + gi) if gi else fa for fa, gi in authors[:3]) + "; et al."] if len(authors) > 6 \
        else ["; ".join((fa + ", " + gi) if gi else fa for fa, gi in authors)]
    ids = [f"DOI: {f['doi']}"] if f.get("doi") else []
    ids += [f"ISBN-13: {f['isbn']}"] if f.get("isbn") else []
    bracket = ", ".join([f.get("kind", "work")] + ids)
    out = f"* _**{f.get('title', '[title]')}**_ ({f.get('year', 'n.d.')}). [{bracket}]."
    if names[0]:
        out += f" _{names[0].rstrip('.')}._"
    container = f.get("container")
    if container and f.get("editors"):
        eds = people(f["editors"])
        container = "In " + "; ".join((fa + ", " + gi) if gi else fa for fa, gi in eds) + (" (eds.), " if len(eds) > 1 else " (ed.), ") + container
    where = [x for x in (container, locator(f), f.get("publisher")) if x]
    if where:
        out += " " + ", ".join(where) + "."
    if f.get("url"):
        if f.get("available"):
            out += f" Available {f['available']} from: <{f['url']}>"
        else:
            out += f" Retrieved {f.get('retrieved', '[date]')} from: <{f['url']}>"
    return out


def apa_names(authors):
    names = [f"{fa}, {initials(gi)}" if gi else fa for fa, gi in authors]
    if len(names) > 20:
        names = names[:19] + ["... " + names[-1]]
        return ", ".join(names)
    if len(names) > 1:
        return ", ".join(names[:-1]) + ", & " + names[-1]
    return names[0] if names else ""


def dash(pages):
    """A page range with an en dash, as the published styles print it."""
    return (pages or "").replace("--", "-").replace("-", "–")


def report_number(f):
    """(label, number) for a numbered report-like work, or None.

    A number that starts with its own series word ("RFC 8259") keeps it; a bare
    one takes the kind's description ("Working paper" 24-038).
    """
    if f.get("kind") not in NUMBERED or not f.get("issue"):
        return None
    m = re.match(r"^([A-Za-z][A-Za-z.]*)\s+(\S.*)$", f["issue"])
    if m:
        return m.group(1), m.group(2)
    return DESCRIBED.get(f["kind"], "Report"), f["issue"]


def number_phrase(f, apa_style=False):
    """"Working paper 24-038" or "RFC 8259"; APA writes a described kind "Working Paper No. 24-038"."""
    rn = report_number(f)
    if not rn:
        return ""
    label, number = rn
    if apa_style and (label in DESCRIBED.values() or label == "Report"):
        return f"{label.title()} No. {number}"
    return f"{label} {number}"


def is_chapter(f):
    return f.get("kind") in IN_KINDS and bool(f.get("container"))


def sentence_case(title):
    """APA's sentence case, as far as a script can tell: see the module notes."""
    words = title.split(" ")
    out = []
    for i, w in enumerate(words):
        core = re.sub(r"^\W+|\W+$", "", w)
        keep = (i == 0 or core.isupper() and len(core) > 1 or any(c.isdigit() for c in core)
                or re.search(r".[A-Z]", core))
        out.append(w if keep else w.lower())
    text = " ".join(out)
    return SMALL_AFTER.sub(lambda m: m.group(1) + m.group(2).upper(), text)


def apa_title(f):
    if f.get("apa-title"):
        return f["apa-title"]
    title = f.get("title", "")
    made = sentence_case(title)
    if made != title:
        print(f"{f['_slug']}: APA title set in sentence case; check its proper nouns, "
              "or give the right form in an apa-title field", file=sys.stderr)
    return made


def long_date(iso):
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", iso or "")
    if not m:
        return iso
    months = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
              "October", "November", "December")
    return f"{months[int(m.group(2)) - 1]} {int(m.group(3))}, {m.group(1)}"


def apa(f):
    year = f.get("year", "n.d.").lstrip("~")
    head = apa_names(people(f.get("authors")))
    title = apa_title(f)
    described = DESCRIBED.get(f.get("kind"), "")
    numbered = number_phrase(f, apa_style=True)
    publisher = f.get("publisher")
    if f.get("kind") == "dissertation" and publisher:
        described, publisher = f"{described}, {publisher}", None
    described = f" ({numbered})" if numbered else (f" [{described}]" if described else "")
    if head and not head.endswith("."):
        head += "."
    link = doi_url(f)
    if is_chapter(f):
        eds = [f"{initials(gi)} {fa}" if gi else fa for fa, gi in people(f.get("editors"))]
        ed = ", ".join(eds[:-1]) + ", & " + eds[-1] if len(eds) > 1 else (eds[0] if eds else "")
        out = f"{head} ({year}). {title}. In "
        if ed:
            out += f"{ed} ({'Eds.' if len(eds) > 1 else 'Ed.'}), "
        out += f"*{f['container']}*"
        if f.get("pages"):
            out += f" (pp. {dash(f['pages'])})"
        out += "."
        if f.get("publisher"):
            out += f" {f['publisher']}."
    elif f.get("kind") in CONTAINED and f.get("container"):
        out = f"{head} ({year}). {title}. *{f['container']}*"
        if f.get("volume"):
            out += f", *{f['volume']}*" + (f"({f['issue']})" if f.get("issue") else "")
        if f.get("pages"):
            out += f", {dash(f['pages'])}"
        out += "."
    else:
        out = f"{head} ({year}). *{title}*{described}."
        if publisher:
            out += f" {publisher}."
    out = out.lstrip()
    if link and f.get("kind") == "encyclopedia entry" and f.get("retrieved") and not f.get("doi"):
        out += f" Retrieved {long_date(f['retrieved'])}, from {link}"
    elif link:
        out += f" {link}"
    return out


def chicago_names(authors):
    names = []
    for i, (fa, gi) in enumerate(authors):
        names.append((f"{fa}, {gi}" if i == 0 else f"{gi} {fa}") if gi else fa)
    if len(names) > 10:
        names = names[:7] + ["et al."]
        return ", ".join(names)
    if len(names) > 1:
        return ", ".join(names[:-1]) + ", and " + names[-1]
    return names[0] if names else ""


def chicago(f):
    year = f.get("year", "n.d.").lstrip("~")
    head = chicago_names(people(f.get("authors"))).rstrip(".")
    link = doi_url(f)
    title = f.get("title", "")
    if is_chapter(f):
        eds = [f"{gi} {fa}" if gi else fa for fa, gi in people(f.get("editors"))]
        ed = ", ".join(eds[:-1]) + ", and " + eds[-1] if len(eds) > 1 else (eds[0] if eds else "")
        out = f"{head}. {year}. “{title}.” In *{f['container']}*"
        if ed:
            out += f", edited by {ed}"
        if f.get("pages"):
            out += f", {dash(f['pages'])}"
        out += "."
        if f.get("publisher"):
            out += f" {f['publisher']}."
    elif f.get("kind") in CONTAINED and f.get("container"):
        out = f"{head}. {year}. “{title}.” *{f['container']}*"
        if f.get("volume"):
            out += f" {f['volume']}" + (f" ({f['issue']})" if f.get("issue") else "")
        if f.get("pages"):
            out += f": {dash(f['pages'])}"
        out += "."
    else:
        out = f"{head}. {year}. *{title}*."
        if number_phrase(f):
            out += f" {number_phrase(f)}."
        if f.get("publisher"):
            out += f" {f['publisher']}."
    if link:
        out += f" {link}."
    return out


def ieee(f, n):
    names = [f"{initials(gi)} {fa}" if gi else fa for fa, gi in people(f.get("authors"))]
    if len(names) > 6:
        head = names[0] + " et al."
    elif len(names) == 2:
        head = " and ".join(names)
    elif len(names) > 1:
        head = ", ".join(names[:-1]) + ", and " + names[-1]
    else:
        head = names[0] if names else ""
    year = f.get("year", "n.d.").lstrip("~")
    title = f.get("title", "")
    if is_chapter(f):
        eds = [f"{initials(gi)} {fa}" if gi else fa for fa, gi in people(f.get("editors"))]
        out = f"[{n}] {head}, “{title},” in *{f['container']}*"
        if eds:
            out += ", " + ", ".join(eds) + (", Eds." if len(eds) > 1 else ", Ed.")
        if f.get("publisher"):
            out += f", {f['publisher']},"
        else:
            out += ","
        out += f" {year}"
        if f.get("pages"):
            out += f", pp. {dash(f['pages'])}"
    elif f.get("kind") in CONTAINED and f.get("container"):
        out = f"[{n}] {head}, “{title},” *{f['container']}*"
        if f.get("volume"):
            out += f", vol. {f['volume']}"
        if f.get("issue"):
            out += f", no. {f['issue']}"
        if f.get("pages"):
            out += f", pp. {dash(f['pages'])}"
        out += f", {year}"
    else:
        out = f"[{n}] {head}, *{title}*."
        if f.get("publisher"):
            out += f" {f['publisher']},"
        if number_phrase(f):
            out += f" {number_phrase(f)},"
        out += f" {year}"
    if f.get("doi"):
        out += f", doi: {f['doi']}."
    elif f.get("url"):
        out += f". [Online]. Available: {f['url']}"
    else:
        out += "."
    return out


def bib_escape(value):
    return value.replace("&", r"\&").replace("%", r"\%").replace("_", r"\_").replace("#", r"\#")


def bibtex(f):
    kind = BIB_TYPE.get(f.get("kind", ""), "misc")
    key = f["_slug"].replace("-", "_")
    authors = " and ".join(f"{fa}, {gi}" if gi else "{" + fa + "}" for fa, gi in people(f.get("authors")))
    entries = [("author", authors), ("title", "{" + f.get("title", "") + "}"), ("year", f.get("year", "").lstrip("~"))]
    container_key = {"article": "journal", "incollection": "booktitle", "inproceedings": "booktitle",
                     "online": "organization"}.get(kind, "howpublished")
    publisher_key = {"phdthesis": "school", "techreport": "institution", "manual": "organization"}.get(kind, "publisher")
    for field, value in ((container_key, f.get("container")), ("editor", " and ".join(f"{fa}, {gi}" if gi else fa for fa, gi in people(f.get("editors")))),
                         ("volume", f.get("volume")), ("number", report_number(f)[1] if report_number(f) else f.get("issue")), ("pages", (f.get("pages") or "").replace("-", "--")),
                         (publisher_key, f.get("publisher")), ("type", (report_number(f)[0] if report_number(f) else DESCRIBED.get(f.get("kind"))) if kind in ("techreport", "misc", "manual") else None),
                         ("doi", f.get("doi")), ("isbn", f.get("isbn")), ("url", f.get("url")),
                         ("urldate", f.get("retrieved") or f.get("available"))):
        if value:
            entries.append((field, value))
    body = ",\n".join(f"  {k} = {{{bib_escape(v) if k not in ('url', 'doi') else v}}}" for k, v in entries if v)
    return f"@{kind}{{{key},\n{body}\n}}"


def csl(f):
    item = {"id": f["_slug"], "type": CSL_TYPE.get(f.get("kind", ""), "document"), "title": f.get("title", "")}
    names = []
    for fa, gi in people(f.get("authors")):
        names.append({"family": fa, "given": gi} if gi else {"literal": fa})
    if names:
        item["author"] = names
    eds = [{"family": fa, "given": gi} if gi else {"literal": fa} for fa, gi in people(f.get("editors"))]
    if eds:
        item["editor"] = eds
    year = f.get("year", "")
    if re.fullmatch(r"~?\d{4}", year):
        item["issued"] = {"date-parts": [[int(year.lstrip("~"))]]}
        if year.startswith("~"):
            item["issued"]["circa"] = True
    if f.get("kind") in DESCRIBED:
        item["genre"] = DESCRIBED[f["kind"]]
    if report_number(f):
        item["number"] = f["issue"]
    for key, field in (("container-title", "container"), ("volume", "volume"), ("issue", "issue" if not report_number(f) else "_none"), ("page", "pages"),
                       ("publisher", "publisher"), ("DOI", "doi"), ("ISBN", "isbn"), ("URL", "url")):
        if f.get(field):
            item[key] = f[field]
    accessed = f.get("retrieved") or f.get("available")
    if accessed and re.fullmatch(r"\d{4}-\d{2}-\d{2}", accessed):
        item["accessed"] = {"date-parts": [[int(x) for x in accessed.split("-")]]}
    return item


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    ap.add_argument("notes", nargs="+", help="source notes")
    ap.add_argument("--style", default="kit", choices=("kit", "apa", "chicago", "ieee", "bibtex", "csl"))
    ap.add_argument("--out", help="write here instead of printing")
    ap.add_argument("--check", action="store_true", help="compare each note's citation line with its fields")
    args = ap.parse_args()
    notes = []
    for path in args.notes:
        try:
            notes.append(read_fields(path))
        except OSError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 3
    status = 0
    for f in notes:
        missing = [k for k in ("kind", "authors", "year", "title") if not f.get(k)]
        if missing:
            print(f"{f['_slug']}: no {', '.join(missing)} field", file=sys.stderr)
            status = 1
    if args.check:
        report = []
        for f in notes:
            made = kit(f)
            report.append({"note": f["_slug"], "matches": made == f["_line"], "line": f["_line"], "from_fields": made})
            if made != f["_line"]:
                status = 1
        json.dump(report, sys.stdout, indent=1, ensure_ascii=False)
        print()
        return status
    if args.style == "csl":
        text = json.dumps([csl(f) for f in notes], indent=1, ensure_ascii=False) + "\n"
    elif args.style == "bibtex":
        text = "\n\n".join(bibtex(f) for f in notes) + "\n"
    elif args.style == "ieee":
        text = "\n".join(ieee(f, i + 1) for i, f in enumerate(notes)) + "\n"
    elif args.style == "kit":
        text = "\n".join(kit(f) for f in notes) + "\n"
    else:
        # APA and Chicago reference lists run alphabetically by first author.
        fn = {"apa": apa, "chicago": chicago}[args.style]
        text = "\n".join(fn(f) for f in sorted(notes, key=lambda f: f.get("authors", "").lower())) + "\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
    else:
        sys.stdout.write(text)
    return status


if __name__ == "__main__":
    sys.exit(main())
