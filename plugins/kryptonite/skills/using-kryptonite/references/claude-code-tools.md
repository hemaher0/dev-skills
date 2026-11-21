# Claude Code Tools and Workspace Context

Read this reference when skill execution depends on delegation, long-running
commands, permission prompts, the Git workspace, or other environment
restrictions in Claude Code.

## Available Tools

Inspect the tools and instructions exposed by the current session. The tool set
depends on the Claude Code surface, its settings, and the session's permission
mode. Tools that are only listed by name must be loaded before use when the host
says so.

A skill is available when it appears in the session's skill list. Claude Code
discovers project skills under `.claude/skills/<name>/SKILL.md`, personal skills
under `~/.claude/skills/<name>/SKILL.md`, and plugin skills as
`<plugin>:<name>`. Invoke a listed skill through the host's skill tool or as
`/<name>`. A folder under `.agents/`, a vendor checkout, or a plugin cache does
not make a skill available in Claude Code.

Use agent delegation when it serves the task, the relevant workflow calls for
it, and the current instructions and authorization permit it. Tool availability
alone does not authorize parallel work, and user or project instructions can
restrict when agents may be started. When `dispatching-parallel-agents` is
host-listed, use it for independent concurrent tasks. When
`subagent-driven-development` is host-listed, use it for its sequential
implementation and review workflow. Otherwise use the host's agent tool with
explicit scopes, separate write surfaces, recorded requester/owner and assignee
identities, expected evidence, and controller-reviewed results; execute coupled
tasks sequentially. A delegated agent starts without this conversation unless
the host forks it, so give it the facts it needs. Treat its report as evidence
to check, not as completed verification or as the user's approval.

When the host provides a task-tracking tool, track the current steps with it
as the host's instructions describe. Run a command that must keep running, or
that may outlast the shell tool's timeout, with the shell tool's background
option rather than `&` or `nohup`, and read its output when the host reports
completion instead of polling.

Configuration changes, hooks, permission rules, and plugin installation require
their own task scope. Do not treat loading a skill as a request to change user
or project configuration.

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
An empty branch name indicates detached HEAD. A session can start inside a
worktree that the host created; treat that worktree and its branch as
host-managed and follow the host's controls for keeping, handing off, or
removing it. Branch state does not establish which commit, push, or
pull-request operations the environment permits.

Follow the project's Git workspace and finishing procedures, or compatible
available Git skills, for workspace suitability and an authorized integration
or handoff. Use ordinary Git or host tools when no specialized workflow is
available.

Use this skill's [stage routing](../SKILL.md). If `developing-with-specs` or
`writing-agent-handoffs` is host-listed, use it for the working spec or agent
records respectively. Otherwise keep requirements, decisions, criteria, and
evidence in the project's current work record, and record each assignment's
requester/current owner, assignee/author, scope, target, result, gaps, and next
owner action.

## Restricted or Managed Operations

Claude Code asks for permission according to the session's permission mode and
rules. A declined or blocked tool call means the user or a rule refused that
action: adjust the approach, do not repeat the same call, and do not reach the
same effect through another tool or command. Output from hooks is feedback from
the user's configuration. Commands can also run in a sandbox; report a blocked
operation and its cause, and use the host's approval route when one applies.

Prepare reviewable changes and relevant verification evidence within the
authorized scope. Stage, commit, push, or transfer work only as authorized by
the user's task and the applicable Git workflow. Keep unrelated work outside
the candidate. Use host-provided controls when the host owns the operation;
describe only controls available in the current environment.
