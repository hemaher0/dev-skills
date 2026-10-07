# Root Cause Tracing

## Overview

Bugs often manifest deep in the call stack (git init in wrong directory, file created in wrong location, database opened with wrong path). Your instinct is to fix where the error appears, but that's treating a symptom.

**Core principle:** Trace backward through the relevant call chain to locate the
original trigger, then choose a correction supported by that evidence.

## When to Use

Trace callers when the observed failure does not explain where an invalid
value or operation originated. If the trace is unavailable, identify the
missing evidence instead of assuming a correction at the symptom establishes
the cause. Use the [debugging workflow](SKILL.md) for bounded mitigation and
unresolved diagnosis. Consider [defense-in-depth](defense-in-depth.md) when
independent paths could bypass the supported correction.

**Use when:**
- Error happens deep in execution (not at entry point)
- Stack trace shows long call chain
- Unclear where invalid data originated
- Need to find which test/code triggers the problem

## The Tracing Process

### 1. Observe the Symptom
```
Error: git init failed in ~/project/packages/core
```

### 2. Find Immediate Cause
**What code directly causes this?**
```typescript
await execFileAsync('git', ['init'], { cwd: projectDir });
```

### 3. Ask: What Called This?
```typescript
WorktreeManager.createSessionWorktree(projectDir, sessionId)
  → called by Session.initializeWorkspace()
  → called by Session.create()
  → called by test at Project.create()
```

### 4. Keep Tracing Up
**What value was passed?**
- `projectDir = ''` (empty string!)
- Empty string as `cwd` resolves to `process.cwd()`
- That's the source code directory!

### 5. Find Original Trigger
**Where did empty string come from?**
```typescript
const context = setupCoreTest(); // Returns { tempDir: '' }
Project.create('name', context.tempDir); // Accessed before beforeEach!
```

## Adding Stack Traces

When you can't trace manually, add instrumentation:

```typescript
// Before the problematic operation
async function gitInit(directory: string) {
  const stack = new Error().stack;
  console.error('DEBUG git init:', {
    directory,
    cwd: process.cwd(),
    nodeEnv: process.env.NODE_ENV,
    stack,
  });

  await execFileAsync('git', ['init'], { cwd: directory });
}
```

Use diagnostics observable in the actual test/runtime capture. The example
uses `console.error()`; a configured logger, trace collector or debugger can
serve the same purpose. Verify the evidence is available before relying on it.

**Run and capture:**
```bash
npm test 2>&1 | grep 'DEBUG git init'
```

**Analyze stack traces:**
- Look for test file names
- Find the line number triggering the call
- Identify the pattern (same test? same parameter?)

## Finding Which Test Causes Pollution

If something appears during tests but you don't know which test:

Resolve the directory containing this loaded `systematic-debugging` skill and
invoke its bundled `find-polluter.sh`; do not assume the project root contains
the script:

```bash
/path/to/resolved/systematic-debugging-skill/find-polluter.sh '.git' 'src/**/*.test.ts'
```

Runs tests one-by-one, stops at first polluter. See script for usage.
Failed commands, skipped runs, and an empty test selection produce an
incomplete-verification result, not a clean verdict. Inspect a reported failed
command before using absence of pollution as evidence.

## Real Example: Empty projectDir

**Symptom:** `.git` created in `packages/core/` (source code)

**Trace chain:**
1. `git init` runs in `process.cwd()` ← empty cwd parameter
2. WorktreeManager called with empty projectDir
3. Session.create() passed empty string
4. Test accessed `context.tempDir` before beforeEach
5. setupCoreTest() returns `{ tempDir: '' }` initially

**Root cause:** Top-level variable initialization accessing empty value

**Fix:** Made tempDir a getter that throws if accessed before beforeEach

**Also added defense-in-depth:**
- Layer 1: Project.create() validates directory
- Layer 2: WorkspaceManager validates not empty
- Layer 3: NODE_ENV guard refuses git init outside tmpdir
- Layer 4: Stack trace logging before git init

## Key Principle

An immediate failure location is not necessarily the original trigger. Trace
far enough to distinguish the suspected origin from plausible alternatives,
then check the correction against the original symptom. Additional validation
needs an identified bypass path or boundary responsibility; passing checks do
not establish that a bug is impossible. Report an evidence gap when the trace
cannot establish the cause.

## Stack Trace Tips

**In tests:** Choose an output channel the runner actually captures
**Before operation:** Log before the dangerous operation, not after it fails
**Include context:** Directory, cwd, environment variables, timestamps
**Capture stack:** Use the available stack and relevant correlation data;
async boundaries can require additional evidence to connect the path
