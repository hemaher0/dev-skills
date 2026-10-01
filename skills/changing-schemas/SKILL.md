---
name: changing-schemas
description: Use when changing a persisted or externally exchanged data shape and deciding whether existing data or consumers require conversion, compatibility support, or a format version.
---

# Changing Schemas

Make the change required by the current contract. A source edit, commit, push,
or product release does not itself create a new schema version. Development
drafts do not become supported formats merely because they existed in Git.

## Find the existing contract

Inspect the format, its readers and writers, stored data, deployment pattern,
and any documented support promise. Distinguish disposable development data
from data that must survive the change. A project can have retained data or
independently deployed consumers before its first public release.

If external usage or data retention is unclear and changes the decision,
investigate available evidence. Ask the decision owner only when that material
fact cannot be established from the project.

## Choose only the required work

- **Current format only:** When old data can be discarded or regenerated and
  no old consumer must continue, edit the current schema and its users. Do not
  create a version field or migration for intermediate development drafts.
- **Conversion:** When retained data or a deployed schema must change, use a
  conversion or migration suited to the actual storage and rollout. A
  completed one-time conversion does not by itself require permanent support
  for the old format.
- **Compatibility:** When supported old readers, writers, or data must coexist
  with the new form, define which combinations must work and for how long.
  Remove transitional behavior when that obligation ends.
- **Format version:** Add or advance a version discriminator when multiple
  supported formats must be distinguished at read time and the existing
  structure or metadata cannot distinguish them reliably, or when an actual
  external format contract requires one. A version denotes a supported format
  contract, not an edit count. Do not advance it for each schema edit, commit,
  push, or product release.

An optional field with a safe default may leave old data readable without a
migration. A field whose meaning changes while old and new records remain may
need an explicit discriminator even if its type stays the same. Apply the
project's existing version contract when one already exists; do not reuse an
identifier for incompatible retained data.

## Verify and record

Record the supported-format decision, conversion evidence, relevant code
identity, and retirement trigger in the task's working spec and decision
history. Update other project records only as requested or required, following
their locations, formats, and governing workflows. Use relevant installed
document guidance when it applies. When OpenSpec governs externally visible
behavior, keep its requirements and testable scenarios there.

Check the resulting behavior with representative old data or consumers when
conversion or compatibility is required. Record the supported formats,
transition plan, and retirement condition while more than one format is
supported. For a direct change to one disposable development format, use the
project's ordinary checks without creating a version inventory.
