# Claude Cowork Kit

Plugins for people who use Claude in the desktop and mobile apps rather than in a terminal. Install one, start a task, and Claude sets up a project with you: it asks what you want, creates the project's docs, and hands back the one block of text only you can paste. Each project keeps its material as plain files in a folder on your own computer, so nothing you build depends on Claude, and the plugins add the routines that make the project worth opening: a decision worked through one question at a time, an inbox of captures filed to your own conventions, a visit prepared from what changed in your record, a week planned from what is actually on the calendar.

## Who it is for

You use Claude Cowork: the desktop app with a folder connected, and the phone app for everything that does not need the folder. You are not a programmer and do not want to become one to keep notes with Claude.

It is not for Claude Code, the command-line tool developers use, and it is not for plain chat. Most published advice for working with Claude on your own files is written for one of those two, and where this kit disagrees with it, that is usually the difference. If you are comfortable in a terminal, [Claude Code](https://docs.anthropic.com/en/docs/claude-code) will do more than this kit can, and the folder this kit builds works unchanged under it when you get there.

**Four words the rest of this page uses.** A *task* is a conversation in Cowork: inside a project, the composer has a Chat and a Cowork toggle, and a task is what you start with the Cowork side on. A *skill* is a routine Claude runs when what you say matches its description; there is no command to remember. A *plugin* is a set of skills installed once, under Customize in the desktop app, that then works in every project. A *marketplace* is a place the app can install plugins from; this repository is one.

## Why Cowork

You could keep notes with Claude other ways, and each one costs something.

| Approach | Reads your whole folder | Works from your phone | Your material stays plain files | Needs a terminal |
|---|---|---|---|---|
| Chat with a project | no, only what you upload | yes | no, it lives in the account | no |
| An AI plugin in Obsidian or Logseq | yes | no | yes | no |
| Claude Code | yes | no | yes | yes |
| An always-on assistant that watches your screen | it builds its own store | yes | no | no |
| **Cowork with this kit** | yes, while the desktop app is open | yes, from a description of the folder | yes | no |

The phone column of the last row is the whole trick: from the phone, Claude works from a small description of your notes kept in the project, not from the notes themselves, which stay on your computer. That split, what goes in the folder and what goes in the description, is the one idea the kit is built around, and [the explainer](docs/claude-cowork-kit.md) spends its first half on it.

## What is in the kit

Six plugins and a template. Install the core, then only the projects you want; most people should live with the notes project for a week before adding another.

| Plugin | What it is for | Its skills |
|---|---|---|
| `cowork-kit`, **Cowork Kit core** | The setup, and twelve routines that work in any project. | `cowork-setup` asks who you are and hands back your account instructions. For deciding: `cowork-clarify` (one question at a time, recommendation first), `cowork-interview` (Claude draws out what you know, then writes it back), `cowork-confidence`, `cowork-premortem`, `cowork-postmortem`. For understanding: `cowork-again` (the last answer in plainer words), `cowork-questions-for` (the questions for an accountant, a contractor, a teacher), `cowork-meeting-pack` (a brief, a script and a capture sheet before a meeting with a professional), `cowork-transcript`. For continuity: `cowork-where-was-i`, `cowork-wrap-up`. And `cowork-new-binder`, for a project the kit does not describe. |
| `research`, **Research** | Notes and reading: capture from anywhere, file at your desk, answer from what you have read. | `research-setup`, `research-inbox-drain` (the captures, one at a time, into notes to your conventions), `research-source-note` (one note from a handed article, paper or transcript, citation recorded), `research-description-check` (what the description claims that is no longer true). |
| `learn`, **Learning** | A subject, a skill or an exam, learned on purpose, with a plan and a record of what has clicked. | `learn-setup` (the mission and the curriculum), `learn-lesson` (thirty minutes, one concept, intuition first), `learn-quiz` (recall, graded, difficulty rising). |
| `week`, **Your week** | Obligations turned into next actions, and a week planned from the time you actually have. | `week-setup`, `week-triage`, `week-plan`, `week-review`, `week-meeting-notes`, `week-reply` (a draft in your voice; it never sends). |
| `money`, **Money** | Statements and a monthly close, with account details kept out of everything that syncs. | `money-setup` (the privacy floor first), `money-statement`, `money-close`. |
| `medical`, **Medical records** | A record you can compare across visits, and appointments prepared from it. | `medical-setup`, `medical-visit-prep` (the questions from what changed, and a visit pack when someone is coming with you), `medical-record-visit`, `medical-check-in` (a weekly functional log in your own words), `medical-treatment-questions` (grades the evidence an article cites and writes the questions). |
| `template/` | For contributors and readers comfortable editing files: a project plugin with the brackets left in. A project of your own does not need it; the core's `cowork-new-binder` designs one and hands back its text. | None; it is a skeleton. |

Each plugin's README lists its skills with the phrases that trigger them. Everything a skill does you could ask for in a sentence, more slowly; the skills are the upgrade and the instruction blocks are the floor. The setup skills hand back only what the app still needs from your hands: a task can create project docs and read your folder, but it cannot change your settings, create a project, connect a folder or install a plugin.

## Install

Everything installs from the Claude desktop app, under Customize, then Plugins. Two ways:

- **From the marketplace.** Choose **Add marketplace**, enter `ChristopherA/claude-cowork-kit`, and install a plugin from the list it shows. Installing this way also brings updates.
- **From a file.** Download the plugin's `.plugin` file from the [releases page](https://github.com/ChristopherA/claude-cowork-kit/releases) and add it with the upload option on the same Plugins page. The release notes carry each file's checksum.

Turn the plugin on after installing it. Do not drag a `.plugin` file into a task's composer: a plugin dropped there is attached to that one task only and is gone with it. The releases carry whole plugins. A single skill can be added on its own, as a `.skill` file the kit's build writes, under Customize, Skills; that is for someone building from the repository.

Install one plugin at a time, and run its setup before installing the next.

## First run

1. **Back up your notes folder** with whatever you already use. Do it before the first task that is allowed to write, not after. If the folder is in iCloud Drive, turn on Optimize Mac Storage and Time Machine as well; the explainer's section What the connected folder does and does not protect says why.
2. **Install the notes plugin**, shown as **Research** (its file name is `research`), by either path above, and turn it on. It is the project the others learn their habits from, and no other plugin has to come first.
3. **Create the project and connect the folder.** Make an ordinary project in the app and name it, then connect your notes folder to it from the project's page. Do not create the project *from* the folder: a project created that way lives on that computer and does not sync, which silently breaks the phone half of this.
4. **Run the setup.** In a task inside that project, say `set up my notes project`. Claude asks three questions, creates the project docs, and hands back what only you can paste: the account instructions, if your Settings, Account, "Instructions for Claude" field does not carry them yet, and the short project instructions for the Instructions panel at the side of the project page. It then names the day-one checks, the phone check first.
5. **Install the core plugin** (`cowork-kit`, shown as **Cowork Kit core**) when you want its routines; they work in every project. Its own setup, `set up the kit`, is for a reader who starts there instead.

Before you connect a folder, read what the connected folder does and does not protect: `PRIVACY.md` here, and the explainer's section What the connected folder does and does not protect. Everything Claude can reach in a connected folder it may read, and a file in that folder can carry instructions Claude will follow.

Setup takes about thirty minutes for the first project. You make the decisions; Claude does the typing. Where Customize and Settings sit in the app's layout is one of the things the kit is still confirming; both are in the desktop app.

## Status

Release candidate. The notes plugin has had one run in Cowork; the core and the four project plugins have not run yet, and whether the phone app runs plugins is not yet confirmed. Anything the kit is still confirming is marked as such where it appears.

## Where the reasoning lives

- [The explainer](docs/claude-cowork-kit.md): why Cowork, how the three places things can live differ, why the description is not a copy, what the connected folder does and does not protect, the two approval modes, and what the kit will not do. It prints the account instructions and the three voices.
- One document per project under [`docs/binders/`](docs/binders/): [notes](docs/binders/research.md), [learning](docs/binders/learning.md), [your week](docs/binders/week.md), [money](docs/binders/money.md) and [medical records](docs/binders/medical.md), each with the project's use case, its skills and when to reach for each, its setup, a check that it works, and the text its setup writes, printed so you can read it first or paste it by hand with no plugin at all.
- [The skills index](docs/skills.md): every skill in every plugin, what it does, when to reach for it, and what it hands back.
- Each plugin's README, `plugins/<name>/README.md`: its skills and the phrases that trigger them.
- `docs/skill-capabilities.md`: what a Cowork skill can and cannot reach, measured in the app.
- `PRIVACY.md`: what leaves your computer and what does not. `CHANGELOG.md`: what each release changed. `CONTRIBUTING.md`: how to report a problem or change the text.

## For contributors

- `docs/` holds the explainer and, under `docs/binders/`, one document per project; the blocks in every built plugin are generated from those files and never edited by hand. `docs/shared.md` holds the paragraphs several skills carry word for word, and `docs/skills.md` is the public skills index; the build fails when a copy differs or the index does not match the skills.
- `plugins/<name>/` is one directory per plugin: its skills (`skills/<skill>/SKILL.md`, with read-only `scripts/` where a skill runs code), its manifest and README, and the setup skill's `references/`, the last three generated by the build and committed so the tree serves as a marketplace (`.claude-plugin/marketplace.json` lists them).
- `build.py` checks every skill the way Cowork's upload does, generates the manifests, READMEs and setup references from the docs in place (`--check` fails when they drift, or when a generated file is uncommitted in a git checkout), and writes each plugin as a `.plugin` file and each skill as a `.skill` file under `dist/`, which is not tracked.
- `template/` is a project plugin with the brackets left in. `tests/fixture/` is a small notes folder and the project docs a setup run should produce.

## License

BSD-2-Clause-Patent. See `LICENSE`.
