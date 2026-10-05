# research

Your research binder: capture ideas anywhere, file them into notes at your desk, write source notes, and answer from what you have read. Part of the Claude Cowork Kit (CWK).

Each skill expects the research binder the Claude Cowork Kit describes: a research folder connected in the desktop app, a Context document `rules.md` with the working rules, a Context document `map.md` describing the folder, and a Context document `inbox.md` for captures. The scripts in three of its skills only read the folder; the skills write to it only on the reader's yes, and each says in its body what to do when code execution is off.

Version 0.1.0-rc.8 of the Claude Cowork Kit; every plugin in a release carries the kit's version, and the releases are at https://github.com/ChristopherA/claude-cowork-kit/releases.

## Skills

- `research-description-check`: Compares map.md against the research folder and reports every claim that is no longer true, proposing edits without making them. Use for "check the description", "check map.md against my notes".
- `research-inbox-drain`: Processes the capture inbox one item at a time into notes in the research folder, to map.md conventions. Use for "process the inbox", "drain the inbox", "file my captures".
- `research-setup`: Sets up the research binder: three questions, two conventions, then rules.md, map.md and inbox.md in Context and text to paste. Use for "set up my research binder", "notes setup", "set up my notes".
- `research-source-note`: Writes one source note from a book, paper, article or transcript the reader hands over, the source's claims kept apart from the reader's own. Use for "source note", "save this article to my notes".

## Install

In the Claude desktop app, under Customize, Plugins: install it from the marketplace `ChristopherA/claude-cowork-kit`, or upload `research.plugin` from a release, then turn it on. The repository's README, Install, has both paths in full and what not to do; `docs/binders/research.md` there has the setup and the text this plugin's setup hands back.
