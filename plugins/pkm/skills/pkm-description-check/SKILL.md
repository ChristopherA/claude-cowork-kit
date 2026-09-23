---
name: pkm-description-check
description: Compares map.md against the notes folder and reports every claim that is no longer true, proposing edits without making them. Use for "check the description", "check map.md against my notes".
---

# Description check

`map.md` is what Claude knows about the notes when it cannot see them, and at the desk it is the only memory it has. It drifts. This skill reads the folder and the description side by side and reports where they disagree. It changes nothing; the reader decides what to fix.

## Where this runs

This skill belongs to the notes project, whose project docs are `rules.md`, `map.md` and `inbox.md`. Before anything else, check that they are here. If not, this is another project: say which project this skill is for and stop, so nothing is written into the wrong folder or the wrong docs; if this is the right project and it is not set up yet, offer its setup, `set up my notes project`.

## Before starting

Check that the notes folder is reachable. If it is not, say so and stop; a check from project knowledge alone can only find contradictions inside `map.md`, and the reader wants the folder.

Read `rules.md` and `map.md` in full. Note every checkable claim they make. From `map.md`: the folder path; each folder it lists and what it says lives there; the naming rules; the metadata lines a note carries; wrapping; link style; the "not here" list; the settled conventions; the open threads; the current-work section and its date. From `rules.md`: the folder path again (the two must agree), what the project docs hold, and the rules about notes that the folder can show broken. A claim the two docs make differently is reported first, before any comparison with the folder.

## Take the census

Where the census script is available, run it and read its output (see below). Otherwise take the census by reading: list the folders at the top level and one level down; count the notes in each; open the five newest notes and the five oldest and note their first lines, their metadata, whether paragraphs are wrapped, and how they link. Say which method you used.

## Compare, claim by claim

For each claim in `map.md`, say one of three things:

- **Holds.** The folder agrees. Say it in a word; do not list evidence for what is fine.
- **Stale.** The folder disagrees, and the description is what is wrong: a folder that no longer exists or has been renamed, a convention the newest notes do not follow, a naming rule the files do not match, an open thread whose note carries no date newer than months ago, a current-work section older than its date suggests. Quote the claim, say what the folder shows, and propose the replacement wording.
- **Drift in the folder.** The folder disagrees, and the folder is what is wrong: notes without the metadata line, a file in the wrong folder by its own content, mixed wrapping, a note named for a topic rather than a claim where the convention says claim. Name the files, at most ten per finding, and say what would bring them into line. Do not fix them; the reader may prefer to change the convention.

Then look for what `map.md` does not say: a folder it never mentions; a pattern in the newest notes (a metadata line, a naming habit, a kind of link) that has become a convention without being written down; something on the "deliberately not here" list that is, in fact, there.

Check the open threads against the files, not against the description: for each thread `map.md` names, confirm a note for it exists and say the newest date inside it. A thread listed as open whose note is missing, or untouched for months, is reported as such; a claim that something exists is checked by the thing existing.

## The current-work section

Treat it separately, because it goes stale fastest and matters most. Say when it was last updated if the file records that, name the notes and threads with the newest dates inside them (the file's modification time is not reliable on the mount), and ask whether the section still describes what the reader is chewing on. Propose wording only if the reader says what has changed; do not guess at their current work from file activity.

## Report

One short report, in this order: what holds (a line), what is stale in the description (each with proposed wording), what has drifted in the folder (each with the files), what is missing from the description, and the current-work question. Then stop, with one word for how complete the check was: full (script census and the description read whole), partial (census by reading only, or the folder partly reachable), and what was not checked.

If the reader says "apply", two kinds of edit are on offer and they are handled differently. Wording changes to `map.md` or `rules.md` (a renamed folder, a convention written down, a stale sentence replaced, a rule the reader has decided to relax) are safe: make the ones the reader names, one at a time, showing each before writing, then read the doc back and confirm what changed. Offer each through the app's question control, recommended option first. Anything that would change the folder (moving a file, renaming a note, adding a missing metadata line) is not this skill's to do: list those as a proposal for the reader to carry out or to hand to the inbox-drain or source-note skills, and never edit notes in the folder from here.

## The census script

`scripts/census.py` walks the notes folder and prints, as JSON, the folder tree with counts, per-folder file naming patterns, which files carry a `created` line and a `source` line at the top, how many have paragraphs longer than one line (hard-wrapped), the link styles found, and the newest and oldest files by modification time with their dates. It reads only; it needs code execution enabled.

```
python3 scripts/census.py --folder "<notes folder path>" --limit 10
```

The script runs inside the task, in the task's own working space on the side where the notes folder is mounted; it never runs on the reader's computer and never goes into the notes folder or any folder of theirs. The plugin's files live in the task's cloud space, so copy the script into that working space first and run it there. Then say in one plain sentence that a script read the folder; the reader is not a programmer and does not need the mechanics, but is never left unaware that something ran. If the task cannot run scripts, do the same work by reading, as this skill says, and say that you did. Never rely on the folder's modification times: the mount flattens them. Prefer the `created` lines inside notes for age; the script reports both, and its modification times are there only so you can see that they disagree. If the script is not available, take the census by reading, as above.

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never ask what the reader has already said.
