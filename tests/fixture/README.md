# Test fixture for the pkm skills

A small notes folder and the two project docs that go with it, for testing the kit's skills in Cowork before a reader's real notes are involved. The setup skill creates `rules.md`, `map.md` and `inbox.md` as project docs from the reader's answers; `project-docs/` holds the three the test's answers should produce, for comparison. `notes-folder/` is copied by hand into the connected folder after setup, so the check skills have something to find.

Three defects are deliberate, so the description check has something to find: `notes/Topic Note.md` is named for a topic rather than a claim and carries no `created` line; `notes/notes-should-lead-with-the-claim.md` is hard-wrapped where the convention says one paragraph per line; and `map.md` lists an open thread, "why capture and filing are different", whose note does not exist. `CLAUDE.md` at the folder root carries an instruction, because Cowork reads a connected folder's `CLAUDE.md` at the start of a task without being asked (the explainer says so under What the connected folder does and does not protect); it stays so a test run can see that happen.

The inbox holds four captures chosen to exercise each branch of the drain: one that belongs in an existing note, one that is a new idea, one that belongs to another project, and one that is a source to read.
