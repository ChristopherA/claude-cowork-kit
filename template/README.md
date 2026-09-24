# Template for a binder plugin

For a reader comfortable editing files, or a contributor. A reader who wants a binder of their own does not need this: the core plugin's `cowork-new-binder` skill designs the binder and hands back the instructions text, and that text with a few Context documents is the whole binder. This folder is the extra step that turns such a design into a plugin whose setup runs from a phrase.

A copy of this folder, with every `BINDER` and every bracket filled in, is a plugin for a binder the Claude Cowork Kit does not describe. It carries the shape the kit's own binder plugins share: a setup skill that interviews the reader, creates the Context documents, and hands back the one text only the reader can paste, plus whatever routine skills the binder needs.

## What to change

- `.claude-plugin/plugin.json`: the plugin's name (lower case, no spaces), a one-sentence description, your name.
- `skills/BINDER-setup/`: rename the folder to `<name>-setup`, and in `SKILL.md` set `name` to match and fill the brackets. The skill reads `references/project-instructions.md` and hands it back; it never rewrites it.
- `skills/BINDER-setup/references/project-instructions.md`: the binder's project instructions, in the kit's shape (what the binder is for, what belongs elsewhere, where things live, how to answer, what Claude is not). The core plugin's `cowork-new-binder` skill drafts this with you.
- Add a folder under `skills/` for each routine skill, one `SKILL.md` each, with a `name` equal to its folder and a `description` of at most 200 characters ending in the phrases that should trigger it.

## Building the `.plugin` file

The kit's own plugins are built by its `build.py`, which generates the references from the kit's docs. A plugin made from this template is built with Anthropic's `create-cowork-plugin` skill instead, from the Cowork plugin management plugin: install that plugin, start a task in Cowork, say `create a plugin from this folder`, and hand it this folder. It packages the tree as a `.plugin` file for Customize, Plugins, upload. Or add the folder to a Git repository of your own and add that repository as a marketplace.

## Layout

```
BINDER/
  .claude-plugin/plugin.json
  README.md
  skills/
    BINDER-setup/
      SKILL.md
      references/project-instructions.md
    <another-skill>/SKILL.md
```
