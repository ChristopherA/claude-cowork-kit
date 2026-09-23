# The week project

Running your week: obligations turned into next actions, and a week planned from the time you actually have. Its plugin is `week`, shown as **Your week** in the app. The reasoning every project shares is in [the kit's explainer](../claude-cowork-kit.md).

This project exists so that the notes project can stay quiet. A knowledge project that also runs your week fills up with tasks, and every conversation starts with what is due rather than what you are thinking about. Here, what is due is the point. Nothing in this project sends a message or changes a calendar; drafts are handed back, and you send them.

## The skills

- **`week-setup`**, `set up my week project`. Three questions, then the priorities doc and the instructions to paste.
- **`week-triage`**, `triage this` or `sort this pile out`. A dump of half-formed obligations comes back as a short ordered list of next actions, each something you could start today, with nothing around it. Reach for it when the pile is in your head or your inbox and not yet in any list.
- **`week-plan`**, `plan my week`. The week laid out from your calendar and your priorities, assuming less time than you think and more in flight than you said, and saying so when a plan only works if nothing goes wrong. Run it at the start of the week, after triage.
- **`week-review`**, `review my week`. Done, slipped, avoided, what ate the week, energy, in your own words, compared with recent weeks; the priorities doc changes on a yes. Run it at the end of the week, and it makes the next plan honest.
- **`week-meeting-notes`**, `meeting notes`. After a meeting: notes by topic with decisions first, action items with owners, and carry-forward for a series, from this transcript only; into the folder on a yes.
- **`week-reply`**, `draft a reply`. A reply in your voice, from the message you hand over and your earlier replies, then it stops. It never sends.

## Setup

The setup creates one project doc, `priorities.md`, the two or three things that matter this month, which every plan bends around; the review creates a second, `reviews.md`, when it first runs. The general steps are in the explainer under Setting up a project, and the install paths in the repository's README; for this project:

1. **Install the week plugin**, `week`, shown as **Your week**, and turn it on.
2. **Create the project and connect the folder** that holds your working files, drafts, lists, threads you are keeping, earlier replies, from the project's page. Do not create the project *from* the folder.
3. **Run the setup.** In a task inside the project, say `set up my week project`. Claude asks where the folder is, what your current priorities are, and which of the kit's other projects you have; creates the priorities doc; and hands back what only you can paste: the account instructions, if your Settings, Account, "Instructions for Claude" field does not carry them yet (Block 1 in the explainer), and the project instructions below, for the Instructions panel at the side of the project page, not the description.

Without the plugin: paste the account instructions as the explainer says, create the project, ask Claude in a task to create `priorities.md` from your answers, and paste the block below, with the folder path filled in, into the Instructions panel.

## Check it works

1. **At your desk, dump a mess of obligations into a task** and see whether a short ordered list comes back with nothing around it.
2. **From your phone, with the computer closed,** ask what the current priorities are; the doc alone can answer.
3. **Hand over a message** and see whether a draft comes back and the task stops there.

---

## Project instructions

Paste into the project's Instructions panel, with the folder path filled in. The setup hands this back with it filled.

```
# What this project is for

Running my week: tasks, planning, drafting messages, triage, review.

# What belongs elsewhere

This is not where durable notes live. If something I drop here is really a note — an idea worth keeping, something I read — say so and tell me to put it in my knowledge project's inbox. Don't bury it in a task list where I'll never find it again.

Money questions go to my money project and anything medical to my medical project, where I have them. Answer a general question wherever I ask it, but anything needing those files belongs there, and you can't reach them from here.

# Standing facts

My working files are in [FOLDER PATH ON MY COMPUTER]. Current priorities live in this project's docs — read them before planning anything, and update them when they change.

# Default shape of an answer

When I dump a mess of half-formed obligations at you, hand back a short ordered list of concrete next actions, each one something I could actually start today. No encouragement, no framing, no preamble.

# Planning

Ask what's already on my calendar before proposing a schedule. Assume I have less time than I think and more in flight than I've told you. If a plan only works when nothing goes wrong, say so.

Don't pad a list to look complete. Three real things beat eight.
```
