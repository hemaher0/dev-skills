---
name: writing-plans
description: Use when established requirements need a multi-step implementation plan with explicit purposes, dependencies, deliverables, and verification.
---

# Writing Plans

Translate the working spec into actionable work for a capable implementer.
Preserve the reasons and boundaries that matter, while leaving implementation
judgment where the requirements permit it.

Use [developing-with-specs](../developing-with-specs/SKILL.md) to read and maintain
the shared spec. If the goal or a consequential choice is unresolved, use
[brainstorming](../brainstorming/SKILL.md) for that uncertainty rather than
repeating already settled exploration or approval.

## Location and Inputs

Reuse the active plan and the project's configured format and location. If an
existing formal workflow owns tasks, use that artifact and reference it from
the working spec rather than creating a competing plan. Otherwise default to
`<resolved-scratchpad-root>/<work-id>/<work-id>-plan.md`, beside `spec.md`.

A configured durable plan can be the active artifact or retain its decisions;
link it without starting a second task list. Select one execution controller
for the scope, including when formal tasks are executed by another compatible
workflow. Plan review checks requirement coverage and dependencies; technical
review, documentation audit, and Git candidate/message review remain distinct.

Keep the plan basename unique among active SDD plans: the existing SDD helper
uses it to select `.kryptonite/sdd/<plan-basename>/`. A generic `plan.md` in
different work folders would still select the same workspace. For an existing
configured plan with a collision, resolve the workspace conflict before SDD;
do not silently rename the plan or change helper interfaces.

Read the current spec, its revision and sources, affected project files, and
existing checks. Identify missing inputs and distinguish implementation
discovery from decisions that must be resolved before a dependent task.

## Decompose by Purpose

Choose tasks with clear deliverables and meaningful verification boundaries.
Group setup and documentation with the deliverable that needs them; split where
independent responsibility, dependencies, or review justify it. Do not impose
fixed durations, file counts, or a separate task for each mechanical action.

Each task needs its purpose and requirement IDs, relevant scope and exact
artifact paths, dependencies, necessary interfaces, and completion checks.
Define signatures or exchanged data shapes when another task depends on them.
Do not prescribe full implementation code unless exact code is needed to
preserve a fragile contract. Follow existing project patterns without expanding
the task into an unrelated restructure.

## Plan Shape

Use the project's structure when established. Otherwise start with:

```markdown
# [Work Title] Implementation Plan

**Work ID:** [Existing work ID]
**Spec:** [Actual spec path and material revision]
**Goal:** [Original observable result]
**Execution:** [Existing user choice or applicable project workflow]

## Global Constraints

[Applicable governing requirements with IDs and sources; retain exact required values.]

## Dependencies and Open Decisions

[Affected tasks, required inputs, and who resolves material unknowns before dependent work.]

### Task 1: [Deliverable]

**Spec:** [Actual spec path and material revision]
**Purpose and requirements:** [Result this task serves and requirement IDs]
**Scope and constraints:** [Included work, excluded work, and applicable exact constraints]
**Dependencies:** [Task IDs or existing inputs]
**Files:** [Actual create, modify, and relevant check paths]
**Interfaces:** [Required inputs/outputs and exact shared contracts, or none]
**Completion and verification:** [Observable criteria, check method or commands, and expected observations]

- [ ] [Action with enough context to implement]
- [ ] [Check covering the stated result]
```

When SDD is selected, keep numbered `Task N` headings and `- [ ]` checkboxes
for its extraction interface. Other controllers keep their required task format.
Each extracted task must retain its spec reference, purpose, dependencies,
applicable constraints, and completion criteria without relying on neighboring
task prose. References can supply shared evidence; do not duplicate the whole
spec or every other task's code.

A filled plan must be actionable. Replace generic instructions such as "add
appropriate validation" with the required behavior and its checks. Known
unknowns may remain when a named discovery or decision step resolves them
before dependent work. Do not turn an unresolved requirement into invented
code, or leave a blocking placeholder without a resolution step.

Apply the project's test policy and the relevant testing workflow to the actual
change. Include regression or TDD steps when warranted or required; do not add
tests that merely mirror low-impact prose or mechanical edits. A plan does not
authorize commits: include commit checkpoints only when the chosen execution
workflow needs them and existing instructions authorize them.

## Review and Route Execution

Check every material requirement against tasks and covering evidence, including
the original requested outcome. Check task dependencies, shared interfaces,
unsupported scope additions, unresolved blockers, and whether isolated task
briefs remain usable. Revise affected parts and recheck findings as needed.
The [plan review prompt](plan-document-reviewer-prompt.md) supports an independent
review when needed and authorized; self-review does not require dispatch.

Report the plan path and material unresolved decisions. If execution was already
requested, continue using the chosen workflow; do not ask the user to choose
again. Use [executing-plans](../executing-plans/SKILL.md) for direct execution.
Use [subagent-driven-development](../subagent-driven-development/SKILL.md) when
delegation is authorized, suitable, and its task-commit review requirements can
be satisfied. Tool availability alone does not select or authorize delegation.
Planning alone does not authorize starting implementation or remote Git work.
