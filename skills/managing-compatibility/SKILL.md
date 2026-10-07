---
name: managing-compatibility
description: Use when changes to interfaces, retained or exchanged data, or observable behavior may affect existing usage, including compatibility and version-impact decisions for a release or upgrade.
---

# Managing Compatibility

Own the necessary alignment between the current interface, its callers, and
the data it must handle. Identifying an incompatibility is not completion:
implement and verify the required transition within the authorized change.

Keep one supported current interface in normal operation. Do not introduce
parallel old/new APIs, legacy compatibility wrappers, or dual-format runtime
branches. A bounded upgrade procedure may read old data and convert it without
making the old interface a supported product interface. Existing usage may
already work through the current interface without any special legacy path.

## Establish the affected contract

Inspect the actual contract and dependencies affected by the change:

- **Interfaces:** API or function signatures, import paths, CLI arguments,
  configuration keys, and the callers that use them.
- **Data:** Stored or exchanged formats, producers and consumers, and values
  or relationships that must survive a transition.
- **Behavior:** Defaults, units, ordering, error handling, and other observable
  meaning that existing usage relies on, even when the structure is unchanged.

Check declared runtime or dependency constraints when the change affects them;
do not invent an environment matrix for an unrelated edit. Compiling or parsing
successfully does not establish that required behavior or data meaning survives.

Distinguish disposable development data from data that must be preserved.
Drafts do not become supported contracts merely because they existed in Git;
retained data or independent consumers can exist before a public release.
Investigate unclear usage or retention when it changes the decision. Ask only
when a material fact or choice cannot be resolved from available project evidence.

## Make the necessary transition work

- **Existing usage still works:** Keep the one current implementation. Add no
  conversion or version machinery merely because code changed.
- **Callers must change:** Update the affected interface and controlled callers
  together. Establish how independently deployed consumers will transition;
  do not assume control over their updates or permission for downtime.
- **Required data does not fit:** Adapt the current implementation if it can use
  that data while satisfying the intended contract. Otherwise implement the
  necessary conversion into the current form. Preserve required values and
  meaning; do not silently invent missing information or discard retained data.
  Discard or regenerate data only when it is disposable under the actual policy.
- **A support obligation conflicts:** Resolve the actual obligation or transition
  choice before claiming completion. Do not silently add parallel interfaces or
  remove an existing promise to make the change appear ready.

Before changing retained data, establish the execution order and recovery for
interruption or failure that the operation requires. Reverting code alone may
not restore converted data. Keep conversion at the explicit transition boundary;
do not leave automatic old/new dispatch in normal application behavior.

Follow existing API and data-format identification rules. Do not reuse a format
identifier for incompatible retained data or add a version field for development
drafts. An edit, commit, push, or product release does not itself require a new
format version; apply a genuine external version contract when one exists.

## Verify and preserve the decision

Check the affected callers and current interface against representative required
data. For conversion, inspect the converted result and exercise it through the
current interface, including preservation of required values and behavior.
Use checks appropriate to the actual change. An internal edit with no contract
or retained-data impact needs no separate compatibility procedure.

When `developing-with-specs` appears in the current host's available-skills
list, use it to record derived requirements, chosen transitions, relevant
code/data identities, and evidence in the existing working spec and decision
history. Otherwise record those same items and their rationale in the project's
current specification or work record. Follow applicable project document
conventions and governing artifact workflows; do not create another
compatibility ledger. For claims about the resulting state, use
`verification-before-completion` when host-listed. Otherwise inspect the exact
target and representative required data, run the applicable interface and
conversion checks, and record results and limits. Do not infer availability
from a sibling vendor or cache folder.

## Assess release and upgrade readiness

For a requested release or established release trigger, identify the actual
candidate. For a versioned distribution, choose the product version from public
contract changes since the last actual release, when one exists, and the
project's versioning policy. An internal edit alone does not determine the
release type. Keep product versions separate from API or data-format identifiers;
changing a version number does not make incompatible data usable.

Carry the affected code/data identities, source and target contracts, verified
conversion tool or procedure when needed, required execution conditions, and
unresolved prerequisites into the project's release or upgrade procedure.
Treat missing required transition means or validation as an unresolved
prerequisite for the affected release or upgrade.
Prepare only version and upgrade artifacts that procedure requires. Follow
project document conventions or the designated documentation skill for any
required change or upgrade notes.

For package publication, prepare and verify the required upgrade means. Do not
claim that external live data has already been converted. For an authorized
deployment or upgrade, perform the required transition and verify the resulting
code/data state. Publication alone does not authorize live-data mutation; report
prepared, tested, and actually applied work accurately.
