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
references/ are GENERATED here from the explainer (docs/, or --kit PATH)
and never edited by hand; the explainer stays the single source. The
generated files are written IN PLACE under plugins/ and committed, because
the repository is also a Cowork marketplace: .claude-plugin/marketplace.json
at the root lists every plugin by its directory, and Cowork reads the tree
as it is. So each plugin directory carries its manifest, its README and its
setup skill's references/, all generated here; --check fails when any of
them differs from what the explainer and the table below would produce.

Usage:
    python3 build.py                 generate in place, then build dist/
    python3 build.py --check         validate and detect drift, write nothing
    python3 build.py --kit PATH      read the explainer from PATH
"""

import hashlib
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLUGINS_DIR = ROOT / "plugins"
DIST = ROOT / "dist"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
KIT_DEFAULT = ROOT / "docs" / "claude-cowork-kit.md"
PROJECT_SECTIONS = ("learning", "week", "money", "medical")  # each `## The <name> project` section carries one block
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
        "version": "0.1.0",
        "description": (
            "The Claude Cowork Kit's core: a setup interview that hands back the account "
            "instructions and says which project plugins to install next, plus twelve routines "
            "for any project: deciding, interviewing, explaining again, questions for others, a "
            "meeting pack, a transcript, confidence, premortem, postmortem, where was I, wrap-up, "
            "and a new project."
        ),
        "keywords": ["cowork", "setup", "personal", "non-programmer"],
        "setup": "cowork-setup",
        "references": ["global-instructions.md", "voices.md"],
        "readme": (
            "Install this plugin first, then start a task and say `set up the kit`. The setup "
            "skill asks a few questions, hands back the account-wide instructions to paste, and "
            "says which project plugin to install next. The other twelve skills work in any project."
        ),
    },
    "learn": {
        "display": "Learning",
        "version": "0.1.0",
        "description": (
            "Skills for the Claude Cowork Kit's learning project: set a course, run a lesson, "
            "and quiz yourself on what you have learned or read."
        ),
        "keywords": ["learning", "study", "cowork", "tutor"],
        "setup": "learn-setup",
        "references": ["learning-instructions.md"],
        "readme": (
            "Each skill expects the learning project the Claude Cowork Kit describes: a folder of "
            "materials connected in the desktop app and the project docs mission.md, curriculum.md "
            "and progress.md, which the setup creates. Turn on the Learning style for the project, in the style menu."
        ),
    },
    "week": {
        "display": "Your week",
        "version": "0.1.0",
        "description": (
            "Skills for the Claude Cowork Kit's week project: set it up, triage a pile of "
            "obligations into next actions, plan the week, review it, write up a meeting, and "
            "draft a reply without sending it."
        ),
        "keywords": ["productivity", "planning", "cowork", "week"],
        "setup": "week-setup",
        "references": ["week-instructions.md"],
        "readme": (
            "Each skill expects the week project the Claude Cowork Kit describes: a working folder "
            "connected in the desktop app, a priorities doc the setup creates, and a reviews doc the "
            "review creates. Nothing here sends "
            "a message or changes a calendar; drafts are handed back."
        ),
    },
    "money": {
        "display": "Money",
        "version": "0.1.0",
        "description": (
            "Skills for the Claude Cowork Kit's money project: set it up with the privacy floor, "
            "summarize a statement, and close a month against your categories."
        ),
        "keywords": ["money", "budget", "cowork", "household"],
        "setup": "money-setup",
        "references": ["money-instructions.md"],
        "readme": (
            "Each skill expects the money project the Claude Cowork Kit describes: statements in a "
            "connected folder that stays on the computer, and project docs holding only categories, "
            "targets and summaries with no account details. Keep the project in the mode that asks (the explainer, under The two approval modes)."
        ),
    },
    "medical": {
        "display": "Medical records",
        "version": "0.1.0",
        "description": (
            "Skills for the Claude Cowork Kit's medical project: set it up, prepare a visit and its "
            "pack, record a visit into the folder, keep a weekly functional log, and turn a handed "
            "article into questions for the clinician."
        ),
        "keywords": ["medical", "health", "cowork", "records"],
        "setup": "medical-setup",
        "references": ["medical-instructions.md"],
        "readme": (
            "Each skill expects the medical project the Claude Cowork Kit describes: records in a "
            "connected folder that stays on the computer, arranged as the explainer's section The medical "
            "project describes, and project docs holding only a questions list and a bare timeline. Keep the "
            "project in the mode that asks (the explainer, under The two approval modes)."
        ),
    },
    "pkm": {
        "display": "Personal knowledge",
        "version": "0.2.0",
        "description": (
            "Skills for the Claude Cowork Kit's notes project: set the project up, drain the "
            "capture inbox, write a source note, and check the description against the folder."
        ),
        "keywords": ["personal-knowledge", "notes", "cowork", "markdown"],
        "setup": "pkm-setup",
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


def fenced_block_after(text, heading_regex, fence="```"):
    """The first fenced block after the line matching heading_regex."""
    m = re.search(heading_regex, text, re.M)
    if not m:
        fail(f"kit: heading not found: {heading_regex}")
    rest = text[m.end():]
    start = re.search(r"^```(?:markdown)?\n", rest, re.M)
    if not start:
        fail(f"kit: no fenced block after {heading_regex}")
    body = rest[start.end():]
    end = re.search(r"^```$", body, re.M)
    if not end:
        fail(f"kit: unterminated fence after {heading_regex}")
    return body[:end.start()].rstrip("\n") + "\n"


def kit_references(kit_path):
    """Extract every block a setup skill uses, from the explainer's text."""
    kit_path = Path(kit_path).expanduser()
    if not kit_path.exists():
        fail(f"kit document not found: {kit_path} (pass --kit PATH)")
    text = kit_path.read_text()
    block1 = fenced_block_after(text, r"^## Block 1 ")
    block3a = fenced_block_after(text, r"^## Block 3a ")
    block3b = fenced_block_after(text, r"^## Block 3b ")
    block4 = fenced_block_after(text, r"^## Block 4 ")
    voices = {name: fenced_block_after(text, rf"^\*\*{name}\.\*\*") for name in ("Plain", "Warm", "Archivist")}
    if "[PASTE YOUR CHOSEN VOICE HERE]" not in block1:
        fail("kit: Block 1 has no voice placeholder")
    if "[FOLDER PATH ON MY COMPUTER]" in block3a:
        fail("kit: Block 3a carries the folder placeholder, which belongs in Block 3b")
    if "[FOLDER PATH ON MY COMPUTER]" not in block3b:
        fail("kit: Block 3b has no folder placeholder")
    if "[FULL FOLDER PATH ON MY COMPUTER]" not in block4:
        fail("kit: Block 4 has no folder placeholder")
    projects = {name: fenced_block_after(text, rf"^## The {name} project$") for name in PROJECT_SECTIONS}
    asking = fenced_block_after(text, r"^### How Claude asks$").strip()
    for skill_md in sorted(PLUGINS_DIR.glob("*/skills/*/SKILL.md")):
        if asking not in skill_md.read_text():
            fail(f"{skill_md.relative_to(ROOT)}: does not carry the explainer's asking convention word for word (## Asking)")
    for name, body in projects.items():
        if "[FOLDER PATH ON MY COMPUTER]" not in body:
            fail(f"kit: the {name} project's block has no folder placeholder")
    stamp = "<!-- generated by build.py from the Claude Cowork Kit explainer; edit the explainer, not this file -->\n\n"
    refs = {f"{name}-instructions.md": stamp + f"# Project instructions for the {name} project\n\nGoes in that project's Instructions panel, with the folder path filled in.\n\n```\n" + body + "```\n"
            for name, body in projects.items()}
    refs.update({
        "global-instructions.md": stamp + "# Account instructions (the kit's Block 1)\n\nGoes in Settings, Account, \"Instructions for Claude\". Substitute one voice from voices.md where marked.\n\n```\n" + block1 + "```\n",
        "voices.md": stamp + "# The three voices (the kit's Block 2)\n\nOne of these replaces the marked line in global-instructions.md.\n\n"
                     + "".join(f"## {name}\n\n```\n{body}```\n\n" for name, body in voices.items()),
        "project-instructions.md": stamp + "# Project instructions (the kit's Block 3a)\n\nGoes in the project's Instructions panel, not the description. Nothing to fill in.\n\n```\n" + block3a + "```\n",
        "rules-template.md": stamp + "# The working rules (the kit's Block 3b)\n\nCreated as the project doc rules.md, with the folder path filled in.\n\n```markdown\n" + block3b + "```\n",
        "map-template.md": stamp + "# The description (the kit's Block 4)\n\nCreated as the project doc map.md, every bracket filled.\n\n```markdown\n" + block4 + "```\n",
    })
    return refs


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
            "version": spec["version"],
            "description": spec["description"],
            "author": {"name": AUTHOR},
            "keywords": spec["keywords"],
        }
        out[plugin_dir / ".claude-plugin" / "plugin.json"] = json.dumps(manifest, indent=2) + "\n"
        readme = [f"# {name}", "", spec["description"], "", spec["readme"], "", "## Skills", ""]
        for folder in plugin_skills(name):
            fm = frontmatter(folder / "SKILL.md")
            readme.append(f"- `{fm['name']}`: {fm['description']}")
        readme += ["", "## Install", "",
                   "In the Claude desktop app, either add this repository as a marketplace (Customize, Plugins, Add marketplace, `ChristopherA/claude-cowork-kit`) and install the plugin from it, or download the `.plugin` file from a release and upload it (Customize, Plugins, the upload option), then turn it on. A plugin dragged into a task's composer is attached to that task only. To add one skill instead of the set: Customize, Skills, upload the matching `.skill` file.", ""]
        out[plugin_dir / "README.md"] = "\n".join(readme)
        for ref in spec["references"]:
            out[plugin_dir / "skills" / spec["setup"] / "references" / ref] = refs[ref]
        listing.append({
            "name": name,
            "displayName": spec["display"],
            "description": spec["description"],
            "version": spec["version"],
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
    kit = KIT_DEFAULT
    if "--kit" in sys.argv:
        kit = Path(sys.argv[sys.argv.index("--kit") + 1])
    refs = kit_references(kit)
    print(f"ok  references from the explainer: {', '.join(sorted(refs))}")
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
            fail("generated files differ from the explainer; run build.py and commit the result")
        print(f"{len(checked)} skills in {len(PLUGINS)} plugins valid; generated files current; nothing written")
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
