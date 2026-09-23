# medical

Skills for the Claude Cowork Kit's medical project: set it up, prepare a visit and its pack, record a visit into the folder, keep a weekly functional log, and turn a handed article into questions for the clinician.

Each skill expects the medical project the Claude Cowork Kit describes: records in a connected folder that stays on the computer, arranged as the explainer's section The medical project describes, and project docs holding only a questions list and a bare timeline. Keep the project in the mode that asks (the explainer, under The two approval modes).

## Skills

- `medical-check-in`: A weekly check-in in the reader's own words: what they did, what hurt, what helped, how they feel; a dated entry in the functional log. Use for "check in on how I'm doing", "health check-in".
- `medical-record-visit`: After an appointment: a bare timeline line, the visit note from the recording, checklist and portal papers into the folder, the standing files updated, questions struck. Use for "record my visit".
- `medical-setup`: Sets up the medical project: the privacy floor, three questions, then questions.md and timeline.md as project docs and the instructions to paste. Use for "set up my medical project", "medical setup".
- `medical-treatment-questions`: From a handed article or a clinician's suggestion, grades the evidence it cites and writes the questions to ask about the treatment, never from recall. Use for "questions about this treatment".
- `medical-visit-prep`: Before an appointment, drafts the questions from what changed in the record, and on request a visit pack: a handout, a script and a companion checklist. Use for "prep my doctor's visit", "visit pack".

## Install

In the Claude desktop app, under Customize, Plugins: install it from the marketplace `ChristopherA/claude-cowork-kit`, or upload `medical.plugin` from a release, then turn it on. The repository's README, Install, has both paths in full and what not to do.
