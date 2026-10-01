---
name: systematic-debugging
description: Use when a bug, failed check, or unexpected behavior needs causal investigation before choosing a correction
---

# Systematic Debugging

Investigate the difference between expected and observed behavior, then choose
a correction supported by the evidence. A symptom, a causal hypothesis, and a
verified resolution are different claims.

This skill owns failure diagnosis and supported corrections.
[Developing-with-specs](../developing-with-specs/SKILL.md) owns requirements,
[test-driven-development](../test-driven-development/SKILL.md) owns test
selection, and
[verification-before-completion](../verification-before-completion/SKILL.md)
owns the evidence needed for a completion claim. An ordinary document answer
does not need a debugging investigation.

## Scope and Urgency

Identify the expected behavior and its governing requirement or justified
expectation, the actual failure, and the relevant revision and environment.
Check whether the problem is reproducible, intermittent, or known only from
existing observations. Do not silently redefine the expected behavior to
make the failure disappear.

When delay would prolong serious disruption or data loss, use an authorized,
bounded mitigation before completing the diagnosis if needed. Preserve useful
evidence, check the mitigation's effect, and report remaining risk and work.
A rollback, disabled path, or workaround may reduce impact without establishing
the cause or permanently resolving it.

Use the investigation depth needed for the failure. A simple issue may need
only a relevant error, a short trace, and a focused check. The phases below
guide investigation; they do not require irrelevant instrumentation, exhaustive
reading, or a separate document for every observation. Keep material evidence
and decisions in the existing work record.

## Phase 1: Gather Relevant Evidence

- Read the relevant error, stack trace, inputs, and observed state. Establish
  what actually happened before explaining why.
- Reuse a reliable reproduction or existing check. If reproduction is
  unavailable, use logs or other observations and state that limit; do not
  invent a failing baseline.
- Inspect recent changes and configuration when they plausibly affect the
  failure. A recent change is a candidate, not proof of causation.
- In a multi-component system, inspect the boundaries that could distinguish
  the suspected failure locations. Add targeted diagnostics only when existing
  evidence is insufficient; capture relevant state without exposing secrets.
- Trace an invalid value or operation backward when its origin is unclear.
  [Root cause tracing](root-cause-tracing.md) describes that technique.

## Phase 2: Compare Behavior and Constraints

Use working examples, governing contracts, or relevant reference behavior when
they help explain the mismatch. Read the portions needed to understand the
affected path and its dependencies; extend the inspection when that path
depends on additional context.

Compare material differences in inputs, state, timing, environment, and
implementation. Keep plausible alternatives open when the evidence does not
distinguish them. Do not assume a familiar pattern or one successful case
establishes the explanation for this failure.

## Phase 3: Test Causal Hypotheses

State the suspected mechanism, supporting observations, and what result would
support or contradict it. Distinguish an observed fact from an inference or an
unresolved premise; consider alternative explanations when ambiguity matters.

Choose the smallest useful check that separates the candidates or tests the
predicted behavior. Isolate a variable when practical. If the failure depends
on interacting changes, test the relevant combination and explain the
comparison instead of forcing a single-variable explanation.

Inspect the actual result:

- Evidence supports the hypothesis: assess whether competing explanations
  remain, then choose the supported correction.
- Evidence contradicts the hypothesis: revise it using the new information.
- The check cannot exercise the relevant conditions: record an unresolved
  result, then obtain the missing evidence or narrow the claim.

A symptom disappearing after a change does not alone establish a complete
causal explanation. A minimal failure-inducing input or change set helps
localize the failure but still needs interpretation. Do not stack unrelated
changes or repeat a failed attempt without new evidence or a changed hypothesis.

## Phase 4: Correct and Verify

1. **Establish a covering check.** Reuse the smallest reliable reproduction
   or existing check for the symptom. Use
   [test-driven-development](../test-driven-development/SKILL.md) to choose
   useful coverage: a focused automated test, direct exercise, or inspection
   can be appropriate to the defect and its consequences. Observe the real
   pre-fix defect when possible; record a reproduction gap rather than
   inventing a failure. Add a regression test when it protects an uncovered
   behavioral contract; a new framework or persistent test is not required
   for every fix.
2. **Implement the supported correction.** Address the evidenced mechanism
   with a bounded change. Keep unrelated improvements out of the fix; a
   coherent correction may require changes in several files or components.
3. **Verify the result.** Check the original symptom on the corrected target,
   affected regression behavior, and binding project checks. Use
   [verification-before-completion](../verification-before-completion/SKILL.md)
   before reporting success. Separate what the checks establish about behavior
   from what the investigation establishes about its cause.
4. **Reassess an unsuccessful correction.** Use its result to revisit the
   evidence, hypothesis, and model of the system. Repeated failures may warrant
   examining coupling or architecture, but their count does not prove an
   architectural defect. Follow project or invoking-workflow retry limits;
   reaching a limit does not turn unresolved work into success. Seek a decision
   when additional work needs unavailable information or authority.

## Unresolved or External Causes

Environmental, timing-dependent, or external failures still have causes.
Identify the observations and investigated scope, what remains unknown, and
the next useful evidence or responsible owner. Do not claim there is no cause
merely because the current investigation could not establish one.

Choose retries, timeouts, error handling, or monitoring only when they serve
the affected behavior or a justified mitigation. Verify their effect and
limits. Report diagnosis, temporary mitigation, and verified resolution
separately; retain outstanding work for the current or next owner.

## Conditional Techniques

Read these when the diagnosed problem calls for them:

- [Root cause tracing](root-cause-tracing.md): locate the origin of a value or
  operation through its callers.
- [Defense-in-depth validation](defense-in-depth.md): protect independently
  exposed boundaries when one correction can be bypassed.
- [Condition-based waiting](condition-based-waiting.md): wait for an observable
  condition when arbitrary delays cause unreliable checks.

## Design Basis

[Google SRE](https://sre.google/sre-book/effective-troubleshooting/) informs
hypothesis-driven investigation and the distinction between mitigation and
root-cause work.
[Delta debugging](https://www.st.cs.uni-saarland.de/publications/files/zeller-esec-1999.pdf)
accounts for interacting changes and unresolved checks.
[AgentRx](https://arxiv.org/html/2602.02475v2) investigates evidence-grounded
agent failure attribution and describes misleading downstream symptoms.
These sources inform the guidance; they do not establish this skill's
effectiveness.
