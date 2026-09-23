# medical

Skills for the Claude Cowork Kit's medical project: set it up, prepare the questions for a visit from what changed in the record, and record a visit afterward.

Each skill expects the medical project the Claude Cowork Kit describes: records in a connected folder that stays on the computer, and project docs holding only a questions list and a bare timeline. Keep the project in the mode that asks.

## Skills

- `medical-record-visit`: After an appointment, adds a bare dated line to timeline.md, files the clinical detail in the folder only, and strikes answered questions. Use for "record my visit", "log the appointment".
- `medical-setup`: Sets up the medical project: the privacy floor, three questions, then questions.md and timeline.md as project docs and the instructions to paste. Use for "set up my medical project", "medical setup".
- `medical-visit-prep`: Before an appointment, drafts a short list of questions from what changed in the record since the last visit, values quoted exactly. Use for "prep my visit", "questions for my appointment".

## Install

In the Claude desktop app, either add this repository as a marketplace (Customize, Plugins, Add marketplace, `ChristopherA/claude-cowork-kit`) and install the plugin from it, or download the `.plugin` file from a release and upload it (Customize, Plugins, the upload option), then turn it on. A plugin dragged into a task's composer is attached to that task only. To add one skill instead of the set: Customize, Skills, upload the matching `.skill` file.
