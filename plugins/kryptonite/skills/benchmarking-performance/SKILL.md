---
name: benchmarking-performance
description: Use when designing or checking a software performance measurement, comparing implementations or configurations, or reporting a measured speedup, slowdown, latency, throughput, or resource cost.
---

# Benchmarking Performance

Measure the work the claim describes, under conditions that support the intended
decision. Separate a measured difference from its causal explanation and its
importance to users. A fast error, skipped operation or changed workload is not
evidence of a faster implementation.

## Define the claim and comparison

State the proposed claim, metric and unit, workload, timing boundary, relevant
quality or correctness requirements, and the decision it informs. Distinguish
an exploratory estimate from a comparison used to select an implementation.
Use the task's authorized resource budget and execution environment. This
skill does not grant permission to start costly jobs or change allocations.

Read the measurement harness before trusting its output. Record the revisions,
dependencies, build mode, hardware, concurrency and material settings. Identify
what is timed, excluded, counted and checked. Reuse existing harnesses when they
can answer the question; do not create a new benchmark framework by default.

For scientific quality or research conclusions, use the project's domain
protocol as well. Timing evidence alone does not establish model quality,
experimental validity or the appropriateness of a research comparison.

## Establish a meaningful run

- **The work happened:** confirm outputs or work counters correspond to the
  intended operations inside the measured boundary. Await asynchronous work,
  consume lazy results, and synchronize device work when required by the
  runtime's supported timing method. Distinguish enqueue time from completion.
- **The result is valid:** check outputs and count errors, skipped work,
  timeouts and retries. Verify that both sides meet the same required quality.
- **The comparison is fair:** hold workload and relevant conditions constant,
  except for the intended variable. Document tuning, cache state, batching,
  startup and warmup. A comparison of shipped defaults is legitimate when that
  is the decision; label it as such rather than attributing everything to the
  underlying implementation.
- **The host is understood:** inspect competing load and allocation. Isolate
  or balance interference within existing authority; do not stop unrelated
  work. Report interference that cannot be controlled.
- **The magnitude is plausible:** compare the claimed change with measured
  component shares, resource capacity and work counts. Investigate implausible
  improvements before treating them as wins.

Choose sample size, order and stopping criteria for variability and the decision
stakes. Interleave or randomize alternatives when drift would bias a fixed
order. Use appropriate warm or cold conditions and independent repetitions;
request-level samples within one run are not automatically independent runs.
Do not stop at the first favorable result or select only successful runs.

An explicitly requested rough estimate can use a single observed run, labeled
as such, with work and output checks intact. It cannot establish repeatability
or a reliable winner. If the available budget cannot distinguish the sides,
report the comparison as inconclusive instead of inventing precision.

## Explain and assess the result

Use profiles or counters to locate a suspected limiter and map it to the code.
Collect intrusive profiling separately from the timings used for the comparison,
unless instrumentation is itself part of the workload. Check the load generator
as well as the system under test. Distinguish a measured bottleneck from a guess.

Investigate alternative explanations such as caching, invalid output, less work,
unequal configuration and contention. A reproducible measured difference can be
reported while its cause remains unknown; mark that causal limit. When the
question is why the result changed, unresolved causation remains unfinished.

Measure the relevant end-to-end path before making an end-to-end claim from a
microbenchmark. Report a component result within its actual scope and its share
of total cost. Include tradeoffs such as memory, throughput versus latency,
startup cost and output quality when they affect the decision.

When host-listed, use `systematic-debugging` for unexpected measurements and
`verification-before-completion` for the final claim, resolving their exact
installed locations. Otherwise test a discriminating explanation with the
available evidence and match each conclusion to the actual checked outcome.

## Report

Give the supported verdict, workload, revisions, metric and units, run count,
summary statistic and spread or uncertainty. Preserve run data and exact
commands in the existing artifact location so the comparison can be repeated.
State correctness/error checks, observed limiter or unknown cause, material
conditions, end-to-end coverage and remaining uncertainty. Distinguish no
detected difference from proof of equivalence.

## Design basis

Adapted from pstack's [benchmark checklist](https://github.com/cursor/plugins/blob/main/pstack/skills/benchmark-checklist/SKILL.md)
and [explain-the-number principle](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-explain-the-number/SKILL.md).
Repetition and evidence requirements here follow the claim and available
resources rather than a fixed run count or mandatory profiling tool.
