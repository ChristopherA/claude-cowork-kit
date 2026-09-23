# week

Skills for the Claude Cowork Kit's week project: set it up, triage a pile of obligations into next actions, plan the week, review it, and draft a reply without sending it.

Each skill expects the week project the Claude Cowork Kit describes: a working folder connected in the desktop app, a priorities doc the setup creates, and a reviews doc the review creates. Nothing here sends a message or changes a calendar; drafts are handed back.

## Skills

- `week-plan`: Plans the week from the calendar and priorities.md, assuming less time than stated, and flags a plan that only works if nothing goes wrong. Use for "plan my week", "lay out this week".
- `week-reply`: Drafts a reply in the reader's voice from the message they hand over and their earlier replies, then stops; never sends. Use for "draft a reply", "answer this for me", "write back to".
- `week-review`: A weekly review in the reader's words: done, slipped, avoided, what ate the week, energy; compared with recent weeks, carry-forward listed, priorities.md changes on a yes. Use for "review my week".
- `week-setup`: Sets up the week project: three questions, then priorities.md as a project doc and the short instructions to paste. Use for "set up my week project", "week setup".
- `week-triage`: Turns a dump of half-formed obligations into a short ordered list of next actions, each startable today. Use for "triage this", "what do I actually need to do", "sort this out".

## Install

In the Claude desktop app, either add this repository as a marketplace (Customize, Plugins, Add marketplace, `ChristopherA/claude-cowork-kit`) and install the plugin from it, or download the `.plugin` file from a release and upload it (Customize, Plugins, the upload option), then turn it on. A plugin dragged into a task's composer is attached to that task only. To add one skill instead of the set: Customize, Skills, upload the matching `.skill` file.
