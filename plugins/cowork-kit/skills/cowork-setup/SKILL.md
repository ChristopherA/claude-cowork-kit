---
name: cowork-setup
description: Sets up the Claude Cowork Kit: a short interview, the account instructions to paste, and which binder plugin to install next. Use for "set up the kit", "get started", "install the cowork kit".
---

# Kit setup

Start a reader on the Claude Cowork Kit. Ask a few questions, hand back the one block of text that goes in Settings, and say which binder plugin to install next and how. Every binder the kit describes is its own plugin with its own setup skill; this skill is the front door, not the whole house.

The text this skill hands back is in `references/`, generated from the kit's docs when the plugin was packaged: `global-instructions.md` (the account-wide instructions) and `voices.md` (the three voices). Use them as they are; do not rewrite or paraphrase them. Fill in only the marked line.

## What a task can and cannot do

A task can read the project's Context documents, create Context documents in the project it runs in, read a connected folder, and read the reader's Account instructions. It cannot change Settings, set the project's approval mode, create a project, connect a folder, install a plugin, or send anything; those are the reader's, in the app. Say which is which as you go, so the reader never waits for something that will not happen. Whether a task can create a new project is not settled; assume it cannot, and have the reader create projects in the app.

## Before the first question

Read the reader's Account instructions if you can see them. If they already carry the kit's block, say so, name the voice in it, and skip the voice question.

## The interview

Ask as the Asking section says: questions 1 and 2 do not depend on each other and can share one control; question 3 depends on the answer to 2 and goes in the next. Skip any the reader has already answered in their request. Do not ask who the reader is or how they work: nothing this skill writes needs it, a task cannot carry an answer into another project, and the binder setups ask it where it is used.

1. **The voice.** Read `references/voices.md` and offer the three by name with one phrase each: plain, warm, archivist. Plain is listed first because it is the safe default, not because it is better; this is taste.
2. **Which binder first.** Four options, one answer: the research binder (notes and reading), recommended, because every other binder's habits come from it and because most readers build one binder and stop; learning (a subject, a skill, or an exam); running the week; or one of the others, which the reader names in their own words: money, medical records, or something the kit does not describe. Say that the rest can follow one at a time.
3. **For the research binder, if chosen:** whether this task is running inside the project they mean for their notes. Three options: yes, this is it; no, that project does not exist yet; not sure. The answer decides the kickoff below; "not sure" counts as no.

## Hand back the account instructions

From `references/global-instructions.md`, with the chosen voice from `references/voices.md` substituted where marked. It goes in Settings, Account, "Instructions for Claude". Show it whole, in one code block and nothing else inside the fence; the block carries a copy button in the app.

Say plainly that this field reaches every chat on the account, casual chat included, not only Cowork tasks. Anything the reader wants that is right for one project and wrong elsewhere belongs in that project's instructions, not here. If the field already holds text of the reader's own, say to add the block below it rather than replace it, and to cut whatever the two say twice.

## Say what to install next

For each binder the reader chose, in the order they chose them:

- **Research:** the `research` plugin, shown as Research. In the desktop app, Customize, Plugins: install it from the kit's marketplace if that is how the core was installed, or download `research.plugin` from the kit's releases page (https://github.com/ChristopherA/claude-cowork-kit/releases) and add it with the upload option. Turn it on. A plugin dragged into a task's composer is attached to that task only, so use Customize. Then, in the project meant for the research binder, with the research folder connected, start a task and say `set up my research binder`. That setup asks about the folder, creates the three Context documents, and hands back the short project instructions.
- **Learning, the week, money, medical:** each is its own plugin with its own setup, installed the same way, from the marketplace or from its file on the releases page, and run with its phrase: `learn` and `set up my learning binder`; `week` and `set up my week binder`; `money` and `set up my money binder`; `medical` and `set up my medical binder`. Each binder's document in the kit, `docs/binders/<name>.md`, carries its instructions block for a reader who would rather paste by hand. For money and medical, say now that the project should stay in the mode that asks before acting, and that the setup opens by saying what the folder does and does not protect.
- **Something else:** say that the core's `cowork-new-binder` skill designs a binder the kit does not describe, hands back its Instructions text, and points at the kit's template for a plugin of its own; offer to run it next, once the account block is pasted, by saying `new binder`.

Install one plugin at a time and run its setup before the next; a reader who installs five plugins at once cannot tell which skill did what.

## The research binder kickoff

If the reader chose the research binder and answered that this task is inside the project they mean for it, create one Context document now: `inbox.md`, a heading and nothing else, and say that it is the capture inbox and that the research setup will keep it. Do not create `map.md` or `rules.md` here; the `research` setup creates them from the folder. Otherwise create nothing and say that the research setup creates the inbox.

## End

Report what exists now: the field waiting for a paste, the plugin to install next with its setup phrase, and the inbox document if you created one. Then name the one day-one check: open Settings, Account, and see the block there; if the field is empty, the paste did not land. End with one word for completeness: full, partial (with what is missing), or minimal (stopped early).

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never ask what the reader has already said. Silence is never a yes: a yes is a tap on the control or a word.

## What this skill does not do

It does not set any setting, install any plugin, connect any folder, or create a project. It does not run a binder's setup; each binder plugin has its own. It does not hand back project instructions; `cowork-new-binder` drafts them for a binder the kit does not describe.
