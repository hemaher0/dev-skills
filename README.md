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

## Skills

| Skill | Purpose |
| --- | --- |
| [using-kryptonite](skills/using-kryptonite/SKILL.md) | Discover and invoke relevant skills. |
| [brainstorming](skills/brainstorming/SKILL.md) | Refine requirements and produce an approved design. |
| [using-git-worktrees](skills/using-git-worktrees/SKILL.md) | Create or verify an isolated Git workspace. |
| [writing-plans](skills/writing-plans/SKILL.md) | Write implementation tasks with verification steps. |
| [executing-plans](skills/executing-plans/SKILL.md) | Execute an implementation plan. |
| [subagent-driven-development](skills/subagent-driven-development/SKILL.md) | Execute tasks with implementer and review agents. |
| [dispatching-parallel-agents](skills/dispatching-parallel-agents/SKILL.md) | Investigate independent problems concurrently. |
| [systematic-debugging](skills/systematic-debugging/SKILL.md) | Investigate failures before applying a fix. |
| [test-driven-development](skills/test-driven-development/SKILL.md) | Apply RED-GREEN-REFACTOR to implementation. |
| [requesting-code-review](skills/requesting-code-review/SKILL.md) | Request review against requirements and code changes. |
| [receiving-code-review](skills/receiving-code-review/SKILL.md) | Evaluate feedback before changing code. |
| [verification-before-completion](skills/verification-before-completion/SKILL.md) | Verify results before claiming completion. |
| [finishing-a-development-branch](skills/finishing-a-development-branch/SKILL.md) | Complete the selected branch integration outcome. |
| [writing-skills](skills/writing-skills/SKILL.md) | Develop and validate reusable skills. |

## Working Files

Runtime data uses `.kryptonite/sdd/` and `.kryptonite/brainstorm/`.
Design and plan defaults are `docs/superpowers/specs/` and
`docs/superpowers/plans/`.

## License

[MIT License](LICENSE). Original copyright and attribution are retained.
