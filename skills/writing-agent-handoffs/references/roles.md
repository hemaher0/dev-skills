# Agent Roles and Template Conventions

## Roles

Use the following role values for a participant's activity in the recorded
task. These are local defaults, not a research-standard role taxonomy.

| Role | Activity | Expected result |
| --- | --- | --- |
| `coordinator` | Route requests, track dependencies and ownership, and reconcile returned work within the existing scope. | Updated work state and a clear next action. |
| `planner` | Turn established requirements into a scoped plan with dependencies and completion criteria. | A plan with assumptions and unresolved decisions identified. |
| `implementer` | Implement, fix, or integrate changes within assigned write surfaces. | Changed artifacts and evidence covering the requested behavior. |
| `reviewer` | Independently assess the assigned artifacts against requirements and quality criteria. | Evidence-based findings and scoped verdicts. Review is read-only for the artifacts under review. |
| `researcher` | Investigate a bounded question using identifiable sources. | Findings with sources, limitations, and unresolved questions. |
| `documenter` | Create or update durable documentation under the project's document rules. | Documentation grounded in the accepted behavior and evidence. |

Choose the role for the current assignment, rather than giving an agent a
permanent persona. The same agent can hold different roles in different tasks.
For an independent review, the reviewer must be distinct from the producer of
the work under review. An ownership transfer does not require a role change.
Projects can extend this vocabulary by defining an additional role and its
boundaries before using it.

Keep these concepts separate:

- **Agent identity:** Who actually participates. Reuse host-issued or already
  recorded local identities; a role name is not an agent identity.
- **Role:** What activity that participant performs in this assignment.
- **Owner:** Who is responsible for continuing and resolving the work scope.
- **Authority:** What existing instructions allow the participant to do.

A role or template does not grant permission to delegate, edit, commit, or
perform external actions. `coordinator` does not imply a supervisor hierarchy.
Read-only participants can return report content to an authorized recorder;
retain their identity as the author and identify the recorder separately.

## Ownership and Communication

- [Handoff](../templates/handoff.md): Transfer responsibility for the named
  scope to the next agent. Recording the completed document and making it
  available to that agent completes the transfer. No acknowledgement,
  acceptance, or result report to the previous owner is required. The previous
  owner stops work in the transferred scope.
- [Brief](../templates/brief.md): Assign a bounded activity while the requesting
  agent retains responsibility. Identify the assignee, expected report,
  permitted surfaces, and completion criteria.
- [Report](../templates/report.md): Return results, evidence, or a blocker for
  a specific brief revision. Reporting does not transfer responsibility or
  establish that the owner has verified completion.

If the owner changes while a request is in flight, retain the original request
ID and requester attribution. Transfer the outstanding request in the handoff
and route subsequent reports to the new owner. Preserve the original brief;
record the new reply destination in the existing ownership record or handoff.

## Filling the Templates

- Replace every `{{snake_case}}` placeholder. Use `none` for a field that does
  not apply, `unknown` for an unavailable fact, and `not verified` for an
  unchecked claim. Do not invent identities, paths, authorization, or results.
- YAML metadata values are quoted strings. Escape quotation marks and
  backslashes when substituting them; put multiline prose in the body.
- Use project-root-relative artifact paths and report destinations, or
  absolute paths when the environment requires them. Template-package links
  resolve from their containing template or reference file.
- Remove the authoring comment before publishing a filled document. Repeat
  table rows as needed. A section without relevant entries can contain `none`;
  remove only sections explicitly marked conditional.
- Reuse existing work and task IDs. `request_id` connects a brief and its
  reports; `brief_revision` identifies the exact instructions used. Record a
  new revision for material instruction changes and a distinct `report_id`
  for each report. Preserve earlier reports and authorship.
- Keep each completed handoff as a separate document. Preserve its sender,
  recipient, and state at transfer. A later transfer gets a new handoff ID.
- Treat artifact locations as references to actual outputs, not as substitutes
  for a concise result and next action. Record the exact revision or snapshot
  to which evidence applies, including material uncommitted changes.
- Check identifiers and document revisions before acting on repeated or
  delayed documents. Re-delivery of an existing document does not create a
  new assignment or ownership transfer.

For reports, use these status values:

| Status | Meaning |
| --- | --- |
| `DONE` | The author reports satisfying the brief's completion criteria with covering evidence. |
| `DONE_WITH_CONCERNS` | The author reports completion but identifies material concerns or verification gaps for the owner to assess. |
| `NEEDS_CONTEXT` | A missing input or decision prevents dependent work; state the exact question. |
| `BLOCKED` | A known obstacle prevents continuation; state the obstacle and what would resolve it. |

These are producer claims. The owner evaluates evidence before relying on
them. A failed review criterion or an unresolved blocking issue prevents a
`DONE` claim for a brief that requires those criteria to pass.

## Document Locations

Use project settings and existing workflow paths first. Do not move existing
SDD artifacts or change helper-script paths to adopt these templates. When no
location is established, use a common directory for the same work:

```text
.kryptonite/work/{{work_id}}/
  progress.md
  briefs/{{request_id}}.md
  reports/{{request_id}}-{{report_id}}.md
  handoffs/{{handoff_id}}.md
```

Use the existing progress or ownership record when available; do not create a
second registry. `ownership_record` can refer to a handoff when no separate
record exists. `reply_to` identifies the report destination within that work;
the current ownership record determines the recipient if an owner changes.

Final documentation follows project settings, then the applicable documentation
skill for unspecified details. If neither supplies a location, update relevant
existing documentation or use `docs/{{topic}}.md` for a necessary new document,
outside `.kryptonite`. For development work, finish implementation and
verification, write final documentation, generalize code and final documents,
then discard the task's temporary artifacts after retaining needed information
in durable documents. These templates do not authorize cleanup of other work.

## Research Basis

The template fields are a local design informed by recent research and primary
engineering reports. Their effectiveness has not been measured here.

- MAST identifies failures involving role boundaries, lost context, repeated
  steps, missing information, and inadequate verification. This motivates
  explicit scope, important prior attempts, and evidence linked to criteria.
  [Why Do Multi-Agent LLM Systems Fail?, v3, 2025-10-26](https://arxiv.org/html/2503.13657v3).
- A 2026 preprint proposes trace contracts for checking executions and tracing
  violations. This informs recording artifact versions and distinguishing
  supported outcomes from unverified claims; Markdown fields alone do not
  implement its runtime enforcement.
  [A Trace-Based Assurance Framework for Agentic AI Orchestration, 2026-03-18](https://arxiv.org/html/2603.18096v1).
- Anthropic describes separating production from evaluation and passing
  structured artifacts between sessions. This informs distinct reviewer
  assignments and compact continuation state.
  [Harness design for long-running application development, 2026-03-24](https://www.anthropic.com/engineering/harness-design-long-running-apps).
- A 2026 preprint separates coordination configuration from agent logic. This
  informs keeping ownership and routing explicit rather than deriving them
  from role names. Its findings are specific to its experimental setting.
  [Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems, 2026-05-05](https://arxiv.org/abs/2605.03310).

The no-acknowledgement handoff rule and the six role values are the workflow's
chosen contract; these sources do not prescribe them.
