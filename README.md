# kryptonite

Version: **0.1.0**

kryptonite is a Codex plugin for planning, implementation, debugging, testing,
code review, and development delivery. It is based on
[Superpowers v6.2.0](https://github.com/obra/superpowers/tree/v6.2.0).

Source repository: [hemaher0/dev-skills](https://github.com/hemaher0/dev-skills).

## Package

- [Plugin manifest](.codex-plugin/plugin.json): `kryptonite`, version `0.1.0`.
- [Repository marketplace](.agents/plugins/marketplace.json): `kryptonite-dev`.
- [Bootstrap skill](skills/using-kryptonite/SKILL.md): `using-kryptonite`.
- Skills use the `kryptonite:` invocation namespace.
- The package targets Codex and includes its
  [tool reference](skills/using-kryptonite/references/codex-tools.md).

## Install for a project

Use the project's existing plugin installation procedure, or register this
source in a repository marketplace. For a first local-source setup, run from
the target project's root; reuse an existing suitable source checkout:

```bash
mkdir -p .agents/vendor .agents/plugins .codex
git clone --branch main https://github.com/hemaher0/dev-skills.git .agents/vendor/dev-skills
```

Merge this entry into `.agents/plugins/marketplace.json`, preserving its actual
marketplace name and other plugin entries:

```json
{
  "name": "project-skills",
  "plugins": [
    {
      "name": "kryptonite",
      "source": {"source": "local", "path": "./.agents/vendor/dev-skills"},
      "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
      "category": "Developer Tools"
    }
  ]
}
```

Merge into project `.codex/config.toml`, substituting the existing marketplace
name when it differs from `project-skills`:

```toml
[plugins."kryptonite@project-skills"]
enabled = true
```

Local paths resolve from the marketplace root, which is the project root in
this example. Open the project as trusted, restart the desktop app when needed,
install/enable the plugin through its supported client workflow, and start a
new session. See the [official local plugin guide](https://developers.openai.com/plugins/build/plugins).

### Project settings

Create or update root `AGENTS.local.md` as part of every installation, even
without a separate request for the file. Preserve existing configuration and
established choices.

Read existing project instructions and their configuration sources. Shared
scratchpad/plan/document conventions and retention exceptions belong there;
common workflow and defaults belong to their responsible skills. Keep existing
paths. New unconfigured work uses `.kryptonite/scratchpad/` without adding that
default to another configuration file.

Read the [local development template](skills/developing-with-specs/templates/AGENTS.local.md)
and merge its development section into `AGENTS.local.md`. Fill selected
personal/checkout-specific scratchpad overrides only. If none are needed,
write `Local overrides: None. Use effective project settings and skill defaults.`
in that section instead of omitting the file or copying default paths. Remove
unused template fields and preserve other packages' sections. Follow project
document and Git policies without requiring a particular plugin.

Connect the local file to root instructions. If `AGENTS.md` exists, preserve it
and add the following instruction unless it already reads or resolves to the
local file:

```markdown
Read and follow root AGENTS.local.md when it exists.
```

If `AGENTS.md` is absent, the recommended connection is a relative symbolic
link created from the project root, after writing `AGENTS.local.md`:

```bash
ln -s AGENTS.local.md AGENTS.md
```

Preserve existing files and links; do not replace them or add a self-reference
to a linked local file. If `AGENTS.override.md` takes precedence, ensure it also
reads the local file. Verify the effective connection, including link targets.

Inspect repository facts and reuse established choices first. Confirm unresolved
consequential choices, such as a different storage location or conflicting
project rule, with the project owner before dependent setup. Write the resulting settings
with ordinary file edits; fill applicable values and omit unused fields.
Repeated setup updates the same sections without duplicates or overwritten
policy. Report configured paths, changed instruction files, and any dependent
feature still unconfigured. Settings do not grant execution or Git permissions.
An unresolved choice is pending, not evidence that a setting is unnecessary.

Before declaring installation complete, verify that `AGENTS.local.md` contains
the resolved development settings or the explicit no-override declaration,
has no unused placeholders, and is read through effective root instructions.
Check marketplace paths/name and, in a new session, skill availability and the
resolved scratchpad setting. Required unresolved choices remain pending;
plugin availability alone does not complete configuration.

## Skills

| Skill | Purpose |
| --- | --- |
| [using-kryptonite](skills/using-kryptonite/SKILL.md) | Discover and invoke relevant skills. |
| [brainstorming](skills/brainstorming/SKILL.md) | Explore unresolved goals, necessary conditions, and design choices. |
| [developing-with-specs](skills/developing-with-specs/SKILL.md) | Derive necessary requirements and maintain the working spec and decision history. |
| [writing-plans](skills/writing-plans/SKILL.md) | Connect requirements to purposeful tasks and verification. |
| [executing-plans](skills/executing-plans/SKILL.md) | Execute a plan while reconciling requirements, decisions, and evidence. |
| [subagent-driven-development](skills/subagent-driven-development/SKILL.md) | Execute tasks with implementer and review agents. |
| [dispatching-parallel-agents](skills/dispatching-parallel-agents/SKILL.md) | Investigate independent problems concurrently. |
| [systematic-debugging](skills/systematic-debugging/SKILL.md) | Diagnose observed failures and verify supported corrections. |
| [test-driven-development](skills/test-driven-development/SKILL.md) | Choose useful tests and verification for behavior changes and refactoring. |
| [requesting-code-review](skills/requesting-code-review/SKILL.md) | Request review against requirements and code changes. |
| [receiving-code-review](skills/receiving-code-review/SKILL.md) | Evaluate feedback before changing code. |
| [verification-before-completion](skills/verification-before-completion/SKILL.md) | Verify results before claiming completion. |
| [writing-agent-handoffs](skills/writing-agent-handoffs/SKILL.md) | Transfer responsibility or document assignments and their results. |
| [generalizing-diffs](skills/generalizing-diffs/SKILL.md) | Ground changed code and prose in actual requirements and semantics. |
| [managing-compatibility](skills/managing-compatibility/SKILL.md) | Align changed interfaces and required data, and assess release or upgrade readiness. |
| [writing-skills](skills/writing-skills/SKILL.md) | Develop and validate reusable skills. |

## Working Files

Each responsible skill defines its own artifacts and retention;
[using-kryptonite](skills/using-kryptonite/SKILL.md) connects the stages.
Project settings and existing governing workflows take precedence. Working
specs default to `.kryptonite/scratchpad/<work-id>/spec.md`, plans sit beside
them, agent communication defaults to `.kryptonite/work/<work-id>/`, and SDD
preserves its `.kryptonite/sdd/<plan-basename>/` helper contract.

See [developing-with-specs](skills/developing-with-specs/SKILL.md) for spec and
durable-document placement, and the
[agent record conventions](skills/writing-agent-handoffs/references/roles.md)
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
