---
work_id: "{{work_id}}"
revision: "{{spec_revision}}"
owner: "{{owner_agent}}"
stage: "{{development_stage}}"
---

# {{work_title}} Working Spec

<!--
Use the project's format when one exists. Otherwise adapt this template in the
resolved scratchpad root at <work-id>/spec.md, reusing existing work identities.
Replace every {{snake_case}} placeholder; remove authoring comments before
using the record. Repeat relevant rows, and use "none" for an empty section,
"unknown" for an unavailable fact, and "not verified" for an unchecked claim.
Escape quotes and backslashes in YAML values; keep multiline prose in the body.
Escape literal pipe characters in table cells; keep lengthy detail in prose.
Use project-root-relative artifact paths or actual absolute paths, not paths
relative to this template package. Link formal contracts instead of duplicating
them. The current body describes the current spec; preserve material history.
Record purpose before consequential implementation choices, not retrospectively.
Open questions can remain when their impact and resolution point are explicit;
resolve a blocking question before the work depending on its answer.
-->

## Intent and Scope

- Original request and source: {{original_request_and_source}}
- Desired observable result: {{desired_observable_result}}
- Included scope: {{included_scope}}
- Excluded scope: {{excluded_scope}}
- Governing contracts and project constraints: {{governing_sources_and_constraints}}
- Plan and active work records: {{plan_and_work_record_references}}

## Observed Facts

| ID | Fact | Source and applicable revision | Limits or uncertainty |
| --- | --- | --- | --- |
| {{fact_id}} | {{observed_fact}} | {{fact_evidence}} | {{fact_limits}} |

## Requirements and Acceptance

<!--
Origin: requested, governing, or derived. A derived requirement identifies its
parent requirement or governing constraint and the evidence for its necessity.
Status distinguishes a proposal from an established requirement. Describe the
needed outcome here; put a chosen means in Decisions unless a source mandates it.
-->

| ID | Origin | Required outcome or constraint | Source or parent IDs | Necessity and basis | Acceptance criterion and verification method | Status |
| --- | --- | --- | --- | --- | --- | --- |
| {{requirement_id}} | {{requirement_origin}} | {{required_outcome}} | {{requirement_sources_and_parents}} | {{requirement_necessity_and_basis}} | {{observable_criterion_and_method}} | {{requirement_status}} |

## Decisions

<!--
Connect the basis to the current goal and conditions, including for defaults
and inherited choices. Scale checks to impact, uncertainty, and reversibility.
Link unresolved premises to Assumptions and Open Questions and identify the
needed-by point in Check. Selection, recording, and execution do not establish
that a choice is suitable or turn it into a requested requirement.
-->

| ID | Purpose and requirement IDs | Selected means | Basis and actual alternatives | Consequences and affected artifacts | Check | Status |
| --- | --- | --- | --- | --- | --- | --- |
| {{decision_id}} | {{decision_purpose_and_requirements}} | {{selected_solution}} | {{decision_basis_and_alternatives}} | {{decision_consequences}} | {{decision_check}} | {{decision_status}} |

## Assumptions and Open Questions

| ID | Unverified premise or question | Impact and dependent work | Resolution method, responsible agent, and needed-by point | State |
| --- | --- | --- | --- | --- |
| {{question_id}} | {{unverified_premise_or_question}} | {{question_impact_and_dependencies}} | {{question_resolution}} | {{question_state}} |

## Verification Evidence

<!--
Check the original outcome as well as derived conditions. Result: MET, NOT_MET,
or NOT_VERIFIED. Name the actual artifact snapshot and spec revision checked.
A passing implementation test does not by itself establish that the requirement
was the right one. Preserve evidence references before temporary files expire.
Keep implementation correctness, suitability of the chosen means, and the
requested outcome distinct; each claim needs evidence covering its assumptions.
-->

| Requirement or decision IDs | Check and expected observation | Actual evidence | Spec revision and artifact snapshot | Result | Limits or next action |
| --- | --- | --- | --- | --- | --- |
| {{verified_ids}} | {{check_and_expected_observation}} | {{actual_evidence}} | {{checked_revisions}} | {{verification_result}} | {{verification_limits_or_next_action}} |

## Decision and Change History

<!--
Append material changes with actual actor and stage or known time. Preserve
superseded reasoning. If recording late, say so; do not invent earlier approval
or timestamps. Identify affected plans, checks, and evidence requiring renewal.
-->

| Event | Actor and stage or known time | Previous expectation or decision | Change and purpose | Reason and source | Affected requirements, artifacts, and evidence |
| --- | --- | --- | --- | --- | --- |
| {{history_event_id}} | {{history_actor_and_stage}} | {{previous_expectation}} | {{change_and_purpose}} | {{change_reason_and_source}} | {{change_impact}} |

## Durable Completion References

- Final documentation location and governing placement rule: {{final_documentation_and_rule}}
- Applied requirements and necessary rationale retained in: {{durable_spec_and_rationale_references}}
- Verification evidence retained in: {{durable_evidence_references}}
- Deviations, unresolved issues, and remaining work: {{deviations_and_remaining_work}}
- Temporary artifacts and retention state: {{temporary_artifacts_and_retention_state}}
