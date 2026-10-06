---
name: developing-with-specs
description: Use before and during software development to derive necessary requirements from user intent and project evidence, maintain a working spec and decision history, and verify the delivered result.
---

# Developing With Specs

Give implementation choices a purpose before acting. Connect the user's desired
result to necessary conditions, chosen solutions, planned work, and evidence
that the original result was achieved. Apply this throughout exploration,
planning, implementation, and verification, rather than as a separate phase.

## One Working Spec Per Work

Resolve `Scratchpad root` from effective project instructions or their existing
configuration source. A selected personal/checkout path in root
`AGENTS.local.md` overrides that location within project policy. An absent,
empty, or placeholder value is unset; use the project setting, then
`<project-root>/.kryptonite/scratchpad/` when neither supplies a path. Resolve
relative paths from that project root and use absolute paths as configured.
Installation follows the source README and its configuration template.
Ordinary development uses the resolution above without initializing unrelated
settings. Shared workflow, plan, documentation and retention rules stay
with their responsible owners.

Reuse the current work ID and existing working spec. For new work, the default
is `<resolved-scratchpad-root>/<work-id>/spec.md`. Keep the current spec and its
decision history together, identify the current owner and revision, and state
the actual path. Create only the needed directory and record. If the configured
location is unavailable, resolve that problem rather than silently substituting
another location. Do not move ongoing records just to adopt this layout.

Use the [spec template](templates/spec.md) when no project format applies.
Scale its content to the change; a small change can use a compact record with
the same distinctions and covering checks. These are local defaults, not a
requirement to introduce another project registry.

Read the request, governing contracts, and relevant repository evidence.
Existing formal specs remain authoritative. Reference their requirements
instead of copying a competing contract into the scratchpad. Use the owning
workflow when a formal contract needs changing; for OpenSpec-governed behavior,
the required change and delta-spec workflow still applies. A working spec or
plan alone does not replace that contract.

## Derive Requirements Before Choosing Means

Keep these categories distinct:

| Category | What establishes it |
| --- | --- |
| Requested requirement | The user's desired result, scope, or explicit constraint. |
| Governing constraint | An applicable project policy or formal contract, with its source. |
| Observed fact | Inspected behavior, interface, data, or environment, with evidence and limits. |
| Derived requirement | A condition needed for a requested result or governing constraint under the observed project conditions. |
| Selected solution | A chosen way to satisfy a requirement, with a purpose and rationale. |
| Assumption or open question | An unverified premise, its effect, and how and when to resolve it. |

Give requirements stable IDs. For a derived requirement, identify its parent
requirement or governing constraint, the evidence supporting the derivation,
and an observable acceptance criterion. Check whether the condition is actually
necessary in this project or only one possible implementation. An unsupported
derivation remains a proposal or assumption; it is not an established fact.

For example, a CSV export may need the project's existing access restrictions
to satisfy its governing authorization contract. Streaming is a selected means
whose justification depends on output size and resource constraints. Do not
promote that technique to a requirement merely because it is familiar.

Existing code establishes current behavior, not desired behavior. A preference,
"best practice," or passing implementation tests alone does not justify an
addition. Refine omitted necessities within existing authorization; consult the
user when a decision changes their goal, crosses the agreed scope, or needs
information or authority that cannot otherwise be obtained.

## Ground Consequential Choices

For a choice that materially affects the requested result, its interpretation,
or the cost of dependent work, connect its purpose to evidence that applies
under the actual conditions. Identify the unresolved premises, the consequence
of being wrong, and the check needed before later work relies on those premises.
Scale the evidence and verification effort to impact, uncertainty, and
reversibility. Applicable prior validation, authoritative sources, direct
observations, and supported tradeoffs can provide a basis; routine low-impact
details can use ordinary implementation judgment.

Treat a default or inherited choice as a candidate. Reuse it when its governing
source or evidence applies to the current goal and conditions; otherwise retain
the missing basis as an assumption. A selected means does not become a user
requirement through repetition, inclusion in a plan, or execution. Keep the
origin and evidential status of each consequential choice accurate as work moves
between design, implementation, and verification.

Give a consequential unresolved premise a resolution method and needed-by point.
An authorized investigation can obtain that evidence, and independent work can
continue. Resolve it before work whose validity or value depends on treating it
as true. Recording the uncertainty or passing a check for another claim does
not discharge it. When the premise concerns domain suitability, use the
available domain workflow or authoritative evidence alongside software checks;
no particular plugin, literature search, or exhaustive comparison is required.

## Record Purposeful Decisions and Changes

Before a material choice drives implementation, record the goal or requirement
it serves, why it is appropriate, its evidence or tradeoff, affected artifacts,
and the check that will assess it. Include alternatives when there is a real
choice; do not invent alternatives to fill a quota.

Record choices affecting requirements, observable behavior, interfaces, scope,
dependencies, verification, or consequential implementation strategy. Mechanical
work determined by an existing rule can reference it. Related choices can share
an entry when their purpose, basis, and affected work remain clear; a separate
entry for every editing action is unnecessary.

Keep the current body up to date and append material history with the actual
actor, stage or known time, prior expectation, change, reason, and impact.
Preserve earlier reasoning and link superseding decisions rather than erasing
them. Increment the spec revision for material requirement or decision changes.
Do not fabricate sources, timestamps, approval, or contemporaneous reasoning.
If a choice was recorded late, acknowledge that and reconcile its effects.

New facts can arise in a plan, implementation, review, or verification. Resolve
the affected spec, plan, and acceptance checks together before dependent work.
Identify evidence made stale by a relevant change and recheck that scope;
unaffected evidence need not be discarded. Do not silently weaken criteria or
redefine the goal to fit the implementation. Existing approval continues to
cover the same scope; honor actual user and project review gates.

## Keep Ownership Explicit

The current work owner reconciles the shared spec. Give an assignee the spec
path and revision, governing inputs, bounded scope, authority, and expected
report. Workers return proposed decisions and evidence in their assigned
records rather than independently overwriting the shared spec.

Use the [brief](../writing-agent-handoffs/templates/brief.md) and
[report](../writing-agent-handoffs/templates/report.md) when documented
delegation is needed: the requesting agent retains responsibility. A
[handoff](../writing-agent-handoffs/templates/handoff.md) transfers the named
scope to the next owner when recorded and made available, without requiring a
response or acknowledgement. Transfer unresolved questions and outstanding
requests with it; their reports follow the new owner. These semantics apply
to peers and subagents alike. Follow the existing
[role and record conventions](../writing-agent-handoffs/references/roles.md).
A report is evidence for the owner to assess, not automatic acceptance or a
grant of authority.

## Verify the Original Result and Preserve Its Basis

Check both whether the derived requirements and selected solutions remain
faithful to the user's intent and whether the delivered artifacts satisfy the
current spec. Verify the original requested outcome as well as its supporting
conditions. Tests generated from an implementation can miss the same omitted
requirement as that implementation; use the governing criteria and evidence
appropriate to the actual outcome. Record failures and unverified claims.

Write or update final durable documentation using project settings, then the
applicable documentation skill or procedure for unspecified details. Otherwise,
update relevant existing documents or create a necessary `docs/<topic>.md`
outside `.kryptonite`. Preserve the applied behavior, scope, necessary
derivations, decision rationale, governing references, and verification basis.
Accurate existing documents can be reused; a routine commit does not require
a new final document. Present the durable references and scoped results, and
the applied spec and history while they remain available.

Supply that document owner with the reconciled requirements/criteria, spec
revision, actual artifacts, review outcomes, and covering evidence. Resolve
returned conflicts in the affected spec/plan/evidence before dependent work.
Preserve necessary applied information in durable sources; references to
temporary files scheduled for disposal cannot be the only retained basis.
Documentation ownership does not transfer implementation scheduling, technical
verdicts, or temporary-record retention authority.

Use [using-kryptonite](../using-kryptonite/SKILL.md) to route requested commit
preparation. This skill supplies its governing requirements and documentation
basis; it does not authorize Git operations or define another commit schedule.

Dispose of only this completed work's temporary spec and related artifacts
within existing authority, after needed information is preserved durably and
required stages are complete. Honor project retention and explicit deferrals;
keep records needed by remaining work, outstanding requests, or the next owner.
Use [writing-agent-handoffs](../writing-agent-handoffs/SKILL.md) for communication
records. A commit, review, or handoff alone does not satisfy these conditions,
and Git resource cleanup is a separate decision. A temporary spec must not
remain the only reference for delivered behavior after disposal.

## Design Basis

These writing rules adapt requirement traceability and validation from the
[NASA handbook](https://www.nasa.gov/reference/system-engineering-handbook-appendix/),
artifact reconciliation from
[Spec Kit](https://github.github.io/spec-kit/guides/evolving-specs.html), and
decision rationale and history from
[Microsoft's ADR guidance](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record).
[WiseSpec](https://arxiv.org/html/2609.00568v1) investigates structured,
iteratively refined requirements for coding agents. These sources inform the
design; they do not establish this template or path convention as a standard
or prove that it improves agent performance.
