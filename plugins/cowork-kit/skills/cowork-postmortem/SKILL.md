---
name: cowork-postmortem
description: Works through what went wrong in four questions and ends with one change to the instructions or description, with approval. Use for "what went wrong", "postmortem", "why did that happen".
---

# Postmortem

Something went wrong: a note filed in the wrong folder, a capture lost, a description that turned out stale, a convention broken three times. Answer four questions about it, then change one thing so it does not happen again. Four questions, one change. Not a report.

## The four questions

Answer each in a sentence or two, in this order, from what you can actually see in the files and the conversation. Where you are guessing, say so.

1. **How was it caught?** By the reader noticing, by a check, by accident. This matters because the way it was caught is the only detection you know works.
2. **Why did it happen?** The immediate cause: which instruction was followed, which was missing, which file was stale, what was assumed.
3. **What gap let it happen?** Not the moment but the system: a rule that lives only in someone's head, a convention the project's docs do not state, a step the routine skips, a place where two files can drift apart.
4. **What prevents it next time?** One change, the smallest that closes the gap named in question three. Prefer a sentence in the project's rules or description doc (`rules.md` or `map.md` in the notes project, the priorities, mission, categories or questions doc elsewhere) over a new procedure, and prefer a check that fires anyway over one that depends on remembering. The Instructions field is closed to a task and holds only what should never change, so a change lands there only when the reader wants a boundary moved.

## Propose the change

Show the exact wording and where it goes: which section of which project doc, or which note. Ask for the yes through the app's question control, recommended option first, and write it only after the yes; read the doc back and confirm the change landed. If the right fix is in the project instructions, which only the reader can edit, hand them the sentence to paste and say so.

If the honest answer to question four is that nothing reasonable prevents it, say that; not every mistake earns a rule, and a rule that never fires is the dilution the kit warns about.

## Ending

Report what was done and what is left open. End with one word for completeness: full, partial (with what is missing), or minimal (stopped early).

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never ask what the reader has already said. Silence is never a yes: a yes is a tap on the control or a word.

## What this skill does not do

It does not assign blame, to the reader or to itself; the questions are about the system. It does not fix the original mistake unless asked; that is a separate, smaller job. It does not add more than one change per postmortem.
