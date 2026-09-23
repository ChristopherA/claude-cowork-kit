---
name: PROJECT-setup
description: Sets up the [PROJECT] project: a short interview, the project docs, and the instructions to paste. Use for "set up my [PROJECT] project", "[PROJECT] setup".
---

# Setup

Build the [PROJECT] project from a few answers. Create what a task can create, the project docs, and hand back what only the reader can paste, the project instructions. Read the folder if one is connected; do not write into it during setup.

The text this skill hands back is in `references/project-instructions.md`. Use it as it is; do not rewrite or paraphrase it. Fill in only the folder path.

## What a task can and cannot do

A task can read the project docs, create project docs in the project it runs in, read a connected folder, and read the reader's Account instructions. It cannot change Settings, set the project's approval mode, create a project, connect a folder, install a plugin, or send anything; those are the reader's, in the app. Say which is which as you go, so the reader never waits for something that will not happen.

## Before the first question

Check whether the project docs already exist. If they do, say so and stop; do not run setup twice.

## The interview, one question at a time

Ask as the Asking section says, grouping the questions whose answers do not depend on each other in one control and putting the dependent ones after. Skip any the reader has already answered in their request. Reflect each answer back in a phrase before going on.

1. **The folder.** Where the files for this project are on their computer, or whether there are none yet. If they name a folder, confirm you can reach it; if you cannot, say so and continue from their description.
2. [**THE QUESTION THAT SHAPES THE FIRST DOC.**]
3. [**THE QUESTION THAT SHAPES THE SECOND DOC, IF ANY.**]

## Create the project docs

Create [`FIRST-DOC.md`] as a project doc: [WHAT IT HOLDS, IN ONE SENTENCE]. Create [`SECOND-DOC.md`] the same way. Read each back and confirm it exists as a project doc. If project docs cannot be created from a task, say so, show the texts in full, and say the rest depends on them.

## Hand back the text to paste

The project page has two text fields that look alike, a one-line description under the title and an Instructions panel at the side, and readers put the instructions in the description. So hand back two things, in this order, and say which field each goes in. If the project's description already holds the instructions text, say so and tell the reader to move it.

0. **The description**, one line, for the field under the title: `[PROJECT]: [WHAT IT HOLDS]. The rules are in Instructions.`
1. **Project instructions**, from `references/project-instructions.md`, with the folder path filled in and nothing else changed. It goes in the Instructions panel. Show it whole, in one code block and nothing else inside the fence.

The instructions go into a field only the reader can fill: a task can create project docs and cannot set the project's instructions or description, and the shell a task runs in is a Linux space apart from the reader's computer, so it cannot put text on their clipboard either. Do not try; hand the text back and say where it goes. The text goes in a code block of its own, which carries a copy button in the app.

## End

Report what exists now: the project docs by name and the two fields waiting for a paste. Name one day-one check: from the phone, ask something a project doc alone can answer.

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never ask what the reader has already said. Silence is never a yes: a yes is a tap on the control or a word.

## What this skill does not do

It does not write into the folder. It does not set any setting. It does not paste anything anywhere; it hands text back. It does not hand back the account-wide instructions; any of the kit's own project setups, or the core plugin's setup, does.
