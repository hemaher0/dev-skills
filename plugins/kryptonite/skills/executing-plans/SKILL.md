---
name: executing-plans
description: Use when carrying out an authorized written multi-step implementation plan, including continuation after an agent handoff.
---

# Executing Plans

Execute the plan against its purposes and governing requirements. Keep the
working spec, decisions, and verification aligned as implementation reveals
new facts. This workflow supports direct execution in the current session or
continuation by a successor; available subagent tools do not force a switch.

## Establish the Current Work

Read the plan and its referenced spec, revision, applicable project rules,
relevant files, and progress record. If `developing-with-specs` appears in the
current host's available-skills list, use it throughout execution. Otherwise
maintain the current project spec or work record directly: preserve the goal,
requirements and sources, consequential decisions and rationale, assumptions,
acceptance criteria, evidence, and material history. Do not infer availability
from a sibling vendor or cache folder. If resuming a handoff, establish the
transferred scope and current ownership; no response or acknowledgement to the
previous owner is required.

For Git work, follow the project's Git workspace procedure or a compatible
available Git skill to decide whether the existing workspace is suitable under
project policy and actual authorization. Inspect its branch and local changes;
do not overwrite unrelated work or infer permission for staging, commits,
or integration from the plan.
An ongoing user-approved checkout need not be replaced solely to run this skill.

Check plan/spec revision alignment, dependencies, critical gaps, and the
observable completion criteria. Resolve supported issues within existing
authority. When a consequential answer or authorization is unavailable, identify
the exact decision and pause dependent work while continuing independent work.
At each consequential choice's needed-by point, check its purpose, applicable
evidence or tradeoff, unresolved premises, consequence of error, and required
validation. A plan or execution request does not validate its unresolved
premises; obtain applicable evidence within the authorized scope before later
tasks rely on them.

## Execute by Purpose

For each task:

1. Confirm which requirement and result it serves, its inputs, boundaries, and
   completion criteria. Reuse the active progress record rather than creating
   a second ledger; recognize completed work by its applicable evidence.
2. Perform the planned work within its contracts. Before a consequential choice
   not already determined by the spec, record its purpose, basis, and effects.
   Use implementation judgment for mechanical details the plan leaves open.
3. If new facts change a requirement or strategy, reconcile the spec, plan,
   affected checks, and stale evidence before dependent work. Preserve the
   previous reasoning and distinguish a justified refinement from a change to
   the user's goal requiring their decision.
4. Run the task's covering verification and inspect the actual result. For an
   unexpected failure, use `systematic-debugging` when it is host-listed.
   Otherwise reproduce or inspect the observation, compare it with the expected
   behavior, test a causal hypothesis, make the supported correction, and
   recheck the original symptom and relevant regressions. A failed test is
   evidence to investigate, not an automatic reason to ask the user or weaken
   its criterion.
5. Record artifacts, decisions, and results; mark completion only when evidence
   covers the task's criteria. Report gaps explicitly and continue dependent
   tasks only when their prerequisites are satisfied.

Follow actual project review gates and the user's instructions. Do not pause
between tasks to request permission already covering the work. Stop dependent
execution when a governing requirement is contradictory, a material question
cannot be resolved, required authority is missing, or an obstacle cannot be
corrected within scope. State what was tried and what would unblock it.

For a delegated activity, use the existing brief/report records: the requesting
owner retains responsibility and evaluates returned evidence. For a full
ownership transfer, use the project's transfer record or the installed
`writing-agent-handoffs` template when that skill is host-listed. Without
either, record sender, successor, transferred scope, authority, spec/plan
revisions, current state, remaining work, outstanding requests, evidence gaps,
and the first continuation action. Do not treat a report as an ownership
transfer or demand a reply to a handoff.

## Verify and Complete

If `verification-before-completion` is host-listed, use it to compare delivered
artifacts with the current spec and original intent. Otherwise perform that
comparison directly: inspect the actual target, run checks that cover each
material criterion and the user's observable outcome, and record revisions,
results, limitations, and unresolved mismatches. Passing component tests alone
may not cover the result.

For final durable documentation and spec retention, use
`developing-with-specs` when host-listed; otherwise update the project's existing
durable document with the applied requirements, decisions, artifacts, and
evidence. For communication records, use `writing-agent-handoffs` when
host-listed; otherwise preserve request/owner/author identity, scope, target,
evidence, gaps, and retention state in the existing progress record. Route
requested commit preparation through `using-kryptonite` when host-listed, or
through the project's Git review procedure with ordinary Git inspection. This
skill owns plan execution and progress; reuse the same spec and progress paths.

Present reviewable durable references and scoped results; while temporary
records remain, identify the applied spec and its history. Preserve records for
pending stages and remaining work. Implementation completion does not itself
request a commit, authorize publication, or make ongoing records disposable.
