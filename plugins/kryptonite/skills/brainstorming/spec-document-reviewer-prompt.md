# Spec Document Reviewer Prompt Template

Use this prompt for an independent spec review when needed and delegation is
authorized. Otherwise apply its checks directly. Review is read-only for the
artifacts under review.

**Purpose:** Check that the spec represents the requested result, justified
necessary conditions, and a usable basis for planning.

**Inputs:** Actual spec path and revision, original request reference, governing
contracts, and relevant project evidence. Do not substitute the spec's own
assertions for checking their sources.

```text
You are reviewing a working spec before dependent planning or implementation.

Spec and revision: [SPEC_FILE_PATH_AND_REVISION]
Original request: [REQUEST_REFERENCE]
Governing contracts and project evidence: [SOURCE_REFERENCES]
Assigned review scope: [REVIEW_SCOPE]

Check:
- Intent: Is the original observable result preserved?
- Derivation: Are necessary conditions missing? Are added requirements linked
  to a goal or governing constraint with supporting evidence?
- Distinctions: Are facts, derived requirements, selected means, and assumptions
  kept distinct, rather than presenting a habitual solution as necessary?
- Consistency and scope: Are there contradictions or unsupported additions?
- Verifiability: Do criteria cover the original result as well as its parts?
- Readiness: Can downstream work proceed without a material guess? Open questions
  are acceptable if their impact, resolution, and dependency boundary are clear.

Flag issues with a concrete effect on correctness, scope, or downstream work.
Do not block for style, section length, a missing optional section, or an
explicit nonblocking unknown. A proposed necessity is not scope creep merely
because the user did not name it; inspect its actual derivation.

Return:
Status: Approved | Issues Found
Reviewed spec revision and source references
Issues: requirement/section, evidence, why it matters, affected work
Verification limits or unresolved source questions
Advisory recommendations, if useful
```

Approval is a scoped review verdict. It does not replace required user decisions,
transfer responsibility, or authorize implementation or external actions.
