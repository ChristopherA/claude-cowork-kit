# Claude Cowork Kit

Plugins for people who use the Claude desktop and mobile apps with Cowork rather than Claude Code, with the architecture explained beside them. A reader installs the core plugin, runs its setup skill, and is walked into one project at a time: a personal knowledge base first, then learning, the week, money and medical records, each its own plugin with an install skill that builds the project and hands back only what the reader must paste by hand.

## Layout

- `docs/` -- the explainer, `claude-cowork-kit.md`: why Cowork, what a connected folder does and does not protect, the approval modes, the privacy floor, and the instruction blocks each plugin's setup skill hands back. The explainer is the single source; the blocks in a built plugin are generated from it, never edited by hand.
- `plugins/<name>/` -- one directory per plugin: its skills (`skills/<skill>/SKILL.md`, with read-only `scripts/` where a skill runs code) and its manifest.
- `build.py` -- checks every skill the way Cowork's upload does, generates the setup references from the explainer, and writes each plugin as a `.plugin` file and each skill as a `.skill` file under `dist/`, which is not tracked.
- `tests/fixture/` -- a small notes folder and the project docs a setup run should produce, for exercising the skills in Cowork before a reader's real notes are involved.

## Status

Pre-release. Two plugins build: `cowork-kit`, the core, and `pkm`, the knowledge project. The knowledge plugin has had one run in Cowork; the core has not run yet, and the other project plugins are not yet built.

## License

BSD-2-Clause-Patent. See `LICENSE`.
