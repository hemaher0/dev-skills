---
name: preventing-recurring-errors
description: Use when repeated corrections, reverts or review findings reveal a recurring error pattern and the task is to prevent recurrence through structure, checks or focused guidance.
---

# Preventing Recurring Errors

Turn a demonstrated failure pattern into a proportionate prevention mechanism.
Find what repeatedly permits the mistake and verify that the correction blocks
the relevant bad cases while retaining legitimate behavior. More instruction
text is not by itself evidence that recurrence is prevented.

## Establish the pattern and scope

Read the relevant corrections, commits, reverts, reviews, tests and existing
rules within the authorized project scope. Group mistakes by their causal
mechanism and violated requirement, not by similar wording. Separate independent
occurrences from copied reports of the same event.

For each candidate class, record representative evidence, the required behavior,
how the existing design or check permits the error, and the affected boundary.
Distinguish a demonstrated repeat from an untested hypothesis. Do not impose a
fixed occurrence count or claim that one prevention measure eliminates every
possible future error.

A single bug with no demonstrated recurring pattern belongs to ordinary
debugging. A request to analyze repetition remains read-only unless fixes are
authorized. Do not expand a correction into a repository-wide redesign because
similar code exists elsewhere.

## Select the prevention mechanism

Consider these options in order of how directly they remove the cause, while
weighing migration cost, legitimate uses and the actual task scope:

| Mechanism | Suitable condition |
| --- | --- |
| Ownership, interface or data-model change | The wrong path exists because responsibilities, sources of truth or valid states are ambiguous. |
| Types or static checks | Invalid usage can be recognized reliably before execution. |
| Runtime validation | An invariant depends on values or independently exposed boundaries that static checks cannot establish. |
| Behavioral tests | A repeatable observation detects the actual failure and current coverage misses it. |
| Focused guidance or examples | The decision needs judgment or relevant context that a reliable mechanical check cannot capture. |

Choose the smallest effective combination. A structural preference does not
justify an unrelated migration. A checker should identify the violated rule and
the supported correction. Scope enforcement to a meaningful boundary; do not
require repository-wide cleanup merely to prevent new violations.

For example, two independently edited lists drifting apart may call for one
source of truth and derived output. A disagreement about whether two concepts
are actually the same first needs a domain decision; blindly merging the lists
would encode the wrong rule more strongly.

Route consequential design and compatibility decisions through the project's
existing workflows. When host-listed, `systematic-debugging` owns individual
failure diagnosis, `managing-compatibility` owns affected consumers and retained
data, `test-driven-development` owns check selection, and `writing-skills` owns
necessary reusable guidance. Resolve their exact installed locations. Without
them, inspect the causal evidence, preserve required consumers and data, choose
covering checks, and write focused guidance only for the remaining judgment.

## Prove the intended protection

Reproduce a representative past mistake safely or construct a faithful case
from its evidence. Show the prevention mechanism rejects or detects that case
for the intended reason, and check a valid case and a meaningful exception.
If a historical reproduction is unavailable, state the substitute and its
limits rather than claiming the original failure was exercised.

For a structural fix, demonstrate that the supported entry point preserves
required behavior and no longer permits the identified invalid state or path.
For lint or test protection, verify the check is actually wired into the
promised development or CI path. A local check does not prove CI execution.
Avoid source-string assertions that merely recognize the new instruction.

Keep useful human rationale when enforcement cannot explain the requirement.
Consolidate obsolete instructions only after checking their remaining audience
and contract. A working check does not automatically make all documentation
unnecessary. Preserve justified exceptions with clear conditions and ownership;
use expiry or approval only when the project's policy or actual risk requires it.

## Report and retain

Record the error class, evidence, selected mechanism and rationale, affected
scope, bad/valid-case results, integration status and remaining gaps in the
existing work record. Link a rule to its enforcement where that helps future
maintenance; do not mandate a new registry or edit every agent instruction file.

Separate implemented prevention, verified protection and proposed follow-up.
The task's existing development and Git workflows govern review, commits and
publication; this skill creates no automatic commit schedule or new approval
gate. Route later recurrence back to the causal model and coverage gap.

## Design basis

Adapted from pstack's [correct](https://github.com/cursor/plugins/blob/main/pstack/skills/correct/SKILL.md)
and [encode-lessons-in-structure](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-encode-lessons-in-structure/SKILL.md).
Prevention here follows demonstrated mechanisms and proportional scope, with
positive cases and evidence limits alongside rejected examples.
