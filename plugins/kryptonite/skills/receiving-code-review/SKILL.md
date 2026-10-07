---
name: receiving-code-review
description: Use when evaluating review feedback before changing code, especially when a suggestion is unclear or conflicts with requirements or project evidence
---

# Receiving Code Review

Evaluate feedback against the intended outcome and actual project evidence
before accepting, rejecting, or implementing it.

**Core principle:** Verify before implementing. Clarify what affects the decision.

## Evaluate Each Finding

1. Read the full review and identify its request, scope, governing requirements,
   and reviewed revision or snapshot. Check whether later changes affect it.
2. Understand the claimed defect or suggestion and its consequence. Distinguish
   a binding requirement, technical defect, optional improvement, and question.
3. Check the relevant code, interfaces, compatibility constraints, and evidence.
   Judge the claim against the original goal and necessary supporting
   requirements, not merely the producer's rationale.
4. Record the disposition and basis in the existing review report or work record.
   Preserve finding IDs and prior evidence when the decision changes.
5. Implement accepted changes within the owning workflow, then verify the
   affected behavior. Return actual changes, target, covering evidence, and
   unresolved findings through its report.

When `writing-agent-handoffs` appears in the current host's available-skills
list, use its existing records where applicable. Otherwise use the project's
review record or record the request/finding IDs, reviewer and producer,
reviewed target, evidence, disposition, owner, and next action in the current
work record. Do not infer availability from a sibling vendor or cache folder.
The current owner retains responsibility for disposition and follow-up;
receiving feedback does not transfer ownership or grant additional authority.

## Handle Unclear or Conflicting Feedback

Pause the unclear item and any work that depends on its resolution. Determine
dependencies from shared code, interfaces, assumptions, and requirements.
Continue clear items only when their independence is established and the owning
workflow permits it. If the relationship is unknown, pause the affected scope
until it is resolved.

Ask a specific question or obtain the missing evidence. Do not treat ambiguity
as rejection, successful verification, or permission to guess. Unresolved
binding feedback prevents approval or completion of the affected scope.

Use existing project instructions, governing decisions, and technical evidence
to resolve conflicts. The user controls intended scope; factual technical
claims still require verification regardless of who made them. Escalate an
unresolved material intent or authority conflict to the current owner or user
before dependent changes, rather than requesting confirmation for every finding.

## Check Purpose Before Adding or Removing Functionality

An absence of internal call sites is evidence about internal usage, not proof
that behavior is unnecessary. Before proposing removal, check:

- Public or external consumers, configuration, jobs, dynamic invocation, and
  documented contracts.
- Compatibility commitments and supported platforms or versions.
- Whether the behavior is necessary to achieve the original requested outcome,
  including supporting requirements the user did not explicitly name.

Use relevant searches such as `rg` alongside those sources. If the necessity
or consumer contract remains unknown, record that gap before a removal decision.
Conversely, a suggestion for a more elaborate implementation needs a concrete
requirement, defect, or constraint; convention alone does not justify new scope.

## Record the Decision

| Disposition | Basis and next action |
| --- | --- |
| Accepted | Record the demonstrated issue and required outcome; fix within the existing scope and authority. |
| Rejected | Record contrary evidence or the governing decision; preserve the finding for later review. |
| Needs context or evidence | Record the precise gap, affected work, and needed input or investigation. |
| Deferred | Record a nonblocking suggestion and rationale under the owning workflow's policy. |

Apply the project's severity and blocking rules. Do not silently drop feedback,
downgrade a valid blocker to finish, or defer a binding failure as optional work.
A reasoned rejection is different from postponing an accepted defect.

## Fix and Verify

Prioritize valid blockers and dependencies. Group coherent fixes where the
owning workflow permits; do not invent a competing scheduler or retry policy.
Use focused checks that cover the changed behavior and relevant regressions,
or valid existing evidence when its target and assumptions still apply.

The fix report identifies addressed finding IDs, actual artifact revisions,
checks and results, and remaining limits. A statement that a fix was made
does not itself close the finding. The owning workflow determines confirmation,
required re-review, and completion gates.

When a fix changes a commit-preparation candidate, return its actual target and
affected evidence to the owner. Renew affected checks and technical review
under the invoking workflow's gates and limits. Keep unaffected findings and
checks; do not treat the earlier verdict as approval of materially changed
artifacts.

## Communicate the Technical Basis

Follow actual user and project communication rules. State the requirement,
evidence, decision, or fix respectfully and concretely. Courtesy is compatible
with technical rigor; agreement or gratitude does not replace evaluation.

When pushing back, explain the conflicting contract or observed behavior and
what evidence would change the decision. If later evidence disproves the
pushback, correct the recorded basis and proceed with the supported change.

When external replies are already authorized, use the relevant review thread
and preserve the finding's context. This skill does not authorize sending
messages to other people.

## Examples

- One finding concerns an isolated documentation typo; another is unclear about
  a shared API contract. Fix the typo if independence is established and the
  workflow permits it; pause the API change and its dependent work.
- A public endpoint has no internal callers but is covered by an external
  integration contract. Do not remove it based on the local search result.
- A review marked `DONE` identifies an unverified binding criterion. Record
  the evidence gap and obtain the required check; do not infer approval from
  the assignment status.
