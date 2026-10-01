---
name: test-driven-development
description: Use when implementing features, fixing bugs, or refactoring and deciding whether test-first development or a new regression test adds useful coverage
---

# Test-Driven Development

Use test-first development when a meaningful test can guide a behavior change.
Choose verification from the intended outcome, likely failures, and existing
coverage. A new test must protect an observable contract rather than merely
record that a file or function changed.

**Core principle:** Keep feedback useful and early. Do not manufacture failure
to satisfy a sequence.

Classify work by its intended effect on behavior, not by new files or functions.
A feature added to an existing system and a bug correction change behavior;
extracting a helper into a new file can preserve it. Compatibility changes need
explicit criteria even when described as cleanup.

## Choose the Check Before the Change

Follow explicit user and project testing requirements. Otherwise identify the
governing behavior or criterion, a plausible wrong result, and what already
checks it. Consider failure likelihood and consequence as well as the cost and
reliability of the proposed check.

| Situation | Useful approach |
| --- | --- |
| Low-impact copy, formatting, or an obvious mechanical change whose result can be established directly | Inspect the diff or actual artifact, including rendered output when relevant. Add no new persistent test. |
| Behavior-preserving refactoring with adequate coverage | Establish a passing baseline and preserve it through the change using relevant existing checks. Extend coverage only for a demonstrated gap; do not add a test per new helper. |
| A reproduced bug or new binding behavior with a useful, repeatable test and a coverage gap | Add or extend a focused behavioral test. Prefer test-first when the current behavior genuinely fails the intended criterion. |
| An important existing behavior needs protection before a change | Add useful contract or characterization coverage for the affected boundary. It can pass immediately; label observed behavior separately from desired requirements. |
| An automated check would be brittle, duplicate existing coverage, or only mirror implementation | Use an adequate existing check, direct exercise, or inspection. State remaining uncertainty rather than inventing a ceremonial test. |

Direct inspection is enough only when it establishes the relevant outcome.
File type, line count, and how obvious an edit looks do not establish its risk:
a one-character authorization-boundary change can need a focused regression
test, while changing ordinary display copy can be checked in the rendered UI.
Configuration changes can also alter significant behavior.

A new test is unnecessary when it adds no meaningful protection. This is an
ordinary implementation decision within existing authority, not a recurring
request for permission. Resolve missing requirements or evidence when they
prevent the decision; preserve any binding project checks.

## Implement New or Changed Behavior

Derive desired results and necessary supporting conditions from the governing
criteria, not from a candidate implementation. Choose a small set of relevant
cases and boundaries; reuse existing tests and harnesses rather than writing
speculative tests for every prospective helper. For test guidance, use
[writing-good-tests.md](writing-good-tests.md).

1. **RED:** For a real defect or unmet behavior, run the focused test against
   the current implementation and check the failure's cause. A broken harness
   or unrelated environment failure does not demonstrate the intended defect.
2. **GREEN:** Implement the smallest complete change that satisfies the
   governing behavior, including its necessary supporting requirements. Run
   the focused check and checks for directly affected behavior.
3. **REFACTOR:** Improve a concrete design or maintainability problem while
   preserving the verified behavior. Avoid mixing unrelated behavior changes
   into the cleanup.

If a test passes immediately, check whether the criterion is already satisfied,
an existing test already covers it, or the assertion misses the intended risk.
Keep useful passing coverage; repair a weak test's oracle or scope when needed.
Do not distort the expected result or damage correct implementation to make it
fail. RED is evidence of a genuine gap, not a separate deliverable.

Test observable behavior at a useful consumer boundary. Exact values or calls
are appropriate when they are contractual; private helper structure and source
text are usually poor substitutes for behavior. Prefer real components and
appropriate maintained fakes; use bounded mocks when needed for the checked
contract or a difficult external/error boundary.

## Refactor While Preserving Behavior

Identify the concrete structural problem to improve and the observable behavior
to preserve: relevant results, errors, state changes, and external effects.
Fewer lines or more helpers alone do not establish an improvement.

1. Establish the baseline using the check selected above. Reuse relevant passing
   tests when adequate; direct inspection or static checks can suffice for a
   low-impact mechanical change. Characterize unprotected behavior when useful.
2. Make bounded structural changes while preserving those behavioral criteria.
   The normal flow is passing before and after; no new failure or helper-level
   test is required solely because structure changes.
3. Check preservation and whether the named structural problem improved. Broaden
   checks for an uncovered boundary, consequential semantic risk, or substantial
   rewrite; a focused old/new comparison can help when existing tests are weak.

Investigate unexpected failures rather than updating expectations merely to
match the refactored output. Test imports, fixtures, or wiring may need changes;
preserve their behavioral obligations using the guidance in writing-good-tests.md.
Passing selected cases is preservation evidence within their scope, not proof
of universal equivalence or an observed RED/GREEN cycle.

When a task mixes refactoring and behavior changes, keep their criteria and
verification steps distinct. Necessary structural preparation may precede the
new behavior; this separation does not require extra branches or commits.

## When Code Already Exists

Preserve correct implementation. Do not delete it or restart solely because
the test was written later. Add or extend meaningful coverage when warranted,
or use the adequate existing/direct check selected above.

For a bug regression, reproduce the actual previous defect in an isolated
old revision or supplied reproduction when available and useful. Do not disturb
shared Git state or introduce an artificial fault merely to reconstruct RED.
If only a passing check is available, describe that evidence honestly; do not
claim an observed test-first or failing-baseline cycle.

For poorly understood or undertested code, characterize the affected boundary
when useful before a substantial transformation. Record selected inputs and
observed pre-change outcomes with their source revision or snapshot. Such a
test can pass on its first execution; complete knowledge of the intended
behavior is not a prerequisite for recording what currently happens.

Label that baseline as observed behavior. Investigate whether it is intended
without treating an existing defect as an accepted requirement. An intentional
correction needs its own desired-behavior criterion; do not silently update
the preservation baseline to bless the correction or its implementation.

## Verify and Record Proportionately

During development, run the smallest adequate checks for the changed behavior
and its dependencies. Broaden for a concrete integration/regression risk or
project requirement. Reuse evidence only when its target, environment, and
assumptions remain applicable. Assess warnings by their consequence and project
rules; pristine output is not a substitute for correct behavior.

In the existing work record or report, retain the material criterion, chosen
check and rationale, actual target, commands or observations, results, and gaps.
Record RED/GREEN only when observed. A low-impact edit needs no separate TDD
document, duplicate checklist, new harness, or suite solely to satisfy this skill.

[systematic-debugging](../systematic-debugging/SKILL.md) owns investigation of
unexpected failures. This skill owns the test-selection and implementation
feedback approach; it does not add a retry policy.
[verification-before-completion](../verification-before-completion/SKILL.md)
owns evidence for final claims. Passing one test does not establish every
requirement or authorize completion beyond its coverage.

## Basis

The selection rules are a local adaptation of
[ISTQB risk-based testing guidance](https://astqb.org/5-2-risk-management/).
The test-first cycle follows
[Canon TDD](https://newsletter.kentbeck.com/p/canon-tdd).
The separate preservation workflow follows
[Fowler's refactoring workflows](https://martinfowler.com/articles/workflowsOfRefactoring/fallback.html);
observed baselines follow
[Feathers's characterization testing](https://michaelfeathers.silvrback.com/characterization-testing).
Empirical work on
[TDD process characteristics](https://arxiv.org/abs/1611.05994) supports examining
iteration properties alongside test/code order; its limited observational
results do not establish universal superiority of either order or measure this
agent workflow's effectiveness.
