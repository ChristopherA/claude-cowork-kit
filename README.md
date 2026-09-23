# Claude Cowork Kit

Plugins for people who use Claude in the desktop and mobile apps rather than in a terminal. Install one, start a task, and Claude sets up a project with you: it asks what you want, creates the project's docs, and hands back the one block of text only you can paste. Each project keeps its material as plain files in a folder on your own computer, so nothing you build depends on Claude, and the plugins add the routines that make the project worth opening: a decision worked through one question at a time, an inbox of captures filed to your own conventions, a visit prepared from what changed in your record, a week planned from what is actually on the calendar.

## Who it is for

You use Claude Cowork: the desktop app with a folder connected, and the phone app for everything that does not need the folder. You are not a programmer and do not want to become one to keep notes with Claude.

It is not for Claude Code, the command-line tool developers use, and it is not for plain chat. Most published advice for working with Claude on your own files is written for one of those two, and where this kit disagrees with it, that is usually the difference. If you are comfortable in a terminal, [Claude Code](https://docs.anthropic.com/en/docs/claude-code) will do more than this kit can, and the folder this kit builds works unchanged under it when you get there.

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
| `cowork-kit`, **Cowork Kit core** | The setup, and twelve routines that work in any project. | `cowork-setup` asks who you are and hands back your account instructions. For deciding: `cowork-clarify` (one question at a time, recommendation first), `cowork-interview` (Claude draws out what you know, then writes it back), `cowork-confidence`, `cowork-premortem`, `cowork-postmortem`. For understanding: `cowork-again` (the last answer in plainer words), `cowork-questions-for` (the questions for an accountant, a contractor, a teacher), `cowork-meeting-pack` (a brief, a script and a capture sheet before a meeting with a professional), `cowork-transcript`. For continuity: `cowork-where-was-i`, `cowork-wrap-up`. And `cowork-new-project`, for a project the kit does not describe. |
| `pkm`, **Personal knowledge** | Notes and reading: capture from anywhere, file at your desk, answer from what you have read. | `pkm-setup`, `pkm-inbox-drain` (the captures, one at a time, into notes to your conventions), `pkm-source-note` (one note from a handed article, paper or transcript, citation recorded), `pkm-description-check` (what the description claims that is no longer true). |
| `learn`, **Learning** | A subject, a skill or an exam, learned on purpose, with a plan and a record of what has clicked. | `learn-setup` (the mission and the curriculum), `learn-lesson` (thirty minutes, one concept, intuition first), `learn-quiz` (recall, graded, difficulty rising). |
| `week`, **Your week** | Obligations turned into next actions, and a week planned from the time you actually have. | `week-setup`, `week-triage`, `week-plan`, `week-review`, `week-meeting-notes`, `week-reply` (a draft in your voice; it never sends). |
| `money`, **Money** | Statements and a monthly close, with account details kept out of everything that syncs. | `money-setup` (the privacy floor first), `money-statement`, `money-close`. |
| `medical`, **Medical records** | A record you can compare across visits, and appointments prepared from it. | `medical-setup`, `medical-visit-prep` (the questions from what changed, and a visit pack when someone is coming with you), `medical-record-visit`, `medical-check-in` (a weekly functional log in your own words), `medical-treatment-questions` (grades the evidence an article cites and writes the questions). |
| `template/` | A project plugin with the brackets left in, for a project of your own. | The core's `cowork-new-project` fills it with you. |

Each plugin's README lists its skills with the phrases that trigger them. A skill is a routine Claude runs when what you say matches its description; there is no command to remember, and everything a skill does you could ask for in a sentence, more slowly. The setup skills hand back only what the app still needs from your hands: a task can create project docs and read your folder, but it cannot change your settings, create a project, connect a folder or install a plugin.

## Install

Everything installs from the Claude desktop app, under Customize, then Plugins. Two ways:

- **From the marketplace.** Choose **Add marketplace**, enter `ChristopherA/claude-cowork-kit`, and install a plugin from the list it shows. Installing this way also brings updates.
- **From a file.** Download the plugin's `.plugin` file from the [releases page](https://github.com/ChristopherA/claude-cowork-kit/releases) and add it with the upload option on the same Plugins page. The release notes carry each file's checksum.

Turn the plugin on after installing it. Do not drag a `.plugin` file into a task's composer: a plugin dropped there is attached to that one task only and is gone with it. To add a single skill instead of a whole plugin, download its `.skill` file from the same release and upload it under Customize, Skills.

Install one plugin at a time, and run its setup before installing the next.

## First run

1. Install **Cowork Kit core** and turn it on.
2. Start a task and say `set up the kit`. Claude asks which voice you want and which project first, hands back one block of text for you to paste into Settings, Account, "Instructions for Claude", and names the plugin to install next.
3. Before you connect a folder, read the explainer's section on what the connected folder does and does not protect. It is the one thing worth knowing in advance: everything Claude can reach in a connected folder it may read, and a file in that folder can carry instructions Claude will follow.
4. Install the project plugin Claude named, create the project in the app, connect its folder, and in a task inside it say `set up my notes project` (or the project's own phrase, in its README). That setup creates the project docs and hands back the short instructions to paste into the project's Instructions panel.

Setup takes about thirty minutes for the first project. You make the decisions; Claude does the typing.

## Status

Release candidate. The notes plugin has had one run in Cowork; the core and the four project plugins have not run yet, and whether the phone app runs plugins is not yet confirmed. Anything the kit is still confirming is marked as such where it appears.

## Where the reasoning lives

- [The explainer](docs/claude-cowork-kit.md): why Cowork, how the three places things can live differ, why the description is not a copy, the two approval modes, the privacy floor for money and medical records, and what the kit will not do. It prints every block a setup hands back, so you can read what a setup will write before running it, or paste it by hand with no plugin at all.
- Each plugin's README, `plugins/<name>/README.md`: its skills and the phrases that trigger them.
- `docs/skill-capabilities.md`: what a Cowork skill can and cannot reach, measured in the app.

## For contributors

- `docs/` holds the explainer, the single source: the blocks in every built plugin are generated from it and never edited by hand. `docs/shared.md` holds the paragraphs several skills carry word for word; the build fails when a copy differs.
- `plugins/<name>/` is one directory per plugin: its skills (`skills/<skill>/SKILL.md`, with read-only `scripts/` where a skill runs code), its manifest and README, and the setup skill's `references/`, the last three generated by the build and committed so the tree serves as a marketplace (`.claude-plugin/marketplace.json` lists them).
- `build.py` checks every skill the way Cowork's upload does, generates the manifests, READMEs and setup references from the explainer in place (`--check` fails when they drift, or when a generated file is uncommitted in a git checkout), and writes each plugin as a `.plugin` file and each skill as a `.skill` file under `dist/`, which is not tracked.
- `template/` is a project plugin with the brackets left in. `tests/fixture/` is a small notes folder and the project docs a setup run should produce.

## License

BSD-2-Clause-Patent. See `LICENSE`.
