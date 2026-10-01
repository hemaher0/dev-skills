---
name: writing-agent-handoffs
description: Use when preparing documented assignments or requesting and consolidating handoff documents from parallel agents, including ownership, evidence, and remaining work.
---

# Writing Agent Handoffs

Make a task understandable to the next owner without relying on inherited
conversation context. Distinguish the assigned work, the agent's interpretation,
and the actual outcome. A handoff documents authority already granted; it does
not authorize delegation, edits, commits, or external actions.

## Identify Participants and Tasks

Use the owning document's fields to distinguish these identities:

- **Run ID:** The execution scope. Reuse the host's run/session ID or the
  project's execution ID. If neither exists, the coordinator creates one
  unique ID using the project's allocator or a UUID and records it once.
- **Task ID:** The work being assigned. Reuse the authoritative work-item or
  plan task ID. Retain the plan reference when task numbers are only unique
  within a plan. Task identity persists when the assignee changes.
- **Owner ID:** The actual assignee. Use the agent ID returned by the host.
  If the host provides no ID, the coordinator allocates a local ID such as
  `worker-01` and records it together with the run ID. Only the coordinator
  allocates these local IDs; check existing assignments to avoid duplicates.
- **Role:** The participant's responsibility, such as implementation, review,
  or coordination. Record the role alongside the owner ID; a role name alone
  does not identify a participant.

Record the ID sources and bindings in the existing assignment or handoff record,
including the coordinator and intended recipient. Treat `(run ID, owner ID)`
as the ownership reference. A local fallback ID is not a host-issued ID. If a
host ID becomes available only after dispatch, mark the assignment as awaiting
that binding and record the returned ID when it is available; do not invent it.

Reuse recorded run IDs and owner bindings when resuming the same execution.
Allocate a fresh local owner ID for a replacement agent and do not recycle the
previous ID within that run. On transfer, preserve the task ID and record the
previous owner, new owner, and transfer time or development stage. Keep previous
contributions attributed to their actual authors. Old records with unknown
identities stay explicitly unknown unless evidence establishes the binding.

## Prepare the Assignment

The coordinator identifies the authoritative request and applicable spec or
plan, then gives each worker a documented assignment containing:

- Run and task identities, owner and recipient references, and their roles.
- The original request or its authoritative source, preserving its intent.
- The worker's goal and interpretation, with assumptions distinguished from
  explicit requirements and unresolved decisions identified.
- Included and excluded work, relevant constraints, and acceptance criteria.
- The worker's responsibilities, permitted write surfaces, dependencies,
  interfaces with other tasks, and the owner of shared integration.
- Relevant inputs, the assigned workspace or revision when applicable, and
  the applicable spec reference, expected deliverables, and verification evidence.
- Where to write the return handoff and who receives it.

Use actual task IDs and paths when known. Do not invent repository locations
or permission grants to fill a document. The worker reads the assignment and
reports material misunderstandings or blockers to the coordinator before
dependent work. Reconcile those differences with the authoritative request.

## Request the Return Handoff

Tell each worker at assignment time to produce a handoff before ownership
transfer or completion. An existing report can serve as the handoff if it
contains the needed information. Request a concise return message with the
document path and status so the coordinator can find the full evidence.

The return document records:

- The run, task, and author identities, role, and intended recipient matching
  the recorded assignment, plus any ownership transfer.
- Assigned goal, understood scope, and the work actually completed.
- Changed artifacts and their paths; actual branch and commit or revision
  identifiers when the work uses version control. Identify uncommitted work.
- Decisions and deviations, their sources, evidence and rationale, any
  authorization they needed, and added or revised spec requirements.
- Checks performed, commands and results, and material verification gaps.
- Remaining work, blockers, risks supported by evidence, and the next action
  with its owner and dependencies.

Preserve uncertainty. A worker's completion statement is a claim for the
coordinator to verify against artifacts and evidence.

## Coordinate Parallel Ownership

Assign separate handoff paths for independent workers. Each worker writes only
its assigned document; the coordinator owns consolidation and shared
integration. Give an overlapping artifact one writer or provide isolation
under the project's workflow. Do not let workers overwrite a shared handoff
or commit through a shared document checkout.

Follow the project's document locations, schema, and access rules. When linked
child work items are configured, attach each worker's handoff to its assigned
child and let the coordinator update the parent. Otherwise reuse the existing
report area or state a suitable temporary location; avoid a competing history.
Keep private task context within its authorized audience.

## Accept the Handoff

The coordinator reads each document, verifies its run, task, owner, and role
against the assignment, checks material claims against the actual artifacts,
and reconciles gaps or overlapping assumptions before dependent work. Resolve
an identity mismatch before accepting a handoff under the wrong task or owner.
Record which work was accepted, what remains unresolved, and who owns the
next action. Verify the combined result with checks suited to integration;
individual handoffs alone do not establish that the combined work succeeds.

For development work, use
[developing-with-specs](../developing-with-specs/SKILL.md) to consolidate the
applied working spec and decision history in the task scratchpad. The
coordinator presents that reference and the reasons for changes to the user
at completion; worker-only reports do not establish that the user knows what
spec the delivered work used.
