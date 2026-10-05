# Text the skills share

Paragraphs that more than one skill carries word for word. Each block below is the single source: `build.py --check` fails when a skill listed for it in the build's `SHARED` table carries a copy that differs, so a fix here reaches every copy and a fix in one copy is caught. The asking convention is the one shared text not here; it lives in the explainer, under "How Claude asks", because the reader is promised it.

## What a task can and cannot do

```
A task can read the project's Context documents, create Context documents in the project it runs in, read a connected folder, and read the reader's Account instructions. It cannot change Settings, set the project's approval mode, create a project, connect a folder, install a plugin, or send anything; those are the reader's, in the app. Say which is which as you go, so the reader never waits for something that will not happen.
```

## Another binder's project

```
Before anything else, check whether this project already holds another binder: `map.md` is the research binder's, `mission.md` the learning binder's, `priorities.md` the week binder's, `categories.md` the money binder's and `timeline.md` the health binder's. If one of them is here and it is not this binder's own, say which binder this project holds, that each binder needs a project and a folder of its own, and stop; this binder's documents created here would mix the two.
```

## Grouping the questions

```
Ask as the Asking section says, grouping the questions whose answers do not depend on each other in one control and putting the dependent ones after. Skip any the reader has already answered in their request.
```

## The two fields

```
The project page has two text fields that look alike, a one-line description under the title and an Instructions panel at the side, and readers put the instructions in the description. So hand back two things, in this order, and say which field each goes in. If the project's description already holds the instructions text, say so and tell the reader to move it.
```

## Hand the text back

```
The instructions go into a field only the reader can fill: a task can create Context documents and cannot set the project's Instructions or description, and the shell a task runs in is a Linux space apart from the reader's computer, so it cannot put text on their clipboard either. Do not try; hand the text back and say where it goes. The text goes in a code block of its own, which carries a copy button in the app.
```

## The account block

```
Before the project instructions, read the reader's Account instructions if you can see them. If they carry the kit's block, say so and name the voice in it; do not ask the voice again. If they do not, or you cannot see them, ask which voice they want, plain, warm or archivist, one phrase each from `references/voices.md`, plain first as the safe default, and hand back `references/global-instructions.md` with that voice substituted where marked, in a code block of its own: it goes in Settings, Account, "Instructions for Claude", reaches every chat on the account, casual chat included, and is pasted once for all the kit's binders. If the field already holds text of the reader's own, say to add the block below it and cut whatever the two say twice. No plugin has to be installed before this one.
```

## Running a script

```
Where a script runs depends on what it reads. The research folder is on the reader's computer, and a task reaches it through its link to that computer; the task's cloud workspace sees a file only once it is copied there. So a script that reads the whole folder, such as the census or the drain's candidate search, runs in the computer's own shell, in place, from the research plugin as the desktop app installed it on that computer. The app lists its installed plugins in a `manifest.json` under `~/Library/Application Support/Claude/local-agent-mode-sessions/`, two folders down (the account, then the organization) in `rpm/`, and the plugin named `research` is the folder beside it named by its `id`. Find it through the manifest, never by searching the computer for the script, since older copies of the plugin can sit elsewhere; run it from there with the computer's python3, from a scratch folder outside the research folder, and never copy it anywhere. Before running, compare the installed script's `--version` with the `__version__` line in this skill's own copy of the script. If they differ, tell the reader a newer version of the plugin is available and to upgrade it in the Claude app under Customize, Plugins, and offer to continue now by reading instead. If no installed copy is found, or it cannot be read, do the work by reading and say why. A script that needs one file, a PDF or a draft note, may instead run in the cloud workspace on a copy of that file. Either way it is never copied into the research folder or any folder of the reader's, and anything it writes reaches the folder only as this skill says, after a yes. When many files go into the folder at once, write them with the computer's shell and check each one landed by its checksum, so a dropped link to the computer can be resumed from where it stopped. Then say in one plain sentence that a script read the folder; the reader is not a programmer and does not need the mechanics, but is never left unaware that something ran. If the task cannot run scripts, do the same work by reading, as this skill says, and say that you did. Never rely on the folder's modification times: syncing and copying reset them.
```

## The evidence words

```
strong (several controlled trials, a systematic review, or a guideline named), moderate (some trials, mixed results, or experts disagreeing), limited (small studies or case reports, or a plausible mechanism), anecdotal (people report it helped, no controlled study named), derived from a model, not tested (the claim follows from a mathematical or computational model and the source cites no test of it), none stated
```
