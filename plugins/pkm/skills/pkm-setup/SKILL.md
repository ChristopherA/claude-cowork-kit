---
name: pkm-setup
description: Sets up the notes project: four questions, then rules.md, map.md and inbox.md as project docs and the short instructions to paste. Use for "set up my notes project", "install the kit", "run setup".
---

# Setup

Build the notes project the Personal Knowledge Kit describes, from four answers. Create what a task can create, the three project docs, and hand back what only the reader can paste, the short project instructions. Read the notes folder; do not write into it, except to create empty folders when the reader is starting from nothing and has said yes.

The texts this skill hands back are in `references/`, generated from the kit document when the plugin was packaged: `project-instructions.md` (the short text for the Instructions field), `rules-template.md` (the working rules doc), `map-template.md` (the description), `voices.md` (the three voices), `global-instructions.md` (the account-wide instructions, which the core plugin's setup hands back; this skill only reads it to recognize a voice). Use them as they are; do not rewrite them, and do not paraphrase them into the conversation. Fill in only the marked fields.

## Before the first question

Check whether a project doc named `map.md` already exists. If it does, this project is already set up: say so, offer the description check instead, and stop. Do not run setup twice.

## Four questions, one at a time

Ask each, wait for the answer, and reflect it back in a phrase before the next. Skip any the reader has already answered in their request.

1. **The folder.** Where the notes folder is on their computer, or whether they need to start one. If they name a folder, confirm you can reach it; if you cannot, say so and continue from their description, marking in `map.md` that the folder section is to be checked at the desk. If they are starting one, propose the default layout from the description template (inbox, sources, notes, threads, archive), show it, and create the empty folders only after a yes.
2. **The voice.** Read `references/voices.md` and offer the three by name with one phrase each: plain, warm, archivist. Do not recommend one; this is taste. If the account instructions already carry the kit's block with one of the voices in it, say which and skip the question.
3. **Who they are and how they work.** Three or four sentences: what they do, what the notes are for, when and how they work with them. Not a biography; the things you would otherwise guess wrong.
4. **Current work.** Two or three sentences: the open questions, the thing eating their attention this month. Ask for the open threads by name if they have any.

## Look at the folder

If the folder is reachable, read it before writing anything: the top-level folders, a sample of file names in each, roughly how many files, whether notes carry a `created` line, whether paragraphs are wrapped, and how notes link. Describe what is there. The template's folder layout is a default for an empty folder, not a description of theirs.

## Create the three project docs

Create `rules.md` as a project doc from `references/rules-template.md`, with the folder path filled in and nothing else changed; the reader revises it later, with you, one rule at a time.

Create `map.md` as a project doc from `references/map-template.md`, with every bracket filled from the answers and from what the folder showed. The folder sections describe the real folder. The conventions section holds what the folder shows plus anything the reader said is settled. Set the date. Leave nothing in brackets; where an answer is missing, ask rather than invent.

Create `inbox.md` as a project doc: a heading and nothing else.

Read all three back and confirm they exist as project docs. The app may file them under a `claude/` folder inside the project; that is fine, and the other skills find them by name. If project docs cannot be created from a task, say so plainly, show the three texts in full so the reader can add them however the app allows, and say that the rest of the kit depends on them.

## Hand back the text to paste

The project page has two text fields that look alike, a one-line description under the title and an Instructions panel at the side, and readers put the instructions in the description. So hand back two things, in this order, and say which field each goes in. If the project's description already holds the instructions text, say so and tell the reader to move it.

0. **The description**, one line, for the field under the project's title. Offer this: `Personal knowledge base: notes and reading. The rules are in Instructions; the notes are in [folder name].` with the folder name filled in.

The instructions go into a field only the reader can fill: a task can create project docs and cannot set the project's instructions or description, and the shell a task runs in is a Linux space apart from the reader's computer, so it cannot put text on their clipboard either. Do not try; hand the text back and say where it goes. The text goes in a code block of its own, which carries a copy button in the app.

1. **Project instructions**, from `references/project-instructions.md`, as they are; there is nothing to fill in. It goes in the Instructions panel on the project's page, not in the project's description; the description is visible to a task too, but it is a label, and the reader should not have to know that it happens to work.
The account-wide instructions are the core plugin's job, handed back by its setup skill; if the reader's Account field does not yet carry the kit's block (you will have seen at question 2), say so and point them there rather than handing it back here.

Show the block whole, one code block, and nothing else inside the fence.

## End

Report what exists now: the three project docs by name, the folders created if any, and the two fields waiting for a paste, the description and Instructions. Then name the three day-one checks from the kit, in order: at the desk, ask what is in the notes; from the phone with the computer closed, ask something the description alone can answer; send a capture from the phone and check it lands in the inbox doc. Do not run them; the reader does.

## What this skill does not do

It does not write or change any note. It does not set any setting. It does not paste anything anywhere; it hands text back. It does not hand back the account-wide instructions; the core plugin's setup does. It does not run twice on a project that already has a description.
