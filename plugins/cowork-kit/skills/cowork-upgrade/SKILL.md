---
name: cowork-upgrade
description: Brings a binder made with an earlier release up to this one: compares its documents and folder with what its setup makes now and proposes each change, one at a time. Use for "upgrade my binder".
---

# Upgrade a binder

A binder's setup runs once. Later releases of the kit change what a setup writes, a template's wording, a folder the binder keeps, the shape of a note, and nothing carries those changes into a binder that already exists, so its skills go on reading the old documents and following the old wording. This skill compares one binder with what its setup makes in this release and proposes each difference as a change, one at a time, keeping everything the reader filled in or decided for themselves.

## Which binder

Look at the project's Context documents to see which binder this is: `map.md` is the research binder's, `mission.md` the learning binder's, `priorities.md` the week binder's, `categories.md` the money binder's and `timeline.md` the health binder's. If none is here, say that this project holds no binder made by the kit and stop; if more than one is, ask which to upgrade. Upgrade one binder per run.

## What this release makes

The skill carries, in its references, what each binder's setup is in this release: `references/<binder>-setup.md` is that binder's setup skill as it ships, and the other files beginning with the binder's name are the text it uses, the project instructions and, for research, the templates for `rules.md` and `map.md` (`research-rules-template.md`, `research-map-template.md`). The first line of each names the release it came from. Read the binder's setup reference and its texts in full, for what each Context document should contain, which folders the binder keeps and what its notes look like; the setup's own steps, its questions and its order, are not run here.

## Before starting

Read every Context document the binder has, in full, and check whether its folder is reachable; the documents can be upgraded without the folder, the folder and its notes cannot. Then say what is about to be compared, and that nothing changes without a yes.

## Compare and propose

Go through the binder in this order, and for each difference say what this release has, what the binder has, and whether the difference is the kit's or the reader's. A difference that could be the reader's own decision (a rule they relaxed, a folder they renamed, a convention of theirs) is asked about, with keeping theirs recommended; one that is plainly the old release's wording is proposed as a change.

1. **The Context documents.** Compare each with its template or with what the setup reference says it holds. Propose each change by itself, showing the old wording and the new, and fill the new wording from what the binder already says (the folder path, the reader's sections, their conventions), never from the template's brackets. When a wording this release changes also appears in another of the binder's Context documents (a renamed binder in the instructions and in the description's "not here" list, say), propose the matching change in each, together. A section the reader left as brackets, or marked as not written yet, stays as it is unless they want to write it now.
2. **The project instructions.** A task cannot change the Instructions panel. If the instructions are visible here and differ from this release's text, hand back the new text in a code block of its own, saying it goes in the project's Instructions panel and replaces what is there.
3. **The folder.** For each folder this release's setup names that the binder's folder lacks, offer to create it, or to name an existing folder of the reader's as its home and record that in the description; for example, a research binder's empty `notes/` can become its `topics/`, or stay and be named as the topic home.
4. **The notes.** Notes written in an earlier shape are upgraded one at a time, each shown and written on a yes, never in bulk. For the research binder, run the research plugin's census first to find them (its description-check skill's script), then for each old source note: add the citation fields from the document itself, make and check the citation line with the cite script, move an evidence remark from the key points into an EVIDENCE block, make the note compound if an original sits beside it (the original into `originals/` under the note's name, a rendition written with the pdf-info script), check its quotes, and remove the old flat file. A note whose level does not match what it holds is raised (adding what the level needs) or lowered (dropping what it does not), asked as a choice with a recommendation from how the reader will use the source. The scripts are the research plugin's, run in place from where the desktop app installed it, as that plugin's skills describe under running a script; if it is not installed, or its version differs from this release, say so (an older install is upgraded in the Claude app under Customize, Plugins) and do the same work by reading.

Deleting or moving a file in the folder needs the reader's permission in the app as well as their yes here. Say so before the first one, and ask for the permission once for the session rather than once per file. If the link to the computer drops and comes back, the app may ask for the permission again; say before asking that it is the same permission, asked again after the reconnect, so the second prompt does not look like a repeat. A note renamed, such as an undated work whose date turns up, is a move: show the old name and the new, find every link to the old name and fix it in the same change, and delete the old file only once the new one is written and nothing links to the old.

## What not to do

Do not rewrite anything the reader wrote: their sections, their notes' contents, their own rules. Do not apply changes in bulk, or carry a yes from one change to the next. Do not touch another binder's documents or folder. Do not run the setup again; it would ask its questions from the start and overwrite the reader's answers.

## Ending

Report what changed, what the reader kept on purpose, and what is left (notes not yet upgraded, instructions waiting to be pasted). On a yes, record the release: in a research binder, update the Kit release line under Where the folder is in `map.md` to this release and today's date; in another binder, add a line saying so at the end of its main document. The next upgrade starts from there. End with one word for completeness: full, or partial with what is left.

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never build an option or a draft from outside knowledge of the reader, such as what is public about the account's name: draw only on what they have said and what their folder shows. Never ask what the reader has already said. Silence is never a yes: a yes is a tap on the control or a word.
