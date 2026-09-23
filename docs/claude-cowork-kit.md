# The Claude Cowork Kit

Plain files that stay yours, and a Claude that knows them.

This kit is a set of plugins for Claude Cowork, with the reasoning beside them. A few words are used throughout and mean one thing each. *Cowork* is the mode of the Claude desktop and mobile apps that works inside projects and on your files. A *task* is one piece of work you start there, in a workspace of its own that is cleared when it ends. A *plugin* is a bundle you install once, in the desktop app under Customize, and a *skill* is one routine inside it: a way of doing a job that Claude picks up when you ask for that job in a phrase. The *marketplace* is the list the app can install plugins from, and this kit's repository is one.

The kit describes five projects, one for each part of life that files accumulate around: your notes and reading, something you are learning, your week, your money, your medical records. Each is its own plugin, whose setup skill asks a few questions, creates the project's docs, and hands back only what the app still needs from your hands. A core plugin carries routines that work in any project. Every project has the same shape: a folder of plain files on your own computer, a small description of it kept where your phone can read it, and a Claude that begins each conversation already knowing both. The files are ordinary. Open them in any editor, back them up, sync them however you like, or walk away from Claude entirely and still have everything.

This document is the part no plugin can carry: why Cowork, what the connected folder does and does not protect, the two approval modes, and what the kit will not do. Each project has a document of its own under `binders/`, with its use case, its skills, its setup, a check that it works, and the text its setup writes, printed so you can read it before running anything or paste it by hand. The account-wide text every project shares, the account instructions and the voices, is printed here. The repository's README says how to install; this document says why.

Setup takes about thirty minutes for the first project. You make the decisions; Claude does the typing.

---

## What this is for

The problem is not too little information. It is that the parts of life you keep files about, reading, learning, the week, money, health, each produce more than you can file, and the filing does not keep up with the capturing or the thinking. A good thought on a walk is gone by the time you are home. The statement you meant to reconcile sits unopened. The question you wanted to ask the doctor was clear a week ago and is gone at the appointment. Most systems for this fail not because they store too little but because keeping them going is a second job.

This kit is built for a few specific moments, and every project has its own version of each:

- A thought, a receipt, a symptom, captured from your phone in ten seconds and filed later, without deciding anything about where it goes at the moment you catch it.
- Something new connecting to something old, and Claude noticing, because it starts every conversation knowing what is in your files and what you are working on.
- A question at 11pm, answered from what you already have, with the laptop shut.
- The pile, worked through one item at a time at your desk, filed to your own conventions rather than left for a someday that never comes.

It is not a second brain that thinks for you, and it is not a search engine over your files. It is a Claude that begins each conversation already knowing what your files are and what you are working on. That turns out to be most of the value, and it is the part that survives if you stop using Claude tomorrow, because it lives in folders of plain files you can read yourself.

### What it won't do

It will not fetch for you: a task cannot reach the web on its own, use your browser or your logins, or keep anything installed from one session to the next, so a bookmark does not become a saved article and a citation by itself, and a patient portal does not get read. You save the PDF or paste the page, and Claude turns what you handed it into a note to your conventions. If you come expecting a pipeline, the kit will look broken when it is only scoped.

The limit is a floor, not a wall. Because everything here is plain files in ordinary folders, the same folders work unchanged under tools that run on your computer with your access to the web, when you are ready for them, and the description you write for this kit is the seed of what such a tool reads. Nothing you build now has to be redone.

### Why Cowork

You could do this other ways, and it is worth saying what each one costs.

**A notes app on its own,** Obsidian or Logseq with or without an AI plugin, gives you the same folder of files. What it does not give you is a Claude that can read the whole folder, write into it to your conventions, and answer from a description of it on your phone when the computer is closed. The plugins are desk-bound and each knows one app. This kit keeps your vault exactly as it is and adds that layer beside it.

**Claude Code,** the command-line tool, is the more powerful choice for someone at home in a terminal: it opens inside your folder, reads it directly, and anything it runs, runs on your computer with your access to the web. The price is a terminal, and no phone. Cowork is the same Claude reached through the desktop and mobile apps, and the price you pay instead is the description-versus-copy split explained below and the fact that the folder is reachable only while the desktop app is open. The two are not a fork in the road: start here, and when you want that tooling, point it at the same folder.

**An always-on assistant** that builds its memory by watching your screen is less work, and what you get back is a memory in that app's store, in that app's shape; this kit is the opposite bet, deliberate capture into plain files that are yours.

---

## What you need

A Claude plan that includes Cowork, and the Claude desktop app installed on the computer where your files live.

A folder for the project's files. An existing one is fine; an Obsidian or Logseq vault works as-is, and you should not reorganize it to match anything here. Connect that folder and only that folder: not Documents, not your home folder, not the parent it sits in. Everything Claude can reach it may read, and everything it reads goes to the session.

About thirty minutes, and a second sitting a couple of weeks later to trim what didn't work.

Optionally, Claude on your phone. That's what makes capture-from-anywhere work, and it's half the value.

One thing to know about cost. Cowork tasks draw on your plan's usage allowance much faster than chat does, so a plan that feels roomy for conversation can feel tight for file work. A long session also gets worse as it goes; start a fresh one for each piece of work rather than carrying a day's worth in one window.

---

## What you end up with

Five separate projects: one for notes and reading, one for running your week, one for money, one for medical records, one for learning something on purpose.

Separate, not one assistant that knows everything about you. That's worth saying plainly up front, because "one companion that remembers me" is the natural thing to expect and it isn't what this builds. Claude's memory is scoped to each project and doesn't cross between them, so a single all-knowing assistant isn't really on offer. The separation turns that constraint into something useful: your medical records don't surface while you're planning a work week, and a project you never share can't be shared by accident.

There is a second reason for the separation, beyond what memory allows. A knowledge project that also runs your week fills up with tasks, and the notes drown in them: every conversation starts with what is due rather than what you are thinking about. Keeping the knowledge project quiet is what makes it worth opening. The week, the money, the medical records, and whatever you are learning each get a project of their own, with its own plugin and its own document under `binders/`, and you build those only if you want them.

Most people should build one project, live with it for a week, and add the others only if they want them. All five at once is a lot of setup for a system you haven't tried yet.

---

## How it works

Three places things can live, and only two of them last. Then one fact about memory that decides what goes where.

**The folder on your computer is where the work lives.** Every file, unbounded in size, searchable, yours. Claude can reach it only while your computer is awake and the desktop app is running: from your desk, or from your phone if the computer happens to be open at home. Close the laptop and the folder is out of reach from everywhere.

**Project knowledge is what Claude carries with it.** A small set of docs attached to each project, reachable from your phone at 11pm, and still there when the laptop is shut. Small is the point: it holds a description of your files, not a copy of them.

**The session is a workbench that gets cleared.** Everything Claude does during a conversation happens in temporary space that's wiped when the conversation ends. This catches people constantly: they watch Claude build something good, close the window, and it's gone. Anything that matters has to land in one of the first two.

**Memory is for sessions that run in the cloud.** Claude remembers things across conversations, and that memory is scoped to each project. But a session that runs on your computer, the kind that reads your folder, does not use memory at all. So at your desk, the very place you'd expect Claude to remember last time, it works from two things only: the description in project knowledge and what's actually in the folder. That is why the description exists, and why it has to be kept true. (As Anthropic documents it, September 2026.)

### The description is not a copy

The tempting move is to upload your whole folder into project knowledge so Claude "knows" it. Don't. Project knowledge has to fit in what Claude can read at once, a few hundred pages as of September 2026, and past that point Claude stops reading your files and starts retrieving fragments of them. A real collection of notes blows through that, and what you'd get back is fuzzy search over fragments instead of Claude reading the actual file.

So project knowledge holds a *description* of your files: what's in them, how they're named, what you're currently chewing on. Plus any genuinely new writing you asked Claude for. Never copies of file bodies: the same text in two places drifts apart, and the drift is silent, so Claude ends up confidently working from the stale one.

The test for what goes where: **would I need this when I'm away from my computer?** If yes, project knowledge. Otherwise the folder.

### Capture and filing are different jobs

Capture from anywhere, phone, web, a thought on a walk, into an inbox doc in project knowledge. No decision about where it goes at the moment you catch it.

Drain that inbox later, at your desk, where the folder is connected and filing can be deliberate. The split falls out of the architecture rather than being imposed on it: the inbox is in the cloud because capture has to work everywhere, the files are on disk because filing shouldn't be rushed.

### If you can't read it yourself, it doesn't belong in your files

It's tempting to let Claude maintain elaborate metadata schemas and generated index files, because Claude is good at it and the retrieval feels clever. That structure rots the moment you stop using the agent, and leaves you a pile only software can love.

Plain markdown. Folders you can open in any editor. Filenames you can scan. Project knowledge is the Claude-specific layer and it should be the expendable one: if you deleted every project tomorrow, your files should be entirely intact and still make sense.

If you've seen kits that keep a memory file in the folder that Claude writes to as it learns, that's the same idea placed differently. This kit keeps the description where your phone can read it and keeps Claude's own bookkeeping out of your files on purpose: a file Claude maintains for Claude's benefit is exactly the pile only software can love.

The same test decides whether something earns a file at all, in any of the projects: would it help to have this written down the next time you talk to someone about it or make a decision? A capture, a source you will want again, a condition, a course, a priority: yes. A one-off question, a bad day, something already covered by a file you have: no, and the conversation is enough. Not everything needs tracking, and a folder of files nobody reopens is the second job this kit exists to avoid.

### Projects don't talk to each other

Claude working in one project cannot read or write another project's docs, and memory doesn't cross over either. Mostly this is the feature described above, but it has a sharp edge: a file filed in the wrong project doesn't get moved later. It sits there with the wrong context attached, and nothing reconciles it but you.

That's why each project's instructions block has a section telling Claude what belongs elsewhere, and to name the right project and stop rather than helpfully filing things wherever you happen to be standing.

### How Claude asks

Every skill in the kit asks its questions the same way, through the question control, the prompt a task shows with options to tap rather than a question to type an answer to. This is the rule every skill carries, and you can hold them to it. The one exception is a question that tests you, in the learning project: there no option is marked as recommended, because the mark would be the answer.

```
Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never ask what the reader has already said. Silence is never a yes: a yes is a tap on the control or a word.
```

---

## What the connected folder does and does not protect

Everything Claude can reach in a connected folder it may read, and everything it reads goes to the session, which runs in the cloud. Connect the folder the project is about and only that folder.

Two of the projects, money and medical, carry data you'd mind leaking, and it's worth being exact. **The sensitive material stays in the folder on your computer, and project docs hold only what you'd be relaxed about syncing.** That keeps your statements and records out of project knowledge, out of every other project, and off your phone. It does not keep them off Anthropic's servers: when Claude reads a statement to answer you, that statement goes to the session. Anthropic's own safety guidance says to avoid giving Claude local access to financial documents at all. Plenty of people are fine with a session reading a bank statement or a lab result and would never let it near a password; others draw the line further back. Where you draw it is yours to decide, and those two projects assume you've decided to let Claude read the records. One floor for everyone: credentials, logins, and card numbers never go in a connected folder or a pasted message. And keep both of those projects in the mode that asks before acting.

A file in a connected folder can carry instructions Claude will follow without being asked: Cowork reads certain files at the root of a connected folder at the start of a task, the way developer tools do. That is the reason to connect only folders whose contents you wrote or trust, and it is why this kit keeps its rules in the project docs rather than in a file on disk: your phone can read a project doc and cannot read the folder, and a file Claude can edit and then obeys unprompted is the wrong place for rules. Cowork also has folder instructions, set on the desktop when you connect the folder; the kit does not use them. Your instructions go in the two places described under Setting up a project.

Back the folder up before the first session that's allowed to write, with whatever you already use: Time Machine, your sync service's version history, git if that's your habit. Claude should never be the only copy of anything, and the kit's own rule that Claude shows you what it would change and waits for a yes is an instruction, not a backup; an instruction can be misread.

**If the folder is in iCloud Drive,** either in iCloud Drive itself, where the Files app on your phone reaches it too, or in Desktop or Documents with Desktop & Documents Folders turned on, two settings matter. Turn on Optimize Mac Storage, in System Settings under your name, then iCloud, then Drive: its label there promises the full contents of iCloud Drive stay on the Mac while there is room, and Claude can read only a file that is actually on the Mac. A file iCloud has moved off to free space still shows in the folder, with its size, and Claude cannot open it. And have Time Machine on, whatever else you use. A task reorganizing a synced folder has been reported copying files like that as empty ones and then deleting the originals, and iCloud's Recently Deleted did not bring them back; Time Machine did.

---

## The two approval modes

Cowork can pause for your approval before it acts on the world, sending, sharing, changing files outside the session, or it can act without asking. Whichever you pick, it always asks before permanently deleting a file, and the kit's own instructions make Claude show you what it would change in your folder and wait for a yes. The default is to ask. Leave it there for a project until you've watched it work for a while; switch a project to acting freely only when you've stopped reading the approvals because they're always right. For a project holding anything you'd mind leaking, keep it asking. Where that line sits is yours to draw; the kit only insists that you draw it on purpose. The switch is in the desktop app's Cowork settings; the kit has not yet pinned whether it is set per project or once for all tasks, so until you find it, the default, which asks, is what you have.

---

## Setting up a project

Every project is built the same way. The repository's README, under Install and First run, has the install steps in full and what not to do; each project's document has its own setup phrase and the docs its setup creates. The shape:

1. **Back the folder up** if you have not already; the section above says why.
2. **Install the project's plugin,** by either path the README gives, and turn it on. No plugin is a prerequisite for another: start with whichever project you want, though the notes project is the one the others learn their habits from.
3. **Create the project and connect the folder.** Make an ordinary project in the app and name it; the one-line description under the title is a label, and a sentence is enough. Then connect the folder to it from the project's page in the desktop app. Do not create the project *from* the folder: a project created from a folder lives on that computer and doesn't sync, which breaks the phone half of this entirely. If unsure, make an ordinary project and connect the folder to it.
4. **Run the setup.** In a task inside the project, say the phrase the project's document gives. Claude asks its questions, creates the project docs, and hands back what only you can paste: the account instructions, printed below, with your voice filled in, if your Settings, Account, "Instructions for Claude" field does not carry them yet; and the project instructions, for the Instructions panel at the side of the project page, not the one-line description under the title.

That is the whole gap between this and a one-click install: one install and two pastes, the first time, and one paste for each project after. A task can create project docs and read your folder, but it cannot write Settings, create a project, connect a folder, or install a plugin. Those are yours, and the steps above are exactly them. The core plugin, whose routines work in any project, is installed when you want them; its own setup, `set up the kit`, hands back the account instructions for a reader who starts there instead.

### Without the plugins

Everything a setup does can be done by hand from the printed blocks, in this order:

1. **Settings, Account, "Instructions for Claude".** Paste the account instructions printed below, with your chosen voice substituted in. The app's own label on this field says it reaches chats and Cowork alike; it is not the Cowork entry in the Settings sidebar.
2. **Create the project and connect the folder,** as in step 3 above.
3. **Ask Claude to create the project docs** the project's document names, from the texts printed there. The app has no way to create a project doc by hand, and a task can.
4. **Paste the project instructions** from the project's document into the Instructions panel at the side of the project page, not into the description.

---

## The account instructions

Paste into Settings, Account, "Instructions for Claude", with one of the voices below substituted where marked. These apply to every conversation, in every project, in chat as well as in tasks. Every project's setup hands this block back when the field does not carry it yet, and the core plugin's setup hands it back on its own.

```
I am not a programmer. Don't suggest code, scripts, or terminal commands unless I explicitly ask.

[PASTE YOUR CHOSEN VOICE HERE]

Answer in the chat by default. Make a file, doc, or page only when I ask for one, or when the thing itself is the deliverable.

If a request could reasonably mean two different things, ask me one question before starting rather than guessing.

Never send a message, reply to an email, create or change a calendar event, or delete anything without showing me exactly what you'd do and waiting for me to say go. Drafts are always fine.

Anything you build that isn't saved to a project doc or to a folder on my computer disappears when the session ends. Save it, or tell me it's disposable.

Where you're uncertain, say so in the sentence where it matters. Don't hedge everything to be safe, and don't state a guess as fact.

When you tell me you've changed something I'll look at, read it back and confirm the change landed before reporting it done. If I say it still looks wrong and the source says otherwise, tell me that instead of editing again.

When you finish something, tell me what changed and where it is — the folder and file name, or which project doc. One or two sentences.
```

The Account field reaches every conversation you have with Claude anywhere, casual chat included, and a task reads it as chat does; Cowork also has global instructions of its own under Settings, Cowork, reaching only tasks, and what that entry adds is something the kit is still confirming, so the account instructions go in the Account field either way.

**A trap worth naming.** Whatever goes in the Account field hits everything, including casual chat and every other project. "No bullet lists" is right for knowledge notes and actively wrong for a productivity project whose job is handing back ordered lists. Only universal preferences go global. Anything right in one project and wrong in another stays local, even at the cost of a little duplication; duplication you chose beats a rule that silently fights you in half your work.

The block above is at about the length where adding more starts diluting what's already there. If you add something, take something out.

---

## The voices

One of these goes into the account instructions where marked. They differ in warmth, not in honesty: all three keep Claude from flattering you, which is the part worth protecting.

**Plain.** Direct and unadorned.

```
Be direct. No preamble, no restating my question back to me, no summarizing at the end what you just said. Don't tell me an idea is interesting or that I've asked a good question. If I'm wrong, lead with that.
```

**Warm.** Friendly without being soft on the substance.

```
Be warm but never flattering. Encouragement about the work is fine; praise for asking is not. Skip preamble and don't restate my question back to me. If I'm wrong, say so kindly and say it first — don't soften it into a maybe.
```

**Archivist.** Spare, for people who want a filing system rather than a conversation.

```
Be spare. Record and retrieve rather than converse. Answer in as few words as the question allows, skip preamble entirely, and don't add commentary I didn't ask for. If I'm wrong, say so in one sentence.
```

All three tell Claude not to restate your question. Anthropic's own advice for delegating big deliverables is the opposite: have Claude repeat the ask back and pile up clarifying questions before starting. That advice is for handing off a report; this kit is for keeping files, where one question when something is genuinely ambiguous is the right amount. If you find yourself delegating bigger work from these projects, the voice block is the place to change it.

---

## Maintenance

**Prune.** People add instructions and never subtract. The failure is invisible: past a certain length Claude starts quietly weighting the wrong ones. Anything that never changed its behavior should go. The same goes for memory: everything Claude has remembered about you is listed under Topics in the Memory settings, where you can read, edit, or delete each entry, and pause or reset the whole thing. Read it at the two-week sitting; a wrong memory is a wrong instruction you never wrote.

**Widen the leash on purpose.** Every project's instructions make Claude show you what it would change in your folder and wait for a yes. That's right for the first weeks and wrong forever: a Claude that must ask before every rename is one you'll stop using for filing. At the two-week sitting, decide what it has earned, filing inbox items into the folder without a yes is the usual first step, renames and deletions the usual last, and change that sentence in the Instructions panel to say exactly that. Relax it deliberately, one permission at a time, rather than leaving it forever or dropping it on day one.

**Scheduled tasks are where this starts paying off,** with one shape to keep in mind. A scheduled task runs in the cloud, on its own, whether or not your computer is on, and for the same reason it cannot be tied to a folder on your computer at all. So a scheduled task works from project knowledge and connected services: a weekly pass that reads the inbox doc and the description, pulls the reading list out of the captures, and lists what's changed since last week. Anything that needs the folder itself, surfacing notes untouched in six months, finding where last week's thinking contradicts something from March, is a task you start at your desk, or a saved prompt you run there. Don't schedule anything that touches sensitive records or sends messages on your behalf; nobody is watching a scheduled run.

**The plugins.** The kit's skills ship as plugins, one per project plus the core. The README's table lists every plugin with its skills in a phrase, the skills index beside this document, `skills.md`, says for each skill when to reach for it and what it hands back, and each plugin's own README lists the phrases that trigger them. Install them one at a time, and run each plugin's setup before installing the next.

The instruction blocks are the floor and the plugins are the upgrade: everything a skill does, you can ask for in a sentence, more slowly. Skills trigger from their description rather than needing a command you have to remember. They run in Cowork tasks, not in plain chat, and whether the phone app runs them is something the kit is still confirming; the instruction blocks work from the phone regardless, which is why they are the floor. When you write your own, three good ones beat fifteen half-finished.

---

## The projects

One document each, under `binders/`: the project's use case, its skills and when to reach for each, its setup, a check that it works, and the text its setup writes, printed so you can read it first or paste it by hand. Each shares the account instructions and differs in what is distinctive about the work. Build them when you want them, not all at once.

- [Notes](binders/research.md): notes and reading. Capture from anywhere, file at your desk, answer from what you have read. The first project, and the one the others learn their habits from.
- [Learning](binders/learning.md): a subject, a skill or an exam, learned on purpose, with a plan and a record of what has clicked.
- [Your week](binders/week.md): obligations turned into next actions, and a week planned from the time you actually have.
- [Money](binders/money.md): statements and a monthly close, with account details kept out of everything that syncs.
- [Medical records](binders/medical.md): a record you can compare across visits, and appointments prepared from it.

For a project the kit does not describe, the core plugin's `cowork-new-binder` skill designs one with you and hands back its text.

---

*The framing of this kit, an on-ramp that names the outcome, a kickoff message that does the setup it can, a choice of voice, and the caution about treating outside material as data rather than instruction, owes a debt to Peter Kaminski's PKAI Starter Kit.*
