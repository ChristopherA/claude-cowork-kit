# What leaves your computer, and what does not

The kit has two projects that read things you would mind leaking, a bank statement and a medical record, so this is said once, plainly, outside the explainer.

**The folder stays on your computer.** Claude reaches a connected folder only while the desktop app is open on that computer. Nothing in the folder syncs anywhere because of the kit, and nothing the kit sets up copies a note, a statement or a record into the project.

**What Claude reads goes to Anthropic.** When a task reads a file to answer you, that file's contents are sent to Claude, which runs on Anthropic's servers. A local session runs its tools on your computer, but Claude itself still runs on Anthropic's servers, so choosing one does not keep a file's contents on your machine. That is how Claude reads anything, and it is why the kit tells you to connect only the folder you mean and never a parent of it. Anthropic's own safety guidance says to avoid giving Claude local access to financial documents at all; the money and medical binders assume you have decided to let it read the records, and say so.

**Context documents sync.** The Context documents a setup creates in a project (the description of your notes, the capture inbox, a priorities list, a questions list, a timeline of visits with no clinical detail) live in your account and reach your phone. The kit keeps them free of anything you would mind syncing: no account numbers, balances or transaction rows, no results, diagnoses or medications. Each skill that writes one says what it keeps out.

**Memory is per project** and is used by sessions that run in the cloud; the memory settings list what has been remembered and let you edit, pause or reset it.

**Never in a connected folder or a pasted message:** credentials, logins, card numbers. And connect only folders whose contents you wrote or trust, because a file in a connected folder can carry instructions Claude will follow without being asked.

**The kit itself collects nothing.** It is text. Nothing in it phones home, and the scripts in the research plugin read your folder and write nothing.

The details, with what the kit has and has not yet confirmed in the running app, are in the explainer, `docs/claude-cowork-kit.md`, under What the connected folder does and does not protect, and in the money and medical documents under `docs/binders/`.
