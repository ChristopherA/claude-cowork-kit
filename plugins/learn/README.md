# learn

Skills for the Claude Cowork Kit's learning project: set a course, run a lesson, and quiz yourself on what you have learned or read.

Each skill expects the learning project the Claude Cowork Kit describes: a folder of materials connected in the desktop app and the project docs mission.md, curriculum.md and progress.md, which the setup creates. Turn on the Learning style for the project, in the style menu.

## Skills

- `learn-lesson`: Runs one lesson of about thirty minutes on one concept, intuition first, from mission.md and progress.md, and records what clicked. Use for "next lesson", "teach me the next thing", "study".
- `learn-quiz`: Tests recall one question at a time from the lesson, the progress record or a handed note, grading each answer and raising the difficulty. Use for "quiz me", "test me on this chapter".
- `learn-setup`: Sets up the learning project: an interview, then mission.md, curriculum.md and progress.md as project docs and the instructions to paste. Use for "set up my learning project", "set my course".

## Install

In the Claude desktop app, either add this repository as a marketplace (Customize, Plugins, Add marketplace, `ChristopherA/claude-cowork-kit`) and install the plugin from it, or download the `.plugin` file from a release and upload it (Customize, Plugins, the upload option), then turn it on. A plugin dragged into a task's composer is attached to that task only. To add one skill instead of the set: Customize, Skills, upload the matching `.skill` file.
