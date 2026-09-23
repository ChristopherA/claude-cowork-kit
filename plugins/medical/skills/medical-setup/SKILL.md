---
name: medical-setup
description: Sets up the medical project: the privacy floor, three questions, then questions.md and timeline.md as project docs and the instructions to paste. Use for "set up my medical project", "medical setup".
---

# Setup

Build the medical project the Claude Cowork Kit describes, from three answers. Say what the folder does and does not protect before anything else, create what a task can create, the two project docs, and hand back what only the reader can paste, the project instructions. Read the records folder if it is reachable; do not write into it.

The text this skill hands back is in `references/`, generated from the kit's explainer when the plugin was packaged: `medical-instructions.md` (the project instructions). Use it as it is; do not rewrite it, and do not paraphrase it into the conversation. Fill in only the folder path where it is marked.

## What a task can and cannot do

A task can create project docs in the project it runs in and read a connected folder. It cannot set Settings, set the project's approval mode, create a project, connect a folder, or install a plugin; those are the reader's, in the app. Say which is which as you go, so the reader never waits for something that will not happen.

## Before the first question

Check whether a project doc named `timeline.md` already exists. If it does, this project is already set up: say so and stop. Do not run setup twice.

Then say plainly, in a short paragraph of your own words, what this project does and does not protect, before asking anything. The records stay in the folder on the reader's computer, and the project docs hold only what they would be relaxed about syncing: a list of questions for appointments and a bare timeline of visit dates, nothing clinical. That keeps the records out of project knowledge, out of every other project, and off the phone. It does not keep them off Anthropic's servers: a session that reads a record to answer sends that record to the session, which runs in the cloud. Credentials and logins for portals never go in a connected folder or a pasted message. This project should stay in the mode that asks before acting, which only the reader can set. And if Claude can use the reader's screen at all, patient portals and health apps should be blocked from it in Cowork's settings, which is also the reader's to do. Ask whether they want to go on; a reader who draws the line further back can stop here with nothing created.

## Three questions, one at a time

Ask each, wait for the answer, and reflect it back in a phrase before the next. Ask through the app's question control where there is a choice, the recommended option first. Skip any the reader has already answered in their request.

1. **The folder.** Where the records folder is on their computer. If they name it, confirm you can reach it; if you cannot, say so and continue from their description, and say that the visit-prep and record-a-visit skills need the folder and run at the desk. If it is reachable, look only at the top-level folders and file names, enough to describe how the records are arranged; do not read a record, and do not quote anything from one.
2. **Their clinicians, by role.** The roles they see, such as a primary care doctor, a specialist by specialty, a dentist; no names are needed, and the timeline uses roles, not names. Do not ask about conditions, medications, or results; those are in the folder, and this skill does not read them.
3. **The next appointment.** The date and the clinician's role, if known. If there is none scheduled, say that is fine and leave the timeline's next-visit line out.

## Create the two project docs

Create `questions.md` as a project doc: a heading, `Questions for my next appointment`, and nothing else. The visit-prep skill fills it, and the reader reads it from the phone in the waiting room.

Create `timeline.md` as a project doc: a heading, one line naming the form of each entry (date, clinician role, purpose, nothing clinical), and the next appointment as its first line if the reader gave one, marked as upcoming. Nothing from the folder goes in it.

Read both back and confirm they exist as project docs. The app may file them under a `claude/` folder inside the project; that is fine, and the other skills find them by name. If project docs cannot be created from a task, say so plainly, show the two texts in full so the reader can add them however the app allows, and say that the other two skills depend on them.

## Hand back the text to paste

The project page has two text fields that look alike, a one-line description under the title and an Instructions panel at the side, and readers put the instructions in the description. So hand back two things, in this order, and say which field each goes in. If the project's description already holds the instructions text, say so and tell the reader to move it.

0. **The description**, one line, for the field under the project's title. Offer this: `Medical records: visits, results, and questions for appointments. The rules are in Instructions; the records are in [folder name] and stay there.` with the folder name filled in.

The instructions go into a field only the reader can fill: a task can create project docs and cannot set the project's instructions or description, and the shell a task runs in is a Linux space apart from the reader's computer, so it cannot put text on their clipboard either. Do not try; hand the text back and say where it goes. The text goes in a code block of its own, which carries a copy button in the app.

1. **Project instructions**, from `references/medical-instructions.md`, with the folder path filled in where it is marked and nothing else changed. It goes in the Instructions panel on the project's page, not in the project's description.

Show the block whole, one code block, and nothing else inside the fence.

## End

Report what exists now: the two project docs by name and the two fields waiting for a paste, the description and Instructions. Then name the three things only the reader can do, in order: paste the instructions; check that the project is in the mode that asks before acting; and, if Claude can use the screen, block patient portals and health apps from it in Cowork's settings. Then name the day-one check: from the phone with the computer closed, open the project and ask for the questions list; it should come back empty, with no record in it.

## What this skill does not do

It does not read or quote a record, and it does not write into the folder. It does not set any setting, set the approval mode, create a project, connect a folder, or install a plugin. It does not paste anything anywhere; it hands text back. It does not hand back the account-wide instructions; the core plugin's setup does. It does not run twice on a project that already has a timeline.
