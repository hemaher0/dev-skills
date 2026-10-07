# Codex Tools and Workspace Context

Read this reference when skill execution depends on command execution outside
the sandbox, the current delegation tools, Git workspace, or environment
restrictions.

## Available Tools

Inspect the tools and instructions exposed by the current harness. Use agent
delegation when it serves the task, the relevant workflow calls for it, and
the current instructions and authorization permit it. Tool availability alone
does not authorize parallel work.

When `dispatching-parallel-agents` appears in the current host's
available-skills list, use it for independent concurrent tasks. When
`subagent-driven-development` is host-listed, use it for its sequential
implementation and review workflow. Otherwise use the host's ordinary agent
tools with explicit scopes, separate write surfaces, recorded requester/owner
and assignee identities, expected evidence, and controller-reviewed results;
execute coupled tasks sequentially. Do not infer availability from files in a
vendor checkout or plugin cache. If a required host capability is absent,
report the limitation and choose a supported way to carry out the authorized
work.

Configuration changes and plugin installation require their own task scope.
Do not treat loading a skill as a request to change user configuration.

## Inspect the Git Workspace

When the task involves Git workspace or integration decisions, use read-only
inspection to identify the repository and its current state:

```bash
git rev-parse --show-toplevel
git rev-parse --git-dir
git rev-parse --git-common-dir
git branch --show-current
git worktree list --porcelain
```

Interpret the paths and worktree metadata together; do not classify a submodule
or other separate Git directory as a linked worktree from one path comparison.
An empty branch name indicates detached HEAD. It does not establish which
branch, commit, push, or pull-request operations the environment permits.

Follow the project's Git workspace and finishing procedures, or compatible
available Git skills, for workspace suitability and an authorized integration
or handoff. Use ordinary Git or host tools when no specialized workflow is
available. Respect ownership of an externally managed workspace and the host's
instructions.

Use this skill's [stage routing](../SKILL.md). If `developing-with-specs` or
`writing-agent-handoffs` is host-listed, use it for the working spec or agent
records respectively. Otherwise keep requirements, decisions, criteria, and
evidence in the project's current work record, and record each assignment's
requester/current owner, assignee/author, scope, target, result, gaps, and next
owner action. Distinguish assigned code checkouts from the work owner's shared
spec and reporting paths.

## Restricted or Managed Operations

Check actual permissions and operation results separately from branch state.
When an operation is blocked, report its cause and use the harness's approval
or handoff mechanism when applicable. Do not substitute another unauthorized
mutation for the blocked action.

Do not use heredocs in shell commands submitted for execution outside the
sandbox. Use supported structured arguments or file-editing tools for
multiline content. This rule applies to submitted command syntax; sandboxed
commands and literal heredoc text in files or documentation remain allowed.

Prepare reviewable changes and relevant verification evidence within the
authorized scope. Stage, commit, push, or transfer work only as authorized by
the user's task and the applicable Git workflow. Keep unrelated work outside
the candidate. Use host-provided controls when the host owns the operation;
describe only controls available in the current environment.
