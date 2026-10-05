---
name: research-import
description: Files the works cited in a pile of the reader's own writing: each citation checked against its work, filed in one batch, with a corrections report. Use for "import the sources from my drafts".
---

# Import sources from your writing

The reader hands over writing of their own, drafts, a blog series, published pieces, and wants to keep what it cites. The source-note skill files one source at a time and asks why each was saved; this skill does the whole pile at once, at the citation level, and checks every citation against the work it names. Checking at that scale finds errors in the reader's writing, a wrong year, a title cut short, authors out of order, a claim the cited work does not make, and the list of those is often worth more to the reader than the notes, so it is handed back on its own.

## Where this runs

This skill belongs to the research binder, whose Context documents are `rules.md`, `map.md` and `inbox.md`. Before anything else, check that they are here. If not, this project belongs to another binder: say which binder this skill is for and stop, so nothing is written into the wrong folder or the wrong documents; if this is the right binder and it is not set up yet, offer its setup, `set up my research binder`.

## Before starting

Read `rules.md` and then `map.md` if you have not this conversation: the folder path, where sources and the reader's own works live (`sources/` and `works/` by default), the naming rule, the link style, the citation form and the metadata a note carries, and the Topics section. Check that the research folder is reachable; importing is desk work, and if the folder cannot be reached, say so and stop.

Ask which pieces to read, if the reader has not said, and where they are: files in `inbox/`, files elsewhere in the folder, or pasted text. If any of it is paid or client work, or someone else's writing, ask before reading it into the binder; work material may not belong in a personal one. Say that the pieces are read and not changed, and that nothing is filed until the reader approves the batch.

## 1. Extract

Read every piece in full. List each work it cites, from reference lists, inline citations, footnotes and links, and for each keep the piece and the sentence that cites it: that sentence is how the reader used the work, and it is what the report and any inferred WHY SAVED are built from. Then merge the list across pieces: two entries are one work when they share a DOI or a URL, or a title and a first author. Search the sources folder and `works/` for each by its link and its title; a work with a note already is not filed again, and its new uses are listed as additions the reader may want made to that note. A work of the reader's own is a works note, not a source note, offered as the source-note skill describes, its BRIEF written from the work itself and marked as drafted; the drafts being mined are not filed as works.

Say how many pieces were read, how many citations they hold and how many distinct works that comes to.

## 2. Check each citation

Check every work against the work itself, never against memory and never against another citation of it: the DOI's landing page, the publisher's page, the work's own title page or masthead, or the page at its URL. Confirm the title in full, every author in order, the year, the container, the volume, issue and pages, and the publisher. Where the reader's writing attributes a specific fact, number or quotation to the work, look for it in the work and say whether it is there.

Give each work one status: **checked** (every field confirmed), **partly checked** (name the fields that could not be confirmed and why), or **not reachable** (the page refused, a paywall, a dead link; say which). A site the computer's network refuses is named, with the note that the organization's admin settings hold the allowlist; do not try another route to it. With many works, go through them in batches and report each batch as it finishes, so a dropped link loses one batch rather than the whole check.

## 3. Show the batch

Show the whole batch before writing anything, as a table: each work's citation line as it would be filed, its status, the piece or pieces that cite it, and the topic each use bears on, named from the reader's writing and from the topic notes and Topics lines that exist. Below the table, list the additions proposed for notes that already exist.

WHY SAVED is left out unless the reader asks for it. If they ask for it to be inferred from their writing, write each from how the piece used the work, in the form `WHY SAVED (inferred from my <piece>; confirm or replace): ...`, which the description check lists until the reader confirms or replaces it; never infer one from the work itself.

Ask for one approval for the batch through the control, with the option of leaving works out by name. A yes to the batch is a yes to each note in it as shown, and to nothing else.

## 4. File

Write each work as a flat source note at the `citation` level, named by the folder's naming rule: a `created` line, `level: citation`, the citation fields from the check, and a `checked` line saying when and against what the citation was checked, or that it could not be. The citation line comes from the source-note skill's cite script, run with `--check` on every note before it is written. A partly checked or unreachable work carries only the fields that were confirmed, and its line says what is missing rather than guessing.

```
python3 cite.py "<draft note>" ["<draft note>" ...] --check
```

Where a script runs depends on what it reads. The research folder is on the reader's computer, and a task reaches it through its link to that computer; the task's cloud workspace sees a file only once it is copied there. So a script that reads the whole folder, such as the census or the drain's candidate search, runs in the computer's own shell, in place, from the research plugin as the desktop app installed it on that computer. The app lists its installed plugins in a `manifest.json` under `~/Library/Application Support/Claude/local-agent-mode-sessions/`, two folders down (the account, then the organization) in `rpm/`, and the plugin named `research` is the folder beside it named by its `id`. Find it through the manifest, never by searching the computer for the script, since older copies of the plugin can sit elsewhere; run it from there with the computer's python3, from a scratch folder outside the research folder, and never copy it anywhere. Before running, compare the installed script's `--version` with the `__version__` line in this skill's own copy of the script. If they differ, tell the reader a newer version of the plugin is available and to upgrade it in the Claude app under Customize, Plugins, and offer to continue now by reading instead. If no installed copy is found, or it cannot be read, do the work by reading and say why. A script that needs one file, a PDF or a draft note, may instead run in the cloud workspace on a copy of that file. Either way it is never copied into the research folder or any folder of the reader's, and anything it writes reaches the folder only as this skill says, after a yes. When many files go into the folder at once, write them with the computer's shell and check each one landed by its checksum, so a dropped link to the computer can be resumed from where it stopped. Then say in one plain sentence that a script read the folder; the reader is not a programmer and does not need the mechanics, but is never left unaware that something ran. If the task cannot run scripts, do the same work by reading, as this skill says, and say that you did. Never rely on the folder's modification times: syncing and copying reset them.

Write the notes with the computer's shell, straight into the sources folder, and check each one landed by its checksum against what was approved; when the link to the computer drops, the checksums say which notes are in and the filing resumes from there. Read back a sample to confirm the format.

Then route each work to its topic, on a yes for the whole list: a work bearing on an existing topic note is offered to that note through the topic-note skill; a work bearing on a topic with no note yet goes on that topic's line in `map.md`'s Topics section, as "<topic> — not written yet; sources waiting: <links>", adding the line if the topic has none. Never write a topic pointer onto the source note itself.

## 5. The corrections report

Hand back, separately from the notes, a report for the author: for each piece, every citation that differs from the work it names (the year, the title, the authors or their order, the container, the pages), with what the piece says, what the work says and where that was checked; then every claim the piece attributes to a work that the work does not contain, quoted from the piece, with what the work says instead if anything. List the works that could not be reached, since their citations are unconfirmed rather than right. Offer to save it as `corrections-YYYY-MM-DD.md` beside the pieces it corrects, or in `inbox/` when they are not in the folder; it is the reader's to act on, and nothing in their writing is changed.

## What not to do

Do not change the reader's writing. Do not file a field the check did not confirm, or fill one from memory. Do not write a WHY SAVED the reader did not ask for, or key points, abstracts or quotes; every note filed here is at the citation level, and the source-note skill takes a work further when a topic note cites it. Do not delete the pieces or anything else from the folder; if the reader wants files moved or removed afterwards, ask, and say first that deleting needs their permission in the app. If the link to the computer drops and comes back, the app may ask for the permission again; say before asking that it is the same permission, asked again after the reconnect, so the second prompt does not look like a repeat.

## Ending

Report the counts: works filed, works already noted with additions proposed, works routed to topic notes and to waiting lines, and the corrections found. End with one word for completeness: full, or partial with what is left (works not reachable, a batch not filed).

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never build an option or a draft from outside knowledge of the reader, such as what is public about the account's name: draw only on what they have said and what their folder shows. Never ask what the reader has already said. Silence is never a yes: a yes is a tap on the control or a word.
