# cowork-kit

The Claude Cowork Kit's core: a setup interview that hands back the account instructions and says which project plugins to install next, plus twelve routines for any project: deciding, interviewing, explaining again, questions for others, a meeting pack, a transcript, confidence, premortem, postmortem, where was I, wrap-up, and a new project.

Install this plugin first, then start a task and say `set up the kit`. The setup skill asks a few questions, hands back the account-wide instructions to paste, and says which project plugin to install next. The other twelve skills work in any project.

## Skills

- `cowork-again`: Says the last answer again in plain words, with the context the reader was missing, and nothing new. Use for "wait, what", "say that again", "I did not follow", "simpler".
- `cowork-clarify`: Settles a decision one question at a time, finding what already decides it and recommending first, ending with a summary and no action. Use for "help me decide", "what are my options".
- `cowork-confidence`: Says plainly what Claude is confident about, what it is not, and what would close the gap, then asks whether to proceed. Use for "how sure are you", "confidence check", "what don't we know".
- `cowork-interview`: Draws out what the reader knows before anything is designed: rounds of questions with recommendations, then a write-back of what was understood. Use for "interview me", "stress-test my plan".
- `cowork-meeting-pack`: Before a meeting with a professional: a one-page brief for them, a script for the reader, and a capture sheet for a companion, the asks first. Use for "prep this meeting", "meeting pack".
- `cowork-new-project`: Designs a project the kit does not describe: its purpose, boundaries and docs, then the instructions text and a plugin from the kit's template. Use for "new project", "a project for something else".
- `cowork-postmortem`: Works through what went wrong in four questions and ends with one change to the instructions or description, with approval. Use for "what went wrong", "postmortem", "why did that happen".
- `cowork-premortem`: Before the reader sends, decides or commits: what goes wrong, how they would know, what they would regret, then one change or a go. Use for "premortem", "before I send this", "what could go wrong".
- `cowork-questions-for`: Writes the questions for someone who holds what the reader lacks, an accountant, a contractor, a teacher, ordered by what matters, one idea each. Use for "questions for", "what should I ask".
- `cowork-setup`: Sets up the Claude Cowork Kit: a short interview, the account instructions to paste, and which project plugin to install next. Use for "set up the kit", "get started", "install the cowork kit".
- `cowork-transcript`: Cleans a raw transcript at a stated level: speakers named, filler trimmed, terms fixed, nothing paraphrased, saved beside the raw one for the project's next step. Use for "clean up this transcript".
- `cowork-where-was-i`: Reads current work, the inbox and the newest notes, and recommends the one next step rather than a menu. Use for "where was I", "what should I do next", "I've lost the thread".
- `cowork-wrap-up`: Writes where this session leaves off, done, open, the first next step and what to watch, into a project doc the next session or the phone reads. Use for "wrap up", "leave a note for next time".

## Install

In the Claude desktop app, under Customize, Plugins: install it from the marketplace `ChristopherA/claude-cowork-kit`, or upload `cowork-kit.plugin` from a release, then turn it on. The repository's README, Install, has both paths in full and what not to do.
