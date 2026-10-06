# learn

Your learning binder: learn a subject, a skill or an exam on purpose, with a course plan, short lessons and quizzes, and a record of what has clicked. Part of the Claude Cowork Kit (CWK).

Each skill expects the learning binder the Claude Cowork Kit describes: a folder of materials connected in the desktop app and the Context documents mission.md, curriculum.md and progress.md, which the setup creates. Claude's Learning style is optional here: a task cannot turn it on, and the lesson skill does that work inside a task.

Version 0.1.0-rc.11 of the Claude Cowork Kit; every plugin in a release carries the kit's version, and the releases are at https://github.com/ChristopherA/claude-cowork-kit/releases.

## Skills

- `learn-lesson`: Runs one lesson of about thirty minutes on one concept, intuition first, from mission.md and progress.md, and records what clicked. Use for "next lesson", "teach me the next thing", "let's study".
- `learn-quiz`: Tests recall one question at a time from the lesson, the progress record or a handed note, grading each answer and raising the difficulty. Use for "quiz me", "test me on this chapter".
- `learn-setup`: Sets up the learning binder: an interview, then mission.md, curriculum.md and progress.md as Context documents and the instructions to paste. Use for "set up my learning binder", "I want to learn".

## Install

In the Claude desktop app, under Customize, Plugins: install it from the marketplace `ChristopherA/claude-cowork-kit`, or upload `learn.plugin` from a release, then turn it on. The repository's README, Install, has both paths in full and what not to do; `docs/binders/learning.md` there has the setup and the text this plugin's setup hands back.
