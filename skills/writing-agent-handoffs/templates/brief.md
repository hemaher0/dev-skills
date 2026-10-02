---
kind: brief
request_id: "{{request_id}}"
brief_revision: "{{brief_revision}}"
work_id: "{{work_id}}"
task_id: "{{task_id}}"
requester_agent: "{{requester_agent}}"
requester_role: "{{requester_role}}"
assignee_agent: "{{assignee_agent}}"
assignee_role: "{{assignee_role}}"
owner_agent: "{{requester_agent}}"
recorded_by: "{{recorded_by}}"
recorded_at: "{{recorded_at}}"
ownership: retained
work_root: "{{work_root}}"
ownership_record: "{{ownership_record}}"
reply_to: "{{reply_destination}}"
---

<!--
Authoring instructions: Read ../references/roles.md in the template package.
Use its predefined role values and placeholder conventions. Identify the
expected report destination and exact brief revision. Keep purpose, scope,
authority, completion criteria and return routing. Omit irrelevant metadata,
bullets, tables and sections; concise prose is sufficient for a small task.
Remove this comment before publishing and the review section for non-review work.
-->

# Brief: {{title}}

## Responsibility and Assignment

{{requester_agent}} retains responsibility for {{owned_work_scope}} and asks
{{assignee_agent}} to perform {{assigned_activity}} as {{assignee_role}}.
Return results or a blocker through a report for request {{request_id}}, brief
revision {{brief_revision}}. This assignment does not transfer ownership.
If a separate handoff changes the owner, follow the recorded successor and
reply destination while preserving this request's identity.

## Goal and Scope

- Original request or authoritative source: {{original_request_or_source}}
- Requested outcome: {{requested_outcome}}
- Included work: {{included_work}}
- Excluded work: {{excluded_work}}
- Governing spec, plan, or decisions: {{governing_references}}
- Constraints and interfaces with other work: {{constraints_and_interfaces}}

## Inputs and Authority

- Workspace and relevant artifact paths: {{workspace_and_artifact_paths}}
- Assigned revision or snapshot: {{assigned_revision_or_snapshot}}
- Required inputs and dependencies: {{required_inputs_and_dependencies}}
- Existing authority source: {{authority_source}}
- Permitted write surfaces or read-only boundary: {{permitted_surfaces}}
- Decisions the assignee can make within this scope: {{permitted_decisions}}
- Unresolved assumptions or questions: {{assumptions_and_questions}}
- Stop or request clarification when: {{stop_or_clarification_conditions}}

## Completion Criteria

Use observable criteria. Identify the evidence needed to establish each one.

| Criterion ID | Required behavior or result | Expected evidence |
| --- | --- | --- |
| {{criterion_id}} | {{required_result}} | {{expected_evidence}} |

## Expected Report

- Deliverables and their destinations: {{deliverables_and_destinations}}
- Report destination: {{reply_destination}}
- Required verification and its scope: {{required_verification}}
- Role-specific findings or output format: {{role_specific_report_requirements}}
- Work that depends on this result: {{dependent_work}}

Use `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, or `BLOCKED`. Include actual
artifacts, criterion outcomes, evidence versions, and unresolved work. For a
blocker or missing context, identify the exact input or decision needed from
the current owner instead of claiming completion.

## Review Assignment (Conditional)

- Review mode: {{task_review_or_final_review_or_other}}
- Producer whose work is being reviewed: {{producer_agent}}
- Baseline and target revisions or snapshots: {{review_base_and_target}}
- Brief, producer report, and review package: {{review_input_references}}
- Required spec compliance and quality verdicts: {{required_review_verdicts}}
- Review scope, severity definitions, and blocking criteria: {{review_scope_and_severity_rules}}

The reviewer is distinct from the producer. Review the assigned artifacts
without modifying them. Return the report through the permitted reporting
surface or an authorized recorder; do not turn the review into implementation.
