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
original goal and supporting requirements in the current working spec using
[developing-with-specs](../developing-with-specs/SKILL.md).

A test, inspection, or review covers its checked scope. A passing component
test alone does not establish every requirement, and checking source data
alone does not verify that a derived document copied it correctly.
An "all" or "every" claim needs coverage of the entire stated set; otherwise
identify the checked subset.

For a failure's causal explanation, assess the discriminating evidence using
[systematic-debugging](../systematic-debugging/SKILL.md). A corrected symptom
does not alone establish the cause or permanent prevention. Distinguish a
tested behavioral correction, a causal explanation, and temporary mitigation.

## Choose and Inspect Adequate Evidence

Use a focused test or build, reproduction, direct artifact/UI/API inspection,
static check, or other observation that establishes the claimed outcome.
Follow binding project checks. Use
[test-driven-development](../test-driven-development/SKILL.md) when deciding
whether a new test or test-first approach adds useful coverage.

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

Use [using-kryptonite](../using-kryptonite/SKILL.md) for commit-preparation
routing. This skill owns completion evidence, not another preparation or
review loop.

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
