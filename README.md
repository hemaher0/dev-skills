# kryptonite

Version: **0.1.0**

kryptonite is a Codex plugin for planning, implementation, debugging, testing,
code review, and development delivery. It is based on
[Superpowers v6.2.0](https://github.com/obra/superpowers/tree/v6.2.0).

Source repository: [hemaher0/dev-skills](https://github.com/hemaher0/dev-skills).

## Repository layout

```text
.agents/plugins/marketplace.json
plugins/kryptonite/
  .codex-plugin/plugin.json
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

## Optional plugin compatibility

This repository also remains a Codex plugin package:

- [Plugin manifest](plugins/kryptonite/.codex-plugin/plugin.json): `kryptonite`, version `0.1.0`.
- [Repository marketplace](.agents/plugins/marketplace.json): `kryptonite-dev`.
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

Each selected skill retains its own responsibility when installed alone.
References to another skill are optional: use the exact installed name and
location from the current host's available-skills list. Do not treat an
adjacent folder in this vendor checkout or a plugin cache as an available skill,
because a host-listed project, global, or plugin copy may be a different
revision. When a companion is absent, follow the concrete project or inline
fallback in the selected skill.

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
