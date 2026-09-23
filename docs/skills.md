# The kit's skills

Every skill in every plugin: what it does, in the skill's own words, when to reach for it, and what it hands back. A skill is one routine inside a plugin, picked up when you ask for its job in a phrase; the phrases are at the end of each description. Everything a skill does you could ask for in a sentence, more slowly. Every skill asks its questions through the app's question control, never writes into your folder or a project doc without a yes, and ends with one word for how complete the work was: full, partial or minimal, with what is missing.

The descriptions below are the ones the skills carry, and the build checks that they match; the plugin READMEs carry the same descriptions. The reasoning behind each project is in its document under `projects/`, and the kit's case is in [the explainer](claude-cowork-kit.md).

## Cowork Kit core, `cowork-kit`

The setup, and twelve routines that work in any project. None of them needs a particular folder or project doc; each reads what the project it runs in has. The ones that write, write only a project doc, and only on a yes.

### `cowork-again`

Says the last answer again in plain words, with the context the reader was missing, and nothing new. Use for "wait, what", "say that again", "I did not follow", "put that more simply".

**When to reach for it.** The last answer did not land.

**What it hands back.** The same answer in plainer words, with the context you were missing and nothing that was not in the first one. Usually shorter than the answer it re-pitches.

### `cowork-clarify`

Settles a decision one question at a time, finding what already decides it and recommending first, ending with a summary and no action. Use for "help me decide", "what are my options".

**When to reach for it.** A decision you keep circling: which of two shapes, whether something deserves a note, what to do about a thing that has come up three times. Claude finds what already decides it and recommends; you decide.

**What it hands back.** One question at a time through the question control, with the recommendation first, and at the end a summary of what was decided and why. It does none of it; it says where a decision would be recorded and waits to be asked.

### `cowork-confidence`

Says plainly what Claude is confident about, what it is not, and what would close the gap, then asks whether to proceed. Use for "how sure are you", "should I trust this", "what don't we know".

**When to reach for it.** Before you act on an answer: you want to know what Claude actually knows here and what it is guessing.

**What it hands back.** Three lists, confident, not confident, and what would close the gap, then the question of whether to go on. It does not proceed on its own.

### `cowork-interview`

Draws out what the reader knows before anything is designed: rounds of questions, then a write-back of what was understood. Use for "ask me questions first", "get it out of my head".

**When to reach for it.** The knowledge is in your head and has to come out before anything is designed: a plan with branches, a new project's scope, a piece of writing you have not yet said the point of. The opposite direction from clarify.

**What it hands back.** Rounds of questions until nothing is left silently assumed, then a written note of what Claude understood, offered for a project doc or a thread on a yes. Nothing is built from it until you ask.

### `cowork-meeting-pack`

Before a meeting with a professional: a one-page brief for them, a script for the reader, and a capture sheet for a companion, the asks first. Use for "prep this meeting", "meeting pack".

**When to reach for it.** A short meeting with a professional where the slot is expensive and the preamble would eat it, and especially when someone is coming with you to take notes.

**What it hands back.** Three documents: a one-page brief the professional can scan, a script you follow, and a capture sheet for whoever takes notes, the asks first; each written on a yes. For a clinician, the medical project's visit prep does this from the record.

### `cowork-new-project`

Designs a project the kit does not describe: its purpose, boundaries and docs, then the instructions text and a plugin from the kit's template. Use for "new project", "a project for something else".

**When to reach for it.** You want a project for something the kit does not describe, with the same shape as the ones it does.

**What it hands back.** The project's purpose, boundaries, folder and docs designed with you in rounds, then the Instructions text in the kit's form to paste. It creates no project and installs nothing; for a plugin, it points at the template and Anthropic's plugin builder.

### `cowork-postmortem`

Works through what went wrong in four questions and ends with one change to the instructions or description, with approval. Use for "what went wrong", "postmortem", "why did that happen".

**When to reach for it.** Something went wrong: a capture lost, a note filed in the wrong folder, a convention broken three times.

**What it hands back.** Four questions about the system rather than the blame, and one change to the instructions or the description, made with your approval. It does not fix the original mistake unless asked.

### `cowork-premortem`

Before the reader sends, decides or commits: what goes wrong, how they would know, what they would regret, then one change or a go. Use for "premortem", "before I send this", "what could go wrong".

**When to reach for it.** You are about to send, decide or commit to something and want to know what goes wrong before it does.

**What it hands back.** The likely failure, how you would know, what you would regret, then one change or a go. It sends, decides and commits nothing.

### `cowork-questions-for`

Writes the questions for someone who holds what the reader lacks, an accountant, a contractor, a teacher, ordered by what matters. Use for "questions for my accountant", "what should I ask them".

**When to reach for it.** Someone else holds what you need, an accountant, a contractor, a landlord, a teacher, a lawyer, and you want to arrive with the right questions rather than think of them afterwards.

**What it hands back.** A short document of questions ordered by what matters, one idea each, offered as a dated project doc on a yes. You send it or take it; the skill contacts no one.

### `cowork-setup`

Sets up the Claude Cowork Kit: a short interview, the account instructions to paste, and which project plugin to install next. Use for "set up the kit", "get started", "install the cowork kit".

**When to reach for it.** You are starting with the kit itself rather than with a project, or you want the account instructions without any project plugin installed yet. A project's own setup hands the same block back when the field is empty, so most readers never need this one.

**What it hands back.** The account instructions with your chosen voice filled in, for Settings, Account, "Instructions for Claude", and the name of the project plugin to install next with its setup phrase.

### `cowork-transcript`

Cleans a raw transcript at a stated level: speakers named, filler trimmed, terms fixed, nothing paraphrased, saved beside the raw one for the project's next step. Use for "clean up this transcript".

**When to reach for it.** You have a raw transcript from a meeting tool, a dictation app or a recording someone transcribed, and the notes built on it would inherit its errors.

**What it hands back.** A clean copy at the level you chose, speakers named, filler trimmed, terms fixed, nothing paraphrased, saved beside the raw one on a yes, with the uncertain attributions counted. It starts from text; a task cannot transcribe audio.

### `cowork-where-was-i`

Reads current work, the inbox and the newest notes, and recommends the one next step rather than a menu. Use for "where was I", "what was I in the middle of", "what should I do next".

**When to reach for it.** You are back at the project after a gap and do not want to choose from a list.

**What it hands back.** One next step, chosen from the current-work section, the inbox and the newest notes, with the reason. It files and edits nothing.

### `cowork-wrap-up`

Writes where this session leaves off, done, open, the first next step and what to watch, into a project doc the next session or the phone reads. Use for "wrap up for today", "write down where we are".

**When to reach for it.** The session is ending and the next one, or the phone at 11pm, should start from where this one stopped.

**What it hands back.** A short project doc: done, open, the first next step and what to watch, read back after writing. It records the state of the work, not a summary of the conversation.

## Personal knowledge, `pkm`

The notes project's four skills. All but the setup read `rules.md` and `map.md` first and write into the folder only after a yes; the three that read the folder run at the desk.

### `pkm-description-check`

Compares map.md against the notes folder and reports every claim that is no longer true, proposing edits without making them. Use for "check the description", "check map.md against my notes".

**When to reach for it.** At the two-week sitting, and whenever an answer from the phone comes back wrong.

**What it hands back.** Every claim in `map.md` that the folder no longer bears out, with the edit proposed for each. It changes nothing; you decide what to fix.

### `pkm-inbox-drain`

Processes the capture inbox one item at a time into notes in the notes folder, to map.md conventions. Use for "process the inbox", "drain the inbox", "file my captures".

**When to reach for it.** At your desk with the folder connected, when the inbox has a handful of captures. A short drain often is the habit that keeps the second job away.

**What it hands back.** Each item placed, an existing note to update, a new note, another project, a source to read, shown, and written into the folder only after a yes; at the end, how many were filed, redirected, deferred and left.

### `pkm-setup`

Sets up the notes project: three questions, then rules.md, map.md and inbox.md as project docs and the short instructions to paste. Use for "set up my notes project", "notes setup", "set up my notes".

**When to reach for it.** Once, in a task inside the new notes project, after the folder is connected.

**What it hands back.** The three project docs created, `rules.md`, `map.md` and `inbox.md`, and the two things only you can paste: the account instructions if your Settings field is empty, and the short project instructions for the Instructions panel. It then names the day-one checks, the phone check first.

### `pkm-source-note`

Writes one source note from a book, paper, article or transcript the reader hands over, the source's claims kept apart from the reader's own. Use for "source note", "save this article to my notes".

**When to reach for it.** You have read, or are about to read, something worth keeping: a book, a paper, an article, a transcript. You do the fetching; a source behind a login or a paywall is yours to save or paste.

**What it hands back.** One note in the sources folder, written the way `map.md` says notes are written, the citation recorded in its form, the source's claims kept apart from your own, on a yes.

## Learning, `learn`

The learning project's three skills. The lesson and the quiz run from the project docs, so they work from the phone with the computer closed; only the setup looks at the materials folder.

### `learn-lesson`

Runs one lesson of about thirty minutes on one concept, intuition first, from mission.md and progress.md, and records what clicked. Use for "next lesson", "teach me the next thing", "let's study".

**When to reach for it.** Whenever you have half an hour. It picks up where the progress record says you are.

**What it hands back.** One concept, intuition first, with you thinking before Claude explains and explaining back before anything is called settled; at the end, the lines it would write into `progress.md`, written on a yes, and the name of the next lesson.

### `learn-quiz`

Tests recall one question at a time from the lesson, the progress record or a handed note, grading each answer and raising the difficulty. Use for "quiz me", "test me on this chapter".

**When to reach for it.** Once there is something to quiz: after a few lessons, or with a chapter or a note in hand.

**What it hands back.** One question at a time, each graded, the difficulty rising; at the end, what was confirmed, what the gaps are, and which items the record had as settled that the quiz did not bear out, with the progress record updated on a yes.

### `learn-setup`

Sets up the learning project: an interview, then mission.md, curriculum.md and progress.md as project docs and the instructions to paste. Use for "set up my learning project", "I want to learn".

**When to reach for it.** Once, in a task inside the new learning project.

**What it hands back.** An interview of six questions, the curriculum drafted whole for your yes, then `mission.md`, `curriculum.md` and `progress.md` created, and the two things only you can paste: the account instructions if your Settings field is empty, and the project instructions with the subject and folder filled in.

## Your week, `week`

The week project's six skills. Nothing here sends a message or touches a calendar; drafts and plans come back in the chat, and the folder and `priorities.md` change only on a yes.

### `week-meeting-notes`

After a meeting: notes by topic with decisions first, quotes inline from this transcript only, action items with owners, carry-forward for a series; to the folder on a yes. Use for "meeting notes".

**When to reach for it.** After a meeting, with a cleaned transcript, the capture sheet from a meeting pack, or your memory of it.

**What it hands back.** One note by topic with decisions first, action items with owners, quotes from this transcript only and carry-forward for a series, into the working folder on a yes; what you owe from it offered to `priorities.md`.

### `week-plan`

Plans the week from the calendar and priorities.md, assuming less time than stated, and flags a plan that only works if nothing goes wrong. Use for "plan my week", "lay out this week".

**When to reach for it.** At the start of the week, after triage, once Claude knows what is already on your calendar.

**What it hands back.** The week laid out in the chat, assuming less time than you think and more in flight than you said, with a sentence saying so when a plan only works if nothing goes wrong. It writes to no calendar.

### `week-reply`

Drafts a reply in the reader's voice from the message they hand over and their earlier replies, then stops; never sends. Use for "draft a reply", "answer this for me", "write back to".

**When to reach for it.** A message needs an answer in your voice and you would rather edit a draft than start from nothing.

**What it hands back.** The draft, in your voice from the replies of yours it can read, with brackets where only you can decide. It never sends, by any route.

### `week-review`

A weekly review in the reader's words: done, slipped, avoided, what ate the week, energy; compared with recent weeks, priorities.md changes on a yes. Use for "review my week", "how did my week go".

**When to reach for it.** At the end of the week, before planning the next one.

**What it hands back.** A dated entry in a reviews doc in your own words, done, slipped, avoided, what ate the week, energy, compared with recent weeks, with what was carried forward untouched, and the change to `priorities.md` the week earned, on a yes.

### `week-setup`

Sets up the week project: three questions, then priorities.md as a project doc and the short instructions to paste. Use for "set up my week project", "week setup".

**When to reach for it.** Once, in a task inside the new week project.

**What it hands back.** `priorities.md` created from your answers, and the two things only you can paste: the account instructions if your Settings field is empty, and the project instructions with the folder filled in.

### `week-triage`

Turns a dump of half-formed obligations into a short ordered list of next actions, each startable today. Use for "triage this", "sort this pile out", "turn this into a to-do list".

**When to reach for it.** The obligations are in your head, an email thread or a voice note, and not yet in any list.

**What it hands back.** A short ordered list of concrete next actions, each startable today, with nothing around it. It goes in the chat; nothing is scheduled, sent or started.

## Money, `money`

The money project's three skills. Every figure traces to a row in a file in the folder, nothing that identifies an account reaches a project doc, and none of them logs in anywhere.

### `money-close`

Closes a month: categorizes its transactions against categories.md, shows the arithmetic, compares with targets.md, writes a summary with no account details. Use for "close the month".

**When to reach for it.** At the end of a month, when its files are in the folder.

**What it hands back.** The month's transactions categorized against `categories.md`, the arithmetic shown, the month compared with each target in `targets.md`, and a summary with no account details written to a project doc on a yes. It stops at a missing file rather than working around it.

### `money-setup`

Sets up the money project: the privacy floor, three questions, then categories.md and targets.md as project docs and the instructions to paste. Use for "set up my money project", "money setup".

**When to reach for it.** Once, in a task inside the new money project. It opens by saying what the folder does and does not protect and asks whether to go on.

**What it hands back.** `categories.md` and `targets.md` created from your answers with no account details or figures from a statement in either, and the two things only you can paste: the account instructions if your Settings field is empty, and the project instructions with the folder filled in.

### `money-statement`

Summarizes one statement or export from the folder into categories and totals with no account details, every figure traced to a row. Use for "summarize this statement", "read this bank export".

**When to reach for it.** At your desk with the folder connected, one statement or export at a time.

**What it hands back.** Categories and totals with every figure traced to a row and the arithmetic shown, what did not fit named rather than forced, nothing that identifies an account; written to a project doc on a yes.

## Medical records, `medical`

The medical project's five skills. The folder holds the clinical record and the project docs hold only the questions list and the bare timeline; none of them diagnoses, interprets, or reassures.

### `medical-check-in`

A weekly check-in in the reader's own words: what they did, what hurt, what helped, how they feel; a dated entry in the functional log. Use for "check in on how I'm doing", "health check-in".

**When to reach for it.** Once a week or so, in your own words.

**What it hands back.** A dated entry in the functional log in the folder, what you did, what hurt, what helped, how you feel, and the one or two things that moved against the last few entries. Nothing clinical reaches a project doc.

### `medical-record-visit`

After an appointment: a bare timeline line, the visit note from the recording, checklist and portal papers into the folder, the standing files updated, questions struck. Use for "record my visit".

**When to reach for it.** After an appointment, with the recording or its transcript, the companion's checklist and the portal papers.

**What it hands back.** A dated line in `timeline.md` with nothing clinical in it, the visit note and the papers into the folder, the standing files updated so the next prep starts from a current record, and the answered questions struck, each step on a yes.

### `medical-setup`

Sets up the medical project: the privacy floor, three questions, then questions.md and timeline.md as project docs and the instructions to paste. Use for "set up my medical project", "medical setup".

**When to reach for it.** Once, in a task inside the new medical project. It opens by saying what the folder does and does not protect.

**What it hands back.** `questions.md` and `timeline.md` created with nothing clinical in them, the folder's standing files offered as headed empty files if it has none, and the two things only you can paste: the account instructions if your Settings field is empty, and the project instructions with the folder filled in.

### `medical-treatment-questions`

From a handed article or a clinician's suggestion, grades the evidence it cites and writes the questions to ask about the treatment, never from recall. Use for "questions about this treatment".

**When to reach for it.** A treatment has been offered or you have found one, and you have an article, a study or the clinician's suggestion as you recorded it.

**What it hands back.** What the source claims and on what evidence, graded in one of five words, strong, moderate, limited, anecdotal, none stated, only for what it cites, and the gaps turned into questions for the clinician, added to `questions.md` on a yes. It does not research and does not say whether to try it.

### `medical-visit-prep`

Before an appointment, drafts the questions from what changed in the record, and on request a visit pack: a handout, a script and a companion checklist. Use for "prep my doctor's visit", "visit pack".

**When to reach for it.** Before an appointment, at your desk with the folder connected; on a first visit, from what you tell it.

**What it hands back.** A short list of questions drawn from what changed in the record since the last visit, values quoted exactly, added to `questions.md` on a yes; and on request a visit pack, a one-page handout, a script and a companion checklist, each written to the folder on a yes.

## The template

`template/` has no skills; it is the skeleton of a project plugin, with the brackets left in, for a contributor or a reader comfortable editing files. A project of your own does not need it: the core's `cowork-new-project` designs one and hands back its text.
