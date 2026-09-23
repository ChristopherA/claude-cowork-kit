---
name: learn-setup
description: Sets up the learning project: an interview, then mission.md, curriculum.md and progress.md as project docs and the instructions to paste. Use for "set up my learning project", "set my course".
---

# Setup

Build the learning project the Claude Cowork Kit describes, from a short interview. Create what a task can create, the three project docs, and hand back what only the reader can paste, the project instructions. Read the materials folder if it is connected; do not write into it.

The text this skill hands back is in `references/`, generated from the kit's explainer when the plugin was packaged: `learning-instructions.md` (the text for the Instructions panel). Use it as it is; do not rewrite it, and do not paraphrase it into the conversation. Fill in only the marked brackets.

The shape of the interview, a mission and a curriculum with an intuition target per lesson, is learned from Matt Pocock's teach skill and derwells's learn skill, both written for Claude Code with tooling; only the shapes are taken, and the docs here are plain markdown the reader can read on a phone.

## What a task can and cannot do

A task can create project docs in the project it runs in and read a connected folder. It cannot write Settings, create a project, connect a folder, or install a plugin; those are the reader's, in the app. Say which is which as you go, so the reader never waits for something that will not happen.

## Before the first question

Check whether a project doc named `mission.md` already exists. If it does, this project is already set up: say so, offer to read `progress.md` back and pick up from there, and stop. Do not run setup twice.

## The interview, one question at a time

Ask each through the app's question control where there is a choice, the first option being the one to take when unsure, and wait for the answer. Reflect it back in a phrase before the next. Skip any the reader has already answered in their request.

1. **What.** The subject, skill, or exam, in a phrase. If it is an exam, its name and format if they know it.
2. **Why, and by when.** One or two sentences on why now, and a date if there is one. If there is no date, say that the mission will carry none rather than invent a horizon.
3. **How they will know.** What done looks like: an exam passed, a thing built, a conversation held, a chapter explained to someone. Offer those four as choices and take a free answer over any of them.
4. **Where they stand.** Their current level, in their own words, and what they already know that is nearby. This is what the first lesson builds from, so ask for the honest version, not the modest one.
5. **How they like to learn.** Offer a few: worked examples first, the big picture first, problems to fail at before any explanation, reading then discussion. Recommend problems first, because intuition-first teaching leans on it, and take their answer over the recommendation.
6. **The materials.** Where the book, papers, or course files are on their computer, or whether there are none yet. If they name a folder, confirm you can reach it; if you cannot, say so and continue from their description, marking in `mission.md` that the folder is to be checked at the desk.

## Look at the materials

If the folder is reachable, read it before drafting the curriculum: the top-level folders, a sample of file names in each, a table of contents if there is one. Describe what is there in a few sentences. If it is not reachable, or there are no materials, build the curriculum from the subject and the reader's answers and say that it will be revised once the materials are in view.

## Create the three project docs

Create `mission.md` as a project doc: what they are learning, why, by when, how they will know, where they stand today, how they like to learn, and where the materials are. Short enough to read on a phone; a screen at most.

Draft `curriculum.md` before creating it: units, and under each unit its lessons, one line per lesson naming the one idea that lesson is meant to make intuitive. Aim for lessons of about thirty minutes each. Show the draft whole and wait for a yes; a no or an edit changes the draft. Then create it as a project doc.

Create `progress.md` as a project doc: a heading, the three states as sections in this order, settled, shaky, untested, and every lesson from the curriculum listed under untested. Nothing is settled on day one.

Read all three back and confirm they exist as project docs. The app may file them under a `claude/` folder inside the project; that is fine, and the other skills find them by name. If project docs cannot be created from a task, say so plainly, show the three texts in full so the reader can add them however the app allows, and say that the lesson and quiz skills depend on them.

## Hand back the text to paste

The project page has two text fields that look alike, a one-line description under the title and an Instructions panel at the side, and readers put the instructions in the description. So hand back two things, in this order, and say which field each goes in. If the project's description already holds the instructions text, say so and tell the reader to move it.

0. **The description**, one line, for the field under the project's title. Offer this: `Learning [subject]: the plan, the progress record, and the practice. The rules are in Instructions; the materials are in [folder name].` with the subject and the folder name filled in.

The instructions go into a field only the reader can fill: a task can create project docs and cannot set the project's instructions or description, and the shell a task runs in is a Linux space apart from the reader's computer, so it cannot put text on their clipboard either. Do not try; hand the text back and say where it goes. The text goes in a code block of its own, which carries a copy button in the app.

1. **Project instructions**, from `references/learning-instructions.md`, with the subject and the folder path filled in where the brackets are and nothing else changed. It goes in the Instructions panel on the project's page, not in the project's description; the description is visible to a task too, but it is a label, and the reader should not have to know that it happens to work.

Show the block whole, one code block, and nothing else inside the fence.

## The Learning style

Say that Claude has a built-in Learning style, in the style menu, that makes it ask questions rather than hand over answers, and that the reader should turn it on for this project: it does most of what the instructions ask for and does it more reliably than a paragraph can. A task cannot turn it on. Say also that whether the style carries into a Cowork task is something to check on day one, below.

## End

Report what exists now: the three project docs by name, and the two fields waiting for a paste, the description and Instructions. Then name the day-one checks, in order: in this project, with the style turned on, ask Claude a direct question about the subject and see whether it answers or asks; from the phone with the computer closed, ask where the progress record says you are. Do not run them; the reader does. Say that the first lesson is `next lesson`, and that `quiz me` works once there is something to quiz.

## What this skill does not do

It does not teach; the lesson skill does. It does not write into the materials folder. It does not set any setting, turn on a style, connect a folder, create a project, or install a plugin. It does not paste anything anywhere; it hands text back. It does not hand back the account-wide instructions; the core plugin's setup does. It does not run twice on a project that already has a mission.
