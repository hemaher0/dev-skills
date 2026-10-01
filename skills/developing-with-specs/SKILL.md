---
name: developing-with-specs
description: Use before and during software development to maintain a working spec and decision history in a scratchpad, elaborate missing requirements, and present the spec actually used at completion.
---

# Developing With Specs

Autonomously turn the user's intent into an actionable spec, even when the user
has not supplied one. Write and maintain the working spec and decision history
in a scratchpad as development reveals new facts and choices. At completion,
the user must be able to inspect what was specified, what changed, why the
agent made those choices, and what was implemented.

## Establish the Working Spec in a Scratchpad

Read `Scratchpad root` from the target project's root `AGENTS.local.md`; the
[local configuration template](templates/AGENTS.local.md) provides its
placeholder. Resolve a configured relative path from that project's root and
use an absolute path as configured. If the file or setting is absent, the value
is empty, or its placeholder is unresolved, use
`<project-root>/.kryptonite/scratchpad/`. The project root is the target
project's root, not the installed plugin's directory or the shell's current
subdirectory.

Create the resolved directory when needed. Reuse the existing task document
there, or create a clearly named task-specific Markdown document following the
project's format. State its path and keep the working spec and decision history
together there, with an explicit owner and audience. Preserve the record and
needed evidence for the final handoff under the project's retention rules.
If a configured location cannot be used, report and resolve that problem rather
than silently choosing another location.

Read the request, applicable contracts, and relevant repository evidence, and
reference those sources from the scratchpad. Existing formal specs remain
governing inputs; keep the working spec consistent with them. When a change
requires a formal contract update, use its owning workflow and link the result
from the scratchpad. For OpenSpec-governed behavior, use the required change
and delta-spec workflow with verifiable scenarios. A scratchpad or plan alone
does not replace a required formal behavior spec.

A small change can have a compact scratchpad spec; it still needs the relevant
behavior, constraints, decisions, and acceptance checks.

Capture the interpreted goal, included and excluded work, observable behavior,
constraints, responsibilities, dependencies, and acceptance criteria. Identify
the original request and other authoritative sources. Distinguish:

- Explicit user requirements and established contracts.
- Observed facts, with their sources and applicable limits.
- Derived requirements, with the goal and evidence that justify them.
- Agent-selected solutions, with their rationale and consequences.
- Unverified assumptions and open questions, with how they can be resolved.

Existing code establishes current behavior; it does not by itself establish
the user's desired behavior. Do not present an agent preference or inference
as a user requirement. Fill reasonable gaps from evidence and project
conventions within the user's authorization; raise decisions that need
unavailable information or authority.

## Record Choices as They Are Made

Record development choices in the scratchpad's decision history as work
proceeds. Include choices made during implementation, verification, and integration,
not just choices in the initial design. Do not omit a choice solely because
the agent considers it routine or obvious. Mechanical work already determined
by an existing requirement can refer to that requirement; related choices can
share an entry when all affected work and the common rationale remain clear.

For each decision, preserve enough information to establish:

- What was decided, by whom, and when or at which development stage.
- Which goal or requirement it serves and whether it was requested, derived,
  or selected by the agent.
- Why the choice is appropriate, with concrete evidence or a stated tradeoff;
  include relevant alternatives when an actual choice between them was made.
- Its assumptions, uncertainty, affected behavior or artifacts, and checks.
- Whether it remains active, was revised, was rejected, or is unresolved.

"Best practice" or "the tests pass" alone does not explain why a choice meets
the user's goal. Distinguish observed support from an assumption. Gather
evidence or keep the uncertainty visible when the rationale is insufficient.
Do not fabricate reasons, sources, timestamps, or user approval afterward.

## Evolve the Spec During Implementation

New facts can require additions or revisions. Record the previous expectation,
the change, its reason and source, and its effect on implementation and
acceptance checks. Preserve superseded decisions in the scratchpad's history,
revision links, or a change log. The final working spec describes the actual
accepted behavior; its history explains how that behavior was reached.

Autonomous refinement within existing authorization does not require advance
approval of every choice. Honor review gates explicitly required by the user
or project and approvals already covering the same scope. A change that
contradicts the user's requirement or exceeds that authority needs the user's
decision before dependent work. Silence is not approval when approval is needed.

Do not silently weaken an acceptance criterion or redefine a requirement to
make an implementation appear correct. Explain and resolve a mismatch. If an
earlier choice was not recorded, document the omission honestly and reconcile
the affected spec and artifacts; do not disguise the entry as contemporaneous.

## Coordinate Delegated Decisions

Give each worker the scratchpad spec reference and governing inputs, its
assigned scope and authority, and where to record choices and proposed changes.
Workers keep their assigned records current and return decision references
with their handoffs. The coordinator owns the consolidated scratchpad working
spec and reconciliation
of cross-task changes; workers use their assigned records and do not overwrite
the shared scratchpad independently.

Use [writing-agent-handoffs](../writing-agent-handoffs/SKILL.md) when documented
parallel assignments and returns are needed. Consolidate worker decisions,
their evidence, and spec changes before the final user handoff. A worker's
report alone does not establish that a change is justified or authorized.

## Verify and Present the Applied Spec

Check both whether the spec remains faithful to the user's intent and whether
the implementation meets the spec. Inspect the resulting artifacts against
the current spec and decision history. Account for implemented choices and
spec changes; a passing test or a structural validator alone does not establish
that the chosen requirements were appropriate.

At completion, explicitly present a reviewable reference to the scratchpad's
final applied spec and decision history, including applicable governing
contract references, plus a concise account of:

- The behavior, scope, and responsibilities the implementation actually used.
- Requirements and decisions added or changed during development and why.
- Agent-selected solutions and the evidence or tradeoffs behind them.
- Acceptance checks and results, deviations, and unresolved assumptions.

A silent file update or an unlinked worker report does not satisfy this
handoff. The user must be able to review the actual basis of the delivered work.
