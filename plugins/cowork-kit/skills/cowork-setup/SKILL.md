---
name: cowork-setup
description: Sets up the Claude Cowork Kit: a short interview, the account instructions to paste, and which project plugin to install next. Use for "set up the kit", "get started", "install the cowork kit".
---

# Kit setup

Start a reader on the Claude Cowork Kit. Ask a few questions, hand back the one block of text that goes in Settings, and say which project plugin to install next and how. Every project the kit describes is its own plugin with its own setup skill; this skill is the front door, not the whole house.

The text this skill hands back is in `references/`, generated from the kit's explainer when the plugin was packaged: `global-instructions.md` (the account-wide instructions) and `voices.md` (the three voices). Use them as they are; do not rewrite or paraphrase them. Fill in only the marked line.

## What a task can and cannot do

A task can read the reader's Account instructions, create project docs in the project it runs in, and read a connected folder. It cannot write Settings, install a plugin, or connect a folder; those are the reader's, in the app. Whether a task can create a new project is not settled; assume it cannot, and have the reader create projects in the app. Say which is which as you go, so the reader never waits for something that will not happen.

## Before the first question

Read the reader's Account instructions if you can see them. If they already carry the kit's block, say so, name the voice in it, and skip the voice question.

## The interview, one question at a time

Ask as the Asking section says: questions 1 and 2 do not depend on each other and can share one control; question 3 depends on the answer to 2 and goes in the next. Skip any the reader has already answered in their request. Do not ask who the reader is or how they work: nothing this skill writes needs it, a task cannot carry an answer into another project, and the project setups ask it where it is used.

1. **The voice.** Read `references/voices.md` and offer the three by name with one phrase each: plain, warm, archivist. Plain is listed first because it is the safe default, not because it is better; this is taste.
2. **Which project first.** Four options, one answer: the knowledge base (notes and reading), recommended, because every other project's habits come from it and because most readers build one project and stop; learning (a subject, a skill, or an exam); running the week; or one of the others, which the reader names in their own words: money, medical records, or something the kit does not describe. Say that the rest can follow one at a time.
3. **For the knowledge base, if chosen:** whether this task is running inside the project they mean for their notes. Three options: yes, this is it; no, the notes project does not exist yet; not sure. The answer decides the kickoff below; "not sure" counts as no.

## Hand back the account instructions

From `references/global-instructions.md`, with the chosen voice from `references/voices.md` substituted where marked. It goes in Settings, Account, "Instructions for Claude". Show it whole, in one code block and nothing else inside the fence; the block carries a copy button in the app.

Say plainly that this field reaches every chat on the account, casual chat included, not only Cowork tasks. Anything the reader wants that is right for one project and wrong elsewhere belongs in that project's instructions, not here. If the field already holds text of the reader's own, say to add the block below it rather than replace it, and to cut whatever the two say twice.

## Say what to install next

For each project the reader chose, in the order they chose them:

- **Knowledge base:** the `pkm` plugin, shown as Personal knowledge. In the desktop app, Customize, Plugins: install it from the kit's marketplace if that is how the core was installed, or download `pkm.plugin` from the kit's releases page (https://github.com/ChristopherA/claude-cowork-kit/releases) and add it with the upload option. Turn it on. A plugin dragged into a task's composer is attached to that task only, so use Customize. Then, in the project meant for notes, with the notes folder connected, start a task and say `set up my notes project`. That setup asks about the folder, creates the three project docs, and hands back the short project instructions.
- **Learning, the week, money, medical:** each is its own plugin with its own setup, installed the same way, from the marketplace or from its file on the releases page, and run with its phrase: `learn` and `set up my learning project`; `week` and `set up my week project`; `money` and `set up my money project`; `medical` and `set up my medical project`. The kit's explainer carries each project's instructions block in that project's section for a reader who would rather paste by hand. For money and medical, say now that the project should stay in the mode that asks before acting, and that the setup opens by saying what the folder does and does not protect.
- **Something else:** say that the core's `cowork-new-project` skill designs a project the kit does not describe, hands back its Instructions text, and points at the kit's template for a plugin of its own; offer to run it next, once the account block is pasted, by saying `new project`.

Install one plugin at a time and run its setup before the next; a reader who installs five plugins at once cannot tell which skill did what.

## The knowledge base kickoff

If the reader chose the knowledge base and answered that this task is inside the project they mean for it, create one project doc now: `inbox.md`, a heading and nothing else, and say that it is the capture inbox and that the notes setup will keep it. Do not create `map.md` or `rules.md` here; the `pkm` setup creates them from the folder. Otherwise create nothing and say that the notes setup creates the inbox.

## End

Report what exists now: the field waiting for a paste, the plugin to install next with its setup phrase, and the inbox doc if you created one. Then name the one day-one check: open Settings, Account, and see the block there; if the field is empty, the paste did not land.

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never ask what the reader has already said.

## What this skill does not do

It does not set any setting, install any plugin, connect any folder, or create a project. It does not run a project's setup; each project plugin has its own. It does not hand back project instructions; `cowork-new-project` drafts them for a project the kit does not describe.
