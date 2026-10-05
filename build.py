#!/usr/bin/env python3
"""Package the Claude Cowork Kit's plugins for Cowork.

Reads every plugin under plugins/<name>/skills/, checks each skill the way
Cowork's upload will, and writes to dist/:

  <plugin>.plugin        one plugin per directory, installed once
  <skill>.skill          each skill on its own, for a reader who wants one

Both are ZIP files. A .skill holds the skill folder as its top-level
directory, the layout the official skill-creator packager produces. A
.plugin holds the plugin tree at the ZIP root, the layout the
create-cowork-plugin skill produces.

Setup skills hand the reader the kit's own instruction blocks, so their
references/ are GENERATED here from the kit's docs (docs/, or --kit DIR)
and never edited by hand: the explainer, docs/claude-cowork-kit.md, carries
the account block, the voices and the asking convention, and each binder's
document under docs/binders/ carries that binder's blocks, so those files
stay the single source. The generated files are written IN PLACE under plugins/ and committed, because
the repository is also a Cowork marketplace: .claude-plugin/marketplace.json
at the root lists every plugin by its directory, and Cowork reads the tree
as it is. So each plugin directory carries its manifest, its README and its
setup skill's references/, all generated here; --check fails when any of
them differs from what the docs and the table below would produce,
and, in a git checkout, when any of them is untracked or differs from
HEAD: content that matches the docs but is not committed is exactly
what leaves the public listing stale after a pathspec commit.

Usage:
    python3 build.py                 generate in place, then build dist/
    python3 build.py --check         validate and detect drift, write nothing
    python3 build.py --kit DIR       read the docs from DIR instead of docs/
"""

import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLUGINS_DIR = ROOT / "plugins"
DIST = ROOT / "dist"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
DOCS_DEFAULT = ROOT / "docs"  # the explainer and binders/<name>.md
KIT_VERSION = (ROOT / "VERSION").read_text().strip()  # the one version every plugin carries
HOMEPAGE = "https://github.com/ChristopherA/claude-cowork-kit"
RELEASES = f"{HOMEPAGE}/releases"
SHARED_DOC = ROOT / "docs" / "shared.md"
TEMPLATE_SKILLS = ROOT / "template" / "skills"
BINDER_DOCS_WITH_BLOCK = ("learning", "week", "money", "health")  # docs/binders/<name>.md carries `## Project instructions`
AUTHOR = "Christopher Allen"
DESCRIPTION_LIMIT = 200  # Cowork rejects a longer description on upload
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
SKIP_DIRS = {"__pycache__", "node_modules", "evals"}
SKIP_FILES = {".DS_Store"}


# One entry per plugin directory. `setup` names the skill that receives the
# generated references listed in `references`; the reference names are keys
# of what kit_references() produces.
PLUGINS = {
    "cowork-kit": {
        "display": "CWK Core",
        "description": (
            "CWK Core, the Claude Cowork Kit's routines for any binder: a setup interview that hands back the account instructions and names the binder to install next, plus deciding, interviewing, explaining again, questions for others, a meeting pack, a transcript, confidence, premortem, postmortem, where was I, wrap-up, and a new binder."
        ),
        "keywords": ["cowork", "setup", "personal", "non-programmer", "cwk"],
        "setup": "cowork-setup",
        "doc": "docs/claude-cowork-kit.md",
        "references": ["global-instructions.md", "voices.md"],
        "readme": (
            "No plugin has to come first. Install this one when you want its routines, or start "
            "here: in a task, say `set up the kit`, and the setup skill asks a few questions, hands "
            "back the account-wide instructions to paste, and says which binder plugin to install next. The other twelve skills work in any binder."
        ),
    },
    "learn": {
        "display": "CWK Learning Binder",
        "description": (
            'Your learning binder: learn a subject, a skill or an exam on purpose, with a course plan, short lessons and quizzes, and a record of what has clicked. Part of the Claude Cowork Kit (CWK).'
        ),
        "keywords": ["learning", "study", "cowork", "tutor", "cwk"],
        "setup": "learn-setup",
        "doc": "docs/binders/learning.md",
        "references": ["learning-instructions.md", "global-instructions.md", "voices.md"],
        "readme": (
            "Each skill expects the learning binder the Claude Cowork Kit describes: a folder of "
            "materials connected in the desktop app and the Context documents mission.md, curriculum.md "
            "and progress.md, which the setup creates. Claude's Learning style is optional here: a task cannot turn it on, and the lesson skill does that work inside a task."
        ),
    },
    "week": {
        "display": "CWK Week Binder",
        "description": (
            'Your week binder: triage a pile of obligations into next actions, plan and review the week, write up a meeting, and draft a reply without sending it. Part of the Claude Cowork Kit (CWK).'
        ),
        "keywords": ["productivity", "planning", "cowork", "week", "cwk"],
        "setup": "week-setup",
        "doc": "docs/binders/week.md",
        "references": ["week-instructions.md", "global-instructions.md", "voices.md"],
        "readme": (
            "Each skill expects the week binder the Claude Cowork Kit describes: a working folder "
            "connected in the desktop app, a priorities document the setup creates, and a reviews document the "
            "review creates. Nothing here sends "
            "a message or changes a calendar; drafts are handed back."
        ),
    },
    "money": {
        "display": "CWK Money Binder",
        "description": (
            'Your money binder: summarize a statement and close each month against your categories, with account details kept out of everything that syncs. Part of the Claude Cowork Kit (CWK).'
        ),
        "keywords": ["money", "budget", "cowork", "household", "cwk"],
        "setup": "money-setup",
        "doc": "docs/binders/money.md",
        "references": ["money-instructions.md", "global-instructions.md", "voices.md"],
        "readme": (
            "Each skill expects the money binder the Claude Cowork Kit describes: statements in a "
            "connected folder that stays on the computer, and Context documents holding only categories, "
            "targets and summaries with no account details. Keep the project in the mode that asks (the kit's explainer, under The two approval modes)."
        ),
    },
    "health": {
        "display": "CWK Health Binder",
        "description": (
            'Your health binder: prepare for an appointment, record a visit, keep a weekly log, and turn an article into questions for your clinician; records, never diagnosis. Part of the Claude Cowork Kit (CWK).'
        ),
        "keywords": ["health", "medical", "cowork", "records", "cwk"],
        "setup": "health-setup",
        "doc": "docs/binders/health.md",
        "references": ["health-instructions.md", "global-instructions.md", "voices.md"],
        "readme": (
            "Each skill expects the health binder the Claude Cowork Kit describes: records in a "
            "connected folder that stays on the computer, arranged as the kit's docs/binders/health.md "
            "describes, and Context documents holding only a questions list and a bare timeline. Keep the "
            "project in the mode that asks (the kit's explainer, under The two approval modes)."
        ),
    },
    "research": {
        "display": "CWK Research Binder",
        "description": (
            'Your research binder: capture ideas anywhere, file them into notes at your desk, write source notes, and answer from what you have read. Part of the Claude Cowork Kit (CWK).'
        ),
        "keywords": ["research", "notes", "cowork", "markdown", "cwk"],
        "setup": "research-setup",
        "doc": "docs/binders/research.md",
        "references": ["research-instructions.md", "rules-template.md", "map-template.md", "voices.md", "global-instructions.md"],
        "readme": (
            "Each skill expects the research binder the Claude Cowork Kit describes: a research folder "
            "connected in the desktop app, a Context document `rules.md` with the working rules, a "
            "Context document `map.md` describing the folder, and a Context document `inbox.md` for captures. "
            "The scripts in three of its skills only read the folder; the skills write to it only on "
            "the reader's yes, and each says in its body what to do when code execution is off."
        ),
    },
}


# Text more than one skill carries word for word: each heading in docs/shared.md
# and the skills (glob under plugins/ and template/) that must carry its block.
SETUPS = [f"plugins/{n}/skills/{s['setup']}/SKILL.md" for n, s in PLUGINS.items() if n != "cowork-kit"] + ["template/skills/*-setup/SKILL.md"]
SHARED = {
    "What a task can and cannot do": SETUPS + ["plugins/cowork-kit/skills/cowork-setup/SKILL.md"],
    "Another binder's project": SETUPS,
    "Grouping the questions": SETUPS,
    "The two fields": SETUPS,
    "Hand the text back": SETUPS,
    "The account block": [g for g in SETUPS if g.startswith("plugins/")],
    "Running a script": ["plugins/research/skills/research-description-check/SKILL.md",
                         "plugins/research/skills/research-inbox-drain/SKILL.md",
                         "plugins/research/skills/research-source-note/SKILL.md"],
    "The evidence words": ["plugins/research/skills/research-source-note/SKILL.md",
                           "plugins/health/skills/health-treatment-questions/SKILL.md"],
}


FAILURES = []


def fail(msg):
    """Record a failure and go on, so one run reports every failure it can see."""
    print(f"FAIL: {msg}", file=sys.stderr)
    FAILURES.append(msg)


def stop_if_failed():
    """Exit once, after every check that could run has run."""
    if FAILURES:
        print(f"{len(FAILURES)} failure(s); nothing written", file=sys.stderr)
        sys.exit(1)


def frontmatter(path):
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        fail(f"{path}: no frontmatter")
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        key, _, value = line.partition(":")
        fm[key.strip()] = value.strip().strip('"')
    return fm


def check_skill(folder):
    skill_md = folder / "SKILL.md"
    if not skill_md.exists():
        fail(f"{folder.name}: SKILL.md missing (the file name is upper case)")
        return folder.name, 0
    fm = frontmatter(skill_md)
    extra = set(fm) - ALLOWED_KEYS
    if extra:
        fail(f"{folder.name}: frontmatter keys not allowed: {sorted(extra)}")
    name = fm.get("name", "")
    desc = fm.get("description", "")
    if name != folder.name:
        fail(f"{folder.name}: name '{name}' does not match the folder")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        fail(f"{folder.name}: name is not kebab-case")
    if not desc:
        fail(f"{folder.name}: description missing")
    if "<" in desc or ">" in desc:
        fail(f"{folder.name}: description contains angle brackets")
    if len(desc) > DESCRIPTION_LIMIT:
        fail(f"{folder.name}: description is {len(desc)} characters, limit {DESCRIPTION_LIMIT}")
    for script in (folder / "scripts").glob("*.py") if (folder / "scripts").is_dir() else []:
        try:
            compile(script.read_text(), str(script), "exec")
        except SyntaxError as e:
            fail(f"{script.relative_to(ROOT)}: does not compile: {e}")
    return name, len(desc)


def files_of(folder):
    for p in sorted(folder.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(folder)
        if any(part in SKIP_DIRS for part in rel.parts) or rel.name in SKIP_FILES or rel.suffix == ".pyc":
            continue
        yield p, rel


def fenced_block_after(text, heading_regex, source):
    """The first fenced block after the line matching heading_regex, in the doc at source."""
    m = re.search(heading_regex, text, re.M)
    if not m:
        fail(f"{source}: heading not found: {heading_regex}")
        return ""
    rest = text[m.end():]
    start = re.search(r"^```(?:markdown)?\n", rest, re.M)
    if not start:
        fail(f"{source}: no fenced block after {heading_regex}")
        return ""
    body = rest[start.end():]
    end = re.search(r"^```$", body, re.M)
    if not end:
        fail(f"{source}: unterminated fence after {heading_regex}")
        return ""
    return body[:end.start()].rstrip("\n") + "\n"


def read_doc(path):
    """The text of one kit document, or a failure naming the file."""
    if not path.exists():
        fail(f"kit document not found: {path} (pass --kit DIR, the docs directory)")
        return ""
    return path.read_text()


def stamp(source):
    return f"<!-- generated by build.py from the Claude Cowork Kit's {source}; edit that file, not this one -->\n\n"


def kit_references(docs_dir):
    """Extract every block a setup skill uses, from the kit's docs.

    The explainer carries the account instructions, the voices and the
    asking convention; docs/binders/research.md carries the project
    instructions, the working rules and the description; every other
    binder document carries its block under `## The project instructions`. A missing file or
    block fails naming the file.
    """
    docs_dir = Path(docs_dir).expanduser()
    explainer = docs_dir / "claude-cowork-kit.md"
    notes_doc = docs_dir / "binders" / "research.md"
    text = read_doc(explainer)
    notes = read_doc(notes_doc)
    explainer_rel = "docs/claude-cowork-kit.md"
    notes_rel = "docs/binders/research.md"
    block1 = fenced_block_after(text, r"^## The account instructions$", explainer_rel)
    block3a = fenced_block_after(notes, r"^## The project instructions$", notes_rel)
    block3b = fenced_block_after(notes, r"^## The working rules, ", notes_rel)
    block4 = fenced_block_after(notes, r"^## The description, ", notes_rel)
    voices = {name: fenced_block_after(text, rf"^\*\*{name}\.\*\*", explainer_rel) for name in ("Plain", "Warm", "Archivist")}
    if "[PASTE YOUR CHOSEN VOICE HERE]" not in block1:
        fail("kit: the account instructions have no voice placeholder")
    if "[FOLDER PATH ON MY COMPUTER]" in block3a:
        fail("kit: the project instructions carry the folder placeholder, which belongs in the working rules")
    if "[FOLDER PATH ON MY COMPUTER]" not in block3b:
        fail("kit: the working rules have no folder placeholder")
    if "[FULL FOLDER PATH ON MY COMPUTER]" not in block4:
        fail("kit: the description has no folder placeholder")
    binders = {}
    for name in BINDER_DOCS_WITH_BLOCK:
        rel = f"docs/binders/{name}.md"
        binders[name] = fenced_block_after(read_doc(docs_dir / "binders" / f"{name}.md"), r"^## The project instructions$", rel)
    asking = fenced_block_after(text, r"^### How Claude asks$", explainer_rel).strip()
    for skill_md in sorted(list(PLUGINS_DIR.glob("*/skills/*/SKILL.md")) + list(TEMPLATE_SKILLS.glob("*/SKILL.md"))):
        if asking not in skill_md.read_text():
            fail(f"{skill_md.relative_to(ROOT)}: does not carry the explainer's asking convention (docs/claude-cowork-kit.md, How Claude asks) word for word (## Asking)")
    check_shared_text()
    check_residue()
    check_project_sections()
    check_skills_index()
    check_research_scripts()
    for name, body in binders.items():
        if "[FOLDER PATH ON MY COMPUTER]" not in body:
            fail(f"kit: the {name} binder's block has no folder placeholder")
    refs = {f"{name}-instructions.md": stamp(f"docs/binders/{name}.md") + f"# Project instructions for the {name} binder\n\nGoes in that project's Instructions panel, with the folder path filled in.\n\n```\n" + body + "```\n"
            for name, body in binders.items()}
    refs.update({
        "global-instructions.md": stamp(explainer_rel) + "# The account instructions\n\nGoes in Settings, Account, \"Instructions for Claude\". Substitute one voice from voices.md where marked.\n\n```\n" + block1 + "```\n",
        "voices.md": stamp(explainer_rel) + "# The voices\n\nOne of these replaces the marked line in global-instructions.md.\n\n"
                     + "".join(f"## {name}\n\n```\n{body}```\n\n" for name, body in voices.items()),
        "research-instructions.md": stamp(notes_rel) + "# The project instructions\n\nGoes in the project's Instructions panel, not the description. Nothing to fill in.\n\n```\n" + block3a + "```\n",
        "rules-template.md": stamp(notes_rel) + "# The working rules\n\nCreated as the Context document rules.md, with the folder path filled in.\n\n```markdown\n" + block3b + "```\n",
        "map-template.md": stamp(notes_rel) + "# The description\n\nCreated as the Context document map.md, every bracket filled.\n\n```markdown\n" + block4 + "```\n",
    })
    return refs


CONTEXT_DOCUMENTS = {  # each binder plugin's setup Context documents, which every one of its other skills must name
    "research": ["rules.md", "map.md", "inbox.md"],
    "learn": ["mission.md", "curriculum.md", "progress.md"],
    "week": ["priorities.md"],
    "money": ["categories.md", "targets.md"],
    "health": ["questions.md", "timeline.md"],
}


def check_project_sections():
    """Every non-setup skill of a binder plugin says where it runs and names its Context documents.

    Plugins installed under Customize reach every project, so a skill that does
    not check its project writes into whatever folder is connected.
    """
    for plugin, docs in CONTEXT_DOCUMENTS.items():
        for skill_md in sorted((PLUGINS_DIR / plugin / "skills").glob("*/SKILL.md")):
            if skill_md.parent.name.endswith("-setup"):
                continue
            text = skill_md.read_text()
            if "## Where this runs" not in text:
                fail(f"{skill_md.relative_to(ROOT)}: no '## Where this runs' section (the project check)")
            if not any(f"`{d}`" in text for d in docs):
                fail(f"{skill_md.relative_to(ROOT)}: names none of the {plugin} binder's Context documents {docs}")


SKILLS_INDEX = ROOT / "docs" / "skills.md"


def check_skills_index():
    """docs/skills.md lists every skill under its plugin with the description its SKILL.md carries.

    A missing skill, a listed skill that no longer exists, and a description
    that drifted each fail by name, so the public index cannot go stale.
    The README names every skill too, in a line of its own words, so a new
    skill cannot ship without one.
    """
    if not SKILLS_INDEX.exists():
        fail(f"{SKILLS_INDEX.relative_to(ROOT)}: missing (the public skills index)")
        return
    lines = SKILLS_INDEX.read_text().splitlines()
    listed = {}
    for i, line in enumerate(lines):
        m = re.fullmatch(r"### `([a-z0-9-]+)`", line)
        if m:
            after = [l for l in lines[i + 1:i + 4] if l.strip()]
            listed[m.group(1)] = after[0] if after else ""
    expected = set()
    for name, spec in PLUGINS.items():
        heading = f"## {spec['display']}, `{name}`"
        if heading not in lines:
            fail(f"docs/skills.md: no heading '{heading}'")
        for folder in plugin_skills(name):
            fm = frontmatter(folder / "SKILL.md")
            expected.add(fm.get("name"))
            if fm.get("name") not in listed:
                fail(f"docs/skills.md: {fm.get('name')} ({name}) is not listed")
            elif listed[fm["name"]] != fm["description"]:
                fail(f"docs/skills.md: {fm['name']}'s description differs from its SKILL.md")
    for stale in sorted(set(listed) - expected):
        fail(f"docs/skills.md: lists {stale}, which no plugin carries")
    readme = (ROOT / "README.md").read_text()
    for skill in sorted(expected):
        if f"`{skill}`" not in readme:
            fail(f"README.md: {skill} has no line under What is in the kit")


RESIDUE = re.compile(r"\\[0-9n]")


def check_research_scripts():
    """Run the research plugin's scripts on the fixture and compare with what it was built to show.

    The fixture's compound source carries two quotes that must pass the quote
    check against its rendition, and a copy with one word changed must fail;
    the census must find the planted lead-only folder and the two topic notes
    that cite no source; every fixture source note's citation line must be
    the one cite.py makes from its fields, and its BibTeX and CSL must hold
    one entry per note.
    A script that breaks then fails the build instead of reaching a reader.
    """
    scripts = PLUGINS_DIR / "research" / "skills"
    folder = ROOT / "tests" / "fixture" / "research-folder"
    name = "example-2024-notes-that-last"
    note = folder / "sources" / name / f"{name}.md"
    rendition = folder / "sources" / name / "renditions" / f"{name}.md"
    quote_check = scripts / "research-source-note" / "scripts" / "quote_check.py"
    census = scripts / "research-description-check" / "scripts" / "census.py"

    def run(args):
        return subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True)

    out = run([quote_check, "--note", note, "--rendition", rendition])
    if out.returncode != 0:
        fail(f"quote_check.py: the fixture's quotes do not pass (exit {out.returncode}): {out.stdout[-300:]}{out.stderr[-300:]}")
    altered = ROOT / "dist" / "quote-check-control.md"
    altered.parent.mkdir(exist_ok=True)
    altered.write_text(note.read_text().replace("has no reader but its author", "has no reader except its author"))
    out = run([quote_check, "--note", altered, "--rendition", rendition])
    altered.unlink()
    if out.returncode != 1:
        fail(f"quote_check.py: a quote with one word changed was not caught (exit {out.returncode})")

    out = run([census, "--folder", folder])
    try:
        report = json.loads(out.stdout)
        sources, topics = report["sources"], report["topics"]
    except (ValueError, KeyError):
        fail(f"census.py: no sources report from the fixture (exit {out.returncode}): {out.stderr[-300:]}")
        return
    want = {"lead_only": ["sources/simon-1971-designing-organizations"],
            "uncited": [],
            "no_lead": [], "no_rendition": [], "level_mismatch": []}
    for key, value in want.items():
        if sources.get(key) != value:
            fail(f"census.py: on the fixture, sources.{key} is {sources.get(key)!r}, expected {value!r}")
    cite = scripts / "research-source-note" / "scripts" / "cite.py"
    notes = sorted(p for p in (folder / "sources").rglob("*.md") if "renditions" not in p.parts)
    out = run([cite, *notes, "--check"])
    if out.returncode != 0:
        fail(f"cite.py: a fixture note's citation line differs from its fields (exit {out.returncode}): {out.stdout[-400:]}{out.stderr[-200:]}")
    out = run([cite, *notes, "--style", "csl"])
    try:
        if len(json.loads(out.stdout)) != len(notes):
            fail("cite.py: the CSL JSON does not hold one item per fixture note")
    except ValueError:
        fail(f"cite.py: the CSL JSON does not parse: {out.stderr[-200:]}")
    out = run([cite, *notes, "--style", "bibtex"])
    if out.stdout.count("\n@") + out.stdout.startswith("@") != len(notes):
        fail("cite.py: the BibTeX does not hold one entry per fixture note")
    altered = ROOT / "dist" / "cite-control.md"
    altered.write_text(notes[0].read_text().replace("year: ", "year: 1", 1))
    out = run([cite, altered, "--check"])
    altered.unlink()
    if out.returncode != 1:
        fail(f"cite.py: a note whose year field disagrees with its line was not caught (exit {out.returncode})")

    prose = scripts / "research-source-note" / "scripts" / "prose_check.py"
    for note in notes:
        out = run([prose, note])
        if out.returncode != 0:
            fail(f"prose_check.py: {note.relative_to(ROOT)} has prose errors: {out.stdout[-400:]}")
    altered = ROOT / "dist" / "prose-control.md"
    altered.write_text("created: 2026-10-05\nlevel: minimal\n\nBRIEF\n\nThis seminal paper offers a comprehensive account that we found useful for every reader in the field today.\n")
    out = run([prose, altered])
    altered.unlink()
    if out.returncode != 1:
        fail(f"prose_check.py: a brief with an unsupported 'seminal' and a 'we' was not caught (exit {out.returncode})")

    expected = ["topics/Reading.md", "topics/how-a-note-should-open.md"]
    if topics.get("cite_nothing") != expected:
        fail(f"census.py: on the fixture, topics.cite_nothing is {topics.get('cite_nothing')!r}, expected {expected!r}")


def check_residue():
    """No skill or doc carries what a scripted edit leaves behind.

    A regex replacement that writes its backreference or an escaped newline
    literally, `\\1` or `\\n` in running text, reads as a stray character to a
    person and as a broken instruction to Claude, and every other check passes
    it. Fenced blocks and inline code are skipped, since code, and text
    naming the residue, may carry either legitimately.
    """
    docs = [p for p in ROOT.glob("*.md")] + list((ROOT / "docs").rglob("*.md"))
    skills = list(PLUGINS_DIR.rglob("*.md")) + list(TEMPLATE_SKILLS.parent.rglob("*.md"))
    for path in sorted(set(docs + skills)):
        inside = False
        for n, line in enumerate(path.read_text().splitlines(), 1):
            if line.startswith("```"):
                inside = not inside
                continue
            if not inside and RESIDUE.search(re.sub(r"`[^`]*`", "", line)):
                fail(f"{path.relative_to(ROOT)}:{n}: a literal backreference or escaped newline outside a code fence, left by a scripted edit")


def check_shared_text():
    """Every skill listed for a block in docs/shared.md carries it word for word."""
    if not SHARED_DOC.exists():
        fail(f"shared text not found: {SHARED_DOC.relative_to(ROOT)}")
        return
    shared = SHARED_DOC.read_text()
    for heading, globs in SHARED.items():
        block = fenced_block_after(shared, rf"^## {re.escape(heading)}$", "docs/shared.md").strip()
        files = sorted(p for g in globs for p in ROOT.glob(g))
        if not files:
            fail(f"shared.md: no skill matches {globs} for '{heading}'")
        for skill_md in files:
            if block not in skill_md.read_text():
                fail(f"{skill_md.relative_to(ROOT)}: does not carry docs/shared.md's '{heading}' word for word")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def plugin_skills(name):
    skills_dir = PLUGINS_DIR / name / "skills"
    if not skills_dir.is_dir():
        fail(f"plugins/{name}/skills/ missing")
        return []
    skills = sorted(d for d in skills_dir.iterdir() if d.is_dir() and not d.name.startswith("."))
    if not skills:
        fail(f"no skill folders under plugins/{name}/skills/")
    return skills


def generated_files(refs):
    """Every generated path under the tree, mapped to its content."""
    out = {}
    listing = []
    for name, spec in PLUGINS.items():
        plugin_dir = PLUGINS_DIR / name
        manifest = {
            "name": name,
            "version": KIT_VERSION,
            "description": spec["description"],
            "author": {"name": AUTHOR},
            "homepage": HOMEPAGE,
            "repository": HOMEPAGE,
            "license": "BSD-2-Clause-Patent",
            "keywords": spec["keywords"],
        }
        out[plugin_dir / ".claude-plugin" / "plugin.json"] = json.dumps(manifest, indent=2) + "\n"
        readme = [f"# {name}", "", spec["description"], "", spec["readme"], "", f"Version {KIT_VERSION} of the Claude Cowork Kit; every plugin in a release carries the kit's version, and the releases are at {RELEASES}.", "", "## Skills", ""]
        for folder in plugin_skills(name):
            fm = frontmatter(folder / "SKILL.md")
            readme.append(f"- `{fm['name']}`: {fm['description']}")
        readme += ["", "## Install", "",
                   f"In the Claude desktop app, under Customize, Plugins: install it from the marketplace `ChristopherA/claude-cowork-kit`, or upload `{name}.plugin` from a release, then turn it on. The repository's README, Install, has both paths in full and what not to do; `{spec['doc']}` there has the setup and the text this plugin's setup hands back.", ""]
        out[plugin_dir / "README.md"] = "\n".join(readme)
        for ref in spec["references"]:
            out[plugin_dir / "skills" / spec["setup"] / "references" / ref] = refs[ref]
        listing.append({
            "name": name,
            "displayName": spec["display"],
            "description": spec["description"],
            "version": KIT_VERSION,
            "source": f"./plugins/{name}",
        })
    marketplace = {
        "name": "claude-cowork-kit",
        "owner": {"name": AUTHOR},
        "metadata": {"description": "Plugins for people who use Claude Cowork rather than Claude Code, with the reasoning explained beside them."},
        "plugins": listing,
    }
    out[MARKETPLACE] = json.dumps(marketplace, indent=2) + "\n"
    return out


def git_uncommitted(generated):
    """Generated paths that git sees as untracked or changed against HEAD.

    Returns None outside a git checkout, with a note, since a downloaded tree
    has nothing to commit; inside one, every path whose porcelain status is
    not clean, as (status, path) pairs. The content check runs first, so a
    hit here is a file that is right on disk and wrong in the listing.
    """
    rels = [str(p.relative_to(ROOT)) for p in generated]
    try:
        run = subprocess.run(
            ["git", "-C", str(ROOT), "status", "--porcelain", "--untracked-files=all", "--"] + rels,
            capture_output=True, text=True, check=False)
    except FileNotFoundError:
        print("note  git not found; the committed-state check is skipped")
        return None
    if run.returncode != 0:
        print("note  not a git checkout; the committed-state check is skipped")
        return None
    out = []
    for line in run.stdout.splitlines():
        status, rel = line[:2], line[3:]
        out.append(({"??": "untracked"}.get(status, "modified"), rel))
    return out


def build():
    if "-h" in sys.argv or "--help" in sys.argv:
        print(__doc__[__doc__.index("Usage:"):].rstrip())
        return
    unknown = [a for a in sys.argv[1:] if a.startswith("-") and a not in ("--check", "--kit")]
    if unknown:
        fail(f"unknown option {unknown[0]}; see build.py --help")
        stop_if_failed()
    on_disk = sorted(d.name for d in PLUGINS_DIR.iterdir() if d.is_dir() and not d.name.startswith("."))
    if on_disk != sorted(PLUGINS):
        fail(f"plugins/ holds {on_disk} but build.py knows {sorted(PLUGINS)}")
    checked = {}
    for name in PLUGINS:
        for folder in plugin_skills(name):
            skill, n = check_skill(folder)
            if skill in checked:
                fail(f"{skill}: the same skill name in plugins {checked[skill]} and {name}")
            checked[skill] = name
            print(f"ok  {name:12s} {skill:24s} description {n:3d} chars")
    docs = DOCS_DEFAULT
    if "--kit" in sys.argv:
        docs = Path(sys.argv[sys.argv.index("--kit") + 1])
    refs = kit_references(docs)
    print(f"ok  references from the docs: {', '.join(sorted(refs))}")
    for name, spec in PLUGINS.items():
        if spec["setup"] not in checked or checked[spec["setup"]] != name:
            fail(f"{name}: setup skill {spec['setup']} is not among its skills")
        missing = [r for r in spec["references"] if r not in refs]
        if missing:
            fail(f"{name}: unknown references {missing}")
    stop_if_failed()
    generated = generated_files(refs)
    stale = [p for p in generated if not p.exists() or p.read_text() != generated[p]]
    stray = [p for p in PLUGINS_DIR.glob("*/skills/*/references/*") if p not in generated]
    if "--check" in sys.argv:
        if stale or stray:
            for p in stale:
                print(f"drift  {p.relative_to(ROOT)}", file=sys.stderr)
            for p in stray:
                print(f"stray  {p.relative_to(ROOT)}", file=sys.stderr)
            fail("generated files differ from the docs; run build.py and commit the result")
        uncommitted = git_uncommitted(generated)
        if uncommitted:
            for status, rel in uncommitted:
                print(f"{status:6s} {rel}", file=sys.stderr)
            fail("generated files are not committed; git add them and commit before the push")
        stop_if_failed()
        state = "current" if uncommitted is None else "current and committed"
        print(f"{len(checked)} skills in {len(PLUGINS)} plugins valid; generated files {state}; nothing written")
        return
    for p in stray:
        p.unlink()
    for p, content in generated.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
    print(f"ok  {len(generated)} generated files written in place ({len(stale)} changed, {len(stray)} stray removed)")

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    for name in PLUGINS:
        plugin_dir = PLUGINS_DIR / name
        plugin_zip = DIST / f"{name}.plugin"
        with zipfile.ZipFile(plugin_zip, "w", zipfile.ZIP_DEFLATED) as z:
            for src, rel in files_of(plugin_dir):
                z.write(src, str(rel))
            z.write(ROOT / "LICENSE", "LICENSE")
        print(f"\nwrote {plugin_zip.relative_to(ROOT)}  {plugin_zip.stat().st_size} bytes  sha256 {sha256(plugin_zip)}")
        for folder in plugin_skills(name):
            skill_zip = DIST / f"{folder.name}.skill"
            with zipfile.ZipFile(skill_zip, "w", zipfile.ZIP_DEFLATED) as z:
                for src, rel in files_of(folder):
                    z.write(src, str(Path(folder.name) / rel))
                z.write(ROOT / "LICENSE", str(Path(folder.name) / "LICENSE"))
            print(f"wrote {skill_zip.relative_to(ROOT)}  {skill_zip.stat().st_size} bytes  sha256 {sha256(skill_zip)}")


if __name__ == "__main__":
    build()
