---
name: writing-agent-handoffs
description: Use when transferring responsibility for work between agents, or documenting assignments and their results while the requesting agent retains responsibility.
---

# Writing Agent Handoffs

Document the responsibility being transferred or retained, the work's purpose,
and the evidence another agent needs to act. The same rules apply to peer
agents and subagents, within one session or across sessions. These documents
record existing authority; they do not grant permission to delegate, edit,
commit, or perform external actions.

## Choose the Document

| Document | Purpose | Responsibility | Expected response |
| --- | --- | --- | --- |
| [Handoff](templates/handoff.md) | Transfer continuation of a named work scope to the next agent. | Moves from sender to recipient. | No acknowledgement, acceptance, or return report required. |
| [Brief](templates/brief.md) | Request a bounded activity and define its expected result. | Remains with the requesting agent. | Results, missing context, or a blocker through a report. |
| [Report](templates/report.md) | Return the outcome and evidence for a specific brief revision. | Remains with the current owner. | The owner evaluates the result and handles remaining work. |

A report does not become a handoff because it contains enough context to
continue. Use a separate handoff when responsibility actually moves. Reference
existing briefs and reports in that handoff to preserve their context; the
handoff records the transfer.

Read [roles and template conventions](references/roles.md) when preparing or
interpreting these documents. It defines the role vocabulary, identities,
status values, placeholder rules, and document locations. Reuse existing
equivalent records rather than creating duplicate copies merely for formatting.

## Identify the Work and Participants

Reuse the work and task IDs, agent identities, and ownership record already
established by the project or host. Include the plan reference when a task ID
is only unique within that plan. Preserve work and task identity when agents
change; retain authorship of their earlier contributions.

Distinguish the requester, assignee, current owner, author, and recorder in the
record; the same agent can fill multiple fields. The assignee performs the
requested activity; that assignment alone does not make the assignee the owner.
A role describes an activity, not an identity, supervisor relationship, or
permission grant.

Use a recorded local identity when the host supplies none, with its source
and work scope explicit. Do not present a local identity as host-issued or
invent a missing binding. Resolve a missing recipient or scope before recording
a transfer. Mark other unavailable facts as unknown and identify any missing
information that prevents dependent work.

## Delegate Through a Brief and Report

Prepare the [brief](templates/brief.md) before the delegated activity. Record
the requesting owner and assignee, original intent, bounded scope, governing
spec or plan and revision, dependencies, permitted surfaces, completion
criteria, and expected report destination. Distinguish explicit requirements,
derived necessities, selected means, and unresolved assumptions using the
governing spec rather than creating another specification.

Correlate the brief and its reports with `request_id` and `brief_revision`.
For material instruction changes, record a new brief revision and preserve
the earlier basis. Give each report a distinct `report_id`; preserve prior
reports and their actual authors, including when an authorized recorder writes
returned content on their behalf.

The assignee returns a [report](templates/report.md) with actual work, artifact
paths and revisions, criterion outcomes, verification evidence, deviations,
and remaining work. Use `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, or
`BLOCKED` according to the reference. Report missing inputs or blockers before
work that depends on resolving them. Intended checks are not executed evidence.

The current owner checks the report against the brief and actual artifacts,
resolves discrepancies, and decides the next action. Reporting completion is
a claim, not proof of completion or a transfer of responsibility. Preserve
meaningful uncertainty and verify combined outcomes under the owning workflow.

For development work, the current owner reconciles proposed decisions and
evidence into the shared working spec with
[developing-with-specs](../developing-with-specs/SKILL.md). Assignees return
proposals in their reports rather than independently overwriting that spec.

## Transfer Responsibility Through a Handoff

Use one [handoff](templates/handoff.md) per transfer. Identify the sender,
recipient, transferred scope, existing authority, governing references,
current state, actual workspace and revision, material uncommitted changes,
and evidence. Carry forward important decisions, unsuccessful prior attempts,
verification gaps, blockers, outstanding requests, and a concrete first action.

Recording the completed handoff and making it available to the named recipient
completes the transfer. The sender stops work within the transferred scope.
No acknowledgement, acceptance, or result report to the sender is required.
Responsibility for any scope outside the transfer remains as previously recorded.

Update the existing ownership record, or use the handoff itself when no
separate record exists. The recipient checks the transferred state and relevant
artifact revisions before dependent work and continues within the existing
authority; this check is not an acceptance gate for the transfer.

If requests remain in flight, retain their request IDs, original requester
attribution, briefs, and revisions. Include their assignees, latest reports,
open findings, and needed decisions in the handoff. Route later reports to
the successor owner using the updated reply destination; preserve the original
brief and record the destination change in the ownership record or handoff.

## Use Briefs and Reports for Code Review

Use [requesting-code-review](../requesting-code-review/SKILL.md) when the owning
workflow calls for code review. Carry its review scope and output requirements
in the brief's conditional review section: governing requirements and revision,
producer, baseline and target, producer report, available evidence, and
severity and blocking criteria. For a multi-commit change, use the recorded
start and end of the assigned work so the range covers the entire change.

The independent reviewer is distinct from the producer and inspects the
assigned artifacts without modifying them. Return the review report through
the permitted reporting surface, or through an authorized recorder when the
reviewer cannot write there. Preserve the reviewer as the author.

Use the report's conditional review section to record the applicable verdicts,
findings with IDs, severity, locations and evidence, and verification limits.
Include the review workflow's detailed output in that report or reference its
existing artifact. Completing a review assignment does not mean the reviewed
implementation passed; state both the report status and review verdicts.

Evaluate feedback with
[receiving-code-review](../receiving-code-review/SKILL.md) before implementing
suggestions. The current owner retains responsibility for disposition and
resolution. A delegated fix uses a brief linked to the findings and a report
with the changes and covering evidence. The owning development workflow
determines review timing, re-review, and completion gates.

## Keep Records Available and Finalize

Follow project settings and existing workflow paths first, including existing
SDD helper-script destinations. The fallback location is
`.kryptonite/work/<work-id>/`, with `briefs/`, `reports/`, and `handoffs/` as
defined in the reference. Reuse the existing progress or ownership record;
do not introduce a second registry or move existing artifacts for this layout.

Give independent writers separate record paths and one writer or appropriate
isolation for shared artifacts. The current owner consolidates shared state.
Follow configured child work-item links and document schemas where available,
and keep private context within its authorized audience. Check identities and
revisions before acting on delayed or repeated documents; re-delivery does not
create another assignment or ownership transfer. A durable child work item
retains task history and links these records; its parent relation does not
replace a brief/report or establish a handoff. An authorized recorder may append
an assignee's events without changing their authorship or granting write access.

Keep records needed by outstanding requests, unresolved findings, remaining
work, or the next owner. Sending a handoff or report does not itself trigger
cleanup. Dispose of only completed communication records within existing
authority after their necessary decisions, evidence, and continuation state
are preserved and project retention permits it. Preserve other active work.

For development finalization, use
[developing-with-specs](../developing-with-specs/SKILL.md) to preserve the applied
requirements and evidence in durable documentation. Pending required stages
still need their records. This skill owns communication and transfer semantics,
not a separate commit or generalization schedule.
