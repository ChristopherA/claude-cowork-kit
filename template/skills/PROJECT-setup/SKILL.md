---
name: PROJECT-setup
description: Sets up the [PROJECT] project: a short interview, the project docs, and the instructions to paste. Use for "set up my [PROJECT] project", "[PROJECT] setup".
---

# Setup

Build the [PROJECT] project from a few answers. Create what a task can create, the project docs, and hand back what only the reader can paste, the project instructions. Read the folder if one is connected; do not write into it during setup.

The text this skill hands back is in `references/project-instructions.md`. Use it as it is; do not rewrite or paraphrase it. Fill in only the folder path.

## Before the first question

Check whether the project docs already exist. If they do, say so and stop; do not run setup twice.

## The interview, one question at a time

Ask each through the app's question control where there is a choice, recommended option first, and wait. Reflect the answer back in a phrase before the next. Skip any the reader already answered.

1. **The folder.** Where the files for this project are on their computer, or whether there are none yet. If they name a folder, confirm you can reach it; if you cannot, say so and continue from their description.
2. [**THE QUESTION THAT SHAPES THE FIRST DOC.**]
3. [**THE QUESTION THAT SHAPES THE SECOND DOC, IF ANY.**]

## Create the project docs

Create [`FIRST-DOC.md`] as a project doc: [WHAT IT HOLDS, IN ONE SENTENCE]. Create [`SECOND-DOC.md`] the same way. Read each back and confirm it exists as a project doc. If project docs cannot be created from a task, say so, show the texts in full, and say the rest depends on them.

## Hand back the text to paste

The project page has two text fields that look alike, a one-line description under the title and an Instructions panel at the side. Hand back two things, in this order, and say which field each goes in.

0. **The description**, one line, for the field under the title: `[PROJECT]: [WHAT IT HOLDS]. The rules are in Instructions.`
1. **Project instructions**, from `references/project-instructions.md`, with the folder path filled in and nothing else changed. It goes in the Instructions panel. Show it whole, in one code block and nothing else inside the fence.

A task cannot set the project's instructions or description, change Settings, or put text on the reader's clipboard; hand the text back and say where it goes.

## End

Report what exists now: the project docs by name and the two fields waiting for a paste. Name one day-one check: from the phone, ask something a project doc alone can answer.

## What this skill does not do

It does not write into the folder. It does not set any setting. It does not paste anything anywhere; it hands text back. It does not hand back the account-wide instructions; the core plugin's setup does.
