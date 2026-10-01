---
kind: report
report_id: "{{report_id}}"
request_id: "{{request_id}}"
brief_path: "{{brief_path}}"
brief_revision: "{{brief_revision}}"
work_id: "{{work_id}}"
task_id: "{{task_id}}"
original_requester_agent: "{{original_requester_agent}}"
author_agent: "{{author_agent}}"
author_role: "{{author_role}}"
recipient_agent: "{{current_owner_agent}}"
recipient_role: "{{current_owner_role}}"
owner_agent: "{{current_owner_agent}}"
recorded_by: "{{recorded_by}}"
recorded_at: "{{recorded_at}}"
ownership: retained
ownership_record: "{{ownership_record}}"
status: "{{report_status}}"
---

<!--
Authoring instructions: Read ../references/roles.md in the template package.
Use its role and status values. Preserve the actual author's identity when a
different agent records this report. Resolve the recipient from the current
ownership record. Remove this comment before publishing. Remove the review
section for a non-review report.
-->

# Report: {{title}}

## Result and Responsibility

{{author_agent}} returns {{result_summary}} for request {{request_id}}, brief
revision {{brief_revision}}, to the current owner {{current_owner_agent}}.
Responsibility remains with that owner. This report is a result claim or
request for input; it is neither an ownership transfer nor an owner acceptance.

- Assigned goal and understood scope: {{assigned_goal_and_understood_scope}}
- Work actually performed: {{work_actually_performed}}
- Current status and reason: {{report_status}} — {{status_reason}}
- Exact input or decision needed, if any: {{needed_input_or_decision}}

## Artifacts and Target State

- Workspace and environment: {{workspace_and_environment}}
- Result revision or snapshot: {{result_revision_or_snapshot}}
- Uncommitted changes, if any: {{uncommitted_changes}}

| Artifact | Location or reference | Produced, changed, or inspected | Relevant result |
| --- | --- | --- | --- |
| {{artifact}} | {{artifact_location}} | {{artifact_activity}} | {{artifact_result}} |

## Completion Criteria and Evidence

Use the criterion IDs from the brief. Mark each criterion `MET`, `NOT_MET`, or
`NOT_VERIFIED`; a description of an intended check is not evidence that it ran.

| Criterion ID | Outcome | Observation or evidence reference | Checked revision or snapshot |
| --- | --- | --- | --- |
| {{criterion_id}} | {{criterion_outcome}} | {{criterion_evidence}} | {{criterion_evidence_revision}} |

| Check or investigation performed | Environment and target | Actual result | Log or source reference |
| --- | --- | --- | --- |
| {{check_or_investigation}} | {{check_environment_and_target}} | {{actual_check_result}} | {{check_log_or_source}} |

- Verification gaps and limits on the result: {{verification_gaps_and_limits}}

## Decisions, Deviations, and Prior Attempts

| Decision or deviation | Source, evidence, or rationale | Effect on scope or result |
| --- | --- | --- |
| {{decision_or_deviation}} | {{decision_basis}} | {{decision_effect}} |

| Material failed or abandoned attempt | Observed result | What a later agent should retain |
| --- | --- | --- |
| {{prior_attempt}} | {{attempt_result}} | {{continuation_relevant_information}} |

- Unverified assumptions or open questions: {{assumptions_and_open_questions}}

## Review Findings (Conditional)

- Review scope and target: {{review_scope_and_target}}
- Spec compliance verdict and evidence: {{spec_compliance_verdict_and_evidence}}
- Quality verdict and evidence: {{quality_verdict_and_evidence}}

| Finding ID | Severity under the brief's rules | Location and evidence | Criterion or consequence | Recommended action |
| --- | --- | --- | --- | --- |
| {{finding_id}} | {{finding_severity}} | {{finding_location_and_evidence}} | {{finding_criterion_or_consequence}} | {{recommended_action}} |

- Earlier findings addressed, still open, or not rechecked: {{earlier_finding_dispositions}}
- Limits of the review: {{review_limits}}

## Remaining Work and Owner Action

| Remaining item or blocker | Evidence or dependency | Proposed next actor and action |
| --- | --- | --- |
| {{remaining_item}} | {{remaining_item_evidence_or_dependency}} | {{proposed_next_actor_and_action}} |

- Next decision or action requested from {{current_owner_agent}}: {{requested_owner_action}}

Proposed next actors are recommendations. This report does not assign new
work, change ownership, or grant additional authority.
