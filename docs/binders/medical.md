# The medical binder

Keeping your medical records organized: visits, test results, medications, and the questions you want to ask at your next appointment, as a record you can compare across visits. Its plugin is `medical`, shown as **Medical records** in the app. The reasoning every binder shares is in [the kit's explainer](../claude-cowork-kit.md), and its section on what the connected folder does and does not protect is the one to read before this binder; the setup opens by saying the same thing.

The floor is the same as for money. The records stay in the folder on your computer; the Context documents hold a running list of questions for appointments and a bare timeline of visit dates, nothing clinical, because Context documents sync to the cloud and reach your phone. Claude quotes lab values, dosages and dates exactly as the record has them and never reconstructs one from memory; it is not your doctor, does not diagnose, and does not reassure. Keep this project in the mode that asks before acting, and if Claude can use your screen at all, block your patient portals and health apps from it.

The folder is where the record accumulates, and its shape matters more here than anywhere else in the kit, because a record that lives in one paragraph per visit cannot be compared across visits. The instructions below name a default: an overview; one file per condition, with its timeline, findings and treatment history; medications; providers, with what to expect from each; an action plan; a functional log, the weekly entries in your own words that show gradual change a doctor would otherwise never see; and a research file for treatments you are weighing. Visit documents are named by date and the clinician's role, so a year of them sorts itself. Not everything earns a file: the test is whether it would help to have it written down the next time you talk to a clinician or make a decision; a one-off question or a bad day does not.

## The skills

The skills are built on that folder.

- **`medical-setup`**, `set up my medical binder`. The privacy floor first, then three questions, then the two Context documents and the instructions to paste. If the folder is reachable and holds none of the standing files, it offers to create them empty, with a heading each.
- **`medical-visit-prep`**, `prep my doctor's visit`. Before an appointment, the questions drawn from what has actually changed in the record since the last one, not a generic checklist; on a first visit, from what you tell it. On request, `visit pack`: a one-page handout the clinician can scan, a script you follow, and a checklist a companion fills in with the clinician's exact words.
- **`medical-record-visit`**, `record my visit`. After an appointment: a bare timeline line, the visit note from the recording, the checklist and the portal papers into the folder, the standing files updated so the next prep starts from a current record, and the answered questions struck.
- **`medical-check-in`**, `check in on how I'm doing`. A weekly entry in the functional log, in your own words: what you did, what hurt, what helped, how you feel.
- **`medical-treatment-questions`**, `questions about this treatment`. Reads an article or a clinician's suggestion you hand over, says what it claims and on what evidence it cites, and turns the gaps into questions. It grades the evidence in five words and no others, strong, moderate, limited, anecdotal, none stated, and only for what the source itself cites; it does not research, because a task cannot reach the web and this binder is not the place to work out what is wrong between appointments.

## Setup

The setup creates two Context documents: `questions.md`, the running list of questions for appointments, and `timeline.md`, the bare list of visit dates by clinician role. Neither holds anything clinical. The general steps are in the explainer under Setting up a binder, and the install paths in the repository's README; for this binder:

1. **Install the medical plugin**, `medical`, shown as **Medical records**, and turn it on.
2. **Create the project and connect the folder** that holds your records, from the project's page. Do not create the project *from* the folder.
3. **Run the setup.** In a task inside the project, say `set up my medical binder`. Claude says what the folder does and does not protect; asks where the folder is, which clinicians you see by role, and when the next appointment is; creates the two Context documents; offers the standing files if the folder has none; and hands back what only you can paste: the account instructions, if your Settings, Account, "Instructions for Claude" field does not carry them yet (the account instructions in the explainer), and the project instructions below, for the Instructions panel at the side of the project page, not the description.
4. **In the app,** check that the mode that asks before acting is on, and block patient portals and health apps from screen use if screen use is on.

Without the plugin: paste the account instructions as the explainer says, create the project, ask Claude in a task to create `questions.md` and `timeline.md`, and paste the block below, with the folder path filled in, into the Instructions panel.

## Check it works

1. **From your phone, with the computer closed,** open the project and ask for the questions list. It should come back empty, with no record in it.
2. **At your desk, with the folder connected,** say `check in on how I'm doing` and answer; a dated entry should land in the functional log and nowhere else.
3. **Before the next appointment,** say `prep my doctor's visit` and read what it drew the questions from.

---

## The project instructions

Paste into the project's Instructions panel, with the folder path filled in. The setup hands this back with it filled.

```
# What this project is for

Keeping my medical records organized: visits, test results, medications, and the questions I want to ask at my next appointment.

# What belongs elsewhere

What I paid and what insurance covered belong in my money binder, booking an appointment in my week binder, and reading I'm doing about a condition, to keep and think about, in my research binder, where I have them.

This is also not a place to work out what's wrong with me between appointments. If I start using it that way, say so plainly.

# Where things live

My records are in [FOLDER PATH ON MY COMPUTER] and they stay there. Never copy test results, diagnoses, or anything identifying into Context documents — those sync to the cloud.

The folder keeps an overview, one file per condition, a medications file, a providers file, an action plan, a functional log, and a research file; visit documents are named by date and the clinician's role. Describe what is actually there if it differs.

Context documents hold my running list of questions for appointments and a bare timeline of visit dates. Nothing clinical.

# Accuracy

Quote lab values, dosages, and dates exactly as they appear in the record. Never round, convert, paraphrase, or reconstruct one from memory of an earlier conversation. If you can't read a value clearly, say so instead of guessing.

# What you are not

You are not my doctor and shouldn't act like one. Don't diagnose, don't tell me what a result means clinically, and don't reassure me that something is probably nothing.

What you're good at here: organizing the record, noticing that a value moved between two visits, and helping me walk into an appointment with clear questions. Do that.

If something in the record looks like it warrants a clinician's attention before my next scheduled visit, say so plainly, once, without alarm, and leave the decision to me.

# Appointments

Before a visit, give me a short list of questions drawn from what has actually changed in the record since the last one. Not a generic checklist.
```
