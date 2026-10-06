---
name: using-kryptonite
description: Use when starting a task or when its goal or stage changes, to select applicable skills
---

# Using Kryptonite

Select the skills that guide the current work. Apply them within higher-priority
instructions, the user's requests, project rules, and existing authorization.
A skill does not grant permission for additional actions.

## Select Before Relevant Work

1. Identify the current goal, scope, and unresolved decisions.
2. Check available skill descriptions and select relevant or explicitly
   requested skills. Read their current instructions before the work they govern.
   Clarify missing context when it is needed to determine applicability.
3. Reuse guidance already read while its content and the relevant task
   assumptions remain unchanged. Reconsider selection when the goal, stage,
   constraints, or guidance changes.
4. Briefly identify newly applied skills and their purpose. Reuse the existing
   plan or task tracking; add work items when they help manage the actual task.

Routine acknowledgments, status updates, and follow-up questions within the
same scope do not require repeating selection or restarting a workflow.
A selected skill that proves inapplicable can be set aside without a separate
waiver. Preserve any explicit request to use a named skill; clarify a material
conflict with the current task rather than silently ignoring it.

## Route to the Responsible Skill

| Current work | Routing |
|---|---|
| Software planning or implementation | Establish or reuse the working spec with [developing-with-specs](../developing-with-specs/SKILL.md). Use [brainstorming](../brainstorming/SKILL.md) when goals, constraints, necessary conditions, or consequential choices remain unresolved. |
| A bug, failed check, or unexpected behavior | Use [systematic-debugging](../systematic-debugging/SKILL.md) to investigate before proposing a fix. |
| Creating, revising, or checking reusable agent instructions | Use [writing-skills](../writing-skills/SKILL.md) for authoring and proportional validation. |
| Selecting a checkout or branch before Git implementation | Follow the project's designated Git workspace procedure or a compatible available Git skill. Reuse a suitable existing workspace. |
| Preparing a commit | Update applicable durable documentation through the project's designated documentation skill or procedure → [generalizing-diffs](../generalizing-diffs/SKILL.md) → affected [verification](../verification-before-completion/SKILL.md) and technical re-review under the invoking workflow → project Git review of the actual candidate and message → authorized commit and verification of its result. |
| Finalizing development work | Use [developing-with-specs](../developing-with-specs/SKILL.md) to preserve the applied requirements, decisions, and evidence in durable documents. Follow [writing-agent-handoffs](../writing-agent-handoffs/SKILL.md) for communication-record retention. A routine commit does not establish work completion or authorize record disposal. |
| A branch integration, publication for review, or preservation decision | Follow the project's Git finishing procedure or a compatible available Git skill for the authorized outcome. |
| Release or upgrade preparation, or installation/publication effects of a Git action | Follow the project's release procedure and existing automation. Use [managing-compatibility](../managing-compatibility/SKILL.md) for contract/data readiness and version impact. A Git action alone does not call for a version bump or an extra manual release. |

Reuse settled requirements, decisions, and authorization. Apply process
guidance to the decisions it owns, then the relevant domain or implementation
guidance. Plan execution, agent coordination, code review, test selection,
completion evidence, and Git operations retain their own workflow owners.
When a software task depends on a consequential domain assumption, use the
available domain workflow or authoritative evidence to assess that assumption.
The development workflow retains implementation and spec ownership; its checks
cover only the outcomes they actually examine.

When no specialized Git workflow is available, use ordinary Git or host tools
under project instructions and actual permission controls. A routine authorized
commit does not require a separate branch-finishing workflow.

Enter commit preparation for a user request or an authorized project workflow;
implementation completion alone does not request it. Reuse accurate documents,
valid preparation and checks, and existing authorization for the same scope.
Honor explicit timing deferrals and retain records needed by pending stages.
After a material change, return affected requirements or artifacts to their
owner and renew the necessary preparation; keep unaffected evidence.

## Ground Conclusions and Actions

For answers based on documents, search results, repository state, or tool
output, distinguish observed facts, reasoned inferences, and unknowns. Match
central claims to the evidence's subject, covered set, version, and conditions;
consider alternative explanations for causal or comparative conclusions when
they matter. Gather needed evidence or narrow the claim. Keep material limits
in the conclusion and recommendation, rather than only in a closing caveat.
This is a brief judgment within the task, not a visible per-answer checklist.

Complete the requested result and necessary actions using existing
authorization. Resolve routine choices from context; ask when essential
information or authority is unavailable or a decision changes the agreed
goal or scope. The requested outcome determines deliverables and side effects.

## Assigned Agents

An agent dispatched for a specific task should select the guidance applicable
to that assignment and follow its brief, project constraints, and authority.
It does not need to rerun unrelated global planning or project finishing.
The assigned scope still includes any explicitly required skills and relevant
verification; being a worker does not waive those requirements.

## Codex Tools

Read [codex-tools.md](references/codex-tools.md) when the current task depends
on delegation tools, workspace detection, or Git operations in a managed
environment. Use the actual harness capabilities and permissions.
