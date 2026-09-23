---
name: cowork-new-project
description: Designs a project the kit does not describe: its purpose, boundaries and docs, then the instructions text and a plugin from the kit's template. Use for "new project", "a project for something else".
---

# New project

Give a project the kit does not describe the same shape as the ones it does: a purpose, a line around it, a folder, a few small project docs, and an Instructions text in the kit's form. This skill designs and hands back text; it does not create the project or install anything.

## Before the first question

Ask what the project is for in one sentence, and take that as the working title. If the reader's answer belongs to a project the kit already describes (notes and reading, learning, the week, money, medical records), say so and point them at that project's plugin instead; do not build a second one.

## The interview, as a plan in rounds

Work this as the interview skill does: a first round of numbered questions, each with a recommended answer, then the next round from what the answers open, and a write-back of what you understood before any text is drafted. The first round is usually these five.

1. **What belongs elsewhere.** The neighbouring things that have their own project, so a request for them is redirected rather than absorbed.
2. **The folder.** Whether there is one on the computer, and what in it must never be copied into a project doc.
3. **The project docs.** The two or three small things that should be readable from the phone with the computer closed. Recommend fewer.
4. **The default shape of an answer.** A list, a draft, a summary, prose.
5. **What Claude is not, here.** The role it must not take, and what it is good for instead.

For money-like and medical-like projects, anything the reader would mind leaking, add the kit's floor: sensitive files stay in the folder, docs hold only what is fine to sync, credentials never anywhere, and the project stays in the mode that asks before acting.

## Hand back the design

Draft the Instructions text in the kit's shape from the answers: what the project is for, what belongs elsewhere, where things live, how to answer, what you are not, then the two standing lines (show and wait before changing anything in the folder; read the project docs first). Show it whole, in one code block. Then a one-line description for the field under the project's title, and the list of project docs to create with one sentence each on what they hold.

Say the hand steps the app needs: create the project, connect the folder, paste the Instructions text into the Instructions panel at the side of the project page (not the description), and ask Claude in a task to create the project docs.

## A plugin is optional, and it is not for everyone

The project is complete without a plugin: the Instructions text and the project docs are the project, and a task does everything a setup skill would. Say so first. Then say, once and without pushing it, that a reader who is comfortable editing files can turn the design into a plugin of their own, so its setup runs from a phrase like the kit's: the kit's repository carries a template folder, a copy of it with the bracketed lines filled in from the text drafted above is the plugin, and Anthropic's plugin-management plugin packages a folder as a `.plugin` file from inside a Cowork task. That path needs the repository downloaded, a text editor and the filled-in folder; if the reader would rather not, nothing is lost.

## Asking

Ask through the app's question control whenever there is a choice, and for every wait for a yes. Put up to four questions in one control when their answers do not depend on each other; a question whose answer depends on another goes in the next control. Each question offers two to four options with the recommended one first and marked as recommended; where the choices are not exclusive, allow more than one. The reader can always answer in their own words instead, and an answer in their own words outranks the options. Reflect each answer back in a phrase before going on. Never ask what the reader has already said.

## What this skill does not do

It does not create a project, connect a folder, set any setting, or install anything. It does not write project docs; the reader asks for those in the new project. It does not build the plugin file, and it does not send a reader who did not ask for one down that path.
