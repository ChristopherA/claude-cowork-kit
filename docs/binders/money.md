# The money binder

Tracking your household money: statements, exports, budgets, and the questions you ask about them, with account details kept out of everything that syncs. Its plugin is `money`, shown as **CWK Money Binder** in the app. The reasoning every binder shares is in [the kit's explainer](../claude-cowork-kit.md), and its section on what the connected folder does and does not protect is the one to read before this binder; the setup opens by saying the same thing.

The floor here is exact. Statements and exports stay in the folder on your computer; the Context documents hold your category definitions, your budget targets, and summaries with no account details in them, because Context documents sync to the cloud and reach your phone. Every number Claude gives you traces to a row in a file you gave it, and it never estimates, rounds, or fills in a figure to make a total come out. Keep this project in the mode that asks before acting. If you let Claude use your computer's screen and apps at all, block your banking apps and sites from it in the Cowork settings that govern computer use, so a task in some other project never wanders into them.

## The skills

- **`money-setup`**, `set up my money binder`. The privacy floor first, then three questions, then the two Context documents and the instructions to paste. If you would rather not let a session read your records, it stops there, and the binder can still hold categories and targets you type by hand.
- **`money-statement`**, `summarize this statement`. One statement or export from the folder into categories and totals, every figure traced to a row, nothing that identifies an account in the summary. At your desk, with the folder connected.
- **`money-close`**, `close the month`. A month's transactions categorized against your categories, the arithmetic shown, compared with your targets, and a summary written with no account details. It stops at a missing file rather than working around it.

## Setup

The setup creates two Context documents: `categories.md`, each category with one line saying what falls in it, and `targets.md`, your budget targets as you give them, or a heading and nothing else until you have some. Neither holds an account number, a balance, a transaction row, or the folder path. The general steps and the install paths are in the repository's README, under First run and Install; for this binder:

1. **Install the money plugin**, `money`, shown as **CWK Money Binder**, and turn it on.
2. **Create the project with its folder.** In Claude, open **Projects**, then **New project**, and fill in the dialog:
   - **What are you working on?** The binder's name, such as `Money`.
   - **What are you trying to achieve?** A sentence or two saying what the binder is for. Paste this and change it to suit:

     ```
     My household money: statements, spending categories, and a monthly close against my budget targets.
     ```

     The app reads this when deciding which project a task belongs in; the rules Claude works by come later, from the setup. Keep it general, with no names, conditions or account details: it syncs with the project.
   - **Folder:** choose **Use a folder** and pick the folder that holds your financial files and nothing else.

   Click **Create project**. When Claude asks to change files in the folder, choose **Allow**, not Always allow, so it asks again each time; this binder holds what you would mind leaking.
3. **Run the setup.** On the project page, switch the box at the top from **Chat** to **Cowork**, then say `set up my money binder`. Claude says what the folder does and does not protect and asks whether to go on; then asks where the folder is, what your categories are, and what your targets are; creates the two Context documents; and hands back what only you can paste: the account instructions, if your Settings, Account, "Instructions for Claude" field does not carry them yet (the account instructions in the explainer), and the project instructions below, for **Instructions** on the right of the project page (click its pencil and paste), not the description under the title.
4. **In the app,** keep this project in the mode that asks before acting, and if you have let Claude see and control your screen, keep your banking apps and sites out of its reach.

Without the plugin: paste the account instructions as the explainer says, create the project, create `categories.md` and `targets.md`, either by asking Claude in a Cowork task to write them from your answers or by hand, in the **Context** panel with **+**, **Add text content**, the title typed exactly and every [BRACKET] filled in before you add it, and paste the block below, with the folder path filled in, into **Instructions** on the right of the project page (click its pencil).

## Check it works

First look at the project's **Context** panel: `categories.md` and `targets.md` should be there (one Claude created may show as `claude/` followed by its name, which is fine), with no [BRACKET] left in them, and no account number, balance or figure from a statement, and the capacity bar should be nearly empty, since Context holds a description and never copies of your files. Then:

1. **At your desk, with the folder connected,** drop one statement or export in it and ask for a summary. The summary should show categories and totals and nothing that identifies an account.
2. **From your phone, with the computer closed,** ask what your categories are; the Context document alone can answer, and no figure from a statement should come with it.

---

## The project instructions

Paste into the project's Instructions panel, with the folder path filled in. The setup hands this back with it filled.

```
# What this project is for

Tracking my household money: statements, exports, budgets, and the questions I ask about them.

# What belongs elsewhere

Not investment picking, not tax preparation, and not a place to research either — if I start down one of those, say so. A medical bill's amount belongs here; the clinical record behind it belongs in my health binder.

Anything that isn't about my household's money, tell me which binder it belongs in and stop.

# Where things live

My financial files are in [FOLDER PATH ON MY COMPUTER]. Statements and exports stay there. Never copy account numbers, balances, or transaction rows into Context documents — those sync to the cloud.

Context documents hold my category definitions, my budget targets, and summaries with no account details in them.

# Accuracy

Every number you give me must trace to a row in a file I gave you. Never estimate, interpolate, or round a figure to make a total come out. If data is missing, tell me which file and which period is missing and stop there.

Show the arithmetic whenever it isn't obvious, so I can check it rather than trust it.

If a figure in my own records looks wrong to you, say so before using it in a total.

# What you are not

You are not my financial advisor and shouldn't talk like one. Lay out the numbers and the tradeoffs and let me decide. When I ask whether to do something, tell me what the decision turns on instead of telling me what to pick.

# Never

Don't log into, connect to, or transact on any account. Don't supply a number I didn't give you.
```
