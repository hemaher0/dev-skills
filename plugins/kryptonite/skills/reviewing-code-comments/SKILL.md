---
name: reviewing-code-comments
description: Use when writing or reviewing code comments and docstrings, cleaning redundant explanations, or checking whether a comment hides a design problem or an unenforced constraint.
---

# Reviewing Code Comments

Keep information a maintainer needs but cannot reliably recover from the code.
Remove narration and obsolete explanations. When prose compensates for unclear
code or an unenforced rule, identify the underlying problem before changing it.
Comment count is not a quality target.

## Establish the scope

Use the requested files or diff, including relevant staged, unstaged and new
files. Resolve the actual comparison base from the task and Git state rather
than assuming a branch name. Read surrounding code and callers needed to judge
the comment. A read-only review returns findings without editing files.

This skill covers source comments and docstrings, not general prose editing,
repository documentation ownership, or unsolicited cleanup of unrelated code.
Use the project's public API documentation conventions where they apply.

## Decide what the information does

| Comment's role | Action |
| --- | --- |
| Repeats the nearby expression, supplies a decorative banner, or preserves dead code | Remove when it carries no contractual or operational meaning. |
| States a public API contract, license, attribution, or required notice | Preserve the required information and format. |
| Explains an external protocol, dependency defect, numerical assumption, algorithmic rationale, or non-obvious tradeoff | Verify the claim and keep the smallest useful explanation with its source when available. |
| Describes obsolete behavior | Correct or remove it against actual behavior and the governing contract. |
| Explains surprising behavior in code the project controls | Identify the symbol, the reader's likely misunderstanding, and whether clearer names, data shapes or boundaries would resolve it. |
| Says an operation must occur, must not occur, or must occur in a particular order | Establish the constraint and its current enforcement before removing its only explanation. |

Length, emphatic wording and the presence of a workaround are investigation
signals, not proof that a comment is unnecessary. If its meaning or source is
unclear, retain the needed information and report the unresolved question.
Do not invent a rationale to justify keeping or deleting it.

Check whether a syntactic comment affects tooling or execution: lint and type
suppressions, compiler directives, generated-file markers, coverage exclusions,
doctests and runtime-consumed docstrings can change behavior when removed.
Read the relevant rule or consumer. A style-only or faulty diagnostic may
justify a narrow suppression; a suppressed correctness defect needs a supported
fix, not simply removal of the diagnostic or its explanation.

## Improve code and preserve the constraint

Prefer a concrete name or structure that makes an invariant clear once, at the
boundary that owns it. For example, a comment explaining a delay's unit may
become a meaningful parameter name or unit type. A comment describing an
external timing requirement may still be needed after that rename.

For a claimed constraint:

1. Trace its requirement, relevant implementation and any existing check.
2. Identify the smallest useful enforcement: a type, API boundary, runtime
   validation, behavioral test or maintained static check.
3. Apply a structural or functional change only within the authorized scope.
   If the request covers comments alone, return the proposed code change.
4. Verify that the replacement covers the constraint and relevant valid cases
   before deleting its only documentation. Keep any rationale the mechanism
   cannot communicate. If enforcement remains missing, report it explicitly.

When host-listed, use `investigating-codebase` for unresolved behavior or
rationale, `brainstorming` for consequential design choices, and
`test-driven-development` for useful check selection. Resolve each by its exact
installed name and location. Without them, inspect the code and available
history, state the supported design choice, and check the affected contract
using the project's existing tools. None is a prerequisite for comment review.

## Verify and report

Inspect the final diff for lost requirements, stale references, unsupported
claims and scope expansion. Pure prose removal may need only direct inspection;
directives, public contracts, renames and executable examples need checks for
their affected consumers. Report code changes separately from comment edits.

Return the locations and reasons for material removals, retained constraints,
implemented or proposed structural fixes, evidence and unresolved questions.
Do not claim behavioral preservation from a reduced comment count.

## Design basis

Adapted from pstack's [no-comments workflow](https://github.com/cursor/plugins/blob/main/pstack/skills/no-comments/SKILL.md)
and [comment reviewer](https://github.com/cursor/plugins/blob/main/pstack/agents/comment-sicko.md).
This adaptation preserves uncertain constraints and separates comment cleanup
from authorized code changes; it does not require a particular agent or model.
