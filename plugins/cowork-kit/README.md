# cowork-kit

The Claude Cowork Kit's core: a setup interview that hands back the account instructions and says which project plugins to install next, plus four routines for any project: deciding, checking confidence, finding the thread, and learning from a mistake.

Install this plugin first, then start a task and say `set up the kit`. The setup skill asks a few questions, hands back the account-wide instructions to paste, and says which project plugin to install next. The other four skills work in any project.

## Skills

- `cowork-clarify`: Settles a decision one question at a time, or a plan in rounds, recommending first and ending with a summary and no action. Use for "help me decide", "clarify this", "stress-test my plan".
- `cowork-confidence`: Says plainly what Claude is confident about, what it is not, and what would close the gap, then asks whether to proceed. Use for "how sure are you", "confidence check", "what don't we know".
- `cowork-new-project`: Designs a project the kit does not describe: its purpose, boundaries and docs, then the instructions text and a plugin from the kit's template. Use for "new project", "a project for something else".
- `cowork-postmortem`: Works through what went wrong in four questions and ends with one change to the instructions or description, with approval. Use for "what went wrong", "postmortem", "why did that happen".
- `cowork-setup`: Sets up the Claude Cowork Kit: a short interview, the account instructions to paste, and which project plugin to install next. Use for "set up the kit", "get started", "install the cowork kit".
- `cowork-where-was-i`: Reads current work, the inbox and the newest notes, and recommends the one next step rather than a menu. Use for "where was I", "what should I do next", "I've lost the thread".

## Install

In the Claude desktop app, either add this repository as a marketplace (Customize, Plugins, Add marketplace, `ChristopherA/claude-cowork-kit`) and install the plugin from it, or download the `.plugin` file from a release and upload it (Customize, Plugins, the upload option), then turn it on. A plugin dragged into a task's composer is attached to that task only. To add one skill instead of the set: Customize, Skills, upload the matching `.skill` file.
