# health

Your health binder: prepare for an appointment, record a visit, keep a weekly log, and turn an article into questions for your clinician; records, never diagnosis. Part of the Claude Cowork Kit (CWK).

Each skill expects the health binder the Claude Cowork Kit describes: records in a connected folder that stays on the computer, arranged as the kit's docs/binders/health.md describes, and Context documents holding only a questions list and a bare timeline. Keep the project in the mode that asks (the kit's explainer, under The two approval modes).

Version 0.1.0-rc.8 of the Claude Cowork Kit; every plugin in a release carries the kit's version, and the releases are at https://github.com/ChristopherA/claude-cowork-kit/releases.

## Skills

- `health-check-in`: A weekly check-in in the reader's own words: what they did, what hurt, what helped, how they feel; a dated entry in the functional log. Use for "check in on how I'm doing", "health check-in".
- `health-record-visit`: After an appointment: a bare timeline line, the visit note from the recording, checklist and portal papers into the folder, the standing files updated, questions struck. Use for "record my visit".
- `health-setup`: Sets up the health binder: the privacy floor, three questions, questions.md and timeline.md as Context documents and the instructions to paste. Use for "set up my health binder", "health setup".
- `health-treatment-questions`: From a handed article or a clinician's suggestion, grades the evidence it cites and writes the questions to ask about the treatment, never from recall. Use for "questions about this treatment".
- `health-visit-prep`: Before an appointment, drafts the questions from what changed in the record, and on request a visit pack: a handout, a script and a companion checklist. Use for "prep my doctor's visit", "visit pack".

## Install

In the Claude desktop app, under Customize, Plugins: install it from the marketplace `ChristopherA/claude-cowork-kit`, or upload `health.plugin` from a release, then turn it on. The repository's README, Install, has both paths in full and what not to do; `docs/binders/health.md` there has the setup and the text this plugin's setup hands back.
