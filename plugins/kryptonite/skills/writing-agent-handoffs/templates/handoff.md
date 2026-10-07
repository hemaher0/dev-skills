---
kind: handoff
handoff_id: "{{handoff_id}}"
work_id: "{{work_id}}"
task_id: "{{task_id}}"
from_agent: "{{from_agent}}"
from_role: "{{from_role}}"
to_agent: "{{to_agent}}"
to_role: "{{to_role}}"
recorded_by: "{{recorded_by}}"
recorded_at: "{{recorded_at}}"
ownership: transferred
work_root: "{{work_root}}"
ownership_record: "{{ownership_record}}"
---

<!--
Authoring instructions: Read ../references/roles.md in the template package.
Use its predefined role values and placeholder conventions. Keep one document
per transfer. Keep definite sender/successor, transfer scope and authority,
current state, relevant evidence, pending requests and concrete continuation.
Omit irrelevant metadata, bullets, tables and sections. Remove this comment
before publishing the completed handoff.
-->

# Handoff: {{title}}

## Responsibility Transfer

Responsibility for {{transferred_scope}} moves from {{from_agent}} to
{{to_agent}} when this completed handoff is recorded and made available at
{{handoff_path}}. {{from_agent}} stops work in that scope. {{to_agent}} owns
continuation, outstanding requests, and completion within the existing authority.
No acknowledgement, acceptance, or result report to {{from_agent}} is required.

- Reason for transfer: {{transfer_reason}}
- Existing authority and limits: {{authority_source_and_limits}}
- Outstanding reports now go to: {{reply_destination_for_next_owner}}

## Goal and Governing Context

- Original request or authoritative source: {{original_request_or_source}}
- Intended outcome: {{intended_outcome}}
- Applicable spec or plan: {{spec_or_plan_reference}}
- Scope boundaries and constraints: {{scope_boundaries_and_constraints}}
- Completion criteria still governing this work: {{completion_criteria}}

## Current State

- Overall state: {{current_work_state}}
- Workspace and environment needed to continue: {{workspace_and_environment}}
- Current revision or snapshot: {{current_revision_or_snapshot}}
- Uncommitted or incomplete changes: {{uncommitted_or_incomplete_changes}}
- Start by reading: {{essential_context_paths_and_read_order}}

| Completed work | Artifact or location | Evidence | Evidence revision or snapshot |
| --- | --- | --- | --- |
| {{completed_work}} | {{artifact_reference}} | {{supporting_evidence}} | {{evidence_revision_or_snapshot}} |

## Decisions and Uncertainty

| Decision or constraint | Source or rationale | Consequence for continuation |
| --- | --- | --- |
| {{decision_or_constraint}} | {{decision_source_or_rationale}} | {{continuation_consequence}} |

- Unverified assumptions or open questions: {{assumptions_and_open_questions}}
- Verification gaps: {{verification_gaps}}

## Prior Attempts

Include material failed or abandoned attempts that the next agent should know
before repeating work.

| Attempt | Observed result and evidence | Why it stopped | When retrying would make sense |
| --- | --- | --- | --- |
| {{prior_attempt}} | {{attempt_result_and_evidence}} | {{reason_attempt_stopped}} | {{retry_condition}} |

## Outstanding Requests and Dependencies

Retain request IDs and original requester attribution. The next owner handles
pending reports and any decisions needed to unblock their authors.

| Request ID | Brief and revision | Original requester | Assigned agent and role | Current state or latest report | Next owner action |
| --- | --- | --- | --- | --- | --- |
| {{pending_request_id}} | {{pending_brief_reference_and_revision}} | {{original_requester}} | {{pending_assignee_and_role}} | {{pending_request_state_or_report}} | {{next_owner_action_for_request}} |

- Other dependencies or active processes: {{other_dependencies_or_active_processes}}
- Known blockers and what would resolve them: {{blockers_and_resolution_conditions}}

## Continue From Here

- First concrete action for {{to_agent}}: {{first_action}}

| Remaining action | Prerequisite or dependency | Done when |
| --- | --- | --- |
| {{remaining_action}} | {{remaining_action_prerequisite}} | {{remaining_action_completion_condition}} |

- Finalization workflow and durable documentation destination: {{finalization_requirements}}
- Temporary artifacts still needed for continuation: {{temporary_artifacts_to_retain}}
