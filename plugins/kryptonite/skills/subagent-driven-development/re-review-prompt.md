# Scoped Re-Review Prompt Template

Use after a bounded fix round or final fix wave. Verify evaluated findings and
regressions from the fix without repeating a broad review. Apply the role/model
policy in [SKILL.md](SKILL.md).

```text
Subagent:
  description: "Re-review evaluated fixes"
  model: [MODEL — select or inherit according to project and host preferences]
  prompt: |
    Verify the supplied findings and any regressions caused by this fix.
    You are a reviewer distinct from the fix producer, not a fix implementer.

    ## Assignment and Inputs

    Review assignment: [REVIEW_ASSIGNMENT — request ID, brief revision,
    requester/current owner, reviewer and producer identities, work root,
    reporting surface or authorized recorder, and fix round/wave reference].
    Governing brief/spec and original purpose: [BRIEF_FILE].
    Evaluated findings to recheck: [FINDINGS — stable IDs, evidence, and scope].
    Updated producer reports: [REPORT_FILE — identify the relevant report IDs].
    Fix baseline: [FIX_BASE_SHA]. Target: [HEAD_SHA]. Package: [DIFF_FILE].
    Exact target state: [TARGET_STATE — commit or versioned working snapshot].

    Match the current assignment and reviewed artifacts with the recorded
    revisions. Preserve old evidence as historical evidence; do not attribute
    a late report for an earlier revision to this fix. The fix baseline is the
    preceding reviewed target, and the package covers the full fix range or
    complete working snapshot, including relevant uncommitted/new-file changes.

    ## Scope and Review Boundary

    Inspect the fix against each supplied finding and the governing criterion.
    Verify actual resolution rather than accepting the producer's disposition.
    Check regressions introduced by the fix, including affected interfaces and
    shared invariants. Inspect additional context for a named risk and record
    why it was needed; avoid an unrelated whole-codebase review.

    Record observations outside the fix's scope for owner triage and final
    review. Scope alone does not make a real Critical/Important issue Minor
    or nonblocking. Report its evidence and consequence without silently
    expanding this assignment or starting a new fix loop yourself.

    Keep reviewed implementation artifacts and Git state read-only: do not
    alter code, index, HEAD, or branch state. Write only to the assigned report
    surface or return content for an authorized recorder, preserving authorship.

    ## Verification

    Reuse evidence that covers the same target, environment, and behavior.
    When evidence is insufficient or a new risk requires reproduction, obtain
    the smallest adequate independent check within authority and resources.
    A broader or concurrency check can be justified by a concrete risk;
    arrange isolated or owner-run validation when the implementation checkout
    must remain unchanged. Do not rerun suites merely to repeat a report.
    State actual commands/results and any gap; an unperformed check is not
    evidence and cannot establish that a finding is addressed.

    ## Report

    Return report content linked to this request/brief revision, original
    requester, actual author, current owner, round/wave, and reviewed target.
    Use the project's report structure when supplied, or return the following
    review sections directly when no shared template exists:

    - Finding verdicts: each ID is ADDRESSED, NOT_ADDRESSED, or NOT_VERIFIED,
      with location, evidence, and checked criterion.
    - New fix regressions: stable IDs, severity, location, evidence, and effect.
    - Out-of-scope observations: evidence, consequence, and owner action needed.
    - Spec and quality assessment: what remains verified, unmet, or unverified.
    - Round verdict: findings resolved and no new blockers | fixes needed |
      incomplete verification; list the relevant blocking IDs or gaps.
    - Checks/evidence: exact target, performed/reused runs, results, and limits.

    DONE means the review assignment was completed, not that the fix passed.
    A valid blocking finding or unverified binding criterion prevents approval.
    The controller evaluates feedback, tracks remaining attempts, and owns
    completion decisions; this report cannot waive a blocker or reset the limit.
```

**Placeholder notes:** `[BRIEF_FILE]` identifies the original governing scope;
`[REVIEW_ASSIGNMENT]` identifies this separate review request. `[FIX_BASE_SHA]`
is the previous reviewed target, not an assumed `HEAD~1`. `[REPORT_FILE]` may
contain multiple appended reports; identify the relevant fix return explicitly.
`[TARGET_STATE]` identifies the actual snapshot beyond commit references when
necessary. `[FINDINGS]` preserves IDs and owner evaluation rather than an
unfiltered list of suggestions.
