# Contributing

The kit is one person's work and takes reports and changes from anyone who uses it.

## Reporting a problem

Open an issue on this repository. Say which plugin and skill, what you said, what Claude did, and what you expected; a screenshot of the app helps, with anything private cropped out. A claim in the explainer that the app contradicts is a report too, and the most useful kind: the kit marks what it is still confirming, and a reader's app is where those get settled.

## Changing the text

The account instructions and the voices live once, in `docs/claude-cowork-kit.md`; each binder's paste blocks live once, in its document under `docs/binders/`; the paragraphs several skills share live once, in `docs/shared.md`. Edit those, not the copies. The skills index, `docs/skills.md`, carries every skill's description word for word; a changed description is changed there too. Then:

```
python3 build.py            # regenerate the manifests, READMEs and references in place; build dist/
python3 build.py --check    # what a pull request must pass: skills valid, generated files current and committed
```

`--check` fails on a skill description over 200 characters, a copy of a shared paragraph that differs from its source, a binder skill without its "Where this runs" section, a generated file that differs from what the docs would produce, a skills index that does not match the skills, and, in a git checkout, a generated file left uncommitted. Commit the generated files with the change that caused them.

## Adding a skill

One folder under the plugin's `skills/`, one `SKILL.md`, with `name` equal to the folder and a `description` of at most 200 characters ending in the phrases that should trigger it. Every skill carries the asking convention from the explainer word for word under `## Asking`, and a binder skill carries `## Where this runs` naming its binder's Context documents. Read two of the plugin's existing skills first; the shape is the convention.

## Versions

`VERSION` holds the kit's version and every plugin carries it. A release is a signed tag `v<version>` with the six `.plugin` files and their checksums attached, and a line in `CHANGELOG.md`.
