---
name: research-description-check
description: Compares map.md against the research folder and reports every claim that is no longer true, proposing edits without making them. Use for "check the description", "check map.md against my notes".
---

# Description check

`map.md` is what Claude knows about the notes when it cannot see them, and at the desk it is the only memory it has. It drifts. This skill reads the folder and the description side by side and reports where they disagree. It changes nothing; the reader decides what to fix.

If the reader means the one-line description under the project's title, say that it is a label and that this skill checks `map.md`, the description of the notes.

## Where this runs

This skill belongs to the research binder, whose Context documents are `rules.md`, `map.md` and `inbox.md`. Before anything else, check that they are here. If not, this project belongs to another binder: say which binder this skill is for and stop, so nothing is written into the wrong folder or the wrong documents; if this is the right binder and it is not set up yet, offer its setup, `set up my research binder`.

## Before starting

Check that the research folder is reachable. If it is not, say so and stop; a check from the project's Context alone can only find contradictions inside `map.md`, and the reader wants the folder.

Read `rules.md` and `map.md` in full. Note every checkable claim they make. From `map.md`: the folder path; each folder it lists and what it says lives there; the naming rules; the metadata lines a note carries; wrapping; link style; the "not here" list; the settled conventions; the open threads; the current-work section and its date. From `rules.md`: the folder path again (the two must agree), what the Context documents hold, and the rules about notes that the folder can show broken. A claim the two documents make differently is reported first, before any comparison with the folder.

## Take the census

Where the census script is available, run it and read its output (see below). Otherwise take the census by reading: list the folders at the top level and one level down; count the notes in each; open the five newest notes and the five oldest and note their first lines, their metadata, whether paragraphs are wrapped, and how they link. Say which method you used.

## Compare, claim by claim

For each claim in `map.md`, say one of three things:

- **Holds.** The folder agrees. Say it in a word; do not list evidence for what is fine.
- **Stale.** The folder disagrees, and the description is what is wrong: a folder that no longer exists or has been renamed, a convention the newest notes do not follow, a naming rule the files do not match, an open thread whose note carries no date newer than months ago, a current-work section older than its date suggests. Quote the claim, say what the folder shows, and propose the replacement wording.
- **Drift in the folder.** The folder disagrees, and the folder is what is wrong: notes without the metadata line, a file in the wrong folder by its own content, mixed wrapping, a note named against `map.md`'s naming rule. Name the files, at most ten per finding, and say what would bring them into line. Do not fix them; the reader may prefer to change the convention.

Then look for what `map.md` does not say: a folder it never mentions, and a folder it names that is not there (the census's `folders_check`, given the folders `map.md` lists). A folder the app made for its own output, such as `Claude outputs/`, holds session files rather than research: say so, and propose either a line in `map.md` describing it as session output to leave out of filing and searches, or moving its files somewhere outside the research folder; a pattern in the newest notes (a metadata line, a naming habit, a kind of link) that has become a convention without being written down; something on the "deliberately not here" list that is, in fact, there.

## Sources and topic notes

Check the conventions `map.md` sets for sources and topic notes, from the census's `sources` and `topics` or by reading the sources folder and the topic notes' home:

- Every source folder has a lead file of the folder's own name, and no folder holds only its lead; a single file is never a folder.
- Every original that is a PDF or a saved web page has its rendition beside it, in `renditions/` under the same name.
- A read-level note's quotes can be checked: against its rendition, or labeled as checked in the browser or as unchecked (the census's `quotes_unchecked`); and every works note has a BRIEF (the census's `works.no_brief`).
- No file other than a note sits loose in the sources folder or beside a lead note (the census's `loose_files`): an original belongs in its note's `originals/` folder, under the note's name, and a file with no note is an inbox item.
- Every source note's `level` matches what it contains: `citation` is the line alone, `minimal` has a brief and a short abstract and no key points or quotes, `read` has key points or key quotes.
- Which source notes nothing outside the sources folder cites, and which topic notes cite no source. A link to one of the reader's own works, in `works/`, counts as a citation, both ways.
- `map.md`'s Topics section against the topic notes: a note with no line, a line with no note (a line marked not written yet, with its sources waiting, is a plan rather than a fault; check only that each waiting source exists), and a line whose thinking no longer matches the note's current thinking. The last is stale wording in the description, reported with the note's current thinking as the proposed line.

The first five are drift in the folder, reported with the files as above. The last two are not faults: an uncited source is a candidate for the inbox drain to revisit or for a topic note to take up, and a topic note that cites nothing is the reader's thinking without its sources. List them under their own heading, at most ten each, and say what each could become. Pass `--sources` and `--topics` to the census when `map.md` names other folders for them.

List the lines still waiting for the reader (the census's `awaiting_confirmation`): every WHY SAVED marked as inferred from their writing, and every passage in a topic or works note marked "(Drafted by Claude from ...)". Give the count and the first ten, and say that each stays marked until the reader confirms or replaces it; these are not faults either.

Check the open threads against the files, not against the description: for each thread `map.md` names, confirm a note for it exists and say the newest date inside it. A thread listed as open whose note is missing, or untouched for months, is reported as such; a claim that something exists is checked by the thing existing.

## The current-work section

Treat it separately, because it goes stale fastest and matters most. Say when it was last updated if the file records that, name the notes and threads with the newest dates inside them (the file's modification time is not reliable on the mount), and ask whether the section still describes what the reader is chewing on. Propose wording only if the reader says what has changed; do not guess at their current work from file activity.

## Report

One short report, in this order: what holds (a line), what is stale in the description (each with proposed wording), what has drifted in the folder (each with the files), the sources nothing cites and the topic notes that cite nothing, the lines awaiting the reader, what is missing from the description, and the current-work question. Then stop, with one word for how complete the check was: full (script census and the description read whole), partial (census by reading only, or the folder partly reachable), and what was not checked.

If the reader chooses, through the control, to apply them, two kinds of edit are on offer and they are handled differently. Wording changes to `map.md` or `rules.md` (a renamed folder, a convention written down, a stale sentence replaced, a rule the reader has decided to relax) are safe: make the ones the reader names, one at a time, showing each before writing, then read the document back and confirm what changed. Offer each through the app's question control, recommended option first. Anything that would change the folder (moving a file, renaming a note, adding a missing metadata line) is not this skill's to do: list those as a proposal for the reader to carry out or to hand to the inbox-drain or source-note skills, and never edit notes in the folder from here.

## The census script

`scripts/census.py` walks the research folder and prints, as JSON, the folder tree with counts, per-folder file naming patterns, which files carry a `created` line and a `source` or `level` line at the top, how many have paragraphs longer than one line (hard-wrapped), the link styles found, the newest and oldest files by modification time with their dates, under `sources`, `topics` and `works` the checks above, the lines awaiting the reader, and, given the folders `map.md` names, which are missing and which it does not name. It reads only; it needs code execution enabled.

```
python3 scripts/census.py --folder "<research folder path>" --limit 10 --sources sources --topics topics --works works --folders "<the folders map.md names, comma-separated>"
```

Where a script runs depends on what it reads. A task reaches the research folder through a shell on the reader's computer, a Linux machine there that sees only the folders connected to the task; the task's cloud workspace sees a file only once it is copied there. So a script that reads the whole folder, such as the census or the drain's candidate search, runs in that shell, from the kit's own copy in a hidden `.cwk/scripts/` folder at the top of the research folder, which the census and editors such as Obsidian skip. Before running, compare `python3 .cwk/scripts/<script> --version` with the `__version__` line in this skill's own copy of the script. If the copy is missing, or its version differs, which is what a plugin upgrade causes, write this skill's copy there afresh through the shell, check it landed by its checksum against this skill's copy, and say in one sentence that the kit's scripts were refreshed; otherwise run the copy already there, with its output going to a scratch folder outside the research folder. Nothing of the kit's goes anywhere else in the folder: never among the notes, and never into any other folder of the reader's. If the copy cannot be written, do the work by reading and say why. A script that needs one file, a PDF or a draft note, may instead run in the cloud workspace on a copy of that file. Anything a script writes reaches the notes only as this skill says, after a yes. When many files go into the folder at once, write them with the computer's shell and check each one landed by its checksum, so a dropped link to the computer can be resumed from where it stopped. Then say in one plain sentence that a script read the folder; the reader is not a programmer and does not need the mechanics, but is never left unaware that something ran. If the task cannot run scripts, do the same work by reading, as this skill says, and say that you did. Never rely on the folder's modification times: syncing and copying reset them. Prefer the `created` lines inside notes for age; the script reports both, and its modification times are there only so you can see that they disagree. If the script is not available, take the census by reading, as above.

## Ending

Report what was done and what is left open. End with one word for completeness: full, partial (with what is missing), or minimal (stopped early).

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never build an option or a draft from outside knowledge of the reader, such as what is public about the account's name: draw only on what they have said and what their folder shows. Never ask what the reader has already said. Silence is never a yes: a yes is a tap on the control or a word.
