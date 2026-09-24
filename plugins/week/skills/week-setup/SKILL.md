---
name: week-setup
description: Sets up the week binder: three questions, then priorities.md as a Context document and the short instructions to paste. Use for "set up my week binder", "week setup".
---

# Setup

Build the week binder the Claude Cowork Kit describes, from three answers. Create what a task can create, the one Context document, and hand back what only the reader can paste, the project instructions. Read the working folder if it is reachable; do not write into it.

The texts this skill hands back are in `references/`, generated from the kit's docs when the plugin was packaged: `week-instructions.md` (the project instructions), `global-instructions.md` (the account-wide instructions) and `voices.md` (the three voices). Use them as they are; do not rewrite them, and do not paraphrase them into the conversation. Fill in only the folder path where the block marks it.

## What a task can and cannot do

A task can read the project's Context documents, create Context documents in the project it runs in, read a connected folder, and read the reader's Account instructions. It cannot change Settings, set the project's approval mode, create a project, connect a folder, install a plugin, or send anything; those are the reader's, in the app. Say which is which as you go, so the reader never waits for something that will not happen.

## Before the first question

Before anything else, check whether this project already holds another binder: `map.md` is the research binder's, `mission.md` the learning binder's, `priorities.md` the week binder's, `categories.md` the money binder's and `timeline.md` the medical binder's. If one of them is here and it is not this binder's own, say which binder this project holds, that each binder needs a project and a folder of its own, and stop; this binder's documents created here would mix the two.

Check whether a Context document named `priorities.md` already exists. If it does, this binder is already set up: say so, offer to update the priorities instead, and stop. Do not run setup twice.

## Three questions, one at a time

Ask as the Asking section says, grouping the questions whose answers do not depend on each other in one control and putting the dependent ones after. Skip any the reader has already answered in their request.

1. **The folder.** Where the working files are on their computer: the folder that holds drafts, lists, threads they are keeping, earlier replies. If they name a folder, confirm you can reach it; if you cannot, say so, continue from their description, and mark in `priorities.md` that the folder is to be checked at the desk. The folder is reachable only from a task at the desk; the Context document this skill creates is reachable from the phone as well, which is why the priorities live in the document and not in the folder.
2. **Current priorities.** The two or three things that matter this month, in order, each in a phrase, and the one eating their attention right now. Not everything they owe; the things a plan should bend around. If they offer eight, ask which three would still matter if the other five slipped.
3. **The other binders.** Which of the kit's other binders exist for them: a research binder (notes and reading), a learning binder, a money binder, a medical binder. Offer the four, more than one allowed; choosing none, or saying so in their own words, means none yet. The instructions send notes to the research binder's inbox and money and medical questions to their binders; the answer decides whether those redirects name a binder that exists or one the reader has still to build.

## Create the Context document

Create `priorities.md` as a Context document: a heading, today's date on a line of its own, the priorities from question 2 in order with the one eating attention marked, and a short section naming which other binders exist from question 3, with a line for any that do not yet, so a redirect to one is read as "when you build it". Keep it short enough to read on a phone. Leave nothing in brackets; where an answer is missing, ask rather than invent.

Read it back and confirm it exists as a Context document. The app may file it under a `claude/` folder inside the project; that is fine, and the other skills find it by name. If a Context document cannot be created from a task, say so plainly, show the text in full so the reader can add it however the app allows, and say that the planning skill depends on it.

## The account block

Before the project instructions, read the reader's Account instructions if you can see them. If they carry the kit's block, say so and name the voice in it; do not ask the voice again. If they do not, or you cannot see them, ask which voice they want, plain, warm or archivist, one phrase each from `references/voices.md`, plain first as the safe default, and hand back `references/global-instructions.md` with that voice substituted where marked, in a code block of its own: it goes in Settings, Account, "Instructions for Claude", reaches every chat on the account, casual chat included, and is pasted once for all the kit's binders. If the field already holds text of the reader's own, say to add the block below it and cut whatever the two say twice. No plugin has to be installed before this one.

## Hand back the text to paste

The project page has two text fields that look alike, a one-line description under the title and an Instructions panel at the side, and readers put the instructions in the description. So hand back two things, in this order, and say which field each goes in. If the project's description already holds the instructions text, say so and tell the reader to move it.

0. **The description**, one line, for the field under the project's title. Offer this: `Running my week: tasks, planning, drafts, triage. The rules are in Instructions; the working files are in [folder name].` with the folder name filled in.

The instructions go into a field only the reader can fill: a task can create Context documents and cannot set the project's Instructions or description, and the shell a task runs in is a Linux space apart from the reader's computer, so it cannot put text on their clipboard either. Do not try; hand the text back and say where it goes. The text goes in a code block of its own, which carries a copy button in the app.

1. **Project instructions**, from `references/week-instructions.md`, with the folder path from question 1 in place of the bracket and nothing else changed. It goes in the Instructions panel on the project's page, not in the one-line description under the title, which is a label.

Show the block whole, one code block, and nothing else inside the fence.

## End

Report what exists now: the Context document by name, and the two fields waiting for a paste, the one-line description under the title and the Instructions panel. Then name the three day-one checks, in order: at the desk, dump a mess of obligations into a task and see whether a short ordered list comes back with nothing around it; from the phone with the computer closed, ask what the current priorities are, which the document alone can answer; hand over a message and see whether a draft comes back and the task stops there. Do not run them; the reader does. End with one word for completeness: full, partial (with what is missing), or minimal (stopped early).

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never ask what the reader has already said. Silence is never a yes: a yes is a tap on the control or a word.

## What this skill does not do

It does not write into the working folder. It does not set any setting, create a project, connect a folder, install a plugin, or send anything. It does not paste anything anywhere; it hands text back. It hands back the account-wide instructions only when the Account field does not carry them already. It does not run twice on a project that already has a priorities document.
