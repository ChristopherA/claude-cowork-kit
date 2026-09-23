# money

Skills for the Claude Cowork Kit's money project: set it up with the privacy floor, summarize a statement, and close a month against your categories.

Each skill expects the money project the Claude Cowork Kit describes: statements in a connected folder that stays on the computer, and project docs holding only categories, targets and summaries with no account details. Keep the project in the mode that asks (the kit's explainer, under The two approval modes).

Version 0.1.0 of the Claude Cowork Kit; every plugin in a release carries the kit's version, and the releases are at https://github.com/ChristopherA/claude-cowork-kit/releases.

## Skills

- `money-close`: Closes a month: categorizes its transactions against categories.md, shows the arithmetic, compares with targets.md, writes a summary with no account details. Use for "close the month".
- `money-setup`: Sets up the money project: the privacy floor, three questions, then categories.md and targets.md as project docs and the instructions to paste. Use for "set up my money project", "money setup".
- `money-statement`: Summarizes one statement or export from the folder into categories and totals with no account details, every figure traced to a row. Use for "summarize this statement", "read this bank export".

## Install

In the Claude desktop app, under Customize, Plugins: install it from the marketplace `ChristopherA/claude-cowork-kit`, or upload `money.plugin` from a release, then turn it on. The repository's README, Install, has both paths in full and what not to do; `docs/binders/money.md` there has the setup and the text this plugin's setup hands back.
