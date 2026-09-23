#!/usr/bin/env python3
"""Package the kit's skills for Cowork.

Reads every skill folder under plugins/pkm/skills/, checks each one the way Cowork's
upload will, and writes to dist/:

  pkm.plugin          one plugin carrying every pkm- skill, installed once
  pkm-<name>.skill    each skill on its own, for a reader who wants one

Both are ZIP files. A .skill holds the skill folder as its top-level
directory, the layout the official skill-creator packager produces. A
.plugin holds the plugin tree at the ZIP root, the layout the
create-cowork-plugin skill produces.

The pkm-setup skill hands the reader the kit's own instruction blocks, so
its references/ are GENERATED here from the kit document (docs/, or
--kit PATH) and never edited by hand; the kit stays the single source.

Usage:
    python3 build.py                 build everything into dist/
    python3 build.py --check         validate only, write nothing
    python3 build.py --kit PATH      read the kit document from PATH
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
SKILLS = ROOT / "plugins" / "pkm" / "skills"
DIST = ROOT / "dist"
PLUGIN_NAME = "pkm"
PLUGIN_VERSION = "0.1.0"
PLUGIN_DESCRIPTION = (
    "Skills for the Personal Knowledge Kit's notes project in Claude Cowork: "
    "set the project up, drain the capture inbox, write a source note, check "
    "the description against the folder, and four small routines for deciding, "
    "checking confidence, finding the thread, and learning from a mistake."
)
KIT_DEFAULT = ROOT / "docs" / "personal-knowledge-kit.md"
SETUP_SKILL = "pkm-setup"
AUTHOR = "Christopher Allen"
DESCRIPTION_LIMIT = 200  # Cowork rejects a longer description on upload
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
SKIP_DIRS = {"__pycache__", "node_modules", "evals"}
SKIP_FILES = {".DS_Store"}


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
    """Extract the four blocks the setup skill hands back, from the kit text."""
    kit_path = Path(kit_path).expanduser()
    if not kit_path.exists():
        fail(f"kit document not found: {kit_path} (pass --kit PATH)")
    text = kit_path.read_text()
    try:
        rev = subprocess.run(["git", "-C", str(kit_path.parent), "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        rev = "unknown"
    block1 = fenced_block_after(text, r"^## Block 1 ")
    block3 = fenced_block_after(text, r"^## Block 3 ")
    block4 = fenced_block_after(text, r"^## Block 4 ")
    voices = {name: fenced_block_after(text, rf"^\*\*{name}\.\*\*") for name in ("Plain", "Warm", "Archivist")}
    if "[PASTE YOUR CHOSEN VOICE HERE]" not in block1:
        fail("kit: Block 1 has no voice placeholder")
    if "[FOLDER PATH ON MY COMPUTER]" not in block3:
        fail("kit: Block 3 has no folder placeholder")
    if "[FULL FOLDER PATH ON MY COMPUTER]" not in block4:
        fail("kit: Block 4 has no folder placeholder")
    stamp = f"<!-- generated by build.py from the Personal Knowledge Kit at {rev}; edit the kit, not this file -->\n\n"
    return {
        "global-instructions.md": stamp + "# Account instructions (the kit's Block 1)\n\nGoes in Settings, Account, \"Instructions for Claude\". Substitute one voice from voices.md where marked.\n\n```\n" + block1 + "```\n",
        "voices.md": stamp + "# The three voices (the kit's Block 2)\n\nOne of these replaces the marked line in global-instructions.md.\n\n"
                     + "".join(f"## {name}\n\n```\n{body}```\n\n" for name, body in voices.items()),
        "project-instructions.md": stamp + "# Project instructions (the kit's Block 3)\n\nGoes in the project's instructions field, with the folder path filled in.\n\n```\n" + block3 + "```\n",
        "map-template.md": stamp + "# The description (the kit's Block 4)\n\nCreated as the project doc map.md, every bracket filled.\n\n```markdown\n" + block4 + "```\n",
    }


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def build():
    skills = sorted(d for d in SKILLS.iterdir() if d.is_dir() and not d.name.startswith("."))
    if not skills:
        fail(f"no skill folders under {SKILLS.relative_to(ROOT)}")
    names = []
    for folder in skills:
        name, n = check_skill(folder)
        names.append(name)
        print(f"ok  {name:24s} description {n:3d} chars")
    kit = KIT_DEFAULT
    if "--kit" in sys.argv:
        kit = Path(sys.argv[sys.argv.index("--kit") + 1])
    refs = kit_references(kit)
    print(f"ok  references from the kit: {', '.join(sorted(refs))}")
    if SETUP_SKILL not in names:
        fail(f"{SETUP_SKILL} missing under {SKILLS.relative_to(ROOT)}, so the references have no home")
    if "--check" in sys.argv:
        print(f"{len(names)} skills valid; nothing written")
        return

    if DIST.exists():
        shutil.rmtree(DIST)
    plugin_dir = DIST / PLUGIN_NAME
    (plugin_dir / ".claude-plugin").mkdir(parents=True)

    manifest = {
        "name": PLUGIN_NAME,
        "version": PLUGIN_VERSION,
        "description": PLUGIN_DESCRIPTION,
        "author": {"name": AUTHOR},
        "keywords": ["personal-knowledge", "notes", "cowork", "markdown"],
    }
    (plugin_dir / ".claude-plugin" / "plugin.json").write_text(json.dumps(manifest, indent=2) + "\n")

    readme = [f"# {PLUGIN_NAME}", "", PLUGIN_DESCRIPTION, "",
              "Each skill expects the notes project the Personal Knowledge Kit for Claude Cowork describes: a notes folder connected in the desktop app, a project doc `map.md` describing it, and a project doc `inbox.md` for captures. The three skills with scripts read the folder only; they never write to it without the reader's yes, and each says in its body what to do when code execution is off.",
              "", "## Skills", ""]
    for folder in skills:
        fm = frontmatter(folder / "SKILL.md")
        readme.append(f"- `{fm['name']}`: {fm['description']}")
        dest = plugin_dir / "skills" / folder.name
        for src, rel in files_of(folder):
            (dest / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest / rel)
        if folder.name == SETUP_SKILL:
            (dest / "references").mkdir(exist_ok=True)
            for name, body in refs.items():
                (dest / "references" / name).write_text(body)
    readme += ["", "## Install", "",
               "In the Claude desktop app: Customize, Plugins, add a plugin, and choose this `.plugin` file. To add one skill instead of the set: Customize, Skills, upload the matching `.skill` file.", ""]
    (plugin_dir / "README.md").write_text("\n".join(readme))

    plugin_zip = DIST / f"{PLUGIN_NAME}.plugin"
    with zipfile.ZipFile(plugin_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for src, rel in files_of(plugin_dir):
            z.write(src, str(rel))
    print(f"\nwrote {plugin_zip.relative_to(ROOT)}  {plugin_zip.stat().st_size} bytes  sha256 {sha256(plugin_zip)}")

    for folder in skills:
        skill_zip = DIST / f"{folder.name}.skill"
        packed = plugin_dir / "skills" / folder.name  # the copy, which carries generated references
        with zipfile.ZipFile(skill_zip, "w", zipfile.ZIP_DEFLATED) as z:
            for src, rel in files_of(packed):
                z.write(src, str(Path(folder.name) / rel))
        print(f"wrote {skill_zip.relative_to(ROOT)}  {skill_zip.stat().st_size} bytes  sha256 {sha256(skill_zip)}")


if __name__ == "__main__":
    build()
