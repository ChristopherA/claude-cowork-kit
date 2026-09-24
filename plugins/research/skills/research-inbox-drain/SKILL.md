---
name: research-inbox-drain
description: Processes the capture inbox one item at a time into notes in the research folder, to map.md conventions. Use for "process the inbox", "drain the inbox", "file my captures".
---

# Inbox drain

Work the inbox document down to empty, one item at a time, writing real notes into the research folder. This skill is the "capture and filing are different" rule made into a routine: the reader captured without deciding, and now decides, with you doing the typing.

## Where this runs

This skill belongs to the research binder, whose Context documents are `rules.md`, `map.md` and `inbox.md`. Before anything else, check that they are here. If not, this project belongs to another binder: say which binder this skill is for and stop, so nothing is written into the wrong folder or the wrong documents; if this is the right binder and it is not set up yet, offer its setup, `set up my research binder`.

## Before starting

Read `rules.md` and then `map.md` first if you have not this conversation. The rules say how captures are drained; the description says where the folder is, how notes are named and formatted, what the reader is working on, and which conventions are settled. Every note you write follows them.

Check that the research folder is reachable. If it is not, say so and stop; the inbox is drained at the desk, not from the phone. Do not file into Context documents as a substitute.

Read `inbox.md`, and list the files in the folder's `inbox/` if it has one: those are items too, captured from the desk rather than the phone. Count both and say how many there are. If there are none, say so and stop.

## One item at a time

For each item, in order from the top:

1. Quote the item back, exactly as captured.
2. Say what you think it is, in one sentence, and where it would go: a new note (one idea, named for its claim), an addition to an existing note or thread, a source to record, something for another binder (name which, leave it in the inbox marked with the binder's name for the reader to move, and stop there for that item), or a discard. Where the candidates script is available, run it for the item first (see below); otherwise search the folder for the item's two or three most distinctive words. Then apply the rule that decides between adding and creating: if an existing note covers the idea and its title still fits with this added, propose adding to it; create a new note only when no note covers it, or when the existing note's title would stop making sense; when the capture is adjacent to a note but distinct, propose a new note that links to the existing one and a line in the existing one linking back. When in doubt, add to the existing note. Two notes on one idea are the failure that makes a folder hard to trust, and it is silent.
3. Show the note you would write, or the change you would make to an existing note, in full, formatted to `map.md`'s conventions, with a `created` date of today and a `source` line if the capture came from somewhere.
4. Wait for a yes. A no, an edit, or a redirect changes what you write; silence is not a yes.
5. On a yes: write the note into the folder, read it back to confirm it landed as shown, then remove the item from `inbox.md`; for an item that is a file in the folder's `inbox/`, ask whether to delete that file now that its note exists, delete it only on a yes, and if it is kept, say it will be offered again at the next drain. Then confirm in one line what changed and where, with the file name.

Do not batch. Do not propose the next item until the current one is written and removed. Do not expand a capture into more than it said; a one-line capture that turns out to be a thread the reader wants to think about becomes a short thread note with the capture as its first line, not an essay.

## What a capture can become

A **note** when the capture is an idea: named for the claim it makes, one idea, leading with the claim. A **thread** when it is a question the reader is chewing on, or a capture that clearly continues one already open in `map.md`'s open threads; append to the thread and say so. A **source** when it is something to read, or read: a source note in the sources folder with title, author, link, and the reader's reaction marked as theirs, per the source-note skill if it is installed. A **redirect** when it belongs to the week, money, medical or learning binder: tell the reader which, leave the item in the inbox marked with the binder's name, and move on. A **discard** when the reader says so; never on your own judgment. A **deferral** when the item cannot be filed now (the note it belongs to is unclear, a source is missing, the reader wants to think): leave it in the inbox with a one-line reason under it, so the next drain starts from the reason rather than from scratch. Never delete an item you did not file.

## When you cannot tell

Ask one question, the one whose answer decides where it goes. Do not ask two. Do not guess at a folder because the capture is short. Every question with a choice in it, and every wait for a yes, goes through the app's question control with the recommended option first, so the reader answers with a tap rather than typing.

## Ending

When the inbox is empty, or the reader stops, report: how many items were filed and where, how many were redirected and to which binder, how many were deferred and why, how many remain. End with one word for completeness: full (inbox empty), partial (items remain, with the count), or minimal (stopped early), and name anything left open. If anything you filed touches what `map.md` says the reader is working on, say so in one sentence; do not edit `map.md` unless asked.

## The candidates script

`scripts/candidates.py` searches the research folder for the distinctive words of a capture and prints the notes that mention them, most matches first, as JSON. It reads only; it needs code execution enabled and the folder path. Run it once per item:

```
python3 scripts/candidates.py --folder "<research folder path>" --text "<the capture>" --limit 5
```

The script runs inside the task, in the task's own working space on the side where the research folder is mounted; it never runs on the reader's computer and never goes into the research folder or any folder of theirs. The plugin's files live in the task's cloud space, so copy the script into that working space first and run it there. Then say in one plain sentence that a script read the folder; the reader is not a programmer and does not need the mechanics, but is never left unaware that something ran. If the task cannot run scripts, do the same work by reading, as this skill says, and say that you did. Never rely on the folder's modification times: the mount flattens them.

Use its output as the candidate list in step 2. If it is not available, or code execution is off, search with the folder's own search or by reading the likeliest folder, and say that you did so; the routine is the same.

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never ask what the reader has already said. Silence is never a yes: a yes is a tap on the control or a word.
