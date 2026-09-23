# pkm

Skills for the Claude Cowork Kit's notes project: set the project up, drain the capture inbox, write a source note, and check the description against the folder.

Each skill expects the notes project the Claude Cowork Kit describes: a notes folder connected in the desktop app, a project doc `rules.md` with the working rules, a project doc `map.md` describing the folder, and a project doc `inbox.md` for captures. The three skills with scripts read the folder only; they never write to it without the reader's yes, and each says in its body what to do when code execution is off.

## Skills

- `pkm-description-check`: Compares map.md against the notes folder and reports every claim that is no longer true, proposing edits without making them. Use for "check the description", "is map.md still right".
- `pkm-inbox-drain`: Processes the capture inbox one item at a time into notes in the notes folder, to map.md conventions. Use when the user says "process the inbox", "drain the inbox", or "file my captures".
- `pkm-setup`: Sets up the notes project: four questions, then rules.md, map.md and inbox.md as project docs and the short instructions to paste. Use for "set up my notes project", "notes setup", "set up my notes".
- `pkm-source-note`: Writes one source note from a book, paper, article or transcript the user hands over, citation recorded, source claims kept apart from the user's own. Use for "make a source note", "source note".

## Install

In the Claude desktop app, either add this repository as a marketplace (Customize, Plugins, Add marketplace, `ChristopherA/claude-cowork-kit`) and install the plugin from it, or download the `.plugin` file from a release and upload it (Customize, Plugins, the upload option), then turn it on. A plugin dragged into a task's composer is attached to that task only. To add one skill instead of the set: Customize, Skills, upload the matching `.skill` file.
