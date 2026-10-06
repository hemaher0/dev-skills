---
name: brainstorming
description: Use when a proposed change has unresolved goals, constraints, necessary conditions, or consequential design choices to explore before dependent implementation.
---

# Brainstorming

Turn an incomplete request into a justified design. Establish what result the
user wants, what conditions are necessary in this project, and which means
should achieve it. A clear, already authorized change does not need another
design-approval ceremony.

Use [developing-with-specs](../developing-with-specs/SKILL.md) throughout this
work. Reuse its working spec and history; the default is
`.kryptonite/scratchpad/<work-id>/spec.md`, subject to project configuration.
Do not create a second design-spec copy or commit a document automatically.

## Explore the Missing Decisions

1. Read the request, applicable contracts, and relevant project evidence.
   Identify scope, constraints, current behavior, and the observable result.
   For several independent deliverables, make their boundaries and dependencies
   explicit rather than assuming one tightly coupled implementation.
2. Identify omitted conditions needed for the requested result. Link each
   proposed derivation to its parent requirement or governing constraint and
   the evidence supporting its necessity. Separate these conditions from
   preferred techniques and unverified assumptions.
3. Resolve material uncertainty from available evidence where possible. Ask
   focused questions when the answer changes the goal, scope, acceptance
   criteria, or a consequential design choice. Bundle related questions when
   that helps the user decide; continue independent authorized work meanwhile.
4. Compare viable approaches when an actual choice exists. Explain their
   relevant tradeoffs and the recommendation's purpose. Do not invent a fixed
   number of alternatives or treat a familiar technique as a requirement.
5. Update the shared spec with the resulting requirements, decisions,
   assumptions, acceptance criteria, and material history before those choices
   drive implementation. Scale the detail to the work.

Existing user authorization and project review gates determine whether a
decision needs approval. Present unresolved changes to the user's goal or
agreed scope for their decision before dependent work; do not ask them to
approve the same design again merely because it was written into a file.
Record unsupported premises explicitly rather than quietly deciding them.

## Check Readiness

Review the current spec against the original request and governing evidence:

- Are necessary conditions missing, or are optional means mislabeled as needs?
- Does each material addition have a purpose and a supported derivation?
- Does each consequential choice have evidence applicable to the current goal
  and conditions, or an explicit assumption with a covering check before
  dependent work, as required by
  [developing-with-specs](../developing-with-specs/SKILL.md#ground-consequential-choices)?
- Are the requirements consistent and observable enough to guide work?
- Does verification cover the user's result, not only the selected components?
- Are unresolved questions identified with their impact and resolution point?
  Resolve blockers before dependent work; a nonblocking unknown is not a reason
  to fabricate an answer or reject the entire spec.

Use the [spec review prompt](spec-document-reviewer-prompt.md) for an independent
review when such review is needed and delegation is authorized. Otherwise
perform the check directly. Findings should identify consequential omissions,
contradictions, or unsupported choices, rather than stylistic preferences.

When a multi-step plan is needed, continue with
[writing-plans](../writing-plans/SKILL.md). For a bounded change that needs no
separate plan, continue the authorized implementation with the shared spec and
covering verification. Brainstorming does not mandate a particular executor.

## Visual Companion

A browser-based companion for showing mockups, diagrams, and visual options during brainstorming. Available as a tool — not a mode. Accepting the companion means it's available for questions that benefit from visual treatment; it does NOT mean every question goes through the browser.

Use the companion when showing the subject would help answer the current
question. Explain the browser/server operation when that choice needs a user
decision; honor an existing request or approval without asking again. Start
the server with `--open` when browser opening is authorized and supported by
the host. Follow actual host approval controls. If declined, continue in text
unless the user reopens the choice. No separate-message format is required.

**Per-question decision:** Even after the user accepts, decide FOR EACH QUESTION whether to use the browser or the terminal. The test: **would the user understand this better by seeing it than reading it?**

- **Use the browser** for content that IS visual — mockups, wireframes, layout comparisons, architecture diagrams, side-by-side visual designs
- **Use the terminal** for content that is text — requirements questions, conceptual choices, tradeoff lists, A/B/C/D text options, scope decisions

A question about a UI topic is not automatically a visual question. "What does personality mean in this context?" is a conceptual question — use the terminal. "Which wizard layout works better?" is a visual question — use the browser.

If they agree to the companion, read the detailed guide before proceeding:
`skills/brainstorming/visual-companion.md`
