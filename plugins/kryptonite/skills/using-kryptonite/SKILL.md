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
   Treat a skill as available only when the current host lists it. A folder in
   a vendor checkout, plugin cache, or neighboring installation is not enough.
   Read or invoke the exact installed name and location reported by the host;
   an adjacent source link may be a different revision or package. Clarify
   missing context when it is needed to determine applicability.
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
| Software planning or implementation | When host-listed, use `developing-with-specs` to establish or reuse the working spec and `brainstorming` for unresolved goals or consequential choices. Without them, maintain the project spec or current work record directly with intent, facts, sourced requirements, decisions and rationale, assumptions, criteria, evidence, and history; resolve material uncertainty from project evidence or ask for the necessary decision before dependent work. |
| A bug, failed check, or unexpected behavior | When host-listed, use `systematic-debugging`. Otherwise establish expected and observed behavior, reproduce or inspect the failure, compare relevant conditions, test a discriminating causal hypothesis, make the supported correction, and recheck the symptom and relevant regressions. |
| Creating, revising, or checking reusable agent instructions | When host-listed, use `writing-skills`. Otherwise identify the trigger, responsibility, boundaries, and intended decisions; make the smallest grounded revision; then inspect metadata, links, supporting resources, and realistic application/non-application cases. |
| Selecting a checkout or branch before Git implementation | Follow the project's designated Git workspace procedure or a compatible available Git skill. Reuse a suitable existing workspace. |
| Preparing a commit | Update applicable durable documentation through the project's procedure or an available documentation skill. Use `generalizing-diffs` and `verification-before-completion` when host-listed; otherwise inspect the complete diff for request-specific assumptions, check affected criteria on the exact candidate, and record results and gaps. Renew technical review required by the invoking workflow, then use the project Git procedure to review candidate content, disclosure, secrets, and message before an authorized commit and verify its result. |
| Finalizing development work | When host-listed, use `developing-with-specs` for durable requirements/decision/evidence preservation and `writing-agent-handoffs` for communication-record retention. Otherwise update the project's durable document and current work records directly, preserving ownership, request/result identity, applied requirements, decisions, artifacts, evidence, gaps, and pending stages. A routine commit does not establish work completion or authorize record disposal. |
| A branch integration, publication for review, or preservation decision | Follow the project's Git finishing procedure or a compatible available Git skill for the authorized outcome. |
| Release or upgrade preparation, or installation/publication effects of a Git action | Follow the project's release procedure and existing automation. When host-listed, use `managing-compatibility`; otherwise inspect affected interfaces, callers, retained/exchanged data, observable behavior, transition needs, and representative checks before choosing version impact. A Git action alone does not call for a version bump or an extra manual release. |

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
on command execution outside the sandbox, delegation tools, workspace
detection, or Git operations in a managed environment. Use the actual harness
capabilities and permissions.
