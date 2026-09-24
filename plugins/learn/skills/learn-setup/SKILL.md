---
name: learn-setup
description: Sets up the learning binder: an interview, then mission.md, curriculum.md and progress.md as Context documents and the instructions to paste. Use for "set up my learning binder", "I want to learn".
---

# Setup

Build the learning binder the Claude Cowork Kit describes, from a short interview. Create what a task can create, the three Context documents, and hand back what only the reader can paste, the project instructions. Read the materials folder if it is connected; do not write into it.

The texts this skill hands back are in `references/`, generated from the kit's docs when the plugin was packaged: `learning-instructions.md` (the project instructions), `global-instructions.md` (the account-wide instructions) and `voices.md` (the three voices). Use them as they are; do not rewrite them, and do not paraphrase them into the conversation. Fill in only the marked brackets.

The shape of the interview, a mission and a curriculum with an intuition target per lesson, is learned from Matt Pocock's teach skill and derwells's learn skill, both written for Claude Code with tooling; only the shapes are taken, and the documents here are plain markdown the reader can read on a phone.

## What a task can and cannot do

A task can read the project's Context documents, create Context documents in the project it runs in, read a connected folder, and read the reader's Account instructions. It cannot change Settings, set the project's approval mode, create a project, connect a folder, install a plugin, or send anything; those are the reader's, in the app. Say which is which as you go, so the reader never waits for something that will not happen.

## Before the first question

Before anything else, check whether this project already holds another binder: `map.md` is the research binder's, `mission.md` the learning binder's, `priorities.md` the week binder's, `categories.md` the money binder's and `timeline.md` the medical binder's. If one of them is here and it is not this binder's own, say which binder this project holds, that each binder needs a project and a folder of its own, and stop; this binder's documents created here would mix the two.

Check which of `mission.md`, `curriculum.md` and `progress.md` already exist. If all three do, this binder is already set up: say so, offer to read `progress.md` back and pick up from there, and stop. Do not run setup twice. A document that exists is kept and read back, never recreated; say which you kept. If some exist and not all, an earlier setup stopped partway: say so, ask only what the missing ones need, and take the rest from the ones kept.

## The interview, one question at a time

Ask as the Asking section says, grouping the questions whose answers do not depend on each other in one control and putting the dependent ones after. Skip any the reader has already answered in their request.

1. **What.** The subject, skill, or exam, in a phrase. If it is an exam, its name and format if they know it.
2. **Why, and by when.** One or two sentences on why now, and a date if there is one. If there is no date, say that the mission will carry none rather than invent a horizon.
3. **How they will know.** What done looks like: an exam passed, a thing built, a conversation held, a chapter explained to someone. Offer those four as choices and take a free answer over any of them.
4. **Where they stand.** Their current level, in their own words, and what they already know that is nearby. This is what the first lesson builds from, so ask for the honest version, not the modest one.
5. **How they like to learn.** Offer a few: worked examples first, the big picture first, problems to fail at before any explanation, reading then discussion. Recommend problems first, because intuition-first teaching leans on it, and take their answer over the recommendation.
6. **The materials.** Where the book, papers, or course files are on their computer, or whether there are none yet. If they name a folder, confirm you can reach it; if you cannot, say so and continue from their description, marking in `mission.md` that the folder is to be checked at the desk.

## Look at the materials

If the folder is reachable, read it before drafting the curriculum: the top-level folders, a sample of file names in each, a table of contents if there is one. Describe what is there in a few sentences. If it is not reachable, or there are no materials, build the curriculum from the subject and the reader's answers and say that it will be revised once the materials are in view.

## Create the three Context documents

Create `mission.md` as a Context document: what they are learning, why, by when, how they will know, where they stand today, how they like to learn, and where the materials are. Short enough to read on a phone; a screen at most.

Draft `curriculum.md` before creating it: units, and under each unit its lessons, one line per lesson naming the one idea that lesson is meant to make intuitive. Aim for lessons of about thirty minutes each. Show the draft whole and wait for a yes; a no or an edit changes the draft. Then create it as a Context document.

Create `progress.md` as a Context document: a heading, the three states as sections in this order, settled, shaky, untested, and every lesson from the curriculum listed under untested. Nothing is settled on day one.

Read all three back and confirm they exist as Context documents. The app may file them under a `claude/` folder inside the project; that is fine, and the other skills find them by name. If Context documents cannot be created from a task, say so plainly, show the three texts in full so the reader can add them however the app allows, and say that the lesson and quiz skills depend on them.

## The account block

Before the project instructions, read the reader's Account instructions if you can see them. If they carry the kit's block, say so and name the voice in it; do not ask the voice again. If they do not, or you cannot see them, ask which voice they want, plain, warm or archivist, one phrase each from `references/voices.md`, plain first as the safe default, and hand back `references/global-instructions.md` with that voice substituted where marked, in a code block of its own: it goes in Settings, Account, "Instructions for Claude", reaches every chat on the account, casual chat included, and is pasted once for all the kit's binders. If the field already holds text of the reader's own, say to add the block below it and cut whatever the two say twice. No plugin has to be installed before this one.

## Hand back the text to paste

The project page has two text fields that look alike, a one-line description under the title and an Instructions panel at the side, and readers put the instructions in the description. So hand back two things, in this order, and say which field each goes in. If the project's description already holds the instructions text, say so and tell the reader to move it.

0. **The description**, one line, for the field under the project's title. Offer this: `Learning [subject]: the plan, the progress record, and the practice. The rules are in Instructions; the materials are in [folder name].` with the subject and the folder name filled in.

The instructions go into a field only the reader can fill: a task can create Context documents and cannot set the project's Instructions or description, and the shell a task runs in is a Linux space apart from the reader's computer, so it cannot put text on their clipboard either. Do not try; hand the text back and say where it goes. The text goes in a code block of its own, which carries a copy button in the app.

1. **Project instructions**, from `references/learning-instructions.md`, with the subject and the folder path filled in where the brackets are and nothing else changed. It goes in the Instructions panel on the project's page, not in the one-line description under the title, which is a label.

Show the block whole, one code block, and nothing else inside the fence.

## The Learning style

Say, once, that Claude has a Learning style in the style menu that makes it ask rather than answer. It is optional: a task cannot turn it on, whether it carries into a Cowork task is untested, and nothing in this binder depends on it, since the lesson skill does that work inside a task.

## End

Report what exists now: the three Context documents by name, and the two fields waiting for a paste, the one-line description under the title and the Instructions panel. Then name the day-one checks, in order: in this project, say `next lesson` and see whether it opens with one concept rather than a survey; if they turned the Learning style on, ask a direct question about the subject and see whether it answers or asks; from the phone with the computer closed, ask where the progress record says you are. Do not run them; the reader does. Say that the first lesson is `next lesson`, and that `quiz me` works once there is something to quiz. End with one word for completeness: full, partial (with what is missing), or minimal (stopped early).

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never ask what the reader has already said. Silence is never a yes: a yes is a tap on the control or a word.

## What this skill does not do

It does not teach; the lesson skill does. It does not write into the materials folder. It does not set any setting, turn on a style, connect a folder, create a project, or install a plugin. It does not paste anything anywhere; it hands text back. It hands back the account-wide instructions only when the Account field does not carry them already. It does not run twice on a binder whose three Context documents all exist.
