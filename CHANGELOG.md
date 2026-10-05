# Changelog

Every release is listed here, newest first, with what changed since the one before. The version is the kit's, in `VERSION`; every plugin in a release carries it.

## Unreleased

From a reader's second live run, on rc.10, which confirmed every rc.9 script fix on real files and ran the new upgrade on a real binder. Scripts now run in place from the research plugin as the desktop app installed it on your computer, so nothing has to be copied over each session; each script reports its release with `--version`, and when your computer's copy is older than the skill, you are told a newer version is available and to upgrade under Customize, Plugins. A rendition says which release made it.

The citation script prints report numbers ("Working Paper No. 24-038", "RFC 8259") and writes a standard as a BibTeX technical report. A source note records when and against what its citation was checked. The description check finds works notes without a brief and quotes no one can check, the two shapes an upgrade from rc.9 has to find. `map.md` carries a Kit release line, written by setup and updated by the upgrade. A brief for your own work is written from the work and marked as drafted until you confirm it. The upgrade proposes a changed wording in every document that carries it, treats a renamed note as a move with its links fixed first, and warns that the app may ask for delete permission again after the link to your computer drops.

## 0.1.0-rc.10 (2026-10-05)

From a reader's live run of rc.9 on their own research folder. Renditions of two-column journal articles now read each column in turn, so quotes typed from the page match; the old extraction set the columns side by side and failed every quote in a real paper. A rendition also writes ligatures as plain letters, removes publisher download stamps, which carry the reader's IP address, and leaves a publisher's cover sheet out of the text and the page numbers. The quote check keeps a quote whole when it quotes a phrase itself. The cite script sets APA titles in sentence case and knows sixteen more kinds of work, conference papers, dissertations, news articles, encyclopedia entries, standards and others, with a convention for Wikipedia.

Two new skills. `research-import` files every work a pile of your own writing cites, each citation checked against the work itself and filed after one approval for the batch, and hands back a report of the errors it found in your citations. `cowork-upgrade`, in the core plugin, brings a binder made with an earlier release up to this one, one change at a time, keeping what you filled in.

Your own writing gets a `works/` folder, citable like sources. The source-note skill offers to download a freely available PDF from the publisher or an open repository, never a shadow library, and asks for the file when it is paywalled or the network refuses the site. A web page's rendition is made only from its own text, never from a summary, and quotes are checked in the browser when the shell cannot reach the page. Scripts that read the whole folder run in your computer's shell, since a task's cloud workspace cannot read a folder on your computer. A source waiting for a topic note you have not written yet is kept on that topic's line in `map.md`. Citation counts are asked of you, with the index and date. A WHY SAVED inferred from your writing, or a topic note's thinking drafted from it, is marked until you confirm it. Many topic notes drafted at once can be reviewed in one file. The description check reports a file lying loose in `sources/`, folders `map.md` does not name, such as the app's `Claude outputs`, and the lines waiting for you.

## 0.1.0-rc.9 (2026-10-05)

The research binder writes syntheses, not only source notes. Its folder is now inbox, sources, topics, threads, writing and archive: `topics/` holds one living note per topic, what you currently think first and in your words, then the sources that support or challenge it, and takes the place of one-idea notes, so the inbox drain adds a capture to a topic note or a thread rather than starting another note. A new skill, `research-topic-note`, keeps those notes, and `map.md` gains a Topics section, one line per topic note with its current thinking, so a question from the phone can be answered from what you think. The setup asks where topic notes live and which link style you use, and does not finish while `map.md` still holds a template field.

A second new skill, `research-write-up`, builds a piece for other readers from your topic notes, alone or with co-authors: a record of the piece in `writing/`, a claim map that says whose each claim is and how well it is supported, a scaffold by kind (literature review, paper or spec, brief or memo, essay or post), prose only for the section you ask for, and references in the piece's style with a BibTeX or CSL file. In a shared Google Doc it writes only into the sections you assign.

A source note is written at the level of what you read: `citation` (the line alone), `minimal` (a brief, a short abstract, and why you saved it) or `read` (key points and key quotes as well). Filing asks why you are saving the source and which topic note should cite it, and how it differs from a related work you name, in place of a "My take" line that was usually left empty. A source that comes with a PDF or a web page becomes a folder holding the note, the original in `originals/` and a searchable copy in `renditions/`, page-marked with the numbers the citation uses; every quote is checked word for word and against its page before you see a draft. Each part of a note is written to its own rules, a brief of 20 to 30 words, a short abstract of three or four sentences that leads with what the work does, key points in your words, and strong words like "foundational" only with a dated citation count beside them, and a script checks the prose block by block before you see it. A note carries its citation as fields as well as a line, with a DOI or ISBN-13 in the brackets after the kind, and a script writes it in the kit's form, APA, Chicago, IEEE, BibTeX or CSL. A deep source central to your work can take an analysis and an insights file beside its note. A public web page can be read for you; the explainer no longer says a task cannot reach the web. The citation line carries a Retrieved or Available date and fuller author rules, and the evidence words shared with the health binder gain "derived from a model, not tested".

No skill offers an option or a draft built from what is known about you outside the project, such as what is public about your name; it works from what you have said and what your folder shows. The description check reports source folders without their lead note, originals without their copy, notes whose level does not match what they hold, the sources nothing cites, the topic notes that cite nothing, and topic notes missing from `map.md`'s Topics section.

## 0.1.0-rc.8 (2026-10-04)

Every plugin is named with CWK, short for Claude Cowork Kit, so the six can be found together: search CWK in the app's Discover list. They are CWK Core and CWK Research, Learning, Week, Money and Health Binder, and each description now opens with what that binder does. The medical binder is now the health binder: the plugin is `health`, its skills are `health-setup`, `health-visit-prep`, `health-record-visit`, `health-check-in` and `health-treatment-questions`, and its setup phrase is `set up my health binder`. An installed `medical` plugin does not update into `health`; remove it and add CWK Health Binder.

The setup steps match the app as it now is. A project is created with its folder in one dialog: Projects, New project, a name, a sentence under What are you trying to achieve? (every binder document gives one to paste), then Use a folder. The box on the project page starts on Chat and a setup runs only with Cowork switched on. A Context document can be made by hand as well as by a task. Adding the marketplace only lists the plugins; each is installed once it shows under Yours.

Binders start in one folder on the Mac, outside Documents and Desktop; moving one into iCloud Drive, for the Files app on the phone, is an advanced option with Keep Downloaded set on its folder. On the phone, a conversation started there works from the Context documents only; a Cowork task started on the Mac and continued from the phone, found under Recents, reaches the folder while the Mac is awake with Claude open.

The README is the front door for someone new to Claude: every skill in a line, and a first run that works for whichever binder you start with. The explainer is the reference, with a new section for when something surprises you, and the core setup recommends the binder you asked for. `tests/in-app/developer-checklist.md` lists what to test in the app before a release.

## 0.1.0-rc.7 (2026-09-23)

The iCloud Drive guidance is corrected: Optimize Mac Storage goes off, not on, since on is what lets iCloud move files off the Mac, and off is the best iCloud allows rather than a guarantee, so Time Machine stays on.

The kit agrees with itself: no plugin comes first in any document, including the core plugin's README; the four binder setups that hand back the account instructions no longer say they do not; research setup counts its questions one way; the day-one checks are listed in one order. What Claude reads is said to go to Claude on Anthropic's servers, since a local session runs its tools on your computer and not Claude itself, and the explainer defines a session.

The README names the plan and the usage cost, asks for the privacy read before the step that connects a folder, and keeps the template, single `.skill` files and the capabilities notes under For contributors.

Every binder setup stops in a project that already holds another binder, and a setup that stopped partway resumes, creating only the missing Context documents, where the learning and money setups used to call such a binder set up while their other skills refused to run in it.

A reply is drafted in any binder, since a draft writes nothing. The inbox drain offers to delete a desk capture's file once it is filed, the first weekly review says there is nothing earlier to compare, questions-for offers the folder rather than a Context document where the questions carry figures or results, and the learning setup names its first checks in the order its binder document gives them, testing the project instructions rather than the optional Learning style.

The inbox drain's candidate script matches whole words, ranks the rarer shared words higher, and no longer searches the inbox, the archive or `CLAUDE.md`, so a capture stops matching itself.

`VERSION` carries the release candidate's suffix, so an installed plugin says which candidate it is; every manifest names the license, the homepage and the repository, and every `.plugin` and `.skill` file carries `LICENSE`. `build.py --help` prints its usage, and an unknown option fails instead of running a build. `build.py --check` reports every failure in one run rather than stopping at the first, and fails on a literal backreference or escaped newline left in running text by a scripted edit.

## 0.1.0-rc.6 (2026-09-23)

The kit speaks the app's words: each part of life is a *binder*, one project in the app plus its folder and its *Context documents*, and *project* means only the app's container. The notes plugin is now `research` (shown as Research) with `research-*` skills, every setup's phrase is `set up my <name> binder`, and `cowork-new-project` is `cowork-new-binder`; an installed `pkm` is replaced, not upgraded. Every binder setup hands back the account instructions when the Account field lacks them, so no plugin has to come first, and every binder skill checks that it runs in its own project. The explainer is the kit's case with no binder in it; each binder has its own document under `docs/binders/`, and `docs/skills.md` indexes every skill, checked by the build. A folder in iCloud Drive needs Optimize Mac Storage and Time Machine turned on. The medical plugin's first visit can be prepped before any visit is recorded, and visit prep's section on what changed is whole again. Shared paragraphs are single-sourced and checked by the build, trigger phrases no longer collide, silence is never a yes, every manifest carries the one version in `VERSION`, and a changelog, contributing notes and a privacy statement sit beside the README.

## 0.1.0-rc.5 (2026-09-23)

A review of the kit as a reader meets it, and the fixes it called for. The README opens with what the kit is for and three steps to start. The explainer has one setup order, with the backup and the from-folder warning inside it, and a separate path for building the projects without the plugins; passages that asked the reader to test platform behaviour say what the kit is still confirming; the phone claim is hedged to what the Cowork documentation supports. The core setup asks fewer questions and gives the marketplace path first. Every setup keeps a project doc that already exists. The notes skills rank by dates inside files rather than modification times. Trigger phrases that collided are gone.

## 0.1.0-rc.4 (2026-09-23)

The week project gains `week-meeting-notes`, the after-the-meeting half of the core's meeting pack: decisions apart from the discussion, action items with owners, quotes checked against this meeting's transcript only, and the carry-forward for a meeting in a series.

## 0.1.0-rc.3 (2026-09-23)

The medical plugin grows to five skills: a visit pack from visit prep, record a visit from the recording and papers, a weekly check-in into the functional log, and questions about a treatment from a handed source. Two core skills for any project, `cowork-meeting-pack` and `cowork-transcript`. The week project gains `week-review`. The explainer states once the test for whether something earns a file; the source-note skill grades cited evidence in five fixed words.

## 0.1.0-rc.2 (2026-09-23)

One way of asking: every skill carries the same convention for the app's question control, written once in the explainer and checked by the build. The core grows from six skills to eleven: `cowork-clarify` is separated from `cowork-interview`, and `cowork-again`, `cowork-questions-for`, `cowork-premortem` and `cowork-wrap-up` are new.

## 0.1.0-rc.1 (2026-09-23)

First release candidate: the core plugin with the setup interview and five routines, the notes plugin, the learning, week, money and medical plugins, and the explainer.
