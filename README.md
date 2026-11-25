# kryptonite

Version: **0.1.0**

kryptonite is a skill collection for Codex and Claude Code covering planning,
implementation, debugging, testing, code review, and development delivery. It is
based on [Superpowers v6.2.0](https://github.com/obra/superpowers/tree/v6.2.0).
Selected investigation, review and prevention workflows also adapt ideas from
[pstack](https://github.com/cursor/plugins/tree/main/pstack); see the
[attribution and license](THIRD_PARTY_NOTICES.md).

Source repository: [hemaher0/dev-skills](https://github.com/hemaher0/dev-skills).

## Repository layout

```text
.agents/plugins/marketplace.json
.claude-plugin/marketplace.json
plugins/kryptonite/
  .codex-plugin/plugin.json
  .claude-plugin/plugin.json
  skills/<skill>/SKILL.md
tests/
```

Each skill folder includes its supporting scripts, prompts, and templates.

## Install for a project

Run these commands from the project root. The clone keeps the complete native
source tree, including scripts and templates used by selected skills:

```bash
mkdir -p .agents/vendor .agents/skills
git clone --branch main https://github.com/hemaher0/dev-skills.git .agents/vendor/dev-skills
```

Choose either a selective installation or the all-skills variant. For a
selective installation, edit the list and link only those complete skill
folders:

```bash
for skill in using-kryptonite developing-with-specs systematic-debugging; do
  destination=".agents/skills/$skill"
  if [ -e "$destination" ] || [ -L "$destination" ]; then
    printf 'Preserve existing path: %s\n' "$destination" >&2
    continue
  fi
  ln -s "../vendor/dev-skills/plugins/kryptonite/skills/$skill" "$destination"
done
```

To expose every skill instead:

```bash
for source in .agents/vendor/dev-skills/plugins/kryptonite/skills/*; do
  [ -f "$source/SKILL.md" ] || continue
  skill="${source##*/}"
  destination=".agents/skills/$skill"
  if [ -e "$destination" ] || [ -L "$destination" ]; then
    printf 'Preserve existing path: %s\n' "$destination" >&2
    continue
  fi
  ln -s "../vendor/dev-skills/plugins/kryptonite/skills/$skill" "$destination"
done
```

These commands preserve existing destinations and continue with the remaining
skills. Inspect a skipped path before deliberately replacing it or choosing
a different skill selection. The relative links
remain valid when the project moves because both source and links are under its
`.agents/` directory. The vendor checkout by itself is not a discovered skill.

Start a new Codex session in the project after installation. If the host does
not detect the change automatically, restart it. Ask Codex to use a selected
skill by name, such as `using-kryptonite`, and confirm that the current host's
available-skills list contains that exact name and installed location. A source
folder existing under `.agents/vendor/` does not establish availability.
For an explicit invocation, prompt `Use $using-kryptonite for this task`.

```bash
readlink .agents/skills/using-kryptonite
test -f .agents/skills/using-kryptonite/SKILL.md
```

Update only this project's source checkout. If its installed links use the
previous root `skills/` layout, [relink them after updating](#update-an-existing-installation):

```bash
git -C .agents/vendor/dev-skills pull --ff-only
```

Remove a project skill by unlinking its exposure while retaining the vendor
source for other selected skills:

```bash
unlink .agents/skills/systematic-debugging
```

Project instructions are optional installation inputs. Add or merge the
[local development template](plugins/kryptonite/skills/developing-with-specs/templates/AGENTS.local.md)
only when the project needs to configure a scratchpad root or another setting
owned there. Preserve existing instructions and fill every retained value. The
default scratchpad location needs no project configuration.

## Install globally

Global skills are shared by Codex sessions for this user. Clone the source and
create the discovery directory under `$HOME/.agents`:

```bash
mkdir -p "$HOME/.agents/vendor" "$HOME/.agents/skills"
git clone --branch main https://github.com/hemaher0/dev-skills.git "$HOME/.agents/vendor/dev-skills"
```

Choose either a selective installation or the all-skills variant. For a
selective installation, edit the list:

```bash
for skill in using-kryptonite writing-plans requesting-code-review; do
  destination="$HOME/.agents/skills/$skill"
  if [ -e "$destination" ] || [ -L "$destination" ]; then
    printf 'Preserve existing path: %s\n' "$destination" >&2
    continue
  fi
  ln -s "../vendor/dev-skills/plugins/kryptonite/skills/$skill" "$destination"
done
```

To expose every skill globally instead:

```bash
for source in "$HOME"/.agents/vendor/dev-skills/plugins/kryptonite/skills/*; do
  [ -f "$source/SKILL.md" ] || continue
  skill="${source##*/}"
  destination="$HOME/.agents/skills/$skill"
  if [ -e "$destination" ] || [ -L "$destination" ]; then
    printf 'Preserve existing path: %s\n' "$destination" >&2
    continue
  fi
  ln -s "../vendor/dev-skills/plugins/kryptonite/skills/$skill" "$destination"
done
```

Start a new Codex session after installation, or restart the host if automatic
change detection does not refresh the skill list. Invoke a selected skill by
name and verify its exact name and installed location in the current host's
available-skills list. Check the linked source with:

```bash
readlink "$HOME/.agents/skills/using-kryptonite"
test -f "$HOME/.agents/skills/using-kryptonite/SKILL.md"
```

For an explicit invocation, prompt `Use $using-kryptonite for this task`.

Update or remove only the global installation with the commands below. If its
installed links use the previous root `skills/` layout,
[relink them after updating](#update-an-existing-installation).

```bash
git -C "$HOME/.agents/vendor/dev-skills" pull --ff-only
unlink "$HOME/.agents/skills/requesting-code-review"
```

A global skill applies across projects. If a project also exposes a skill with
the same name, both may appear; Codex does not merge duplicate skills or promise
that one shadows the other. Remove the unintended exposure or use distinct
names rather than relying on precedence.

## Update an existing installation

Earlier checkouts stored the plugin manifest and `skills/` at the repository
root. After pulling the new layout, update only links that still point to that
old dev-skills path. The loops below retain the previous skill selection and
preserve unrelated files, directories, and links. If project instructions or a
custom marketplace reference the old plugin root, update them to
`.agents/vendor/dev-skills/plugins/kryptonite` as well. User-level marketplace
entries use the corresponding `$HOME/.agents/vendor/` path.

For a project, run from its root:

```bash
for destination in .agents/skills/*; do
  [ -L "$destination" ] || continue
  skill="${destination##*/}"
  [ "$(readlink "$destination")" = "../vendor/dev-skills/skills/$skill" ] || continue
  [ -f ".agents/vendor/dev-skills/plugins/kryptonite/skills/$skill/SKILL.md" ] || continue
  unlink "$destination" || continue
  ln -s "../vendor/dev-skills/plugins/kryptonite/skills/$skill" "$destination"
done
```

For the global installation:

```bash
for destination in "$HOME"/.agents/skills/*; do
  [ -L "$destination" ] || continue
  skill="${destination##*/}"
  [ "$(readlink "$destination")" = "../vendor/dev-skills/skills/$skill" ] || continue
  [ -f "$HOME/.agents/vendor/dev-skills/plugins/kryptonite/skills/$skill/SKILL.md" ] || continue
  unlink "$destination" || continue
  ln -s "../vendor/dev-skills/plugins/kryptonite/skills/$skill" "$destination"
done
```

Check the selected links and start a new Codex session as described above.
Plugin-managed caches are separate installations; these loops update only
native skill links.

## Use with Claude Code

Claude Code discovers project skills in `.claude/skills/<name>/SKILL.md` and
personal skills in `~/.claude/skills/<name>/SKILL.md`. The skill folders in
this repository work there without conversion. Keep the source checkout
described above and expose the selected skills from the project root, for
example:

```bash
mkdir -p .claude/skills
for skill in using-kryptonite systematic-debugging; do
  destination=".claude/skills/$skill"
  if [ -e "$destination" ] || [ -L "$destination" ]; then
    printf 'Preserve existing path: %s\n' "$destination" >&2
    continue
  fi
  ln -s "../../.agents/vendor/dev-skills/plugins/kryptonite/skills/$skill" "$destination"
done
```

The link targets are relative to `.claude/skills`. For personal skills, run
the same loop with `$HOME/.claude/skills` and the global source checkout under
`$HOME/.agents/vendor`; the relative targets stay the same. Where symbolic
links are unavailable, such as Windows without Developer Mode, copy each
selected folder completely instead and copy it again after updating the source.

A project that already has a Codex installation under `.agents/skills` can
expose the same kryptonite selection to Claude Code. The loop skips links that
belong to other skill sources and preserves existing destinations:

```bash
mkdir -p .claude/skills
for source in .agents/skills/*; do
  [ -L "$source" ] || continue
  skill="${source##*/}"
  [ "$(readlink "$source")" = "../vendor/dev-skills/plugins/kryptonite/skills/$skill" ] || continue
  destination=".claude/skills/$skill"
  if [ -e "$destination" ] || [ -L "$destination" ]; then
    printf 'Preserve existing path: %s\n' "$destination" >&2
    continue
  fi
  ln -s "../../.agents/vendor/dev-skills/plugins/kryptonite/skills/$skill" "$destination"
done
```

Both hosts then read the same source checkout, so
`git -C .agents/vendor/dev-skills pull --ff-only` updates them together. Links
for skills added later are created separately.

Use a skill by its name, for example `/systematic-debugging`, or let Claude
select it from its description. Confirm that the name appears in the session's
skill list; start a new session if a newly added folder is not listed.

Claude Code can also install this repository as a plugin marketplace:

```bash
claude plugin marketplace add hemaher0/dev-skills
claude plugin install kryptonite@kryptonite-dev
```

Inside a session, `/plugin marketplace add hemaher0/dev-skills` and
`/plugin install <plugin>@<marketplace>` do the same. Plugin skills are
namespaced, for example `/kryptonite:systematic-debugging`. Installation records
the plugin in user settings by default; `--scope project` or `--scope local`
records it in the project's shared or local settings instead. Installed plugins
are separate copies from the folders above, so a skill exposed both ways appears
twice.

Claude Code reads `CLAUDE.md`. It reads `AGENTS.md` only when no `CLAUDE.md` or
`CLAUDE.local.md` exists in the working directory or above it (Claude Code
2.1.277 or later) and does not read `AGENTS.local.md` by itself. When a project
keeps shared instructions in `AGENTS.md` and also has a `CLAUDE.md`, add an
`@AGENTS.md` line to `CLAUDE.md`. An instruction in `AGENTS.md` to read
`AGENTS.local.md` keeps local configuration in effect. `developing-with-specs`
reads a local scratchpad setting from `AGENTS.local.md` or `CLAUDE.local.md`,
which Claude Code loads by itself.

In Claude Code, `using-kryptonite` reads
[claude-code-tools.md](plugins/kryptonite/skills/using-kryptonite/references/claude-code-tools.md)
where Codex uses `codex-tools.md`.

## Optional plugin compatibility

This repository also remains a plugin package for Codex and Claude Code:

- [Plugin manifest](plugins/kryptonite/.codex-plugin/plugin.json): `kryptonite`, version `0.1.0`.
- [Repository marketplace](.agents/plugins/marketplace.json): `kryptonite-dev`.
- [Claude Code plugin manifest](plugins/kryptonite/.claude-plugin/plugin.json) and [marketplace](.claude-plugin/marketplace.json): `kryptonite@kryptonite-dev`.
- [Bootstrap skill](plugins/kryptonite/skills/using-kryptonite/SKILL.md): `using-kryptonite`.
- Plugin-provided skills use the `kryptonite:` invocation namespace.

Plugin installation and enablement are separate from the native skill-folder
procedures above. Plugin commands and the plugin browser can write user-level
configuration and managed cache entries; running them inside a project does not
make that state project-local. Follow the host's plugin documentation when that
packaged route is desired. Do not treat a managed plugin cache, a vendor clone,
or a sibling skill folder as proof that a skill is currently available.

## Skills

| Skill | Purpose |
| --- | --- |
| [using-kryptonite](plugins/kryptonite/skills/using-kryptonite/SKILL.md) | Discover and invoke relevant skills. |
| [brainstorming](plugins/kryptonite/skills/brainstorming/SKILL.md) | Explore unresolved goals, necessary conditions, and design choices. |
| [developing-with-specs](plugins/kryptonite/skills/developing-with-specs/SKILL.md) | Derive necessary requirements and maintain the working spec and decision history. |
| [writing-plans](plugins/kryptonite/skills/writing-plans/SKILL.md) | Connect requirements to purposeful tasks and verification. |
| [executing-plans](plugins/kryptonite/skills/executing-plans/SKILL.md) | Execute a plan while reconciling requirements, decisions, and evidence. |
| [subagent-driven-development](plugins/kryptonite/skills/subagent-driven-development/SKILL.md) | Execute tasks with implementer and review agents. |
| [dispatching-parallel-agents](plugins/kryptonite/skills/dispatching-parallel-agents/SKILL.md) | Investigate independent problems concurrently. |
| [systematic-debugging](plugins/kryptonite/skills/systematic-debugging/SKILL.md) | Diagnose observed failures and verify supported corrections. |
| [test-driven-development](plugins/kryptonite/skills/test-driven-development/SKILL.md) | Choose useful tests and verification for behavior changes and refactoring. |
| [requesting-code-review](plugins/kryptonite/skills/requesting-code-review/SKILL.md) | Request review against requirements and code changes. |
| [receiving-code-review](plugins/kryptonite/skills/receiving-code-review/SKILL.md) | Evaluate feedback before changing code. |
| [verification-before-completion](plugins/kryptonite/skills/verification-before-completion/SKILL.md) | Verify results before claiming completion. |
| [writing-agent-handoffs](plugins/kryptonite/skills/writing-agent-handoffs/SKILL.md) | Transfer responsibility or document assignments and their results. |
| [generalizing-diffs](plugins/kryptonite/skills/generalizing-diffs/SKILL.md) | Ground changed code and prose in actual requirements and semantics. |
| [managing-compatibility](plugins/kryptonite/skills/managing-compatibility/SKILL.md) | Align changed interfaces and required data, and assess release or upgrade readiness. |
| [writing-skills](plugins/kryptonite/skills/writing-skills/SKILL.md) | Develop and validate reusable skills. |
| [reviewing-code-comments](plugins/kryptonite/skills/reviewing-code-comments/SKILL.md) | Remove redundant comments, preserve required rationale, and identify constraints or design problems hidden by prose. |
| [benchmarking-performance](plugins/kryptonite/skills/benchmarking-performance/SKILL.md) | Validate workloads, comparison conditions, actual work and uncertainty behind performance claims. |
| [investigating-codebase](plugins/kryptonite/skills/investigating-codebase/SKILL.md) | Explain current code behavior and investigate evidence for design rationale. |
| [recovering-work-context](plugins/kryptonite/skills/recovering-work-context/SKILL.md) | Reconstruct goals, decisions and attempts from scoped history and reconcile them with live state. |
| [preventing-recurring-errors](plugins/kryptonite/skills/preventing-recurring-errors/SKILL.md) | Identify recurring failure mechanisms and verify proportionate structural or checking remedies. |

Each selected skill retains its own responsibility when installed alone.
References to another skill are optional: use the exact installed name and
location from the current host's available-skills list. Do not treat an
adjacent folder in this vendor checkout or a plugin cache as an available skill,
because a host-listed project, global, or plugin copy may be a different
revision. When a companion is absent, follow the concrete project or inline
fallback in the selected skill.

## Investigation and improvement workflows

The workflows have distinct responsibilities. Code investigation explains
behavior and rationale; context recovery reconstructs the user's work; handoffs
transfer responsibility. Comment review can identify a necessary code change,
but does not authorize it. Recurrence prevention owns the failure pattern and
selects a remedy; debugging, compatibility, tests and skill authoring retain
their parts of an authorized implementation.

Design and review guidance checks caller usage, domain invariants, hidden
mutable state and unnecessary indirection. Compatibility investigation follows
indirect consumers and verifies the facts on which a safety conclusion depends.
Tests are assessed for detecting broken behavior while surviving internal
restructuring. Parallel work separates mutable targets before adding structural
serialization where sharing is necessary.

When no existing procedure fits, the existing planning workflow defines the
completion condition, important unknowns, verification and recovery boundaries,
and one executor. Execution records exploratory hypotheses and observations;
completion checks the integrated result against the original goal. This keeps
one plan and execution controller rather than introducing another mode.

These adaptations preserve project contracts, useful rationale and existing
authorization. They do not require fixed model panels, tool-specific transcript
paths, benchmark repetition quotas or automatic commits. They use scoped
evidence and checks appropriate to the consequence and uncertainty. Sources are
identified in the relevant skills and [third-party notice](THIRD_PARTY_NOTICES.md).

## Working Files

Each responsible skill defines its own artifacts and retention;
[using-kryptonite](plugins/kryptonite/skills/using-kryptonite/SKILL.md) connects the stages.
Project settings and existing governing workflows take precedence. Working
specs default to `.kryptonite/scratchpad/<work-id>/spec.md`, plans sit beside
them, agent communication defaults to `.kryptonite/work/<work-id>/`, and SDD
uses `.kryptonite/sdd/<plan-id>/`, with identity derived from the plan path.
Existing pending SDD records are reconciled before reuse or explicit migration.

[Developing with specs](plugins/kryptonite/skills/developing-with-specs/SKILL.md#ground-consequential-choices)
connects consequential choices to their purpose, applicable evidence, unresolved
premises, and checks before dependent work. Evidence effort follows impact,
uncertainty, and reversibility. A default, plan, or successful execution does not
establish suitability or turn an agent's selection into a user requirement.
Domain suitability and software correctness use their respective evidence.

See [developing-with-specs](plugins/kryptonite/skills/developing-with-specs/SKILL.md) for spec and
durable-document placement, and the
[agent record conventions](plugins/kryptonite/skills/writing-agent-handoffs/references/roles.md)
for brief, report, and handoff paths.

Commit preparation documents the change, generalizes code and final documents,
renews affected verification/review, and uses the project's Git workflow for
actual candidate/message review and the authorized commit. Documentation uses
the project's designated skill or procedure. A routine commit does not finish
the whole work: temporary records are disposed of only after completed-work
information is preserved durably and retention needs are met. Git workspace
cleanup is a separate ownership decision.

## Validation

Run the helper regression checks from this source checkout with Python 3,
Bash, and Git available:

```bash
python3 -m unittest discover -s tests -v
```

The tests exercise task extraction, server option validation, and pollution
investigation using temporary workspaces and controlled external commands.

## License

[MIT License](LICENSE). Original copyright and attribution are retained.
