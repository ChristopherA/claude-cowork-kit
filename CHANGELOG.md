# Changelog

Every release is listed here, newest first, with what changed since the one before. The version is the kit's, in `VERSION`; every plugin in a release carries it.

## Unreleased

- Every project setup hands back the account instructions when the Account field lacks them, so no plugin has to be installed before another; the first run is one install and two pastes.
- Every project skill checks it is running in its own project and stops otherwise, since plugins reach every project.
- The paragraphs several skills share are single-sourced in `docs/shared.md` and the build fails on a copy that differs; the template carries the asking convention.
- The medical plugin's first visit can be prepped before any visit is recorded; the check-in and the treatment questions create their files when missing.
- Trigger phrases carry the project's noun and no two collide on an ordinary sentence; every skill ends with a completeness word; silence is never a yes.
- One version, from `VERSION`, in every manifest; `build.py --check` fails on a generated file left uncommitted.
- The README is the kit's first page; a changelog, contributing notes and a privacy statement exist.
- The explainer is the kit's case with no project in it; each project has its own document under `docs/projects/` with its use case, skills, setup, check and paste blocks; `docs/skills.md` indexes every skill and the build checks it against the skills.
- A folder in iCloud Drive, directly or through Desktop & Documents sync, needs Optimize Mac Storage and Time Machine turned on: Claude cannot read a file iCloud has moved off the Mac, and a reorganizing task has been reported losing such files.

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
