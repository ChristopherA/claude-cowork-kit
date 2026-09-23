# money

Skills for the Claude Cowork Kit's money project: set it up with the privacy floor, summarize a statement, and close a month against your categories.

Each skill expects the money project the Claude Cowork Kit describes: statements in a connected folder that stays on the computer, and project docs holding only categories, targets and summaries with no account details. Keep the project in the mode that asks (the explainer, under The two approval modes).

## Skills

- `money-close`: Closes a month: categorizes its transactions against categories.md, shows the arithmetic, compares with targets.md, writes a summary with no account details. Use for "close the month".
- `money-setup`: Sets up the money project: the privacy floor, three questions, then categories.md and targets.md as project docs and the instructions to paste. Use for "set up my money project", "money setup".
- `money-statement`: Summarizes one statement or export from the folder into categories and totals with no account details, every figure traced to a row. Use for "summarize this statement", "read my export".

## Install

In the Claude desktop app, either add this repository as a marketplace (Customize, Plugins, Add marketplace, `ChristopherA/claude-cowork-kit`) and install the plugin from it, or download the `.plugin` file from a release and upload it (Customize, Plugins, the upload option), then turn it on. A plugin dragged into a task's composer is attached to that task only. To add one skill instead of the set: Customize, Skills, upload the matching `.skill` file.
