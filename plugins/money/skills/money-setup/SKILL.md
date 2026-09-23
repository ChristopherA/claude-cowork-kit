---
name: money-setup
description: Sets up the money project: the privacy floor, three questions, then categories.md and targets.md as project docs and the instructions to paste. Use for "set up my money project", "money setup".
---

# Money setup

Build the money project the Claude Cowork Kit describes, from three answers. Create what a task can create, the two project docs, and hand back what only the reader can paste, the project instructions. Read the financial files folder if it is connected; do not write into it.

The text this skill hands back is in `references/`, generated from the kit's explainer when the plugin was packaged: `money-instructions.md` (the project instructions). Use it as it is; do not rewrite it, and do not paraphrase it into the conversation. Fill in only the folder path where it is marked.

## What a task can and cannot do

A task can read the project docs, create project docs in the project it runs in, and read a connected folder. It cannot set anything in Settings, set the project's approval mode, create a project, connect a folder, or install a plugin; those are the reader's, in the app. Say which is which as you go, so the reader never waits for something that will not happen.

## Before the first question

Check which of `categories.md` and `targets.md` already exist. If `categories.md` does, this project is already set up: say so and stop. Do not run setup twice. A doc that exists is kept and read back, never recreated; say which you kept.

Then, before asking anything, say plainly what the folder does and does not protect, in a short paragraph of your own words that keeps every point of this one. The statements and exports stay in the folder on the reader's computer, and the project docs hold only what they would be relaxed about syncing: categories, targets, and summaries with no account details. That keeps the records out of project knowledge, out of every other project, and off the phone. It does not keep them off the cloud: when a session reads a statement to answer a question, that statement goes to the session, which runs in the cloud, and the reader decides whether that is acceptable. One floor holds for everyone: credentials, logins and card numbers never go in a connected folder or a pasted message. Keep this project in the mode that asks before acting; that is set by the reader, in the app, and a task cannot set it. And if Claude can use the computer's screen and apps at all, block the banking apps and sites from it in Cowork's settings, so a task in some other project never wanders into them.

Ask whether to go on. If the reader would rather not let a session read their records, stop here and say the project can still hold categories and targets they type in by hand; do not argue the point.

## Three questions, one at a time

Ask as the Asking section says, grouping the questions whose answers do not depend on each other in one control and putting the dependent ones after. Skip any the reader has already answered in their request.

1. **The folder.** Where the financial files are on their computer. If they name a folder, confirm you can reach it; if you cannot, say so and continue from their description, and say that the folder is reachable only at the desk. If it is reachable, list the top-level folders and file names and roughly how many files there are, without opening any file; do not read a statement during setup.
2. **The categories.** What categories they sort their spending and income into. Offer to start from a short common set (housing, utilities, groceries, transport, health, insurance, subscriptions, eating out, other) and let them add, rename and remove, or take their own list as given. A category is a name and one line saying what falls in it; ask for the line where a name is ambiguous. Do not invent categories they did not accept.
3. **The targets.** Whether they have budget targets, per category or in total, and for what period. Take the figures exactly as the reader gives them; never propose a figure, and never fill one in from a statement. If they have none, say that `targets.md` will hold a heading and nothing else until they do.

## Create the two project docs

Create `categories.md` as a project doc: a heading, then one line per category, the name and its one-line definition, in the order the reader gave them. Nothing else goes in it.

Create `targets.md` as a project doc: a heading, then one line per target as the reader gave it, with its period. If they gave none, the heading alone.

Neither doc holds an account number, a balance, or a transaction row, and neither names the folder path; the path lives in the instructions. Read both back and confirm they exist as project docs. The app may file them under a `claude/` folder inside the project; that is fine, and the other skills find them by name. If project docs cannot be created from a task, say so plainly, show both texts in full so the reader can add them however the app allows, and say that the statement and close skills depend on them.

## Hand back the text to paste

The project page has two text fields that look alike, a one-line description under the title and an Instructions panel at the side, and readers put the instructions in the description. So hand back two things, in this order, and say which field each goes in. If the project's description already holds the instructions text, say so and tell the reader to move it.

0. **The description**, one line, for the field under the project's title. Offer this: `Household money: statements stay in [folder name] on my computer; the rules are in Instructions.` with the folder name filled in.

The instructions go into a field only the reader can fill: a task can create project docs and cannot set the project's instructions or description, and the shell a task runs in is a Linux space apart from the reader's computer, so it cannot put text on their clipboard either. Do not try; hand the text back and say where it goes. The text goes in a code block of its own, which carries a copy button in the app.

1. **Project instructions**, from `references/money-instructions.md`, with the folder path filled in where it is marked and nothing else changed. It goes in the Instructions panel on the project's page, not in the project's description; the description is visible to a task too, but it is a label, and the reader should not have to know that it happens to work.

Show the block whole, one code block, and nothing else inside the fence. The account-wide instructions are the core plugin's job, handed back by its setup skill; if the reader's Account field does not yet carry the kit's block, say so and point them there rather than handing it back here.

## End

Report what exists now: the two project docs by name, and the two fields waiting for a paste, the description and Instructions. Then name what only the reader can do, in the app: set the project's mode to ask before acting, and block banking apps and sites from screen use if screen use is on. Then name the day-one check: at the desk, with the folder connected, drop one statement or export in it and ask for a summary; the summary should show categories and totals and nothing that identifies an account. Do not run it; the reader does.

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never ask what the reader has already said.

## What this skill does not do

It does not read a statement or write any number into a project doc. It does not set any setting, set the approval mode, create a project, connect a folder, or install a plugin. It does not paste anything anywhere; it hands text back. It does not hand back the account-wide instructions; the core plugin's setup does. It does not advise on investments or tax, log into or connect to any account, or supply a number the reader did not give. It does not run twice on a project that already has category definitions.
