# How the Claude Cowork Kit works

Plain files that stay yours, and a Claude that knows them.

The [README](../README.md) says what the kit is, what each plugin does, and how to install it and run your first setup; it also defines the words used here, under Words you will see. This document is the part no plugin can carry: how the pieces fit together, what the connected folder does and does not protect, how to set up a binder with no plugin at all, and what to change once you have lived with it. Read it before you connect a folder, and come back to it when something surprises you.

- [What this is for](#what-this-is-for), what it won't do, and why Cowork
- [How it works](#how-it-works): the three places things live, and the habits that follow from them
- [When something surprises you](#when-something-surprises-you): what you see, why, and what to do
- [Using your binders from your iPhone or iPad](#using-your-binders-from-your-iphone-or-ipad): what the phone does, with the advanced options on a page of their own
- [What the connected folder does and does not protect](#what-the-connected-folder-does-and-does-not-protect)
- [The two approval modes](#the-two-approval-modes)
- [Setting up a binder without the plugins](#setting-up-a-binder-without-the-plugins), [the account instructions](#the-account-instructions) and [the voices](#the-voices)
- [Maintenance](#maintenance): the second sitting, and what comes after

---

## What this is for

The problem is not too little information. It is that the parts of life you keep files about, reading, learning, the week, money, health, each produce more than you can file, and the filing does not keep up with the capturing or the thinking. A good thought on a walk is gone by the time you are home. The statement you meant to reconcile sits unopened. The question you wanted to ask the doctor was clear a week ago and is gone at the appointment. Most systems for this fail not because they store too little but because keeping them going is a second job.

This kit is built for a few specific moments, and every binder has its own version of each:

- A thought, a receipt, a symptom, captured from your phone in ten seconds and filed later, without deciding anything about where it goes at the moment you catch it.
- Something new connecting to something old, and Claude noticing, because it starts every conversation knowing what is in your files and what you are working on.
- A question at 11pm, answered from what you already have, with the laptop shut.
- The pile, worked through one item at a time at your desk, filed to your own conventions rather than left for a someday that never comes.

It is not a second brain that thinks for you, and it is not a search engine over your files. It is a Claude that begins each conversation already knowing what your files are and what you are working on. That turns out to be most of the value, and it is the part that survives if you stop using Claude tomorrow, because it lives in folders of plain files you can read yourself.

### What it won't do

It will not fetch for you: a task cannot reach the web on its own, use your browser or your logins, or keep anything installed from one session to the next, so a bookmark does not become a saved article and a citation by itself, and a patient portal does not get read. You save the PDF or paste the page, and Claude turns what you handed it into a note to your conventions. If you come expecting a pipeline, the kit will look broken when it is only scoped.

The limit is a floor, not a wall. Because everything here is plain files in ordinary folders, the same folders work unchanged under tools that run on your computer with your access to the web, when you are ready for them, and the description you write for this kit is the seed of what such a tool reads. Nothing you build now has to be redone.

### Why Cowork

You could do this other ways, and each one costs something.

| Approach | Reads your whole folder | Works from your phone | Your material stays plain files | Needs a terminal |
|---|---|---|---|---|
| Chat with a project | no, only what you upload | yes | no, it lives in the account | no |
| An AI plugin in Obsidian or Logseq | yes | no | yes | no |
| Claude Code | yes | no | yes | yes |
| An always-on assistant that watches your screen | it builds its own store | yes | no | no |
| **Cowork with this kit** | yes, while the desktop app is open | yes, from a description of the folder | yes | no |

The phone column of the last row is the whole trick: from the phone, Claude works from a small description of your notes kept in the project's Context, not from the notes themselves, which stay on your computer. That split, what goes in the folder and what goes in the description, is the one idea the kit is built around, and How it works, below, is about it.

**A notes app on its own,** Obsidian or Logseq with or without an AI plugin, gives you the same folder of files. What it does not give you is a Claude that can read the whole folder, write into it to your conventions, and answer from a description of it on your phone when the computer is closed. The plugins are desk-bound and each knows one app. This kit keeps your vault exactly as it is and adds that layer beside it.

**Claude Code,** the command-line tool, is the more powerful choice for someone at home in a terminal: it opens inside your folder, reads it directly, and anything it runs, runs on your computer with your access to the web. The price is a terminal, and no phone. Cowork is the same Claude reached through the desktop and mobile apps, and the price you pay instead is the description-versus-copy split explained below and the fact that the folder is reachable only while the desktop app is open. The two are not a fork in the road: start here, and when you want that tooling, point it at the same folder.

**An always-on assistant** that builds its memory by watching your screen is less work, and what you get back is a memory in that app's store, in that app's shape; this kit is the opposite bet, deliberate capture into plain files that are yours.

---

## How it works

Three places things can live, and only two of them last. Then one fact about memory that decides what goes where.

**The folder on your computer is where the work lives.** Every file, unbounded in size, searchable, yours. Claude can reach it only while your computer is awake and the desktop app is running: in a Cowork task started on the Mac. A conversation started on your phone runs in the cloud and cannot reach the folder; a task started on the Mac and continued from your phone can, while the Mac is awake with Claude open. Close the laptop and the folder is out of reach from everywhere.

**Context is what Claude carries with it.** A small set of Context documents attached to each project, reachable from your phone at 11pm, and still there when the laptop is shut. Small is the point: it holds a description of your files, not a copy of them.

**The session is a workbench that gets cleared.** A task's work runs in a session, in the cloud by default or on your computer; Claude itself runs on Anthropic's servers either way. Everything Claude does during a conversation happens in temporary space that's wiped when the conversation ends. This catches people constantly: they watch Claude build something good, close the window, and it's gone. Anything that matters has to land in one of the first two.

**Memory is for sessions that run in the cloud.** Claude remembers things across conversations, and that memory is scoped to each project. But a session that runs on your computer, the kind that reads your folder, does not use memory at all. So at your desk, the very place you'd expect Claude to remember last time, it works from two things only: the description in Context and what's actually in the folder. That is why the description exists, and why it has to be kept true. (As Anthropic documents it, September 2026.)

### The description is not a copy

The tempting move is to upload your whole folder into Context so Claude "knows" it. Don't. Context holds a few hundred pages at most, as of September 2026; past that, Claude stops reading and starts retrieving fragments, and a real collection of notes is far bigger.

So Context holds a *description* of your files: what's in them, how they're named, what you're currently chewing on. Plus any genuinely new writing you asked Claude for. Never copies of file bodies: the same text in two places drifts apart, and the drift is silent, so Claude ends up confidently working from the stale one.

The test for what goes where: **would I need this when I'm away from my computer?** If yes, Context. Otherwise the folder.

### Capture and filing are different jobs

Capture from anywhere, phone, web, a thought on a walk, into an inbox document in Context. No decision about where it goes at the moment you catch it.

Drain that inbox later, at your desk, where the folder is connected and filing can be deliberate. The split falls out of the architecture rather than being imposed on it: the inbox is in the cloud because capture has to work everywhere, the files are on disk because filing shouldn't be rushed.

### If you can't read it yourself, it doesn't belong in your files

It's tempting to let Claude maintain elaborate metadata schemas and generated index files, because Claude is good at it and the retrieval feels clever. That structure rots the moment you stop using the agent, and leaves you a pile only software can love.

Plain text files, in markdown, the simple format most notes apps use. Folders you can open in any editor. Filenames you can scan. If you already keep notes in a folder, such as one a notes app like Obsidian or Logseq uses, it works as-is and you should not reorganize it to match anything here: move it into your binders folder, or connect it where it is, remembering that a folder in Documents or Desktop may be in iCloud. Context is the Claude-specific layer and it should be the expendable one: if you deleted every project tomorrow, your files should be entirely intact and still make sense.

If you've seen kits that keep a memory file in the folder that Claude writes to as it learns, that's the same idea placed differently. This kit keeps the description where your phone can read it and keeps Claude's own bookkeeping out of your files on purpose: a file Claude maintains for Claude's benefit is exactly the pile only software can love.

The same test decides whether something earns a file at all, in any of the binders: would it help to have this written down the next time you talk to someone about it or make a decision? A capture, a source you will want again, a condition, a course, a priority: yes. A one-off question, a bad day, something already covered by a file you have: no, and the conversation is enough. Not everything needs tracking, and a folder of files nobody reopens is the second job this kit exists to avoid.

### Binders are separate on purpose

Not one assistant that knows everything about you. That's worth saying plainly, because "one companion that remembers me" is the natural thing to expect and it isn't what this builds. Claude's memory is scoped to each project, and so to each binder, and doesn't cross between them, so a single all-knowing assistant isn't really on offer. The separation turns that constraint into something useful: your medical records don't surface while you're planning a work week, and a project you never share can't be shared by accident.

There is a second reason, beyond what memory allows. A research binder that also runs your week fills up with tasks, and the notes drown in them: every conversation starts with what is due rather than what you are thinking about. Keeping the research binder quiet is what makes it worth opening.

The separation has a sharp edge. Claude working in one project cannot read or write another project's Context documents, so a file filed in the wrong binder doesn't get moved later. It sits there with the wrong context attached, and nothing reconciles it but you. That's why each project's instructions block has a section telling Claude what belongs elsewhere, and to name the right binder and stop rather than helpfully filing things wherever you happen to be standing.

Most people should build one binder, live with it for a week, and add the others only if they want them. All five at once is a lot of setup for a system you haven't tried yet.

### How Claude asks

Every skill in the kit asks its questions the same way, through the question control, the prompt a task shows with options to tap rather than a question to type an answer to. Each question comes one at a time in the same box, with **Something else** for an answer in your own words and **Skip** to leave it. No skill offers you an option or a draft built from what is known about you outside the project, such as what is public about your name; it works from what you have said and what your folder shows. This is the rule every skill carries, and you can hold them to it. The one exception is a question that tests you, in the learning binder: there no option is marked as recommended, because the mark would be the answer.

<details>
<summary>The exact rule every skill carries</summary>

```
Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never build an option or a draft from outside knowledge of the reader, such as what is public about the account's name: draw only on what they have said and what their folder shows. Never ask what the reader has already said. Silence is never a yes: a yes is a tap on the control or a word.
```

</details>

### The plugins are the upgrade, not the floor

The instruction blocks are the floor and the plugins are the upgrade: everything a skill does, you can ask for in a sentence, more slowly. Skills trigger from their description rather than needing a command you have to remember. They run in Cowork tasks, not in plain chat, and the phone app does not carry them; the instruction blocks work from the phone regardless, which is why they are the floor. The README lists every skill in a line, and [the skills index](skills.md) says for each when to reach for it and what it hands back. When you write your own, three good ones beat fifteen half-finished.

---

## When something surprises you

Most surprises come from the three places above behaving as described. Where a row needs more than a line, it points at the section that explains it.

| What you see | Why | What to do |
|---|---|---|
| On the phone, the **+** menu offers a **Research** switch. | That is Claude's web research feature, which searches the web at length before answering; it has nothing to do with the research binder. | Leave it off for binder work. |
| Claude says it is running in the cloud and cannot see your folder, or offers you Terminal commands. | The box at the top was on **Chat**, not **Cowork**, or the binder's folder was not ticked under **Add folder**: a chat reads the project's Context documents but not the folder, and the plugins' skills do not run in it. | Start a new conversation in the project, switch the box to **Cowork**, and ask again. |
| Something Claude made during a task is gone after you closed it. | The session is a workbench that is cleared when the task ends. | Before closing, have it saved to the folder or a Context document. The account instructions tell Claude to say when something will not survive. |
| At your desk, Claude does not remember last time. | A session that reads your folder does not use memory. | Keep the description true; it is what Claude works from there. The research binder's description check finds what no longer matches. |
| From your phone, Claude cannot open your notes. | A conversation started on the phone runs in the cloud: it reads the Context documents, not the folder. | Start the task on the Mac and continue it from the phone; see [Using your binders from your iPhone or iPad](iphone-and-ipad.md). Or capture to the inbox from the phone and file at the desk. |
| A file shows in the folder, with its size, and Claude cannot open it. | iCloud moved it off the Mac to save space. | Right-click the binder's folder in Finder and choose Keep Downloaded, or turn Optimize Mac Storage off; see [What the connected folder does and does not protect](#what-the-connected-folder-does-and-does-not-protect). |
| A skill that worked in one task does nothing in the next. | A plugin dragged into a task's composer is attached to that task only. | Install it under Customize, Plugins, and turn it on. |
| Something is filed in the wrong binder. | Binders cannot see each other, so nothing moves it back. | Move it yourself. Each binder's instructions tell Claude to name the right binder and stop. |
| Claude follows an instruction you never gave it. | A file at the root of a connected folder can carry instructions Claude reads at the start of a task. | Connect only folders whose contents you wrote or trust. |
| A long task gets vaguer as it goes. | A long session gets worse as it grows. | Start a fresh task for each piece of work rather than carrying a day's worth in one window. |
| Your plan's allowance runs out faster than you expected. | Cowork tasks draw on it much faster than chat does. | Save Cowork for work on files, and keep conversation in chat. |
| Claude asks before every rename, and you have stopped reading the asks. | Every binder's instructions start by asking for a yes before changing the folder. | Widen the leash on purpose; see [Maintenance](#maintenance). |

---

## Using your binders from your iPhone or iPad

On your phone, the project is there with its description, its instructions and its Context documents. A conversation you start there runs in the cloud: it answers from those documents, and it cannot reach the folder or use the plugins' skills. That is what the inbox and the description are for.

Two more things are possible and take more setting up: working in the folder from the phone, by continuing a task you started on the Mac, and keeping a binder in iCloud Drive so the Files app can open it. [Using your binders from your iPhone or iPad](iphone-and-ipad.md) has both.

---

## What the connected folder does and does not protect

Everything Claude can reach in a connected folder it may read, and everything it reads goes to Claude on Anthropic's servers, whether the session is a cloud one or a local one. Connect the folder the binder is about and only that folder: not Documents, not your home folder, not the parent it sits in. Your binders start out together in one folder; each project gets its own binder's folder inside it, never the shared one. A task started on the Mac and continued from your phone reads and edits the folder too, and what it reads goes to Anthropic the same as at the desk; [Using your binders from your iPhone or iPad](#using-your-binders-from-your-iphone-or-ipad) says how it works.

Two of the binders, money and health, carry data you'd mind leaking, and it's worth being exact. **The sensitive material stays in the folder on your computer, and Context documents hold only what you'd be relaxed about syncing.** That keeps your statements and records out of Context, out of every other binder, and off your phone. It does not keep them off Anthropic's servers: when Claude reads a statement to answer you, that statement goes to Claude on Anthropic's servers. Anthropic's own safety guidance says to avoid giving Claude local access to financial documents at all. Plenty of people are fine with a session reading a bank statement or a lab result and would never let it near a password; others draw the line further back. Where you draw it is yours to decide, and those two binders assume you've decided to let Claude read the records. A folder in iCloud Drive adds Apple to the list of places the records live; that can be worth it for medical records you want on your phone at an appointment, and it is a decision to make on purpose. One floor for everyone: credentials, logins, and card numbers never go in a connected folder or a pasted message. And keep both of those projects in the mode that asks before acting.

A file in a connected folder can carry instructions Claude will follow without being asked: Cowork reads certain files at the root of a connected folder at the start of a task, the way developer tools do. That is the reason to connect only folders whose contents you wrote or trust, and it is why this kit keeps its rules in Context documents rather than in a file on disk: your phone can always read a Context document, and reaches the folder only while Claude is open on an awake Mac, and a file Claude can edit and then obeys unprompted is the wrong place for rules. Cowork also has folder instructions, set on the desktop when you connect the folder; the kit does not use them. Your instructions go in the two places described under Setting up a binder without the plugins.

Back the folder up before the first session that's allowed to write, with whatever you already use: Time Machine, your sync service's version history, git if that's your habit. Claude should never be the only copy of anything, and the kit's own rule that Claude shows you what it would change and waits for a yes is an instruction, not a backup; an instruction can be misread.

**If the folder is in iCloud Drive,** either in iCloud Drive itself, where the Files app on your phone reaches it too, or in Desktop or Documents with Desktop & Documents Folders turned on, know what iCloud can do to it. With Optimize Mac Storage on, iCloud moves files it thinks you are not using off the Mac when space runs short; such a file still shows in the folder, with its size, and Claude cannot open it. So right-click the binder's folder in Finder and choose Keep Downloaded, which keeps that folder on the Mac; or turn Optimize Mac Storage off, in System Settings under your name, then iCloud, then Drive: that keeps the whole of iCloud Drive downloaded on the Mac, the same as choosing Keep Downloaded on every folder. It is the best iCloud allows, not a guarantee, because iCloud can still fail to keep files in sync; turning iCloud Drive off altogether would take the folder away from your other Macs and your phone. So have Time Machine on, whatever else you use. A task reorganizing a synced folder has been reported copying files iCloud had moved off the Mac as empty ones and then deleting the originals, and iCloud's Recently Deleted did not bring them back; Time Machine did.

---

## The two approval modes

Cowork can pause for your approval before it acts on the world, sending, sharing, changing files outside the session, or it can act without asking. Whichever you pick, it always asks before permanently deleting a file, and the kit's own instructions make Claude show you what it would change in your folder and wait for a yes. The default is to ask. Leave it there for a project until you've watched it work for a while; switch a project to acting freely only when you've stopped reading the approvals because they're always right. For a project holding anything you'd mind leaking, keep it asking. Where that line sits is yours to draw; the kit only insists that you draw it on purpose. This is not the prompt you see when you attach a folder, which asks whether Claude may change files in it at all; the README's First run says what to choose there. The approval mode decides whether Claude pauses before each action. The switch is in the desktop app's Cowork settings; the kit has not yet pinned whether it is set per project or once for all tasks, so until you find it, the default, which asks, is what you have.

---

## Setting up a binder without the plugins

The README's First run is the setup with a plugin: one install and two pastes the first time, and one install and one paste for each binder after. A task can create Context documents and read your folder, but it cannot write Settings, create a project, connect a folder, or install a plugin, so those steps are yours either way. Everything else a setup skill does can be done by hand from the printed blocks, in this order:

1. **Settings, Account, "Instructions for Claude".** Paste the account instructions printed below, with your chosen voice substituted in. The app's own label on this field says it reaches chats and Cowork alike; it is not the Cowork entry in the Settings sidebar.
2. **Create the project with its folder,** as the README's First run describes: Projects, New project, a name, a sentence under What are you trying to achieve?, then Use a folder.
3. **Create the Context documents** the binder's document names, from the texts printed there. By hand: in the project's Context panel click **+**, choose **Add text content**, give the title exactly as printed, paste the text, and fill in every [BRACKET] before you add it. Or ask Claude in a Cowork task to create them, which keeps each name exactly as printed and fills the brackets from your answers.
4. **Paste the project instructions** from the binder's document into the Instructions panel at the side of the project page, not into the description.

Each binder's document, under `binders/`, carries its use case, its skills and when to reach for each, its setup phrase, a check that it works, and the texts its setup writes: [research](binders/research.md), [learning](binders/learning.md), [your week](binders/week.md), [money](binders/money.md) and [health](binders/health.md). For a binder the kit does not describe, the core plugin's `cowork-new-binder` skill designs one with you and hands back its text.

---

## The account instructions

Paste into Settings, Account, "Instructions for Claude", with one of the voices below substituted where marked. These apply to every conversation, in every project, in chat as well as in tasks. Every binder's setup hands this block back when the field does not carry it yet, and the core plugin's setup hands it back on its own.

```
I am not a programmer. Don't suggest code, scripts, or terminal commands unless I explicitly ask.

[PASTE YOUR CHOSEN VOICE HERE]

Answer in the chat by default. Make a file, doc, or page only when I ask for one, or when the thing itself is the deliverable.

If a request could reasonably mean two different things, ask me one question before starting rather than guessing.

Never send a message, reply to an email, create or change a calendar event, or delete anything without showing me exactly what you'd do and waiting for me to say go. Drafts are always fine.

Anything you build that isn't saved to a Context document or to a folder on my computer disappears when the session ends. Save it, or tell me it's disposable.

Where you're uncertain, say so in the sentence where it matters. Don't hedge everything to be safe, and don't state a guess as fact.

When you tell me you've changed something I'll look at, read it back and confirm the change landed before reporting it done. If I say it still looks wrong and the source says otherwise, tell me that instead of editing again.

When you finish something, tell me what changed and where it is — the folder and file name, or which Context document. One or two sentences.
```

The Account field reaches every conversation you have with Claude anywhere, casual chat included, and a task reads it as chat does; Cowork also has global instructions of its own under Settings, Cowork, reaching only tasks, and what that entry adds is something the kit is still confirming, so the account instructions go in the Account field either way.

**A trap worth naming.** Whatever goes in the Account field hits everything, including casual chat and every other project. "No bullet lists" is right for research notes and actively wrong for the week binder, whose job is handing back ordered lists. Only universal preferences go global. Anything right in one binder and wrong in another stays local, even at the cost of a little duplication; duplication you chose beats a rule that silently fights you in half your work.

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

All three tell Claude not to restate your question. Anthropic's own advice for delegating big deliverables is the opposite: have Claude repeat the ask back and pile up clarifying questions before starting. That advice is for handing off a report; this kit is for keeping files, where one question when something is genuinely ambiguous is the right amount. If you find yourself delegating bigger work from these binders, the voice block is the place to change it.

---

## Maintenance

Plan a second sitting a couple of weeks after the first, to trim what didn't work.

**Prune.** People add instructions and never subtract. The failure is invisible: past a certain length Claude starts quietly weighting the wrong ones. Anything that never changed its behavior should go. The same goes for memory: everything Claude has remembered about you is listed under Topics in the Memory settings, where you can read, edit, or delete each entry, and pause or reset the whole thing. Read it at the two-week sitting; a wrong memory is a wrong instruction you never wrote.

**Widen the leash on purpose.** Every binder's project instructions make Claude show you what it would change in your folder and wait for a yes. That's right for the first weeks and wrong forever: a Claude that must ask before every rename is one you'll stop using for filing. At the two-week sitting, decide what it has earned, filing inbox items into the folder without a yes is the usual first step, renames and deletions the usual last, and change that sentence in the Instructions panel to say exactly that. Relax it deliberately, one permission at a time, rather than leaving it forever or dropping it on day one.

**Scheduled tasks are where this starts paying off,** with one shape to keep in mind. A scheduled task runs in the cloud, on its own, whether or not your computer is on, and for the same reason it cannot be tied to a folder on your computer at all. So a scheduled task works from Context and connected services: a weekly pass that reads the inbox document and the description, pulls the reading list out of the captures, and lists what's changed since last week. Anything that needs the folder itself, surfacing notes untouched in six months, finding where last week's thinking contradicts something from March, is a task you start at your desk, or a saved prompt you run there. Don't schedule anything that touches sensitive records or sends messages on your behalf; nobody is watching a scheduled run.

---

*The framing of this kit, an on-ramp that names the outcome, a kickoff message that does the setup it can, a choice of voice, and the caution about treating outside material as data rather than instruction, owes a debt to Peter Kaminski's PKAI Starter Kit.*
