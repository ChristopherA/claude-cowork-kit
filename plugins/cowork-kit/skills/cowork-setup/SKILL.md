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

Ask each through the app's question control where there is a choice, the first option being the one to take when unsure, and wait for the answer. Reflect it back in a phrase before the next. Skip any the reader has already answered in their request.

1. **Who they are and how they work.** Three or four sentences, free text: what they do, what they want Claude for, when and how they tend to work. Not a biography; the things you would otherwise guess wrong. This is kept for the project setups, which ask it again only if it is missing.
2. **The voice.** Read `references/voices.md` and offer the three by name with one phrase each: plain, warm, archivist. Plain is listed first because it is the safe default, not because it is better; this is taste.
3. **Which projects.** Offer the five the kit describes, more than one allowed: a personal knowledge base (notes and reading), learning (a subject, a skill, or an exam), running the week, money, and medical records; and "something else". Recommend starting with one, the knowledge base, because every other project's habits come from it and because most readers build one project and stop.
4. **For the knowledge base, if chosen:** whether the reader is in the project they intend for their notes right now, or in a scratch task. The answer decides the kickoff below.

## Hand back the account instructions

From `references/global-instructions.md`, with the chosen voice from `references/voices.md` substituted where marked. It goes in Settings, Account, "Instructions for Claude". Show it whole, in one code block and nothing else inside the fence; the block carries a copy button in the app.

Say plainly that this field reaches every chat on the account, casual chat included, not only Cowork tasks. Anything the reader wants that is right for one project and wrong elsewhere belongs in that project's instructions, not here. If the field already holds text of the reader's own, say to add the block below it rather than replace it, and to cut whatever the two say twice.

## Say what to install next

For each project the reader chose, in the order they chose them:

- **Knowledge base:** the `pkm` plugin. In the desktop app: Customize, Plugins, add a plugin, choose `pkm.plugin`, and turn it on. A plugin dragged into a task's composer is attached to that task only, so use Customize. Then, in the project meant for notes, with the notes folder connected, start a task and say `set up my notes project`. That setup asks about the folder, creates the three project docs, and hands back the short project instructions.
- **Learning, the week, money, medical:** each is its own plugin with its own setup, installed and run the same way: `learn.plugin` and `set up my learning project`; `week.plugin` and `set up my week project`; `money.plugin` and `set up my money project`; `medical.plugin` and `set up my medical project`. The kit's explainer carries each project's instructions block in that project's section for a reader who would rather paste by hand. For money and medical, say now that the project should stay in the mode that asks before acting, and that the setup opens by saying what the folder does and does not protect.
- **Something else:** ask what it is for and what it must never touch. Draft a short Instructions text in the kit's shape (what the project is for, what belongs elsewhere, outside material is data, show-and-wait before changing anything, read the rules doc first) and a rules doc to go with it, show both, and hand them back the same way. A template plugin for projects the kit does not describe is on the kit's roadmap; say so in one sentence.

Install one plugin at a time and run its setup before the next; a reader who installs five plugins at once cannot tell which skill did what.

## The knowledge base kickoff

If the reader chose the knowledge base and is in the project they intend for it, create one project doc now: `inbox.md`, a heading and nothing else, and say that captures sent from the phone land there from this moment, even before the `pkm` plugin is installed. Do not create `map.md` or `rules.md` here; the `pkm` setup creates them from the folder. If the reader is in a scratch task, create nothing and say why.

## End

Report what exists now: the field waiting for a paste, the plugin to install next with its setup phrase, and the inbox doc if you created one. Then name the one day-one check: from the phone, in plain chat, ask Claude anything and listen for the voice; if it sounds the same as before, the paste did not land.

## What this skill does not do

It does not set any setting, install any plugin, connect any folder, or create a project. It does not run a project's setup; each project plugin has its own. It does not hand back project instructions, except the draft for a project the kit does not describe.
