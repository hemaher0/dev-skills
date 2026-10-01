---
name: requesting-code-review
description: Use when a change needs independent review against requirements before dependent work, integration, or release
---

# Requesting Code Review

Request an independent check of the actual change against its intended outcome.
Give the reviewer the relevant purpose, constraints, artifacts, and evidence
rather than the accumulated session history.

**Core principle:** Review the complete assigned change before relying on it.

## When to Request Review

Follow project instructions and the invoking workflow's review gates.
[subagent-driven-development](../subagent-driven-development/SKILL.md) defines
its task, fix, and final reviews. Other useful review points include completing
a major feature, preparing integration, investigating a complex fix, or needing
an independent assessment before further work.

The invoking workflow owns scheduling, fix limits, and re-review. This skill
prepares the request and result; it does not introduce another review loop.
A review request does not itself authorize delegation or integration.

When a material change invalidates existing technical review, establish the
revised target and request only affected review required by the invoking
workflow. This does not replace the project's actual commit-content and
message review.

## Establish the Review Target

Use the recorded starting state of the assigned work and its actual target.
For work that has not started, record the baseline before implementation.
For completed work, retrieve that baseline from the existing work record or
establish it from the task's history and scope. If it cannot be established,
report the missing context rather than guessing.

For a committed range, resolve the baseline and target to full commit IDs.
With those IDs assigned to `BASE_SHA` and `HEAD_SHA`, inspect the whole range:

```bash
git diff --stat "$BASE_SHA" "$HEAD_SHA"
git diff "$BASE_SHA" "$HEAD_SHA"
```

A `HEAD~1`-to-`HEAD` range only covers the last commit; it is not the default
task or branch range. Include earlier task commits even when the latest commit
is a fix.

If the assigned work includes uncommitted changes, provide a versioned snapshot
or equivalent review package covering its relevant committed, staged, unstaged,
and new-file changes. Identify the baseline, exact target contents, and material
environment. A commit-only diff cannot represent that working state. Do not
commit merely to obtain a reviewable range; do not include unrelated work.

## Prepare the Request

Use [writing-agent-handoffs](../writing-agent-handoffs/SKILL.md) and its
[brief](../writing-agent-handoffs/templates/brief.md), or an existing equivalent
record. Responsibility stays with the requesting owner.

Supply:

- Request and brief revision, requester, reviewer, producer, current owner,
  permitted workspace/reporting surfaces, and report destination.
- Original goal, governing spec or plan and revision, binding criterion IDs,
  necessary supporting requirements, constraints, and unresolved assumptions.
- Review mode and scope: task, scoped fix, or whole change; included artifacts,
  baseline and target, review package, and relevant interfaces or dependencies.
- Producer report and available verification evidence, with their checked
  revisions and limits. Producer claims guide inspection rather than prove it.
- Required verdicts and severity/blocking rules. Follow project or workflow
  policy; otherwise treat Critical and Important findings as blocking and Minor
  suggestions as optional.

Choose a reviewer distinct from the producer when delegation is authorized.
Use the invoking workflow's specialized prompt when supplied; otherwise fill
[code-reviewer.md](code-reviewer.md). Keep the reviewer on the assigned scope,
with enough surrounding context to evaluate it.

Review is read-only on implementation artifacts and Git state. Return the
report through the permitted reporting surface, or an authorized recorder who
preserves the reviewer's actual authorship.

## Evaluate the Result

Use the [report](../writing-agent-handoffs/templates/report.md), or the
equivalent existing review record. Correlate it with the request and brief
revision, actual reviewed target, findings, criterion outcomes, evidence, and
verification limits. Route it to the current owner if responsibility has moved.

A review assignment marked `DONE` can still find a failing implementation.
Keep assignment status separate from spec compliance, quality, and readiness
within the assigned scope. A scoped fix review does not approve the entire
change.

Apply [receiving-code-review](../receiving-code-review/SKILL.md) before fixes.
The owner records supported acceptance, rejection, deferral of nonblocking
suggestions, or missing evidence. Valid blocking findings and unverified binding
criteria prevent approval. The invoking workflow decides the next assignment
and required re-review; reaching its fix limit does not waive unresolved issues.

## Example

A task starts at commit A, adds behavior in B, and fixes tests in C. Request
review of A through C, with the task's governing criteria and producer report.
A B-through-C diff would omit the behavior added in B.

If the reviewer completes the assignment but finds a missing binding behavior,
record the completed review and failing verdict separately. Evaluate the finding
before assigning a fix; confirm resolution through the owning workflow.
