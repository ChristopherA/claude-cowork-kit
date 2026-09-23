---
name: week-setup
description: Sets up the week project: three questions, then priorities.md as a project doc and the short instructions to paste. Use for "set up my week project", "week setup".
---

# Setup

Build the week project the Claude Cowork Kit describes, from three answers. Create what a task can create, the one project doc, and hand back what only the reader can paste, the project instructions. Read the working folder if it is reachable; do not write into it.

The text this skill hands back is in `references/`, generated from the kit document when the plugin was packaged: `week-instructions.md` (the project's instructions, for the Instructions panel). Use it as it is; do not rewrite it, and do not paraphrase it into the conversation. Fill in only the folder path where the block marks it.

## What a task can and cannot do

A task can create project docs in the project it runs in, read a connected folder, and read the reader's Account instructions. It cannot set Settings, create a project, connect a folder, install a plugin, or send anything. Those are the reader's, in the app. Say which is which as you go, so the reader never waits for something that will not happen.

## Before the first question

Check whether a project doc named `priorities.md` already exists. If it does, this project is already set up: say so, offer to update the priorities instead, and stop. Do not run setup twice.

Read the reader's Account instructions if you can see them. If they do not yet carry the kit's block, say so once and point the reader at the core plugin's setup, which hands it back; do not hand it back here.

## Three questions, one at a time

Ask each through the app's question control where there is a choice, the recommended option first, and wait for the answer. Reflect it back in a phrase before the next. Skip any the reader has already answered in their request.

1. **The folder.** Where the working files are on their computer: the folder that holds drafts, lists, threads they are keeping, earlier replies. If they name a folder, confirm you can reach it; if you cannot, say so, continue from their description, and mark in `priorities.md` that the folder is to be checked at the desk. The folder is reachable only from a task at the desk; the project doc this skill creates is reachable from the phone as well, which is why the priorities live in the doc and not in the folder.
2. **Current priorities.** The two or three things that matter this month, in order, each in a phrase, and the one eating their attention right now. Not everything they owe; the things a plan should bend around. If they offer eight, ask which three would still matter if the other five slipped.
3. **The other kit projects.** Which of the kit's other projects exist for them: a knowledge project (notes and reading), a learning project, a money project, a medical project. Offer all four, more than one allowed, and "none yet". The instructions send notes to the knowledge project's inbox and money and medical questions to their projects; the answer decides whether those redirects name a project that exists or one the reader has still to build.

## Create the project doc

Create `priorities.md` as a project doc: a heading, today's date on a line of its own, the priorities from question 2 in order with the one eating attention marked, and a short section naming which other kit projects exist from question 3, with a line for any that do not yet, so a redirect to one is read as "when you build it". Keep it short enough to read on a phone. Leave nothing in brackets; where an answer is missing, ask rather than invent.

Read it back and confirm it exists as a project doc. The app may file it under a `claude/` folder inside the project; that is fine, and the other skills find it by name. If a project doc cannot be created from a task, say so plainly, show the text in full so the reader can add it however the app allows, and say that the planning skill depends on it.

## Hand back the text to paste

The project page has two text fields that look alike, a one-line description under the title and an Instructions panel at the side, and readers put the instructions in the description. So hand back two things, in this order, and say which field each goes in. If the project's description already holds the instructions text, say so and tell the reader to move it.

0. **The description**, one line, for the field under the project's title. Offer this: `Running my week: tasks, planning, drafts, triage. The rules are in Instructions; the working files are in [folder name].` with the folder name filled in.

The instructions go into a field only the reader can fill: a task can create project docs and cannot set the project's instructions or description, and the shell a task runs in is a Linux space apart from the reader's computer, so it cannot put text on their clipboard either. Do not try; hand the text back and say where it goes. The text goes in a code block of its own, which carries a copy button in the app.

1. **Project instructions**, from `references/week-instructions.md`, with the folder path from question 1 in place of the bracket and nothing else changed. It goes in the Instructions panel on the project's page, not in the project's description; the description is visible to a task too, but it is a label, and the reader should not have to know that it happens to work.

Show the block whole, one code block, and nothing else inside the fence.

## End

Report what exists now: the project doc by name, and the two fields waiting for a paste, the description and Instructions. Then name the three day-one checks, in order: at the desk, dump a mess of obligations into a task and see whether a short ordered list comes back with nothing around it; from the phone with the computer closed, ask what the current priorities are, which the doc alone can answer; hand over a message and see whether a draft comes back and the task stops there. Do not run them; the reader does.

## What this skill does not do

It does not write into the working folder. It does not set any setting, create a project, connect a folder, install a plugin, or send anything. It does not paste anything anywhere; it hands text back. It does not hand back the account-wide instructions; the core plugin's setup does. It does not run twice on a project that already has a priorities doc.
