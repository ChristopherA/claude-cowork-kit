---
name: research-write-up
description: Drafts prose for other readers from the reader's topic notes, citing the sources those notes cite. Use for "write this up", "draft a post from my notes", "turn my topic note into an article".
---

# Write-up

Draft something other people will read, a post, an essay, a memo, a section of a paper, from the reader's topic notes. A write-up is the last step of the binder: sources are filed, topic notes say what the reader thinks, and the write-up says it to someone else. It drafts from topic notes, never from sources directly, so what it argues is what the reader has already worked out, and what it cites is what their thinking already rests on.

## Where this runs

This skill belongs to the research binder, whose Context documents are `rules.md`, `map.md` and `inbox.md`. Before anything else, check that they are here. If not, this project belongs to another binder: say which binder this skill is for and stop, so nothing is written into the wrong folder or the wrong documents; if this is the right binder and it is not set up yet, offer its setup, `set up my research binder`.

## Before starting

Read `rules.md` and then `map.md` if you have not this conversation: where topic notes live, where the reader's own writing lives, if anywhere, the link style, and the citation form. Read the account instructions' voice if you can see them.

Check that the research folder is reachable. If it is not, say so and stop; a write-up is drafted from notes you have to read.

## What to ask

Ask in one control what you cannot tell from the request: which topic note or notes the piece draws on (offer the topic notes the folder holds), who will read it, what form and about how long, and where it will appear. A request that names a topic with no topic note is answered by offering the topic-note skill first, since there is nothing yet to write up; do not draft from sources to fill the gap.

## Read before drafting

Read each topic note in full, then the source notes it cites. The piece's claims come from the topic notes' current thinking; its evidence from what the cited source notes hold, their abstracts, key points and key quotes. Where an argument needs something the notes do not hold, a source, a step, a figure, name the gap to the reader rather than filling it from recall. Where a topic note lists an open question, the piece keeps it open, or the reader settles it first. Where a source in the topic note challenges the current thinking, the piece does not leave it out.

## Draft

Write in the reader's voice as their account instructions set it, for the readers they named. Lead with the claim, not the background. Use only the quotes the source notes carry as key quotes, word for word with their page; where a source has a rendition, run the quote check on the draft against it (see below) and say in one line that you did and what it found. Say a work is important, foundational or influential only when a source note gives evidence for it.

Cite in the text by author and year, and end with a reference list in the citation form `map.md` gives, one line per source cited. Link a reference only to where a stranger can reach the work, its public URL or DOI. Never link to the reader's folder, a note, a rendition or an original: those are private and will not resolve for anyone else, and `originals/` holds copyrighted material kept for personal use. Nothing private from the notes reaches the piece unless the reader asks for it: a WHY SAVED line, a note's file name, what `map.md` says is deliberately not here.

## Show, then write

Show the whole draft in the conversation, with a short list under it of which topic notes and sources it drew on and any gap you named, and wait. Revise as the reader directs. On a yes, write it where `map.md` says the reader's own writing lives, or, if it names nowhere, as a Context document of the piece's title, which `rules.md` says holds writing the reader asked for; read it back and confirm where it is in one line. End with one word for completeness: full, or partial with what is missing (a gap named, a quote unchecked, a section the reader wants to write themselves).

## What not to do

Do not draft from sources the topic notes do not cite, or from your own knowledge of the subject. Do not change any note: if drafting shows the current thinking is out of date, say so and offer the topic-note skill. Do not publish or send the piece anywhere; it is handed back.

## The quote check

The source-note skill's quote check works on any draft. The script runs in the task's cloud workspace as that skill says; copy `quote_check.py` from the research plugin's `research-source-note/scripts/` folder and run it once per source that has a rendition:

```
python3 quote_check.py --note "<draft>" --rendition "<the source's rendition>"
```

Quotes from other sources show as not found against that rendition; read only the results for the quotes from the source whose rendition was given. If the task cannot run scripts, compare each quote with the source note's key quote by reading, and say that you did.

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never build an option or a draft from outside knowledge of the reader, such as what is public about the account's name: draw only on what they have said and what their folder shows. Never ask what the reader has already said. Silence is never a yes: a yes is a tap on the control or a word.
