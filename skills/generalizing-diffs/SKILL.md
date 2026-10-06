---
name: generalizing-diffs
description: Use when reviewing a Git diff of code, prose, or instructions for overfitting to request wording or examples, conversation-specific labels, speculative suggestions, and unsupported contextual assumptions.
---

# Generalizing Diffs

Context bias occurs when conversational wording, examples, or incidental
circumstances shape an artifact's content, structure, or behavior without
justification. Ground changed artifacts in actual intent, domain meaning,
and established decisions. Generalize the underlying principle within the
supported scope; preserve explicit requirements and useful detail.

## Review Stage

The default development stage is commit preparation routed by
[using-kryptonite](../using-kryptonite/SKILL.md),
after applicable documentation and before affected verification and final
candidate review. An explicit request can authorize this review at another
stage; honor narrower user or project timing instructions. Implementation
completion alone does not trigger it. This skill owns the review method,
not commit execution or temporary-record disposal.

## Establish the Review Boundary

Read the user-selected diff and the surrounding text needed to interpret it.
Use the requested paths or revision range. For pending changes without a
specified range, inspect both working-tree and staged diffs, and identify
relevant untracked files with `git status --short`; read those files directly
because ordinary `git diff` omits them. Do not stage files just to review them.

Check the authoritative spec, user intent, project instructions, naming
conventions, and actual behavior before deciding that a detail is incidental.
Keep the review focused on changed artifacts; inspect callers and unchanged
context when needed to understand semantics or a contract. A request for a
read-only review remains read-only.

## Distinguish Conversation From Requirements

Identify whether a conversational statement was a question, proposed option,
hypothesis, explicit request, or adopted decision. Use the surrounding intent
and subsequent decisions; sentence form alone does not establish authorization.
A suggestion can become a valid requirement when adopted or justified through
the spec's decision process. Its presence or repetition in context does not
make its wording a concept or rule in the artifact.

For a name, comment, convention, or behavior influenced by that statement,
identify the requirement, domain concept, or justified decision it represents.
Even an adopted idea should be expressed through its actual semantics rather
than by mechanically copying a conversational label. Preserve deliberately
specified terms and literal identifiers that belong to a real contract.

## Generalize the Underlying Principle

Review the substance of any changed artifact, including its decisions,
organization, rules, and behavior. Overfitting to a user's request can affect
documents, plans, explanations, recommendations, and reusable instructions
as well as code.

For each request-driven change, identify the intended outcome and the
principle or condition that justifies it. Separate required specifics from
illustrative examples, tentative suggestions, and incidental details. Express
the grounded principle and its applicability so the result remains useful
when those incidental details vary. Examine substantive choices alongside
wording and names; a renamed one-off rule can still overfit the request.

Choose the smallest revision that covers the supported scope. Keep
task-specific facts, exact formats, and explicit limits when the requested
result depends on them. Generalization must preserve the user's actual
requirements. Broader claims, new use cases, frameworks, or unconditional
rules need their own justification; uncertainty about scope should remain
visible rather than becoming an invented requirement.

## Identify Unsupported Assumptions

Look for changes that:

- Treat the current project's paths, tools, platform, or workflow as universal
  defaults without establishing why they are required.
- Turn one incident or preferred solution into an unconditional rule.
- Depend on conversation history through expressions such as "as discussed"
  or "use the same setup" without a discoverable source.
- Make an illustrative example look mandatory or exhaustive, or prescribe a
  rule, structure, or step when the condition that justifies it is absent.
- Describe an inference as an established requirement or broaden a claim
  beyond the evidence that supports it.
- Copy a user's tentative label or phrasing into variable, function, class,
  file, flag, or test names without a stable semantic meaning.
- Add comments that narrate the conversation, attribute an unadopted preference
  to the user, or claim qualities such as speed without supporting evidence.
- Establish a naming prefix or suffix from a temporary workaround or proposal
  instead of the language and project's conventions.
- Introduce defaults, hardcoded cases, branches, or heuristics from a sample
  situation or speculative suggestion without a requirement or justified
  decision supporting the behavior.

For each candidate, identify what supports it: an explicit requirement, an
interface or operational contract, a local convention, an illustrative
example, or an unsupported assumption. A specific detail is not itself bias.

## Rewrite Around Actual Semantics

Preserve the intended outcome, necessary constraints, and established language.
Replace incidental details with the relevant role, project-owned convention,
or observable application condition. Name where authoritative details can be
found when the instruction depends on them. Name code elements for their
responsibility, data, behavior, or domain concept using project conventions.
Write comments about intent, invariants, constraints, and supported tradeoffs
that a reader can understand without the conversation.

Keep genuine local requirements local. Preserve exact commands, identifiers,
paths, and formats when callers or the owning workflow depend on them. Preserve
contextual provenance in spec histories and handoffs where that context is
part of the artifact's purpose. Mark examples as examples. Narrow unsupported
claims rather than replacing them with broader claims.

For renames, update affected references and check consumers, serialization,
configuration, and external interfaces as applicable. Preserve behavior during
a naming or comment cleanup. If the finding concerns unjustified code behavior,
identify the intended behavior and make a functional correction only within
the authorized scope, with appropriate behavioral verification. Do not disguise
a logic change as a cosmetic rewrite or introduce abstraction merely to make
code appear generic. Keep specific domain meaning; replacing `retry_delay`
with `value` loses useful information.

Examples of decisions to examine, not universal replacements:

| Context-shaped artifact | Grounded revision when the meaning is established |
| --- | --- |
| "Store every plan in `docs/plans/`." | "Use the project's designated plan location and format." |
| "Use containers whenever a test fails." | "When the failure is caused by missing or incompatible host dependencies, use a project-supported isolated environment." |
| `smart_retry` copied from "How about smarter retries?" | `retry_with_backoff` when backoff is what the implementation actually does. |
| `# Use the user's preferred shortcut.` | `# Reuse the cached value while it remains valid.` when that invariant explains the code. |
| A branch matching only an incidental example value | Implement the specified condition; preserve the special case if a genuine requirement needs it. |
| A reusable guideline that turns the request's examples into an exhaustive checklist | State the shared principle, its applicability, and required exceptions; keep illustrative examples as examples. |

An exact plan path or execution environment remains appropriate when the
project or an executable helper actually requires it.

## Verify and Return

For each rewrite, check a plausible variation within the intended scope:
does the artifact still satisfy the underlying requirement when incidental
details change? For conditional rules or decisions, also check a boundary
where they should not apply. Check that a reader can understand the artifact
without this conversation, that it describes actual semantics, and that the
original requirement still holds in its intended context. If the rewrite
loses actionable detail or domain meaning, restore the necessary specificity.

When editing is authorized, make the smallest relevant changes and reread the
resulting diff. Run checks that cover renamed references or changed behavior,
and the target artifact's validator when applicable. Record adopted decisions
and functional changes in the owning spec when development uses one. Report
what was grounded, what was preserved as a contract, and unresolved assumptions;
do not claim that wording or naming inspection verifies executable behavior.
