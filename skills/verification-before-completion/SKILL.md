---
name: verification-before-completion
description: Use before claiming a result is complete, correct, fixed, passing, or ready for a commit, integration, release, or handoff
---

# Verification Before Completion

Base each claim on evidence that covers the actual outcome and remains valid
after the latest relevant change. Verify the result, not merely the existence
of a change or another agent's completion report.

## Establish the Claim and Target

Identify the requested outcome, governing criteria, actual artifact revision
or snapshot, and relevant environment. For development work, compare the
original goal and supporting requirements in the current working spec. When
`developing-with-specs` appears in the current host's available-skills list,
use it to maintain that record; otherwise read and update the project's current
spec or work record directly, preserving sourced requirements, decisions,
criteria, evidence, and history. Do not infer availability from a sibling
vendor or cache folder.

A test, inspection, or review covers its checked scope. A passing component
test alone does not establish every requirement, and checking source data
alone does not verify that a derived document copied it correctly.
An "all" or "every" claim needs coverage of the entire stated set; otherwise
identify the checked subset.

Distinguish implementation correctness, suitability of the selected approach,
and achievement of the requested outcome. For suitability, examine each
consequential choice's purpose, applicable evidence or tradeoff, unresolved
premises, consequence of error, and covering check before relying on it. The
`developing-with-specs` skill supplies a fuller workflow when host-listed.
More executions, completed artifacts, or checks for another claim do not extend
the evidence to that question. Use the available domain workflow or relevant
direct evidence when software checks cannot establish applicability.

For a failure's causal explanation, use `systematic-debugging` when it is
host-listed. Otherwise compare expected and observed behavior, reproduce or
inspect the failure, test hypotheses that distinguish plausible causes, and
keep unsupported explanations unresolved. A corrected symptom does not alone
establish the cause or permanent prevention. Distinguish a tested behavioral
correction, a causal explanation, and temporary mitigation.

## Choose and Inspect Adequate Evidence

Use a focused test or build, reproduction, direct artifact/UI/API inspection,
static check, or other observation that establishes the claimed outcome.
Follow binding project checks. When `test-driven-development` is host-listed,
use it to decide whether a new test or test-first approach adds useful
coverage. Otherwise select checks from the observable criterion, plausible
wrong result, consequences, and existing coverage; do not add a test that only
mirrors the implementation.

| Claim | Covering evidence |
| --- | --- |
| Selected tests or a build pass | The actual check result, with failures, warnings, and exit status inspected. |
| A defect is fixed | The original symptom and relevant regression behavior are checked on the corrected target. A real old/new comparison strengthens the evidence when useful and available. |
| A low-impact artifact change is correct | Inspection of the actual changed artifact, including rendered output or references when relevant. |
| A refactoring preserves behavior | Adequate passing baseline and post-change checks for the affected contract. |
| Requirements are met | Material criteria traced to artifacts and appropriate checks, including the user's requested outcome. |
| Delegated work is ready | Returned artifacts inspected and covering evidence assessed independently by the current owner. |

Run missing checks and read their complete results. Reuse earlier evidence
when its target, environment, assumptions, and criteria remain applicable;
repeat affected checks when a relevant change invalidates them. An unrelated
passing check or a previously checked different snapshot is not a substitute.
A useful passing baseline does not need an artificial failure, and direct
inspection does not need a new persistent test merely to qualify as evidence.

## Commit and Integration Candidates

For commit-preparation routing, use `using-kryptonite` when it is host-listed.
Otherwise follow the project's Git procedure, or update durable documentation,
inspect the complete candidate for grounded scope and disclosure, renew affected
verification/review, and review the proposed message before an authorized
commit. This skill owns completion evidence, not another preparation or review
loop.

Verify the actual candidate or establish that the checked artifacts match it.
A working-tree check may include unstaged changes absent from the index;
partial staging can produce a different result. Formatting, hooks, restaging,
conflict resolution, or other edits require renewal of affected evidence.
Use the project Git workflow to review actual commit contents and messages,
then verify the result of any authorized Git operation.

For a material post-review change, renew affected technical review under the
invoking workflow's gates and fix limits. Report unresolved criteria or blockers
rather than treating an exhausted allowance as success.

## Report the Verified Scope

State what was checked, its actual target, and result. Keep material limits
in the central status claim and recommendation, including relevant
version or environment restrictions, rather than only in a closing caveat.
Preserve criterion-linked evidence in the existing work record or report; create no
second verification registry. Separate implementation, documentation, commit,
integration, and complete-work status when they differ.

If a check is unavailable, identify the unverified outcome and actual reason.
Do not imply broader success. Present the applied working spec and history
while retained, or the durable references preserving its governing basis after
completed temporary-record disposal.
