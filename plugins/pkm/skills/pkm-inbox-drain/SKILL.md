---
name: pkm-inbox-drain
description: Processes the capture inbox one item at a time into notes in the notes folder, to map.md conventions. Use when the user says "process the inbox", "drain the inbox", or "file my captures".
---

# Inbox drain

Work the inbox doc down to empty, one item at a time, writing real notes into the notes folder. This skill is the "capture and filing are different" rule made into a routine: the reader captured without deciding, and now decides, with you doing the typing.

## Before starting

Read `map.md` first if you have not this conversation. It says where the folder is, how notes are named and formatted, what the reader is working on, and which conventions are settled. Every note you write follows it.

Check that the notes folder is reachable. If it is not, say so and stop; the inbox is drained at the desk, not from the phone. Do not file into project docs as a substitute.

Read `inbox.md`. Count the items and say how many there are. If there are none, say so and stop.

## One item at a time

For each item, in order from the top:

1. Quote the item back, exactly as captured.
2. Say what you think it is, in one sentence, and where it would go: a new note (one idea, named for its claim), an addition to an existing note or thread, a source to record, something for another project (name which, and stop there for that item), or a discard. Where the candidates script is available, run it for the item first (see below); otherwise search the folder for the item's two or three most distinctive words. Then apply the rule that decides between adding and creating: if an existing note covers the idea and its title still fits with this added, propose adding to it; create a new note only when no note covers it, or when the existing note's title would stop making sense; when the capture is adjacent to a note but distinct, propose a new note that links to the existing one and a line in the existing one linking back. When in doubt, add to the existing note. Two notes on one idea are the failure that makes a folder hard to trust, and it is silent.
3. Show the note you would write, or the change you would make to an existing note, in full, formatted to `map.md`'s conventions, with a `created` date of today and a `source` line if the capture came from somewhere.
4. Wait for a yes. A no, an edit, or a redirect changes what you write; silence is not a yes.
5. On a yes: write the note into the folder, read it back to confirm it landed as shown, then remove the item from `inbox.md`, then confirm in one line what changed and where, with the file name.

Do not batch. Do not propose the next item until the current one is written and removed. Do not expand a capture into more than it said; a one-line capture that turns out to be a thread the reader wants to think about becomes a short thread note with the capture as its first line, not an essay.

## What a capture can become

A **note** when the capture is an idea: named for the claim it makes, one idea, leading with the claim. A **thread** when it is a question the reader is chewing on, or a capture that clearly continues one already open in `map.md`'s open threads; append to the thread and say so. A **source** when it is something to read, or read: a source note in the sources folder with title, author, link, and the reader's reaction marked as theirs, per the source-note skill if it is installed. A **redirect** when it belongs to the week, money, medical or learning project: tell the reader which, leave the item in the inbox marked with the project name, and move on. A **discard** when the reader says so; never on your own judgment. A **deferral** when the item cannot be filed now (the note it belongs to is unclear, a source is missing, the reader wants to think): leave it in the inbox with a one-line reason under it, so the next drain starts from the reason rather than from scratch. Never delete an item you did not file.

## When you cannot tell

Ask one question, the one whose answer decides where it goes. Do not ask two. Do not guess at a folder because the capture is short.

## Ending

When the inbox is empty, or the reader stops, report: how many items were filed and where, how many were redirected and to which project, how many were deferred and why, how many remain. End with one word for completeness: full (inbox empty), partial (items remain, with the count), or minimal (stopped early), and name anything left open. If anything you filed touches what `map.md` says the reader is working on, say so in one sentence; do not edit `map.md` unless asked.

## The candidates script

`scripts/candidates.py` searches the notes folder for the distinctive words of a capture and prints the notes that mention them, most matches first, as JSON. It reads only; it needs code execution enabled and the folder path. Run it once per item:

```
python3 scripts/candidates.py --folder "<notes folder path>" --text "<the capture>" --limit 5
```

Use its output as the candidate list in step 2. If it is not available, or code execution is off, search with the folder's own search or by reading the likeliest folder, and say that you did so; the routine is the same.
