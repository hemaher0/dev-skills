# Code Reviewer Prompt Template

Use for an independent review when the invoking workflow does not supply a
specialized prompt. If `writing-agent-handoffs` appears in the current host's
available-skills list, its brief/report records can carry the assignment.
Otherwise use the project's review records or a compact request and report
containing the assignment identity, requester/current owner, reviewer and
producer, scope, target, criteria, evidence, findings, limits, and next owner
action. File presence in a vendor or cache directory does not establish skill
availability.

**Purpose:** Assess the assigned change against its original goal, governing
requirements, and quality criteria. The owner determines follow-up and approval.

```text
Reviewer assignment:
  description: "Review the assigned code changes"
  prompt: |
    Independently inspect the actual implementation. Evaluate its requirements
    and quality within the assigned scope; do not implement fixes.

    ## Assignment and Inputs

    Assignment: [REVIEW_ASSIGNMENT — request ID, brief reference/revision,
    original requester, current owner, reviewer and producer identities,
    permitted workspace/report destination or authorized recorder].
    Scope: [REVIEW_SCOPE — review mode, included artifacts, binding criteria,
    severity rules, dependencies, and prior findings/dispositions if relevant].

    What was implemented: [DESCRIPTION].
    Governing purpose and spec/plan revision: [PLAN_OR_REQUIREMENTS].
    Recorded baseline: [BASE_SHA]. Target commit, if applicable: [HEAD_SHA].
    Exact target state: [TARGET_STATE — commit or versioned working snapshot].
    Complete review package: [DIFF_FILE].
    Producer report and available evidence: [REPORT_FILE].

    Match these inputs to the actual artifacts and evidence. If a required
    binding is missing or a target cannot be established, report the gap before
    a dependent verdict. The producer's report and rationale are claims to
    check, not proof that the implementation meets its purpose.

    ## Range and Scope

    Inspect the complete assigned range. For committed work:
      git diff --stat [BASE_SHA] [HEAD_SHA]
      git diff [BASE_SHA] [HEAD_SHA]

    The baseline is the recorded beginning of the assigned work, not an
    assumed HEAD~1. Include all task or branch commits appropriate to this
    assignment. If the target includes uncommitted or new-file changes, inspect
    the supplied versioned snapshot/package as well; commit-only diffs omit them.

    A task review assesses its task; a scoped fix review checks the supplied
    findings and regressions from the fix; a whole-change review also checks
    the original goal and integrated interfaces and invariants across tasks.
    Use surrounding context for a concrete criterion or risk and record why
    it was needed. Report material out-of-scope observations to the owner
    without expanding this assignment or starting a new fix loop.
    Scope alone does not reduce a valid finding's severity.

    ## Read-Only Review and Verification

    Keep implementation artifacts and Git state read-only. Do not edit code,
    stage changes, move HEAD, or change branches. Write only to the assigned
    report surface, or return content for an authorized recorder, preserving
    your identity as the actual author.

    Inspect available verification evidence and its target, environment, and
    coverage. Reuse it only when it answers the current question. Obtain the
    smallest adequate independent check for missing, mismatched, contradictory,
    or insufficient evidence or a concrete new risk. A broader check can be
    justified by cross-component risk or project policy.

    Keep checks within existing authority and resources. If a check would
    mutate the reviewed checkout, use an authorized isolated environment or
    request an owner-run check. Record actual commands/results and limitations;
    an intended or unavailable check is not executed evidence.

    ## What to Evaluate

    Spec compliance:
    - Does actual behavior achieve the original requested outcome, including
      necessary supporting requirements and binding global constraints?
    - Are required behavior and compatibility preserved, and additions in scope?
    - Are deviations supported by the governing decisions and evidence?
    - Mark each binding criterion MET, NOT_MET, or NOT_VERIFIED with its basis.
      Distinguish a demonstrated failure from unavailable evidence.
    - Flag defects required by the plan itself so the owner can resolve them;
      do not silently rewrite the requirements or approve a known defect.

    Quality:
    - Check behavior, edge cases, error handling, relevant security and data
      risks, interfaces, and material maintainability of the change.
    - Assess whether checks cover the changed behavior and relevant regression
      risks. Test counts or producer success messages alone are not coverage.
    - Assess migrations, compatibility, and documentation where affected.
      Do not require unrelated production machinery or stylistic alternatives.

    ## Findings and Verdicts

    Apply the brief's severity and blocking policy. Without an override:
    - Critical: severe correctness, security, data, or operational failure.
    - Important: binding requirement failure or a material defect that prevents
      trusting or proceeding with the assigned work.
    - Minor: nonblocking polish or optional improvement.

    Give stable finding IDs, location, observed evidence, affected criterion
    or consequence, and recommended action. Separate required fixes, optional
    suggestions, questions, and verification gaps. Preserve earlier finding
    IDs and record addressed, still-open, or not-rechecked items.

    ## Report

    Return the shared report linked to this request/brief revision, actual
    reviewed target, original requester, author, and current owner. Include:

    - Assignment status: DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED,
      according to the brief's completion criteria and shared status definitions.
    - Spec compliance: compliant | issues found | incomplete verification,
      with criterion outcomes and evidence.
    - Quality: Approved | Needs fixes | Incomplete verification.
    - Strengths: specific supported observations, if any.
    - Findings: IDs, severity, location, evidence, criterion/consequence, action.
    - Verification performed/reused, actual target/environment, results, gaps.
    - Recommendations: clearly nonbinding suggestions.
    - Assessment: readiness within the assigned scope and remaining owner action.

    Completing the review assignment is distinct from the implementation
    passing. Do not approve valid blocking issues or unverified binding criteria.
    A scoped review does not approve the whole change; no verdict grants
    permission to commit, merge, release, or change the workflow's fix limit.
```

## Placeholder Notes

- `[DESCRIPTION]`: Brief summary of the change.
- `[PLAN_OR_REQUIREMENTS]`: Original goal, governing spec/plan revision,
  criterion IDs, constraints, and necessary supporting requirements.
- `[BASE_SHA]` / `[HEAD_SHA]`: Full immutable commit IDs for the recorded
  assigned range. Mark a commit-only target as inapplicable when necessary.
- `[TARGET_STATE]`: The exact reviewed commit or versioned working snapshot,
  including material uncommitted changes.
- `[DIFF_FILE]`: Complete supplied package, or `none` when the commit range
  and accessible artifacts fully represent the assigned target.
- `[REPORT_FILE]`: Producer report and applicable evidence, or explicit gaps.
- `[REVIEW_ASSIGNMENT]` / `[REVIEW_SCOPE]`: Filled brief or precise equivalent
  context, including the permitted reporting surface, mode, and boundaries.

Do not invent unavailable facts or results. Use the shared template conventions
for identities, status, ownership, and report routing.

## Example Assessment

```text
Assignment status: DONE — assigned inspection and report completed.
Spec compliance: issues found.
Quality: Needs fixes.

F-01 | Important | api.ts:42
Evidence: an invalid date is passed to the storage query without validation.
Criterion C-03 requires invalid dates to return a validation error.
Recommended action: reject invalid dates before querying and verify that behavior.

Readiness: Not ready within this scope; F-01 remains blocking.
The owner evaluates the finding and schedules follow-up under the invoking workflow.
```
