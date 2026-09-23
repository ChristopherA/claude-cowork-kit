# What a Cowork skill can do

What is known, as of 2026-09-22, about the environment a Claude Cowork skill runs in, what a script inside one can reach, and which personal-knowledge features that makes easier. Sources are named per claim. Nothing here has been run inside a Cowork task; the last section lists what a first task should probe before any skill relies on it.

## A skill, in three layers

Anthropic's own design note describes a skill as progressive disclosure: the frontmatter `name` and `description` are preloaded so Claude knows when the skill applies; the body of `skill.md` is read only when it does; files beside it (`references/`, `scripts/`) are read or run only when the body says so. The help article on custom skills adds that a skill may "attach executable code files to skill.md, allowing Claude to run code", with Python and Node named, that packages install from PyPI and npm when a skill loads, and that this "requires code execution to be enabled". The Agent Skills specification, which Anthropic's skills follow, says scripts live in `scripts/`, are referenced by relative path from the skill root, may declare their own dependencies inline (PEP 723 for Python, run with `uv run`), must never prompt for input, and should emit structured output to stdout with diagnostics on stderr, with a `--help` and meaningful exit codes, because the agent decides its next step from what the script prints.

The pattern Anthropic uses in its own skills is instructive: the pdf skill is a reference document of command lines and library snippets (`pdftotext`, `qpdf`, pypdf), not a script repository. Claude composes the commands from the reference. A bundled script earns its place when a command is hard to get right first time, when the same transformation recurs, or when the answer must be deterministic.

## Where it runs

Cowork has two execution modes, and the architecture help article is explicit about both. In cloud mode, the default, "the agent loop and code execution run in an isolated, temporary sandbox on Anthropic-managed infrastructure", one per session, destroyed when the session ends. In local mode the agent loop runs on the device and "shell commands and any code Claude writes execute inside a dedicated Linux VM" under the platform hypervisor. In both, a task that needs a local file or the browser reaches it "through the Claude Desktop app on that device", limited to connected folders.

What is inside each sandbox is documented for two environments and inferred for the third:

| Environment | What is documented | Source and status |
|---|---|---|
| Cowork local VM | Ubuntu 22.04 on ARM64; Python 3.10, Node 22, Ruby 3.0, TypeScript; git, pandoc, ffmpeg, ImageMagick, ripgrep, jq, sqlite3; Python pandas, numpy, matplotlib, beautifulsoup4, camelot; Node docx, pptxgenjs, pdf-lib, sharp; Claude Code as the engine | Pedro Vieito's teardown, January 2026, of a running install. Verified by inspection then; may have changed. |
| Cowork cloud sandbox | Not enumerated by Anthropic for Cowork. The Managed Agents cloud sandbox reference, a sibling product on Anthropic infrastructure, lists Ubuntu 24.04 on x86_64, Python 3.10 to 3.13 with uv, Node 20 to 22, git, curl, jq, yq, ripgrep, pandoc, LibreOffice headless, Poppler (`pdftotext`, `pdftoppm`), qpdf, tesseract, ffmpeg, ImageMagick, SQLite via bindings, up to 8 GB memory and 10 GB disk. | Anthropic docs for a different product. Whether Cowork's cloud sandbox is the same image is unverified. |
| API code execution container | Linux, Python-focused, 5 GiB memory and disk, `rg`, `fd`, `sqlite`, unzip and archive tools; no internet at all | Anthropic API docs. Not Cowork. Included because it is the floor: every Anthropic sandbox documented has ripgrep and sqlite. |

The safe planning assumption before the probe was that ripgrep, jq and sqlite3 are present everywhere Anthropic runs code, pandoc and Poppler in the local VM and likely in the cloud, and `fd` and `yq` in some. The probe of 2026-09-22 (design rules below) found sqlite3 and fd in neither Cowork space and yq only in the cloud, so the documented sandboxes above do not describe Cowork's. Python 3 with pandas is present everywhere. Package installation from PyPI and npm works in the local VM (its proxy allows exactly those two registries plus Anthropic's API) and is documented for skills generally.

## What a script can and cannot reach

**Files.** Connected folders are mounted into the session. In the local VM, Vieito found them under `/sessions/<session-name>/mnt/<Folder>/`, with the desktop app translating paths back to `~/Folder/` in what the user sees. A script therefore sees the notes folder as an ordinary directory tree and can walk it, search it and read file metadata. Writes go back through the same mount, which is why the kit's show-and-wait rule matters for anything a script would change. The project's docs (map.md, inbox.md) are project knowledge, not files in that tree; how they appear to a script, if at all, is a probe item.

**Network.** "No access to your network by default" in the architecture article: no private, link-local or cloud-metadata addresses, and egress only through a mandatory proxy. The local VM's proxy allowlists Anthropic's API, PyPI and npm and returns 403 for everything else. So a script cannot fetch a web page, call an API of the reader's, or use the reader's browser session. Web reading is done by Claude's own tools, and the results arrive as text the script can be handed, never fetched by the script.

**Persistence.** Each session's sandbox is destroyed at the end (cloud) or its session directory is isolated and its user retired (local). Nothing a script installs or caches survives to the next session. Vieito noted the local VM's `/tmp` is shared across sessions, which is a leak to avoid, not a feature to use. Anything a skill wants to keep goes into the notes folder or a project doc, through Claude, as content the reader can read.

**The reader's own machine.** Local mode is a VM with the connected folders mounted, not the reader's shell. A script cannot open the reader's apps, read their keychain, or see files outside the connected folders. The Cloud Security Alliance's July 2026 note on the SharedRoot escape is the caveat: a chain from an unprivileged agent to root inside that VM to a writable host mount was demonstrated, Anthropic rated it informative and made cloud execution the default, and local mode was reported unpatched at that date. That is a reason to keep the kit's skills read-mostly and to prefer cloud sessions for untrusted content; its current status is a claim-check item.

## What that makes easier for personal knowledge

The kit's principle is that structure lives in plain files the reader can read, and that Claude-maintained indexes are the rot to refuse. A script that computes a view at the moment it is asked and stores nothing is on the right side of that line; a script that writes an index file is not. Every feature below is a computed view.

**Backlinks and orphans.** `rg` over the folder for links to a note (relative markdown links in the kit's default format, `[[wikilinks]]` in an Obsidian vault) answers "what points here" in one command, and the inverse, notes nothing links to, is a set difference over the same output. This is the feature the LLM-wiki plugin builds a SQLite graph for; over a folder of a few thousand notes ripgrep does it in well under a second with no stored index.

**Untouched notes.** The kit's Maintenance section promises "surface notes untouched in six months". A `find` over the mount by modification time, or a `stat` pass, gives the list. Two caveats to probe: whether the VirtioFS mount preserves the host's modification times, and whether a sync service's own touches (iCloud, Dropbox) make every file look fresh. The kit's `created` date inside the note is the fallback the script can read with `rg`.

**Description versus folder.** The "it will drift" check is a comparison of two lists: the folders and conventions map.md claims, against a `find`-and-`rg` census of what is actually there (folder names, files per folder, the metadata line present or missing at the top of each note, wrapped versus unwrapped paragraphs). A script produces the census as JSON; Claude reads both and reports the differences. Deterministic and cheap, where a purely conversational check reads a sample and guesses.

**Inbox drain support.** Not the drain itself, which is judgment, but the lookups around it: for each captured item, `rg` for its key terms across the folder to find the note it might belong to or duplicate, so the one-at-a-time decision starts with candidates rather than from memory.

**Contradictions and duplicates.** "Where last week's thinking contradicts something from March" is a language task, but its candidate generation is not: `rg` for the distinctive terms of a new note across older ones narrows a few thousand notes to a handful for Claude to read. The same pattern finds near-duplicate source notes by title or by URL.

**Source note hygiene.** For a handed PDF, `pdftotext` (Poppler) or pandoc gives clean text before Claude reads it, which is more reliable than reading a scanned page as an image, and a script can pull the citation fields (title, author, year) from PDF metadata with a Python one-liner. Where the environment has tesseract, a scanned PDF becomes text too.

**Frontmatter and dates.** The kit's notes carry a `created` line and optionally `source`. A script that reads those lines across the folder with `rg` and emits JSON gives Claude a table to answer "what did I read in March" or "which sources have no note yet" without opening every file.

**Learning project.** The progress record is markdown by design, so `jq` does not apply to it directly; a script can still parse its three states (settled, shaky, untested) into JSON for a "what should we drill" answer, and can sample a question bank deterministically so grill-me does not always start at the top. Both are marginal; the learning skills are mostly instructions.

**What scripts do not help with.** Filing, writing, deciding what a note is about, and everything in the appendices that is about judgment. The money project's arithmetic is the one place a script is not optional: a total computed by Python from a CSV is checkable in a way a total produced in prose is not, and the kit's accuracy clause ("show the arithmetic") is easier to honour with the calculation in a script's output.

## Design rules for scripts in the kit's skills

- **Read-mostly.** A script reads the folder and prints; Claude proposes; the reader says yes; Claude writes. A script that writes to the folder is the exception and says so in the skill's description.
- **Computed views, never stored indexes.** Output goes to stdout and into the conversation, not into a file the reader would have to maintain.
- **Structured output, bounded size.** JSON or TSV to stdout, diagnostics to stderr, a `--limit` with a sane default, per the Agent Skills guidance, because the output lands in Claude's context.
- **No network, no assumptions about tools.** Use ripgrep, jq, Python 3 with the standard library, pandoc and pdftotext, all present in both the local and the cloud space as of 2026-09-22 (Python 3.10 locally, 3.11 in the cloud, so write for 3.10); yq exists only in the cloud, and sqlite3 and fd exist in neither, so do not depend on them.
- **Markdown-only fallback.** Every skill states in its body what to do when code execution is off: the same feature by Claude reading, slower and sampled. A non-programmer's default should be the markdown-only version, with the script as the upgrade.
- **Prerequisite stated.** The skill's description or first line says "needs code execution enabled", so the reader knows why it may not run.
- **Description written last, and counted.** Cowork rejects a description over 200 characters, and every first draft this project wrote ran over (218 to 323 characters, seven of seven). Write the body first, then the description as one sentence of purpose plus two or three trigger phrases, and count it before packaging.

## To probe in a first Cowork task, before any skill depends on it

1. In a cloud session and in a local session, run `which rg jq yq sqlite3 pandoc pdftotext fd python3 uv node` and record the two inventories.
2. Confirm the mount path of a connected folder and whether file modification times match the host's.
3. Check whether project docs (map.md, inbox.md) are visible to a script at all, and where.
4. Confirm a skill with a `scripts/` directory uploads as a ZIP and its script runs by relative path.
5. Confirm where the code execution toggle is and its default for a Pro account.
6. Try `uv run` on a PEP 723 script in both modes to see whether package installation from PyPI works in the cloud sandbox as it does in the local VM.
7. Re-read the SharedRoot status against the running app's execution-mode setting.
