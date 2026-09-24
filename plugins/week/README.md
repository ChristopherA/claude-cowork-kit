# week

Skills for the Claude Cowork Kit's week binder: set it up, triage a pile of obligations into next actions, plan the week, review it, write up a meeting, and draft a reply without sending it.

Each skill expects the week binder the Claude Cowork Kit describes: a working folder connected in the desktop app, a priorities document the setup creates, and a reviews document the review creates. Nothing here sends a message or changes a calendar; drafts are handed back.

Version 0.1.0-rc.7 of the Claude Cowork Kit; every plugin in a release carries the kit's version, and the releases are at https://github.com/ChristopherA/claude-cowork-kit/releases.

## Skills

- `week-meeting-notes`: After a meeting: notes by topic with decisions first, quotes inline from this transcript only, action items with owners, carry-forward for a series; to the folder on a yes. Use for "meeting notes".
- `week-plan`: Plans the week from the calendar and priorities.md, assuming less time than stated, and flags a plan that only works if nothing goes wrong. Use for "plan my week", "lay out this week".
- `week-reply`: Drafts a reply in the reader's voice from the message they hand over and their earlier replies, then stops; never sends. Use for "draft a reply", "answer this for me", "write back to".
- `week-review`: A weekly review in the reader's words: done, slipped, avoided, what ate the week, energy; compared with recent weeks, priorities.md changes on a yes. Use for "review my week", "how did my week go".
- `week-setup`: Sets up the week binder: three questions, then priorities.md as a Context document and the short instructions to paste. Use for "set up my week binder", "week setup".
- `week-triage`: Turns a dump of half-formed obligations into a short ordered list of next actions, each startable today. Use for "triage this", "sort this pile out", "turn this into a to-do list".

## Install

In the Claude desktop app, under Customize, Plugins: install it from the marketplace `ChristopherA/claude-cowork-kit`, or upload `week.plugin` from a release, then turn it on. The repository's README, Install, has both paths in full and what not to do; `docs/binders/week.md` there has the setup and the text this plugin's setup hands back.
