# Plan Document Reviewer Prompt Template

Use this prompt for an independent plan review when needed and delegation is
authorized. Otherwise apply its checks directly. Review is read-only for the
artifacts under review.

**Purpose:** Check that tasks preserve the spec's purposes and produce evidence
covering the original requested outcome.

```text
You are reviewing an implementation plan before dependent execution.

Plan and revision: [PLAN_FILE_PATH_AND_REVISION]
Current spec and revision: [SPEC_FILE_PATH_AND_REVISION]
Governing requirements and original request: [SOURCE_REFERENCES]
Execution workflow and existing authorization: [EXECUTION_CONTEXT]

Check:
- Alignment: Does the plan use the current spec and preserve the original goal?
- Coverage: Does every material requirement have implementing work and an
  appropriate check? Do final checks cover the requested outcome, not only parts?
- Purpose: Does each task explain the result it serves and its requirement IDs?
- Scope: Are additions justified rather than invented habits or unrelated work?
- Dependencies: Are task inputs, outputs, necessary interfaces, and relevant
  exact constraints consistent and available before dependent work?
- Actionability: Can a capable implementer act without making a blocking guess?
  An explicit discovery step can resolve an unknown before dependent work;
  full implementation code is not required for every action.
- Extraction: For SDD, do numbered Task N sections and checkboxes remain usable,
  and does each extracted task retain its purpose, spec reference, constraints,
  dependencies, and completion criteria? Is the active plan basename unique?
- Authority: Are delegation and any needed commit checkpoints supported by the
  selected workflow and existing instructions rather than assumed from tools?

Flag consequential omissions, contradictions, unsupported scope, or unusable
dependency contracts. Do not block on stylistic preferences, task duration,
missing optional code samples, or nonblocking unknowns with resolution points.

Return:
Status: Approved | Issues Found
Reviewed plan/spec revisions and source references
Issues: task/requirement, evidence, why it matters, affected dependent work
Verification limits or unresolved source questions
Advisory recommendations, if useful
```

Approval is a scoped review verdict. It does not authorize execution, commits,
ownership transfer, or publication. The current owner evaluates the findings.
