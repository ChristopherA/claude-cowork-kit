# The week binder

Running your week: obligations turned into next actions, and a week planned from the time you actually have. Its plugin is `week`, shown as **Your week** in the app. The reasoning every binder shares is in [the kit's explainer](../claude-cowork-kit.md).

This binder exists so that the research binder can stay quiet. A research binder that also runs your week fills up with tasks, and every conversation starts with what is due rather than what you are thinking about. Here, what is due is the point. Nothing in this binder sends a message or changes a calendar; drafts are handed back, and you send them.

## The skills

- **`week-setup`**, `set up my week binder`. Three questions, then the priorities document and the instructions to paste.
- **`week-triage`**, `triage this` or `sort this pile out`. A dump of half-formed obligations comes back as a short ordered list of next actions, each something you could start today, with nothing around it. Reach for it when the pile is in your head or your inbox and not yet in any list.
- **`week-plan`**, `plan my week`. The week laid out from your calendar and your priorities, assuming less time than you think and more in flight than you said, and saying so when a plan only works if nothing goes wrong. Run it at the start of the week, after triage.
- **`week-review`**, `review my week`. Done, slipped, avoided, what ate the week, energy, in your own words, compared with recent weeks; the priorities document changes on a yes. Run it at the end of the week, and it makes the next plan honest.
- **`week-meeting-notes`**, `meeting notes`. After a meeting: notes by topic with decisions first, action items with owners, and carry-forward for a series, from this transcript only; into the folder on a yes.
- **`week-reply`**, `draft a reply`. A reply in your voice, from the message you hand over and your earlier replies, then it stops. It never sends.

## Setup

The setup creates one Context document, `priorities.md`, the two or three things that matter this month, which every plan bends around; the review creates a second, `reviews.md`, when it first runs. The general steps and the install paths are in the repository's README, under First run and Install; for this binder:

1. **Install the week plugin**, `week`, shown as **Your week**, and turn it on.
2. **Create the project with its folder.** In Claude, open **Projects**, then **New project**, and fill in the dialog:
   - **What are you working on?** The binder's name, such as `Your week`.
   - **What are you trying to achieve?** A sentence or two saying what the binder is for. Paste this and change it to suit:

     ```
     My week: turn what I owe people into next actions, and plan each week from the time I actually have.
     ```

     The app reads this when deciding which project a task belongs in; the rules Claude works by come later, from the setup.
   - **Folder:** choose **Use a folder** and pick the folder that holds your working files, drafts, lists, threads you are keeping, earlier replies.

   Click **Create project**. When Claude asks to change files in the folder, choose **Always allow**.
3. **Run the setup.** On the project page, switch the box at the top from **Chat** to **Cowork**, then say `set up my week binder`. Claude asks where the folder is, what your current priorities are, and which of the kit's other binders you have; creates the priorities document; and hands back what only you can paste: the account instructions, if your Settings, Account, "Instructions for Claude" field does not carry them yet (the account instructions in the explainer), and the project instructions below, for **Instructions** on the right of the project page (click its pencil and paste), not the description under the title.

Without the plugin: paste the account instructions as the explainer says, create the project, create `priorities.md`, either by asking Claude in a Cowork task to write it from your answers or by hand, in the **Context** panel with **+**, **Add text content**, the title typed exactly and every [BRACKET] filled in before you add it, and paste the block below, with the folder path filled in, into **Instructions** on the right of the project page (click its pencil).

## Check it works

First look at the project's **Context** panel: `priorities.md` should be there, with no [BRACKET] left in it, and the capacity bar should be nearly empty, since Context holds a description and never copies of your files. Then:

1. **At your desk, dump a mess of obligations into a task** and see whether a short ordered list comes back with nothing around it.
2. **From your phone, with the computer closed,** ask what the current priorities are; the document alone can answer.
3. **Hand over a message** and see whether a draft comes back and the task stops there.

---

## The project instructions

Paste into the project's Instructions panel, with the folder path filled in. The setup hands this back with it filled.

```
# What this project is for

Running my week: tasks, planning, drafting messages, triage, review.

# What belongs elsewhere

This is not where durable notes live. If something I drop here is really a note — an idea worth keeping, something I read — say so and tell me to put it in my research binder's inbox. Don't bury it in a task list where I'll never find it again.

Money questions go to my money binder and anything medical to my health binder, where I have them. Answer a general question wherever I ask it, but anything needing those files belongs there, and you can't reach them from here.

# Standing facts

My working files are in [FOLDER PATH ON MY COMPUTER]. Current priorities live in this project's Context — read them before planning anything, and update them when they change.

# Default shape of an answer

When I dump a mess of half-formed obligations at you, hand back a short ordered list of concrete next actions, each one something I could actually start today. No encouragement, no framing, no preamble.

# Planning

Ask what's already on my calendar before proposing a schedule. Assume I have less time than I think and more in flight than I've told you. If a plan only works when nothing goes wrong, say so.

Don't pad a list to look complete. Three real things beat eight.
```
