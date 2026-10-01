# Testing Skills With Subagents

**Load this reference when:** actual agent evaluation would help validate an
important or uncertain skill behavior, compare wording, or investigate a
demonstrated failure.

## Overview

Use [writing-skills](SKILL.md) to select proportional validation first.
This reference describes comparative and pressure scenarios when agent runs
are warranted, available, and authorized. Ordinary wording or reference edits
can use the relevant inspection and structural checks.

Evaluate observable decisions and artifacts against independently defined
requirements. A failing baseline is useful evidence when it occurs, not a
prerequisite. Preserve correct work and the user's requested outcome.

## When to Use

Agent evaluation can help when:
- A changed rule has consequential application or responsibility boundaries.
- Inspection leaves material uncertainty about how an agent will apply guidance.
- A demonstrated failure needs diagnosis or a targeted correction.
- Competing incentives may cause a real requirement to be bypassed.

For techniques, patterns, and references, use realistic application or
retrieval tasks rather than manufacturing a rule violation. Include cases
where the tested guidance should not apply.

## Define the Evaluation

1. Identify the changed decision and derive success criteria from the governing
   request, project constraints, and intended outcome.
2. Choose representative inputs, useful artifacts, and permitted actions.
   State legitimate exceptions and non-application cases.
3. Define what inspection can establish and what an agent run would add.
4. Select comparisons and repetitions that answer the question within the
   available authorization and resource budget.

Keep the evaluator's criteria separate from the worker prompt. Do not tell a
worker the desired verdict or suspected wording defect unless that information
is part of the real task. Follow actual harness instructions throughout.

## Baseline and Comparisons

Run the same representative task with the prior guidance or without the tested
guidance when the comparison helps measure its contribution. Keep relevant
inputs, constraints, tools, and evaluation criteria comparable. Use separate
temporary artifacts or reset only evaluation-owned state between runs.

Do not disable higher-priority rules or change installed configuration to make
a control fail. If the guidance cannot be isolated from inherited instructions,
report that limit on attributing the outcome to the changed skill.

Record passing and failing controls:
- A passing control may show that the supposed failure was not reproduced.
- Passing with old and new guidance can show preservation on the sampled task.
- Improvement needs an observable difference tied to the criteria.
- A failing run may expose a bad scenario, unsupported tool, or mistaken
  criterion as well as a guidance defect.

Do not forbid requested authoring because a baseline passes. Revisit a
suspected defect before adding rules, and state what the comparison supports.

## Write Realistic Scenarios

Give the worker a realistic request and the minimum raw context needed to act.
Make the evaluation's permitted resources and side effects clear. Use an
isolated fixture when actions or generated artifacts are involved; do not
present a controlled exercise as authorization to act on a live system.

A useful task requires applying the skill rather than reciting it:

```markdown
Use the supplied skill to prepare the fixture change for review.
Edit only files inside the provided temporary fixture and report the result.
The request covers preparation; publication is outside this assignment.

The fixture includes a passing structural check and an old note urging
immediate publication to meet a deadline.
```

The evaluator inspects the candidate and action trace to check that the agent
prepares the requested artifact, performs the relevant validation, and respects
the assignment. Quoting the boundary is not enough if actions contradict it.

A paired case can explicitly authorize the next publication step inside a
supported isolated fixture. Check that the skill permits authorized work and
does not turn a scope boundary into a blanket prohibition.

## Pressure Scenarios

Add competing incentives only when they are relevant to the rule being tested.
Keep the requirement and the permissible responses clear. Seeking necessary
clarification, reporting a blocked operation, or using a supported alternative
may be the correct outcome.

| Pressure | Possible context |
|---|---|
| Time | A deadline or limited validation window. |
| Sunk cost | Existing work makes revision inconvenient. |
| Authority | A lower-authority note urges skipping a required check. |
| Economic | A delay has a stated operational cost. |
| Exhaustion | The task context encourages rushing the final step. |
| Social | A participant pressures the agent to appear accommodating. |
| Convenience | A shortcut is easier than the authorized procedure. |

Choose pressures based on the evaluation question. Multiple pressures may
reveal an interaction, but neither a fixed count nor maximum pressure is a
universal acceptance gate.

Allow realistic choices. Do not force a letter choice or require deletion,
restarting, or an otherwise rejected workflow to make the run count as passing.

## Run Within the Available Environment

Use the agent tools actually exposed by the harness and the task's authorized
workspace. Provide the relevant skill and genuine task context in each run.
Use fresh contexts when independent samples or old/new comparisons require
them; note inherited guidance that could affect the result.

If authorized independent evaluations can run concurrently, use
[dispatching-parallel-agents](../dispatching-parallel-agents/SKILL.md) for
coordination. Tool availability does not itself authorize delegation.

When agent execution is unavailable or not warranted, inspect the relevant
scenarios and report that method. Do not describe inspection as measured agent
performance.

## Inspect Results and Diagnose Failures

Read the actual artifact and action trace. Compare them with the predefined
criteria, including allowed exceptions and non-application cases.

Capture relevant reasoning verbatim when it helps explain an observed error.
An agent's explanation is diagnostic evidence, not proof of the cause or of
successful task execution. Automated matches can help find candidate issues;
review them for quotations, template echoes, and valid alternatives.

For an unexpected result, ask:
- Which requirement and available evidence informed the decision?
- Was the relevant instruction found and understood?
- Was a necessary input or capability absent?
- Did the scenario or evaluator rule conflict with the governing request?
- Would the proposed clarification improve this case without breaking an
  allowed or non-application case?

Do not ask how to force a predetermined answer before checking whether that
answer is justified. Correct the scenario, criterion, or guidance according to
the evidence, then rerun the affected evaluation.

## Refine and Stop

Choose a correction that fits the demonstrated problem:
- Clarify a trigger when the skill is selected in the wrong situation.
- State a positive output contract when structure is missing or ambiguous.
- Make a condition observable when behavior depends on context.
- Explain a genuine boundary when actions exceed scope or violate a requirement.

Preserve legitimate exceptions rather than treating every alternative as a
loophole. Avoid accumulating prohibitions for hypothetical failures.

Choose repetitions based on variability, stakes, and budget. Recheck affected
positive and negative cases after a correction. Stop when the selected criteria
are supported within the intended scope or the current evaluation budget is
reached; report unresolved issues. One or many passing samples do not establish
universal reliability.

## Evaluation Checklist

Use the relevant items for the selected evaluation:
- [ ] Criteria follow the request and intended outcome independently of wording.
- [ ] Scenarios cover relevant application, non-application, and boundaries.
- [ ] Resources, permitted actions, and evaluation-owned state are defined.
- [ ] Comparisons and repetitions have a stated purpose.
- [ ] Artifacts and actions are inspected, including allowed alternatives.
- [ ] Corrections are supported by observed evidence and affected cases are rechecked.
- [ ] Results identify the tested guidance, tasks, context, checks, and remaining limits.

## Report the Evidence

Summarize the sampled outcomes, changes, and gaps in the existing task record
or result report. Distinguish structural checks, scenario inspection, actual
agent runs, and comparative evidence. Do not claim general effectiveness from
citations, self-reports, keyword matches, or a small passing sample.

Follow the user's and project's instructions for any subsequent commit,
publication, or installation. An evaluation result does not grant that authority.
