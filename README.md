# Claude Cowork Kit

Plugins for people who use Claude in the desktop and mobile apps rather than in a terminal. Install one, start a task, and Claude sets up a binder with you: it asks what you want, creates the binder's Context documents, and hands back the text only you can paste. Each binder keeps its material as plain files in a folder on your own computer, so nothing you build depends on Claude, and the plugins add the routines that make the binder worth opening: a decision worked through one question at a time, an inbox of captures filed to your own conventions, a visit prepared from what changed in your record, a week planned from what is actually on the calendar.

## Who it is for

You use Claude Cowork: the desktop app with a folder connected, and the iPhone or iPad app for capture and questions anywhere, and for work in the folder itself while Claude stays open on your Mac. You are not a programmer and do not want to become one to keep notes with Claude.

You need a Claude plan that includes Cowork and the Claude desktop app on the computer where your files live. Cowork tasks draw on the plan's usage allowance much faster than chat does, so a plan that feels roomy for conversation can feel tight for work on files.

Why Cowork rather than plain chat, a notes app, or a developer tool is argued in [the explainer](docs/claude-cowork-kit.md#why-cowork). The short version: Claude reads your whole folder at your desk or from your phone while Claude is open on the Mac, answers from a small description of it when it is not, and your material stays plain files you own.

## Words you will see

- A **project** is the app's own container: its page has Instructions, Context, a Folder and Scheduled tasks.
- A **Context document** is one of the documents in a project's Context. Claude reads it in every task there, and your phone can reach it.
- A **binder** is one part of your life as the kit sets it up: one project, one folder on your computer, and the Context documents that describe it.
- A **task** is a conversation in Cowork. Inside a project, the composer has a Chat and a Cowork toggle, and a task is what you start with the Cowork side on.
- A **skill** is a routine Claude runs when what you say matches its description. There is no command to remember.
- A **plugin** is a set of skills installed once, under Customize in the desktop app, that then works in every project.
- A **marketplace** is a place the app can install plugins from. This repository is one.

## What is in the kit

Six plugins: five binders and a core. No plugin has to come first: start with the binder you want most, and live with it for a week before adding another. Each skill below is one line; the phrase in quotes is one thing you can say to start it. [The skills index](docs/skills.md) says for every skill when to reach for it and what it hands back.

### Research, `research`

Notes and reading: capture from anywhere, file at your desk, answer from what you have read.

- `research-setup`: sets up the binder in three questions. "Set up my research binder."
- `research-inbox-drain`: files your captures one at a time into your notes. "Process the inbox."
- `research-source-note`: turns an article, paper or transcript you hand over into one note. "Save this article to my notes."
- `research-description-check`: finds what the binder's description says that your folder no longer bears out. "Check the description."

### Learning, `learn`

A subject, a skill or an exam, learned on purpose, with a plan and a record of what has clicked.

- `learn-setup`: an interview, then the mission and the curriculum. "I want to learn."
- `learn-lesson`: thirty minutes on one idea, intuition first. "Next lesson."
- `learn-quiz`: questions one at a time, graded, getting harder. "Quiz me."

### Your week, `week`

Obligations turned into next actions, and a week planned from the time you actually have. Nothing here sends a message or touches a calendar.

- `week-setup`: your priorities for the month, in three questions. "Set up my week binder."
- `week-triage`: turns a pile of half-formed obligations into a short list of next actions. "Sort this pile out."
- `week-plan`: lays out the week from your calendar and priorities. "Plan my week."
- `week-review`: a weekly look back in your own words. "Review my week."
- `week-meeting-notes`: notes from a meeting, decisions and action items first. "Meeting notes."
- `week-reply`: drafts a reply in your voice and stops; it never sends. "Draft a reply."

### Money, `money`

Statements and a monthly close, with account details kept out of everything that syncs.

- `money-setup`: what the folder does and does not protect, then your categories and targets. "Set up my money binder."
- `money-statement`: one statement summarized into categories and totals. "Summarize this statement."
- `money-close`: the month's transactions categorized and compared with your targets. "Close the month."

### Medical records, `medical`

A record you can compare across visits, and appointments prepared from it. None of these skills diagnoses or interprets.

- `medical-setup`: what the folder does and does not protect, then a questions list and a visit timeline. "Set up my medical binder."
- `medical-visit-prep`: the questions to ask, from what changed since the last visit, and a visit pack if someone is coming with you. "Prep my doctor's visit."
- `medical-record-visit`: after an appointment, the visit note filed and the record brought up to date. "Record my visit."
- `medical-check-in`: a weekly entry in your own words about how you are doing. "Health check-in."
- `medical-treatment-questions`: grades the evidence an article cites and turns the gaps into questions for your clinician. "Questions about this treatment."

### Cowork Kit core, `cowork-kit`

Routines that work in any binder, installed beside one when you want them.

- `cowork-setup`: hands back your account instructions, for a reader who starts with the kit rather than a binder. "Set up the kit."
- `cowork-clarify`: settles a decision one question at a time, recommending first. "Help me decide."
- `cowork-interview`: draws out what you know before anything is designed. "Ask me questions first."
- `cowork-confidence`: says what Claude is sure of, what it is not, and what would close the gap. "How sure are you?"
- `cowork-premortem`: before you send or commit, what could go wrong. "What could go wrong?"
- `cowork-postmortem`: after something went wrong, one change so it does not happen again. "What went wrong?"
- `cowork-again`: the last answer again, in plainer words. "Say that again."
- `cowork-questions-for`: the questions to ask an accountant, a contractor, a teacher. "Questions for my accountant."
- `cowork-meeting-pack`: a brief, a script and a note-taker's sheet before a meeting with a professional. "Prep this meeting."
- `cowork-transcript`: cleans up a raw transcript without paraphrasing it. "Clean up this transcript."
- `cowork-where-was-i`: the one next step after a gap. "Where was I?"
- `cowork-wrap-up`: writes down where this session leaves off. "Wrap up for today."
- `cowork-new-binder`: designs a binder for something the kit does not describe. "A binder for something else."

Everything a skill does you could ask for in a sentence, more slowly. The setup skills hand back only what the app still needs from your hands: a task can create Context documents and read your folder, but it cannot change your settings, create a project, connect a folder or install a plugin.

## Install

Everything installs from the Claude desktop app, under Customize, then Plugins. Two ways:

- **From the marketplace.** Choose **Add marketplace**, enter `ChristopherA/claude-cowork-kit`, and install a plugin from the list it shows. Installing this way also brings updates.
- **From a file.** Download the plugin's `.plugin` file from the [releases page](https://github.com/ChristopherA/claude-cowork-kit/releases) and add it with the upload option on the same Plugins page. The release notes carry each file's checksum.

Turn the plugin on after installing it. Do not drag a `.plugin` file into a task's composer: a plugin dropped there is attached to that one task only and is gone with it.

Install one plugin at a time, and run its setup before installing the next.

## First run

Pick the binder you want first. Each one is its own plugin, set up with one phrase:

| Binder | Plugin, as the app shows it | Say, in a task inside its project |
|---|---|---|
| Notes and reading | **Research** (`research`) | `set up my research binder` |
| Something you are learning | **Learning** (`learn`) | `set up my learning binder` |
| Your week | **Your week** (`week`) | `set up my week binder` |
| Money | **Money** (`money`) | `set up my money binder` |
| Medical records | **Medical records** (`medical`) | `set up my medical binder` |

Before you connect a folder, read what the connected folder does and does not protect: `PRIVACY.md` here, and the explainer's section [What the connected folder does and does not protect](docs/claude-cowork-kit.md#what-the-connected-folder-does-and-does-not-protect). Everything Claude can reach in a connected folder it may read, and a file in that folder can carry instructions Claude will follow. The money and medical binders hold what you would mind leaking; their setups say what the folder does and does not protect before anything else.

1. **Make the binder's folder and back it up.** Keep your binders together: one folder, such as `Claude Cowork Binders` in your home folder, with a folder inside it for each binder. Each project gets only its own binder's folder, never the one they share, so the medical binder cannot read your money files. Back it up with whatever you already use, before the first task that is allowed to write. If the folder is in iCloud Drive, read the explainer's iCloud paragraph first: one setting needs changing.
2. **Install the binder's plugin** by either path above, and turn it on.
3. **Create the project with its folder.** In Claude, open **Projects**, then **New project**. Name it under What are you working on?, and say in a sentence what the binder is for under What are you trying to achieve?. Choose **Use a folder** and pick the binder's own folder. Claude then asks to change files in it: choose **Always allow** for research, learning and your week, and **Allow** for money and medical, so those two ask each time. The folder stays on this computer: Claude reaches it from your desk, or from your iPhone or iPad while Claude is open on the Mac and the Mac is awake. The project and its Context documents are in your account; that a project created with a folder shows on your phone is one of the things the kit is still confirming.
4. **Run the setup.** In a task inside that project, say the binder's phrase from the table. Claude asks a few questions, creates the binder's Context documents, and hands back what only you can paste: the account instructions, if your Settings, Account, "Instructions for Claude" field does not carry them yet, and the project instructions for the Instructions panel at the side of the project page. It then tells you what exists and what is waiting for you.
5. **Install the core plugin** (`cowork-kit`, shown as **Cowork Kit core**) when you want its routines; they work in every binder. Its own setup, `set up the kit`, is for a reader who wants the account instructions before choosing a binder.

Each binder's document under [`docs/binders/`](docs/binders/) has its own setup in full and a check that it works. Setup takes about thirty minutes for the first binder, and one install and one paste for each binder after. You make the decisions; Claude does the typing. Where Customize and Settings sit in the app's layout is one of the things the kit is still confirming; both are in the desktop app.

## Status

Release candidate. The research plugin has had one run in Cowork; the core and the four other binder plugins have not run yet, and whether the phone app runs plugins is not yet confirmed. Anything the kit is still confirming is marked as such where it appears.

## Learn more

- [How the kit works](docs/claude-cowork-kit.md): why Cowork, where things live and why, what to do when something surprises you, what the connected folder does and does not protect, setting up a binder by hand, and what to change after two weeks.
- One document per binder under [`docs/binders/`](docs/binders/): [research](docs/binders/research.md), [learning](docs/binders/learning.md), [your week](docs/binders/week.md), [money](docs/binders/money.md) and [medical records](docs/binders/medical.md), each with its setup, a check that it works, and the text its setup writes.
- [The skills index](docs/skills.md): every skill, when to reach for it, and what it hands back.
- `PRIVACY.md`: what leaves your computer and what does not. `CHANGELOG.md`: what each release changed. `CONTRIBUTING.md`: how to report a problem or change the kit.

## License

BSD-2-Clause-Patent. See `LICENSE`.
