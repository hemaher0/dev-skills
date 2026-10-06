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

Keep the marketplace and enablement in the target project using the files
below. Write these project files directly: `codex plugin marketplace add` and
`codex plugin add` save user-level configuration in `~/.codex/config.toml`;
running them from a project directory does not make them project-scoped.
The plugin browser also saves user-level enablement choices.
Neither route is a step in this project-only procedure.

For a first local-source setup, run from the target project's root; reuse an
existing suitable source checkout:

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
this example. Complete the project settings below, then open the project as
trusted and start a new Codex session; restart the desktop app when needed.
Codex uses the project configuration during local marketplace discovery and
refresh. Verify that the plugin's skills are available in that project session.
Project configuration is loaded only for trusted projects.

Codex may keep plugin files in its shared `~/.codex/plugins/cache/`; that cache
location does not determine enablement scope. Existing user-level enablement
remains a separate setting; adding project settings does not remove it.
See the [official project plugin configuration guide](https://developers.openai.com/plugins/build/plugins#enable-or-disable-a-plugin-for-a-repo).

### Project settings

Writing root `AGENTS.local.md` is a required installation step.

1. Read existing project instructions and the
   [local development template](skills/developing-with-specs/templates/AGENTS.local.md).
   Create the file from that template, or merge its development section into
   the existing file. Preserve established settings and other packages' sections.
2. Replace applicable placeholders with actual values. Fill `Scratchpad root`
   with the established project path, or `.kryptonite/scratchpad/` when using
   the documented default. If an existing authoritative configuration already
   owns that value, fill its actual source path instead of duplicating it.
   Resolve relative paths from the project root.
   Remove fields that do not apply.
3. Keep shared project policy in its existing home and reusable workflow rules
   in their skills. Where settings are already maintained elsewhere, reference
   their actual source and verify its contents. The workflow entrypoint is
   [using-kryptonite](skills/using-kryptonite/SKILL.md); scratchpad and spec rules
   are in [developing-with-specs](skills/developing-with-specs/SKILL.md).
4. Connect the local file to root instructions using the procedure below.

If root `AGENTS.md` exists, preserve it and add this instruction unless it
already reads or resolves to the local file:

```markdown
Read and follow root AGENTS.local.md when it exists.
```

If `AGENTS.md` is absent, the recommended connection is a relative symbolic
link from the project root, after writing `AGENTS.local.md`:

```bash
ln -s AGENTS.local.md AGENTS.md
```

Preserve existing files and links and avoid self-references. If
`AGENTS.override.md` takes precedence, ensure it reads the local file.

Before completing installation, read the completed file and any referenced
configuration. Verify that applicable values are filled, no placeholders
remain, the scratchpad path resolves, and effective instructions read the local
file. A generic "use defaults" statement does not replace filled settings.
Check marketplace paths/name and skill availability in a new session.

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
uses `.kryptonite/sdd/<plan-id>/`, with identity derived from the plan path.
Existing pending SDD records are reconciled before reuse or explicit migration.

[Developing with specs](skills/developing-with-specs/SKILL.md#ground-consequential-choices)
connects consequential choices to their purpose, applicable evidence, unresolved
premises, and checks before dependent work. Evidence effort follows impact,
uncertainty, and reversibility. A default, plan, or successful execution does not
establish suitability or turn an agent's selection into a user requirement.
Domain suitability and software correctness use their respective evidence.

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
