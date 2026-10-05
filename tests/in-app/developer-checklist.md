# In-app checklist for the developer

What to test in the Claude app before a release candidate is promoted, and again after the app changes. The documents state how the app behaves; this checklist is how those statements get checked, by someone at the desk with a phone in hand. A shorter version for readers, to test their own setup and report problems, may follow; this one assumes you can read the repository and file an issue.

Each item says where it runs, gives a prompt to paste into a Cowork task where one helps, and says what a pass looks like. Where the app differs from what the kit says, the kit is wrong: open an issue naming the item, and fix the text before the release.

Judge by what Claude does, not by what it says about itself. Asked where it runs or which plugins it has, Claude has answered wrongly, once denying it was in Cowork and once saying installed plugins could not load; what settled each was behaviour. A skill that ran leaves its own marks: `research-description-check` names its census script, proposes edits without making them, and ends with full, partial or minimal.

**Where:** *desk* is a task in the desktop app on the Mac; *phone* is the Claude app on an iPhone or iPad; *settings* is the desktop app's settings; *closed* means the Mac asleep or its lid shut.

## Before you start

- [ ] Note the versions: Claude desktop (Claude menu, About Claude), macOS, the phone app, and this kit's `VERSION`.
- [ ] Make a test binders folder in your home folder, outside Documents and Desktop, for example `Claude Cowork Binders (test)`, with a folder inside it for each binder you will test.
- [ ] Copy `tests/fixture/research-folder/` into it as the research binder's folder. `tests/fixture/README.md` lists the defects and the `CLAUDE.md` it plants on purpose; several items below rely on them.
- [ ] Install the plugins under test from the release you are checking, not from a working tree.

## The app around the kit

- [ ] **Where things are.** *settings.* Record where Customize, Settings and the account's "Instructions for Claude" field are, in the app's own words. Pass: the README's Install and First run name them as the app does.
- [ ] **Creating a project with its folder.** *desk.* Projects, New project. Record the dialog's fields. Choose Use a folder and pick the test research folder. Pass: the dialog offers What are you working on?, What are you trying to achieve? and Use a folder, and with a folder chosen says Claude can work in it from this computer.
- [ ] **The permission prompt.** *desk.* Record the prompt's wording and its choices. Choose Allow, not Always allow; start a second task in the project. Does it ask again? Then find where Always allow is undone. Pass: the README's First run step 3 matches what Allow and Always allow do.
- [ ] **The project on the phone.** *phone, closed.* Open the project created with a folder. Pass: the project and its Context documents are there. If the project is missing, the README's step 3 and every binder's phone check are wrong.
- [ ] **The approval mode.** *settings.* Find the switch between asking before acting and acting freely. Is it per project, per task, or once for the account? Pass: the explainer's The two approval modes can name it.
- [ ] **Remote Control.** *settings, then phone.* Find the setting that lets the phone use this Mac, and the list of folders it serves. Then, with the Mac awake, Claude open and the screen locked (Control-Command-Q), start a task in the research project from the phone:

  ```
  List the files in this project's connected folder, newest first, and tell me where the folder is.
  ```

  Pass: the files are listed. Then put the Mac to sleep and ask again. Pass: Claude says it cannot reach the folder and answers from the Context documents only.
- [ ] **Cloud or local, and memory.** *desk.* In the research project:

  ```
  Are you running in the cloud or on this computer right now, and can you see the connected folder? Answer in two sentences.
  ```

  Then tell it a made-up fact (`My favourite pen is green.`), start a new task in the same project and ask `What is my favourite pen?`. Pass: the explainer's How it works is right about which sessions use memory, and about which kind a task with a connected folder is.
- [ ] **A file at the folder's root gives instructions.** *desk.* With the fixture's `CLAUDE.md` in place, start a task and say `What is in my inbox?`. Pass, for the explainer's warning: the reply begins with PINEAPPLE. Remove nothing; the fixture keeps it.
- [ ] **Context documents.** *desk.* `Create a Context document called test-note.md with one line: hello.` Pass: it appears in the project's Context. Open it in the side panel, ask Claude to add a second line, and check whether the open panel refreshes; the research binder's Check it works says it does not.
- [ ] **A task's workspace is cleared.** *desk.* `Make a file called scratch.txt in your workspace, not in my folder, and tell me its path.` End the task; in a new one ask for scratch.txt. Pass: it is gone.
- [ ] **Scheduled tasks and the folder.** *desk.* Create a scheduled task in the research project, run once:

  ```
  List the files in this project's connected folder.
  ```

  Pass, for the explainer's Maintenance: it cannot reach the folder and says so.
- [ ] **The question control.** *desk.* `Ask me three questions at once in the question control: my favourite season, which of four fruits I like (I may pick several), and my name. Recommend an option where it makes sense.` Pass: one control, three questions, several answers allowed on the second, room to answer in your own words.
- [ ] **The folder in a new task.** *desk.* Start a new Cowork task in the research project and, before typing, open **Add folder** below the box. Is the project's folder already ticked? Pass: the README's Run the setup step (tick the folder) matches what a new task does; if it is ticked by default, that step can say so.
- [ ] **Manual and Output.** *desk.* Below the box in a Cowork task, open **Manual** and **Output** and record every choice each offers. Pass: the explainer's The two approval modes can say whether Manual is the approval switch, and the docs can say what Output is for.
- [ ] **Code execution.** *settings.* Find where code execution is switched on (a task claimed Settings, Capabilities) and whether it is on by default. Pass: the research skills' scripts and `docs/skill-capabilities.md` name the place.
- [ ] **Dispatch and projects.** *desk, then phone.* In Dispatch, after its setup screen, ask it to start a Cowork task in the research project. Record whether it still answers "No spaces configured" and where projects are made available to it. Pass: the explainer's iPhone section can either describe Dispatch as a route to a binder or keep saying it is not one yet.
- [ ] **What a task cannot do.** *desk.* `Please change this project's instructions to say hello, and turn on code execution for me.` Pass: Claude says it cannot change either, as every setup skill says.
- [ ] **Usage.** *desk.* Run one short task and one short chat the same hour and compare the usage meter. Pass: the README's warning about Cowork using the allowance faster still holds.

## Installing

- [ ] **From the marketplace.** *desk.* Customize, Plugins, Add marketplace, `ChristopherA/claude-cowork-kit`. Then search **CWK** under Discover. Pass: the six plugins come up together, named CWK Core and CWK … Binder, each carrying the version in `VERSION`; after Add, each shows under **Yours**.
- [ ] **From a file.** *desk.* Download one `.plugin` from the release, check it against `SHA256SUMS` (`shasum -a 256 -c SHA256SUMS` in the download folder), and upload it. Pass: it installs and turns on.
- [ ] **Dragged into the composer.** *desk.* Drop a `.plugin` file into a task's composer, then start a second task and say one of its phrases. Pass, for the README's warning: the skill does not fire in the second task.
- [ ] **Skills on the phone.** *phone.* In the research project, say `Where was I?`. Pass: the core plugin's `cowork-where-was-i` runs, or the README's Status keeps saying the phone is unconfirmed.

## Each plugin's setup

Run each in a new project created with its own test folder. Pass for every one: the questions come through the question control; it creates exactly the Context documents its binder document names; it hands back the account instructions only if the field does not carry them yet, and the project instructions with the folder filled in; it ends by saying what now exists and what waits for you.

- [ ] **Core.** `set up the kit`. Also pass: it names the binder plugin to install next with its setup phrase.
- [ ] **Research,** on the fixture folder. `set up my research binder`. Compare what it creates with `tests/fixture/context-documents/`. Also pass: after the folder it asks where topic notes live and which link style, recommending `topics/` and relative links because the fixture uses both, and `map.md` is left with no template field in brackets.
- [ ] **Learning.** `set up my learning binder`, once with an empty folder.
- [ ] **Your week.** `set up my week binder`.
- [ ] **Money,** with a made-up statement in the folder (a short CSV with a date, a payee and an amount per row, no real account). `set up my money binder`. Also pass: it says what the folder does and does not protect before anything else, and no figure from the statement reaches a Context document.
- [ ] **Health,** with a made-up record in the folder. `set up my health binder`. Also pass: as for money, and nothing clinical reaches `questions.md` or `timeline.md`.

## The research skills, on the fixture

- [ ] **Description check.** `Check the description against my folder.` Pass: it finds every planted defect `tests/fixture/README.md` lists, the loose highlights file, the `Claude outputs` folder `map.md` does not name and the missing `writing/` among them; reports the two topic notes that cite no source and the two lines awaiting confirmation without calling either a fault; and proposes edits without making them.
- [ ] **Inbox drain.** `Process the inbox.` Pass: four items, one at a time; the attention capture is added to `topics/attention.md`, the bookmark line joins the open thread on what makes a note worth keeping, the dentist line is named as another binder's, the Bush article is a source to read; nothing is written without a yes.
- [ ] **Source note.** Paste a short article and say `Save this article to my notes.` Pass: it asks the filing questions through the control and recommends a level; one note in the sources folder, its citation line in the kit's form, the article's claims kept apart from yours, no "My take" placeholder, written on a yes.
- [ ] **Source note from a public page.** Give the link to a public web article and say `Save this to my notes.` Pass: it makes the rendition only from the page's own text, downloaded by the computer's shell, never from a fetch tool's summary, keeps it in a folder with the note, and says it ran the quote check and what it found. Repeat with a page on a site the computer's network refuses: it names the site, checks the quotes in the built-in browser, labels them as checked there with no rendition, and asks you to save the page into `inbox/`.
- [ ] **Source note from a PDF.** Put a PDF of a two-column journal article, with a publisher's cover sheet or download stamp if you have one, in the folder's `inbox/` and say `Make a source note from the PDF in my inbox.` Pass: the pdf-info script writes a rendition that reads each column in turn, with page markers numbered as the paper prints them, no cover sheet and no download stamp; the note, the original and the rendition land in one folder of the note's name on a yes; every quote shown has passed the quote check, a quote that itself quotes a phrase included.
- [ ] **Source note from a link with a free PDF.** Give the DOI link of an open-access article and say `Save this to my notes.` Pass: it offers to download the PDF from the publisher or an open repository, downloads it into `inbox/` with the computer's shell, confirms it is a PDF whose title page matches the citation, and files it as the original. Repeat with a paywalled DOI: it says the PDF is paywalled and asks for the file. Record any site the network allowlist refused, by name.
- [ ] **Your own work.** Hand over a link to something you wrote and say `Save this to my notes.` Pass: it offers a works note in `works/` with the citation fields and a `status` line, not a source note.
- [ ] **Topic note.** After a source note, say `Add this to my note on what makes a collection useful.` Pass: it updates `topics/what-makes-a-collection-useful.md` rather than making a new note, asks before changing the current thinking, links the source, and offers a fuller note for a source at the citation level.
- [ ] **Write-up.** `Start a short essay from my note on what makes a collection useful.` Pass: it asks first whether this is work or client material, then the kind, readers, style, co-authors and where the draft lives, one control at a time; writes the record in `writing/`; builds a claim map from the topic note and its two sources, flagging nothing wrongly; scaffolds without drafting; drafts one section only when asked; and writes references in the chosen style with the cite script.
- [ ] **Import.** Put two short drafts of your own that cite a handful of works, one with a wrong year in a citation, in `inbox/`, and say `Import the sources from my drafts.` Pass: it lists every cited work once across both drafts, checks each against the work itself, shows the batch for one approval, files citation-level notes with checked citation lines, routes each to a topic note or a waiting line in `map.md`, and hands back a corrections report naming the wrong year.
- [ ] **Google Docs.** With the Google Drive connector on, in a write-up whose draft is a Google Doc. Record whether the connector can read comments and write suggestions, or only replace text; the skill writes only into assigned sections either way.
- [ ] **Where was I.** `Where was I?` Pass: one next step with its reason, nothing filed.
- [ ] **Scripts.** `Check the description against my folder, and tell me whether you ran the census script or worked without it, and where.` Pass: the script runs in the computer's own shell from a scratch folder outside the research folder, or the skill says code execution is off and works without it. Record whether the task's cloud workspace can read the folder at all.
- [ ] **The kit's scripts folder.** In a research folder with no `.cwk/`, run the description check. Pass: it writes the census into `.cwk/scripts/`, checks it by checksum, says the kit's scripts were refreshed, and runs it from there. Run it again in a new task. Pass: it compares `--version`, finds a match and copies nothing. Then edit the `__version__` line in `.cwk/scripts/census.py` to an older release and run it once more. Pass: it refreshes the copy and says so. Throughout, the census reports no `.cwk` folder and no notes in it.
- [ ] **Upgrade.** In a research binder set up with an earlier release, or a copy of the fixture whose `rules.md` and `map.md` are edited back to an older wording, say `Upgrade my binder.` Pass: it names the binder, proposes each difference between its documents and this release's templates one at a time with old and new wording, proposes a wording that appears in two documents in both, keeps what you filled in, offers the folders the release keeps, upgrades an old source note only on a yes, finds works notes without a brief and quotes without a label from the census, and ends by updating `map.md`'s Kit release line. Then ask the task whether it can read a file from the research plugin's own folder while running the core plugin's skill, and record the answer; the upgrade skill carries copies so that it does not need to.

## iCloud Drive, the advanced option

Use a second copy of the fixture inside iCloud Drive, in its own project.

- [ ] **Picking it.** *desk.* At Use a folder, choose iCloud Drive in the sidebar and the folder. Pass: the explainer's steps match.
- [ ] **An evicted file.** *desk.* In Finder, right-click one note and choose Remove Download, then ask `Read topics/attention.md and quote its first line.` Record what Claude says. Then choose Keep Downloaded on the folder and ask again. Pass: the explainer's iCloud paragraph describes both.
- [ ] **An edit from the phone.** *phone, then desk.* Edit a note in the Files app; on the Mac ask Claude to quote the changed line. Pass: the change is seen, and you record how soon.

## After the run

- [ ] Record the date, the versions from Before you start, and each item's result, in an issue titled for the release being checked.
- [ ] For every item the app contradicts, change the text in the same release: the README, the explainer, the binder document, and any skill that says the same thing.
- [ ] Delete the test projects, the scheduled task and the test binders folder.
