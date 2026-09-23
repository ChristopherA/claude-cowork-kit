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
the account block, the voices and the asking convention, and each project's
document under docs/projects/ carries that project's blocks, so those files
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
DOCS_DEFAULT = ROOT / "docs"  # the explainer and projects/<name>.md
KIT_VERSION = (ROOT / "VERSION").read_text().strip()  # the one version every plugin carries
RELEASES = "https://github.com/ChristopherA/claude-cowork-kit/releases"
SHARED_DOC = ROOT / "docs" / "shared.md"
TEMPLATE_SKILLS = ROOT / "template" / "skills"
PROJECT_DOCS_WITH_BLOCK = ("learning", "week", "money", "medical")  # docs/projects/<name>.md carries `## Project instructions`
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
        "display": "Cowork Kit core",
        "description": (
            "The Claude Cowork Kit's core: a setup interview that hands back the account "
            "instructions and says which project plugins to install next, plus twelve routines "
            "for any project: deciding, interviewing, explaining again, questions for others, a "
            "meeting pack, a transcript, confidence, premortem, postmortem, where was I, wrap-up, "
            "and a new project."
        ),
        "keywords": ["cowork", "setup", "personal", "non-programmer"],
        "setup": "cowork-setup",
        "doc": "docs/claude-cowork-kit.md",
        "references": ["global-instructions.md", "voices.md"],
        "readme": (
            "Install this plugin first, then start a task and say `set up the kit`. The setup "
            "skill asks a few questions, hands back the account-wide instructions to paste, and "
            "says which project plugin to install next. The other twelve skills work in any project."
        ),
    },
    "learn": {
        "display": "Learning",
        "description": (
            "Skills for the Claude Cowork Kit's learning project: set a course, run a lesson, "
            "and quiz yourself on what you have learned or read."
        ),
        "keywords": ["learning", "study", "cowork", "tutor"],
        "setup": "learn-setup",
        "doc": "docs/projects/learning.md",
        "references": ["learning-instructions.md", "global-instructions.md", "voices.md"],
        "readme": (
            "Each skill expects the learning project the Claude Cowork Kit describes: a folder of "
            "materials connected in the desktop app and the project docs mission.md, curriculum.md "
            "and progress.md, which the setup creates. Claude's Learning style is optional here: a task cannot turn it on, and the lesson skill does that work inside a task."
        ),
    },
    "week": {
        "display": "Your week",
        "description": (
            "Skills for the Claude Cowork Kit's week project: set it up, triage a pile of "
            "obligations into next actions, plan the week, review it, write up a meeting, and "
            "draft a reply without sending it."
        ),
        "keywords": ["productivity", "planning", "cowork", "week"],
        "setup": "week-setup",
        "doc": "docs/projects/week.md",
        "references": ["week-instructions.md", "global-instructions.md", "voices.md"],
        "readme": (
            "Each skill expects the week project the Claude Cowork Kit describes: a working folder "
            "connected in the desktop app, a priorities doc the setup creates, and a reviews doc the "
            "review creates. Nothing here sends "
            "a message or changes a calendar; drafts are handed back."
        ),
    },
    "money": {
        "display": "Money",
        "description": (
            "Skills for the Claude Cowork Kit's money project: set it up with the privacy floor, "
            "summarize a statement, and close a month against your categories."
        ),
        "keywords": ["money", "budget", "cowork", "household"],
        "setup": "money-setup",
        "doc": "docs/projects/money.md",
        "references": ["money-instructions.md", "global-instructions.md", "voices.md"],
        "readme": (
            "Each skill expects the money project the Claude Cowork Kit describes: statements in a "
            "connected folder that stays on the computer, and project docs holding only categories, "
            "targets and summaries with no account details. Keep the project in the mode that asks (the kit's explainer, under The two approval modes)."
        ),
    },
    "medical": {
        "display": "Medical records",
        "description": (
            "Skills for the Claude Cowork Kit's medical project: set it up, prepare a visit and its "
            "pack, record a visit into the folder, keep a weekly functional log, and turn a handed "
            "article into questions for the clinician."
        ),
        "keywords": ["medical", "health", "cowork", "records"],
        "setup": "medical-setup",
        "doc": "docs/projects/medical.md",
        "references": ["medical-instructions.md", "global-instructions.md", "voices.md"],
        "readme": (
            "Each skill expects the medical project the Claude Cowork Kit describes: records in a "
            "connected folder that stays on the computer, arranged as the kit's docs/projects/medical.md "
            "describes, and project docs holding only a questions list and a bare timeline. Keep the "
            "project in the mode that asks (the kit's explainer, under The two approval modes)."
        ),
    },
    "pkm": {
        "display": "Personal knowledge",
        "description": (
            "Skills for the Claude Cowork Kit's notes project: set the project up, drain the "
            "capture inbox, write a source note, and check the description against the folder."
        ),
        "keywords": ["personal-knowledge", "notes", "cowork", "markdown"],
        "setup": "pkm-setup",
        "doc": "docs/projects/notes.md",
        "references": ["project-instructions.md", "rules-template.md", "map-template.md", "voices.md", "global-instructions.md"],
        "readme": (
            "Each skill expects the notes project the Claude Cowork Kit describes: a notes folder "
            "connected in the desktop app, a project doc `rules.md` with the working rules, a "
            "project doc `map.md` describing the folder, and a project doc `inbox.md` for captures. "
            "The three skills with scripts read the folder only; they never write to it without "
            "the reader's yes, and each says in its body what to do when code execution is off."
        ),
    },
}


# Text more than one skill carries word for word: each heading in docs/shared.md
# and the skills (glob under plugins/ and template/) that must carry its block.
SETUPS = [f"plugins/{n}/skills/{s['setup']}/SKILL.md" for n, s in PLUGINS.items() if n != "cowork-kit"] + ["template/skills/*-setup/SKILL.md"]
SHARED = {
    "What a task can and cannot do": SETUPS + ["plugins/cowork-kit/skills/cowork-setup/SKILL.md"],
    "Grouping the questions": SETUPS,
    "The two fields": SETUPS,
    "Hand the text back": SETUPS,
    "The account block": [g for g in SETUPS if g.startswith("plugins/")],
    "Running a script": ["plugins/pkm/skills/pkm-description-check/SKILL.md",
                         "plugins/pkm/skills/pkm-inbox-drain/SKILL.md",
                         "plugins/pkm/skills/pkm-source-note/SKILL.md"],
    "The evidence words": ["plugins/pkm/skills/pkm-source-note/SKILL.md",
                           "plugins/medical/skills/medical-treatment-questions/SKILL.md"],
}


def fail(msg):
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def frontmatter(path):
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        fail(f"{path}: no frontmatter")
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
        compile(script.read_text(), str(script), "exec")
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
    rest = text[m.end():]
    start = re.search(r"^```(?:markdown)?\n", rest, re.M)
    if not start:
        fail(f"{source}: no fenced block after {heading_regex}")
    body = rest[start.end():]
    end = re.search(r"^```$", body, re.M)
    if not end:
        fail(f"{source}: unterminated fence after {heading_regex}")
    return body[:end.start()].rstrip("\n") + "\n"


def read_doc(path):
    """The text of one kit document, or a failure naming the file."""
    if not path.exists():
        fail(f"kit document not found: {path} (pass --kit DIR, the docs directory)")
    return path.read_text()


def stamp(source):
    return f"<!-- generated by build.py from the Claude Cowork Kit's {source}; edit that file, not this one -->\n\n"


def kit_references(docs_dir):
    """Extract every block a setup skill uses, from the kit's docs.

    The explainer carries Block 1, the voices and the asking convention;
    docs/projects/notes.md carries Blocks 3a, 3b and 4; every other project
    doc carries its block under `## Project instructions`. A missing file or
    block fails naming the file.
    """
    docs_dir = Path(docs_dir).expanduser()
    explainer = docs_dir / "claude-cowork-kit.md"
    notes_doc = docs_dir / "projects" / "notes.md"
    text = read_doc(explainer)
    notes = read_doc(notes_doc)
    explainer_rel = "docs/claude-cowork-kit.md"
    notes_rel = "docs/projects/notes.md"
    block1 = fenced_block_after(text, r"^## Block 1 ", explainer_rel)
    block3a = fenced_block_after(notes, r"^## Block 3a ", notes_rel)
    block3b = fenced_block_after(notes, r"^## Block 3b ", notes_rel)
    block4 = fenced_block_after(notes, r"^## Block 4 ", notes_rel)
    voices = {name: fenced_block_after(text, rf"^\*\*{name}\.\*\*", explainer_rel) for name in ("Plain", "Warm", "Archivist")}
    if "[PASTE YOUR CHOSEN VOICE HERE]" not in block1:
        fail("kit: Block 1 has no voice placeholder")
    if "[FOLDER PATH ON MY COMPUTER]" in block3a:
        fail("kit: Block 3a carries the folder placeholder, which belongs in Block 3b")
    if "[FOLDER PATH ON MY COMPUTER]" not in block3b:
        fail("kit: Block 3b has no folder placeholder")
    if "[FULL FOLDER PATH ON MY COMPUTER]" not in block4:
        fail("kit: Block 4 has no folder placeholder")
    projects = {}
    for name in PROJECT_DOCS_WITH_BLOCK:
        rel = f"docs/projects/{name}.md"
        projects[name] = fenced_block_after(read_doc(docs_dir / "projects" / f"{name}.md"), r"^## Project instructions$", rel)
    asking = fenced_block_after(text, r"^### How Claude asks$", explainer_rel).strip()
    for skill_md in sorted(list(PLUGINS_DIR.glob("*/skills/*/SKILL.md")) + list(TEMPLATE_SKILLS.glob("*/SKILL.md"))):
        if asking not in skill_md.read_text():
            fail(f"{skill_md.relative_to(ROOT)}: does not carry the explainer's asking convention (docs/claude-cowork-kit.md, How Claude asks) word for word (## Asking)")
    check_shared_text()
    check_project_sections()
    for name, body in projects.items():
        if "[FOLDER PATH ON MY COMPUTER]" not in body:
            fail(f"kit: the {name} project's block has no folder placeholder")
    refs = {f"{name}-instructions.md": stamp(f"docs/projects/{name}.md") + f"# Project instructions for the {name} project\n\nGoes in that project's Instructions panel, with the folder path filled in.\n\n```\n" + body + "```\n"
            for name, body in projects.items()}
    refs.update({
        "global-instructions.md": stamp(explainer_rel) + "# Account instructions (the kit's Block 1)\n\nGoes in Settings, Account, \"Instructions for Claude\". Substitute one voice from voices.md where marked.\n\n```\n" + block1 + "```\n",
        "voices.md": stamp(explainer_rel) + "# The three voices (the kit's Block 2)\n\nOne of these replaces the marked line in global-instructions.md.\n\n"
                     + "".join(f"## {name}\n\n```\n{body}```\n\n" for name, body in voices.items()),
        "project-instructions.md": stamp(notes_rel) + "# Project instructions (the kit's Block 3a)\n\nGoes in the project's Instructions panel, not the description. Nothing to fill in.\n\n```\n" + block3a + "```\n",
        "rules-template.md": stamp(notes_rel) + "# The working rules (the kit's Block 3b)\n\nCreated as the project doc rules.md, with the folder path filled in.\n\n```markdown\n" + block3b + "```\n",
        "map-template.md": stamp(notes_rel) + "# The description (the kit's Block 4)\n\nCreated as the project doc map.md, every bracket filled.\n\n```markdown\n" + block4 + "```\n",
    })
    return refs


PROJECT_DOCS = {  # each project plugin's setup docs, which every one of its other skills must name
    "pkm": ["rules.md", "map.md", "inbox.md"],
    "learn": ["mission.md", "curriculum.md", "progress.md"],
    "week": ["priorities.md"],
    "money": ["categories.md", "targets.md"],
    "medical": ["questions.md", "timeline.md"],
}


def check_project_sections():
    """Every non-setup skill of a project plugin says where it runs and names its docs.

    Plugins installed under Customize reach every project, so a skill that does
    not check its project writes into whatever folder is connected.
    """
    for plugin, docs in PROJECT_DOCS.items():
        for skill_md in sorted((PLUGINS_DIR / plugin / "skills").glob("*/SKILL.md")):
            if skill_md.parent.name.endswith("-setup"):
                continue
            text = skill_md.read_text()
            if "## Where this runs" not in text:
                fail(f"{skill_md.relative_to(ROOT)}: no '## Where this runs' section (the project check)")
            if not any(f"`{d}`" in text for d in docs):
                fail(f"{skill_md.relative_to(ROOT)}: names none of the {plugin} project's docs {docs}")


def check_shared_text():
    """Every skill listed for a block in docs/shared.md carries it word for word."""
    if not SHARED_DOC.exists():
        fail(f"shared text not found: {SHARED_DOC.relative_to(ROOT)}")
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
        print(f"\nwrote {plugin_zip.relative_to(ROOT)}  {plugin_zip.stat().st_size} bytes  sha256 {sha256(plugin_zip)}")
        for folder in plugin_skills(name):
            skill_zip = DIST / f"{folder.name}.skill"
            with zipfile.ZipFile(skill_zip, "w", zipfile.ZIP_DEFLATED) as z:
                for src, rel in files_of(folder):
                    z.write(src, str(Path(folder.name) / rel))
            print(f"wrote {skill_zip.relative_to(ROOT)}  {skill_zip.stat().st_size} bytes  sha256 {sha256(skill_zip)}")


if __name__ == "__main__":
    build()
