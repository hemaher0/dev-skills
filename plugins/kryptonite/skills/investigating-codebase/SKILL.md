---
name: investigating-codebase
description: Use when explaining how a subsystem works, locating responsibility or module boundaries, or investigating the evidence behind an existing design decision without assuming a bug or implementation request.
---

# Investigating Codebase

Build an evidence-backed account of current behavior and, when requested, the
reasons for its design. Distinguish what the code does, what historical sources
say was intended, and what remains an inference.

## Frame the question

Identify the target, revision or environment and the question to answer:

- **Behavior and ownership:** entry points, data flow, state, effects, interfaces
  and which component owns a decision.
- **Design rationale:** requirements, alternatives, constraints and events that
  explain the current shape.

A combined question can use both modes. A narrow function question does not
require a system-wide investigation. State a reasonable interpretation of a
vague target and refine it from evidence; ask only for a material missing fact.

Keep the investigation read-only unless the request separately authorizes a
change. A code explanation is not an instruction to refactor, publish findings,
or search unrelated private sources. Do not execute workloads with external
effects merely to illustrate a call path.

## Follow behavior from a concrete entry point

Search the target symbols and read the relevant implementations, consumers and
existing tests. Trace a representative input through boundaries to its output
and effects. Track transformations, invariants, state ownership and material
failure paths; distinguish declarations from code that actually executes.

For a library-dependent claim, inspect the pinned version and relevant local
patches. Check configuration, generated code, registration and serialized data
when direct symbol references cannot establish the path. A name match or a
search with no results is not proof that an indirect consumer exists or does
not exist.

Use the smallest safe runtime observation when static inspection leaves a
material question unresolved. Reuse existing evidence when its revision and
conditions apply. Explain the useful architecture rather than narrating every
line; a small diagram helps when ownership or sequence is otherwise hard to see.

## Investigate rationale through relevant sources

Anchor the question in specific code locations and revisions. Inspect history,
blame, diffs, linked pull requests and issues where available. Follow renames
and earlier changes when the latest edit does not explain the design.

Consult relevant connected documents, discussions or operational evidence when
they bear on the question. Discover supported tools and access before choosing
a source. Do not require a fixed service roster or search every connected
account for a local question. Record unavailable or empty sources when their
absence limits the conclusion; a missing record is not proof no reason existed.

Keep explicit contemporary rationale separate from later recollection and your
own inference. A reverted fix or contradictory report can change the apparent
story. When explaining an agent's actions, inspect the relevant original tool
events and counterevidence rather than relying on a summary that omitted them.

For complicated investigations, split independent questions only when useful
and delegation is authorized. When host-listed, `dispatching-parallel-agents`
owns that coordination; otherwise investigate sequentially using the same
scope and evidence requirements. Multiple agents or models are not required.

## Synthesize and return

Lead with the answer and its material confidence limits. Include only the parts
needed by the question:

- A working mental model, concrete flow and responsibility map.
- Source locations and revisions supporting central claims.
- Documented reasons, supported inferences, competing explanations and gaps.
- Relevant constraints to preserve or reconsider if the investigation precedes
  an authorized change.

Use stable links or identifiable local paths. Label an unverified execution
path as such. Do not turn a historical choice into a current requirement without
checking whether its premise still holds. A chat answer needs no new durable
document unless requested or required by the project's documentation policy.

Use the project's bug workflow for an actual failure, design workflow for an
authorized new design, and history workflow for reconstructing a user's work.
Host-listed `systematic-debugging`, `brainstorming` and
`recovering-work-context` can serve those roles; use their exact installed
locations, or perform the bounded task with the project's ordinary tools.

## Design basis

Adapted from pstack's [how](https://github.com/cursor/plugins/blob/main/pstack/skills/how/SKILL.md)
and [why](https://github.com/cursor/plugins/blob/main/pstack/skills/why/SKILL.md)
workflows. Source selection and investigation depth follow the question rather
than a required model panel or exhaustive connector sweep.
