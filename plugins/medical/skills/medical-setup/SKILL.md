---
name: medical-setup
description: Sets up the medical binder: the privacy floor, three questions, questions.md and timeline.md as Context documents and the instructions to paste. Use for "set up my medical binder", "medical setup".
---

# Setup

Build the medical binder the Claude Cowork Kit describes, from three answers. Say what the folder does and does not protect before anything else, create what a task can create, the two Context documents, and hand back what only the reader can paste, the project instructions. Read the records folder if it is reachable; do not write into it, except to create the standing files as headed empty files when the reader has none and says yes.

The texts this skill hands back are in `references/`, generated from the kit's docs when the plugin was packaged: `medical-instructions.md` (the project instructions), `global-instructions.md` (the account-wide instructions) and `voices.md` (the three voices). Use them as they are; do not rewrite them, and do not paraphrase them into the conversation. Fill in only the folder path where it is marked.

## What a task can and cannot do

A task can read the project's Context documents, create Context documents in the project it runs in, read a connected folder, and read the reader's Account instructions. It cannot change Settings, set the project's approval mode, create a project, connect a folder, install a plugin, or send anything; those are the reader's, in the app. Say which is which as you go, so the reader never waits for something that will not happen.

## Before the first question

Check which of `questions.md` and `timeline.md` already exist. If `timeline.md` does, this binder is already set up: say so and stop. Do not run setup twice. A Context document that exists is kept and read back, never recreated; say which you kept.

Then say plainly, in a short paragraph of your own words, what this binder does and does not protect, before asking anything. The records stay in the folder on the reader's computer, and the Context documents hold only what they would be relaxed about syncing: a list of questions for appointments and a bare timeline of visit dates, nothing clinical. That keeps the records out of the project's Context, out of every other binder, and off the phone. It does not keep them off Anthropic's servers: a session that reads a record to answer sends that record to Claude on Anthropic's servers, whichever kind of session it is. Credentials and logins for portals never go in a connected folder or a pasted message. This project should stay in the mode that asks before acting, which only the reader can set. And if Claude can use the reader's screen at all, patient portals and health apps should be blocked from it in Cowork's settings, which is also the reader's to do. Ask whether they want to go on; a reader who draws the line further back can stop here with nothing created.

## Three questions, one at a time

Ask as the Asking section says, grouping the questions whose answers do not depend on each other in one control and putting the dependent ones after. Skip any the reader has already answered in their request.

1. **The folder.** Where the records folder is on their computer. If they name it, confirm you can reach it; if you cannot, say so and continue from their description, and say that the visit-prep and record-a-visit skills need the folder and run at the desk. If it is reachable, look only at the top-level folders and file names, enough to describe how the records are arranged; do not read a record, and do not quote anything from one.
2. **Their clinicians, by role.** The roles they see, such as a primary care doctor, a specialist by specialty, a dentist; no names are needed, and the timeline uses roles, not names. Do not ask about conditions, medications, or results; those are in the folder, and this skill does not read them.
3. **The next appointment.** The date and the clinician's role, if known. If there is none scheduled, say that is fine and leave the timeline's next-visit line out.

## Create the two Context documents

Create `questions.md` as a Context document: a heading, `Questions for my next appointment`, and nothing else. The visit-prep skill fills it, and the reader reads it from the phone in the waiting room.

Create `timeline.md` as a Context document: a heading, one line naming the form of each entry (date, clinician role, purpose, nothing clinical), and the next appointment as its first line if the reader gave one, marked as upcoming. Nothing from the folder goes in it.

Read both back and confirm they exist as Context documents. The app may file them under a `claude/` folder inside the project; that is fine, and the other skills find them by name. If Context documents cannot be created from a task, say so plainly, show the two texts in full so the reader can add them however the app allows, and say that the other skills depend on them.

## The folder's standing files

If the folder is reachable and holds none of the standing files the instructions name, offer, through the question control, to create them as empty files with a heading each: an overview, medications, providers, an action plan, a functional log, a research file, and one file per condition the reader names. Show the list first and create them only on a yes; nothing goes in them but the heading, and the record-a-visit skill fills them. If the folder already has its own shape, describe it and create nothing.

## The account block

Before the project instructions, read the reader's Account instructions if you can see them. If they carry the kit's block, say so and name the voice in it; do not ask the voice again. If they do not, or you cannot see them, ask which voice they want, plain, warm or archivist, one phrase each from `references/voices.md`, plain first as the safe default, and hand back `references/global-instructions.md` with that voice substituted where marked, in a code block of its own: it goes in Settings, Account, "Instructions for Claude", reaches every chat on the account, casual chat included, and is pasted once for all the kit's binders. If the field already holds text of the reader's own, say to add the block below it and cut whatever the two say twice. No plugin has to be installed before this one.

## Hand back the text to paste

The project page has two text fields that look alike, a one-line description under the title and an Instructions panel at the side, and readers put the instructions in the description. So hand back two things, in this order, and say which field each goes in. If the project's description already holds the instructions text, say so and tell the reader to move it.

0. **The description**, one line, for the field under the project's title. Offer this: `Medical records: visits, results, and questions for appointments. The rules are in Instructions; the records are in [folder name] and stay there.` with the folder name filled in.

The instructions go into a field only the reader can fill: a task can create Context documents and cannot set the project's Instructions or description, and the shell a task runs in is a Linux space apart from the reader's computer, so it cannot put text on their clipboard either. Do not try; hand the text back and say where it goes. The text goes in a code block of its own, which carries a copy button in the app.

1. **Project instructions**, from `references/medical-instructions.md`, with the folder path filled in where it is marked and nothing else changed. It goes in the Instructions panel on the project's page, not in the one-line description under the title, which is a label.

Show the block whole, one code block, and nothing else inside the fence.

## End

Report what exists now: the two Context documents by name and the two fields waiting for a paste, the one-line description under the title and the Instructions panel. Then name the three things only the reader can do, in order: paste the instructions; check that the mode that asks before acting is on, wherever the app sets it; and, if Claude can use the screen, block patient portals and health apps from it in Cowork's settings. Then name the day-one check: from the phone with the computer closed, open the project and ask for the questions list; it should come back empty, with no record in it. End with one word for completeness: full, partial (with what is missing), or minimal (stopped early).

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never ask what the reader has already said. Silence is never a yes: a yes is a tap on the control or a word.

## What this skill does not do

It does not read or quote a record. It writes into the folder only the headed standing files the reader said yes to, and nothing into them but the heading. It does not set any setting, set the approval mode, create a project, connect a folder, or install a plugin. It does not paste anything anywhere; it hands text back. It hands back the account-wide instructions only when the Account field does not carry them already. It does not run twice on a binder that already has a timeline.
