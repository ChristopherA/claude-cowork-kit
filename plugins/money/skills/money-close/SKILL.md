---
name: money-close
description: Closes a month: categorizes its transactions against categories.md, shows the arithmetic, compares with targets.md, writes a summary with no account details. Use for "close the month".
---

# Monthly close

Close one month: gather the files in the folder that cover it, categorize every transaction against `categories.md`, show the arithmetic, compare with `targets.md` where it has content, and write the month's summary to a Context document with no account details in it. This is the statement summary run across a whole month, with the comparison the reader set up the binder for.

## Where this runs

This skill belongs to the money binder, whose Context documents are `categories.md` and `targets.md`. Before anything else, check that they are here. If not, this is another binder: say which binder this skill is for and stop, so nothing is written into the wrong folder or the wrong Context documents; if this is the right binder and it is not set up yet, offer its setup, `set up my money binder`.

## Before starting

Read `categories.md` and then `targets.md` first if you have not this conversation. The first says what the categories are and what falls in each; the second says what the reader is aiming at, per category or in total, or holds a heading and nothing else.

Check that the financial files folder is reachable. If it is not, say so and stop; a month is closed at the desk, not from the phone. Do not close a month from the reader's description of it, from a pasted statement, or from memory of an earlier session.

Ask which month, if the reader did not say, through the app's question control, the most recent complete month first. Then list the files in the folder that cover any part of it, by name and period, and ask the reader to confirm the list; a month with an account missing from it closes as partial, and you cannot tell which accounts they hold from the folder alone. Say before reading that the files' contents go to Claude on Anthropic's servers; if the reader would rather not, stop.

## Working the month

1. Open each file in turn and say what it is: the kind of file, the period it covers, how many rows fall in the month. Do not repeat account numbers, holder names or balances, and do not write them anywhere.
2. Name what is missing before anything is added: a file whose period stops short of the month's end, an account the reader named that has no file, dates between two files that neither covers. Name the file and the period for each, and stop there, as the project's instructions say; the reader fetches the file and asks again. Do not fill the gap from another period or an estimate, and do not close a month with a gap in it.
3. Assign each row in the month to a category from `categories.md`, by its description and the category's definition. A row that fits none goes in a list of its own rather than the nearest category. A transfer between the reader's own accounts, a card paid from their own checking included, is listed as a transfer and kept out of spending and income, so the month does not count it twice.
4. A row that looks wrong, a duplicate across two files, an amount out of scale with its description, a date outside the month, is set aside and named before it goes into any total; it enters only when the reader says so.
5. Show the month: one line per category with its count of rows and total across all files; the uncategorized rows with descriptions and amounts and their total; transfers, count and total, apart; then the month's total spending and income. Under every total, the addition, so the reader can check it rather than trust it. Every figure traces to a row in a file read this session; never estimate, interpolate or round to make a total come out, and never supply a number the reader did not give.
6. Where `targets.md` has content, show one line per target: the target as the reader wrote it, the month's figure beside it, and the difference, with the subtraction shown. Where a target's period is not a month, say what the month's share would be only if the reader's own line says how to divide it; otherwise show the target and the month's figure side by side and say the periods differ. Where `targets.md` is a heading alone, say there are no targets to compare against, and stop there; do not propose any.

Do not batch across months. Do not carry a figure from one month's close into another; each close reads its files.

## Writing it down

Offer to write the month's summary to a Context document named for the month, such as `close-2026-08.md`. Show the text you would write, in full: the files read by the reader's own names for them and the periods they covered, what was missing, the category lines with counts and totals, the uncategorized count and total (the descriptions stay in the chat), the transfers, the month's totals, and the target comparison if there was one. It holds no account number, no balance, and no transaction row. Wait for a yes through the app's question control; silence is not a yes.

On a yes: write it, read it back to confirm it landed as shown, and say the document's name. On a no, leave nothing behind. Never write into the folder, and do not edit `categories.md` or `targets.md` during a close; if the month showed a category is missing or a definition is unclear, say so in one sentence at the end and let the reader change the document in its own step.

## Ending

Report: the month, the files read, what was missing by file and period, how many rows went into categories, how many did not fit and what they were, what was set aside as doubtful, how the month stood against each target, and whether the summary was written and where. End with one word for completeness: full (every file the reader named read whole, every row categorized or listed), partial (a file or period missing, or rows left uncategorized or doubtful, with the counts), or minimal (stopped before the totals, with the reason). If the reader asks what to do about a category over its target, lay out what the decision turns on and stop; the choice is theirs.

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never ask what the reader has already said. Silence is never a yes: a yes is a tap on the control or a word.

## What this skill does not do

It does not change `categories.md` or `targets.md`. It does not write into the folder, and it does not write to a Context document without a yes. It does not close a month from anything but files in the folder, and it does not carry figures between months. It does not advise on investments or tax, log into or connect to any account, or supply a number the reader did not give.
