# Changelog

Every release is listed here, newest first, with what changed since the one before. The version is the kit's, in `VERSION`; every plugin in a release carries it.

## Unreleased

The iCloud Drive guidance is corrected: Optimize Mac Storage goes off, not on, since on is what lets iCloud move files off the Mac, and off is the best iCloud allows rather than a guarantee, so Time Machine stays on.

The kit agrees with itself: no plugin comes first in any document, including the core plugin's README; the four binder setups that hand back the account instructions no longer say they do not; research setup counts its questions one way; the day-one checks are listed in one order. What Claude reads is said to go to Claude on Anthropic's servers, since a local session runs its tools on your computer and not Claude itself, and the explainer defines a session.

The README names the plan and the usage cost, asks for the privacy read before the step that connects a folder, and keeps the template, single `.skill` files and the capabilities notes under For contributors.

Every binder setup stops in a project that already holds another binder, and a setup that stopped partway resumes, creating only the missing Context documents, where the learning and money setups used to call such a binder set up while their other skills refused to run in it.

A reply is drafted in any binder, since a draft writes nothing. The inbox drain offers to delete a desk capture's file once it is filed, the first weekly review says there is nothing earlier to compare, questions-for offers the folder rather than a Context document where the questions carry figures or results, and the learning binder's first check no longer depends on the optional Learning style.

The inbox drain's candidate script matches whole words, ranks the rarer shared words higher, and no longer searches the inbox, the archive or `CLAUDE.md`, so a capture stops matching itself.

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
