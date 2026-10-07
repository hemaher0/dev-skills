# Writing Good Tests

Use this reference when adding or changing a test, selecting a test double,
or investigating brittle coverage. The [owning skill](SKILL.md) determines
whether a new test is warranted; this reference does not require one for every
change.

## Name the Behavior and the Evidence

Identify the governing criterion and the plausible wrong behavior the test
would catch: a rejected valid input, accepted invalid input, missing state
change, incorrect result, or violated boundary contract. Test at a useful
consumer boundary and reuse an existing case when it already protects that risk.

For new or intentionally changed behavior, derive expected results from
requirements, independently checked fixtures, properties, or a genuinely
independent reference. Concrete input/output examples can clarify an ambiguous
requirement before implementation. Reusing the candidate's own helpers on both
sides can reproduce the same defect:

```typescript
// Both sides reuse the same implementation: no independent oracle.
const expected = buildSearchQuery({ tag: 'urgent' });
expect(buildSearchQuery({ tag: 'urgent' })).toBe(expected);

// A specified output, independently derived from the query contract.
expect(buildSearchQuery({ tag: 'urgent' })).toBe('tag:"urgent"');
```

To preserve existing behavior, a pre-change execution or retained baseline can
supply expectations. Capture selected inputs and relevant outputs, errors, or
effects with their source revision or snapshot; keep the expectation independent
of the implementation being transformed. Do not compute both sides using the
same current implementation or regenerate a snapshot merely to match new output.

A characterization test may pass immediately and can document behavior whose
correctness is still unknown. Label it as an observation, not approval of the
behavior. A known correction needs a separately justified desired expectation.
Do not add a wrong expectation, forced assertion failure, or artificial
production fault just to make a useful test start red.

## Distinguish Contracts From Change Detectors

Prefer results, state, and externally meaningful effects over private structure,
helper names, or copied source text. A test that reproduces the implementation
can break during harmless refactoring while missing incorrect behavior.

Exact constants, text, field names, and formats are valid expectations when
they are part of an actual contract, such as a serialized protocol or required
error code. Ordinary copy or formatting changes can instead be inspected
directly. Explain the consumer consequence rather than asserting every literal.

Exercise scripts and executable configuration through meaningful outputs,
effects, or applicable validators. Syntax/schema validation can be useful
without proving runtime behavior. For human prose, inspect accuracy and links;
for agent instructions, use the owning skill-validation workflow when warranted.
Do not turn every document edit into a text-matching regression suite.

Keep assertions stable through behavior-preserving refactoring. Inspect an
internal detail only for a concrete contract or risk that an outcome check
cannot adequately establish.

Test imports, fixture wiring, and setup can change with the structure. Preserve
the checked outcomes and relevant cases, and confirm the revised test still
exercises the consumer contract. Changing an assertion needs an independent
reason, such as an intentional requirement change or a demonstrated flaw in
the old check. Retain that reason in the existing work record; implementation
changes alone do not justify weaker assertions or different expected results.

## Use Test Doubles for a Concrete Boundary

Prefer the real component when its execution is practical and controlled.
Use an appropriate maintained fake when the real dependency is slow, unstable,
or external; use a bounded mock or spy when it is the useful way to exercise
a boundary or hard-to-trigger condition. Keep the behavior under test real.

A double's configured result or mere presence is not evidence of production
behavior. Assert what the real component does with it. Interaction assertions
are useful when payload, call count, or ordering is contractual, such as
enqueuing one job or preserving transaction order; they need not be forbidden.
Avoid checking incidental helper calls just because the implementation uses them.

Represent the dependency's relevant data shape, errors, and side effects
accurately. Preserve the fields and effects the checked contract depends on;
a deliberately scoped projection need not copy an unrelated full response.
State a double's limits when broader integration behavior is not exercised.

Reuse existing doubles and fixtures where appropriate. If mock setup starts
encoding the implementation or maintaining a parallel system, consider a
real-component or integration check that better answers the question. Do not
assume every test needs live external services.

## Keep Tests Reliable and Maintainable

Use controlled inputs, clocks, randomness, and cleanup where the behavior needs
them. Avoid arbitrary sleeps and reliance on another test's execution order.
Run relevant existing cases alongside changed ones; broader runs need a concrete
risk or project requirement.

Put test-only fixture and cleanup machinery in test utilities. Preserve a
production lifecycle method when its contract requires it, even if tests are
its only visible local callers. Do not expose private state or add a production
API merely to make an incidental assertion possible.

Before keeping a test, ask what plausible wrong result it distinguishes and
whether another test already covers that risk. An optional focused mutation
check can help investigate uncertain coverage, but no mutation tool, exhaustive
mutation score, or manufactured RED is required. A passing test alone does not
prove every requirement; report its actual target and coverage.

## Engineering References

These sources inform the local guidance rather than prescribe this exact
workflow or establish its effectiveness for agents:

- [Test behavior, not implementation](https://testing.googleblog.com/2013/08/testing-on-toilet-test-behavior-not.html)
  explains why public behavior usually gives more stable tests than structure.
- [Change-detector tests](https://testing.googleblog.com/2015/01/testing-on-toilet-change-detector-tests.html)
  describes maintenance cost without adequate defect detection.
- [Test fidelity and doubles](https://testing.googleblog.com/2024/02/increase-test-fidelity-by-avoiding-mocks.html)
  discusses real implementations, fakes, and mocks with their tradeoffs.
- [TiCoder](https://arxiv.org/abs/2404.10100) uses user-approved test examples to
  clarify intent in generated code; its study does not establish universal
  superiority of strict test-first ordering.
- [Test-guarded refactoring case study](https://arxiv.org/abs/2604.03135) separates
  baseline test construction from constrained refactoring in one frontend
  codebase; its test infrastructure is not a requirement for every change.
- [Differential evaluation of LLM refactoring](https://arxiv.org/abs/2602.15761)
  finds behavior differences missed by existing tests. It motivates checking
  consequential coverage gaps, not mandatory fuzzing or a universal failure rate.
- [LLM refactoring quality study](https://arxiv.org/abs/2601.13139) distinguishes
  behavioral checks, structural metrics, and automated readability scores;
  improved metrics alone do not establish better human understanding.
