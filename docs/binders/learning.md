# The learning binder

Learning something on purpose: a subject, a skill, or an exam. This binder holds the plan, the record of what has clicked, and the practice. It is deliberately not the research binder: what you learn that is worth keeping goes there, as a note; what lives here goes stale by design once the course is done. Its plugin is `learn`, shown as **Learning** in the app. The reasoning every binder shares is in [the kit's explainer](../claude-cowork-kit.md).

The Context documents here are small on purpose, a mission, a curriculum, a progress record, so that a lesson works from your phone with the computer closed. The reading material itself stays in the folder.

## The skills

- **`learn-setup`**, `set up my learning binder`. An interview of six questions, then the three Context documents and the instructions to paste. The curriculum is drafted and shown whole before it is created, so you can change it.
- **`learn-lesson`**, `next lesson`. About thirty minutes on one concept, intuition first: Claude asks what you think before it explains, builds from your answer, and records what clicked and what is still shaky. Reach for it whenever you have half an hour; it picks up where the progress record says you are.
- **`learn-quiz`**, `quiz me`. Recall one question at a time, from the lesson, the progress record, or a note you hand over; each answer graded, the difficulty rising. Nothing is marked settled because you said you understood it. Use it once there is something to quiz.

Claude also has a built-in Learning style, in the style menu, that makes it ask rather than answer. It is optional: a task cannot turn it on, whether it carries into a Cowork task is untested, and nothing in this binder depends on it, since the lesson skill does that work inside a task. Claude's Study Projects are a chat feature built around the same style, as of September 2026, and likewise nothing here depends on them.

## Setup

The setup creates three Context documents: `mission.md` (what you're learning, why, by when, how you'll know), `curriculum.md` (units and lessons, one idea each lesson is meant to make intuitive) and `progress.md` (what's settled, what's shaky, what's untested). The general steps are in the explainer under Setting up a binder, and the install paths in the repository's README; for this binder:

1. **Install the learning plugin**, `learn`, shown as **Learning**, and turn it on.
2. **Create the project and connect the folder** that holds your materials, the book, the papers, the course files, from the project's page. If there are no materials yet, an ordinary project with no folder is fine. Do not create the project *from* the folder.
3. **Run the setup.** In a task inside the project, say `set up my learning binder`. Claude asks what you are learning, why and by when, how you will know, where you stand, how you like to learn, and where the materials are; drafts the curriculum for your yes; creates the three Context documents; and hands back what only you can paste: the account instructions, if your Settings, Account, "Instructions for Claude" field does not carry them yet (the account instructions in the explainer), and the project instructions below, for the Instructions panel at the side of the project page, not the description.

Without the plugin: paste the account instructions as the explainer says, create the project, then in a task ask Claude to interview you and write the three Context documents from the block below, and paste the block, with the subject and the folder path filled in, into the Instructions panel.

## Check it works

1. **In this project, ask Claude a direct question about the subject** and see whether it answers or asks. The instructions say to ask first.
2. **From your phone, with the computer closed,** ask where the progress record says you are; the document alone can answer.
3. **Say `next lesson`** and give it thirty minutes.

Flashcards synced to a scheduler are one of the things this kit won't do; that needs a tool Cowork doesn't run. Keep a plain question-and-answer list in the folder and review it on a schedule you set in your week binder.

---

## The project instructions

Paste into the project's Instructions panel, with the subject and the folder path filled in. The setup hands this back with both filled.

```
# What this project is for

Learning something on purpose: [SUBJECT, SKILL, OR EXAM]. The plan, the record of what I understand, and the practice.

# What belongs elsewhere

Anything worth keeping past this course — an idea, a source I'll want again — belongs in my research binder's inbox. Say so and stop rather than burying it in a lesson. Scheduling study time belongs in my week binder, where I have one.

This project holds working files that are meant to go stale: the mission, the curriculum, the progress record, practice material.

# Read this first

At the start of a conversation, read the Context documents `mission.md` and `progress.md` before anything else. Pick up where the progress record says I am. Don't re-teach what it marks as settled, and don't skip what it marks as shaky.

# Where things live

My materials — the book, the papers, the course files — are in [FOLDER PATH ON MY COMPUTER]. The project's Context holds `mission.md` (what I'm learning, why, by when, how I'll know), `curriculum.md` (units and lessons, one idea each lesson is meant to make intuitive), and `progress.md` (what's settled, what's shaky, what's untested). Keep all three short enough to read on a phone.

# How to teach me

Intuition first. Before you explain a thing, ask me what I think it is or how I'd approach it, and build from my answer. One concept per session, about thirty minutes. Check that I understand by having me explain it back or apply it, never by asking whether I understood. When I'm wrong, lead me to find it rather than telling me.

# When I say quiz me

Ask one question at a time from the material, and wait. Grade my answer, explain the gap, and make the next question harder. Vary the form — open, short-answer, pick-one — so I can't pattern-guess.

# Recording progress

At the end of each session, write what clicked and what is still shaky into `progress.md`, using three states: settled, shaky, untested. Never mark something settled because I said I understood it; mark it settled when I explained it correctly without help.

# What you are not

You are not the exam and not the credential. Don't tell me I'm ready; show me what the progress record says and let me decide. Don't reassure me about a gap; name it.
```
