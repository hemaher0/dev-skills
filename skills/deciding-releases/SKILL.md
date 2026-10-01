---
name: deciding-releases
description: Use when deciding whether a code change, commit, merge, or push calls for a version bump, release notes, tag, or publication, or when preparing a requested release.
---

# Deciding Releases

Treat a Git operation, a development change, and a release as separate
decisions. Work can accumulate before a release without advancing the product
or plugin version for every commit or push.

## Establish the trigger

Identify the user's requested outcome and the repository's existing release
procedure. Inspect relevant CI, marketplace, or publishing configuration when
a Git action may change what others can install or trigger publication. A
commit, merge, or push alone does not call for a version bump, release notes,
tag, or manual release.

If an existing workflow publishes on the requested Git action, or installers
read the target branch directly, account for that effect before performing it.
Apply the repository's publication checks and resolve any missing authority.
Do not create a second manual release just because automation will publish
one.

## When a release is actually due

For an explicitly requested release or an established release trigger, inspect
the last release, changes since then, the project's versioning policy, and
required notes, tags, assets, and checks. Prepare only the artifacts that
policy calls for. Choose the version from the supported public contract and
the project's convention; an internal schema edit does not automatically
require a major version.

When release notes are required, route their placement, writing, and review
through an available document-routing skill, with the release policy and
verified change list. If none is available, use the repository's document
conventions, local schema when present, and ordinary file tools. This skill
retains the release decision and version choice.

Keep schema format versions separate from product or plugin release versions.
Do not add a release version to a project that has no versioned distribution
merely because it was deployed. Do not advance a plugin manifest version only
to accompany a source push; do that when preparing the plugin release under
its actual policy. Keep temporary local preview identifiers out of published
source.

Report the Git action and any release action separately. Verify each outcome
before claiming it occurred.
