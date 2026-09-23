---
name: cowork-where-was-i
description: Reads current work, the inbox and the newest notes, and recommends the one next step rather than a menu. Use for "where was I", "what was I in the middle of", "what should I do next".
---

# Where was I

Give the reader one next step, chosen from where things actually stand, and say why that one. Not a list of options; the reader asked because they do not want to choose from a list.

## Read the state

In this order, and say which of them you could reach:

1. `wrap-up.md`, if it exists: the note the last session left, with its first next step. Read it first; it is the reader's own statement of where they stopped.
2. The project's own docs, whichever this project has: in the notes project, `map.md`'s "what I'm working on now" and "open threads" sections and `inbox.md` (how many items are waiting, and how old the oldest looks); in the week project, `priorities.md`; in the learning project, `mission.md` and `progress.md`; in the money project, `categories.md` and the newest summary; in the medical project, `questions.md` and `timeline.md`. Say which you found.
3. If the folder is reachable, the notes and threads with the newest dates inside them (a `created` or dated line; the file's modification time is not reliable on the mount): their names and, for the top few, their first lines. If the folder is not reachable, say so; the recommendation then comes from the docs, which is enough for a phone.

Do not ask the reader what they were doing. The point of this skill is that they do not remember, and the files do.

## Choose one step

Weigh, in this order:

- **The wrap-up's next step.** If `wrap-up.md` names a first next step and nothing since contradicts it, that is the recommendation.
- **An open thread with fresh movement.** A thread named in the docs whose note carries a date in the last few days is the most likely place the reader's attention was. Continuing it is the default recommendation.
- **A full inbox.** More than a handful of items, or anything more than a couple of weeks old, means the next step is to drain it, because captures that sit stop meaning anything. Recommend the drain and say how many items.
- **A stale description.** If the newest notes and threads do not match what the docs say the reader is working on, the next step is to fix the description, because every session after this one starts from it.
- **Nothing in motion.** If threads are quiet and the inbox is empty, say so plainly and recommend the reader pick a thread or read something; do not manufacture urgency.

## Say it

One recommendation, in two or three sentences: what to do, why it is the one, and what you saw that made you pick it (the thread's name, the item count, the date). Then one line naming the runner-up, so the reader can override without asking for the list.

If the reader says no, give the runner-up as the new recommendation with the same shape. Do not produce a menu on the second try either.

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never ask what the reader has already said.

## What this skill does not do

It does not file, write, or edit anything. It does not read every note in the folder; the newest few and the description are the whole input. It does not tell the reader what they should care about; it tells them where they left off.
