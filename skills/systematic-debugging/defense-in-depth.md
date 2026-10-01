# Defense-in-Depth Validation

## Overview

When you fix a bug caused by invalid data, adding validation at one place feels sufficient. But that single check can be bypassed by different code paths, refactoring, or mocks.

**Core principle:** Validate independently exposed boundaries when invalid data
can bypass the primary correction. Select checks by the boundary's contract
and the identified failure path; every internal layer does not need a duplicate
check.

## Why Multiple Layers

One boundary check may be sufficient when all affected paths must pass through
it. Additional checks help when another entry path, trust boundary, or dangerous
operation can bypass that protection. Their presence alone does not establish
that the bug is impossible.

Different layers can address different cases:
- Entry validation rejects invalid input at an exposed API boundary
- Business logic enforces the operation's invariants
- Environment guards enforce context-specific constraints
- Debug logging supplies diagnostic evidence; it does not itself prevent failure

## Example Layers

Choose only the layers needed by the actual contract and failure paths. The
following examples illustrate different responsibilities, not a required stack.

### Layer 1: Entry Point Validation
**Purpose:** Reject obviously invalid input at API boundary

```typescript
function createProject(name: string, workingDirectory: string) {
  if (!workingDirectory || workingDirectory.trim() === '') {
    throw new Error('workingDirectory cannot be empty');
  }
  if (!existsSync(workingDirectory)) {
    throw new Error(`workingDirectory does not exist: ${workingDirectory}`);
  }
  if (!statSync(workingDirectory).isDirectory()) {
    throw new Error(`workingDirectory is not a directory: ${workingDirectory}`);
  }
  // ... proceed
}
```

### Layer 2: Business Logic Validation
**Purpose:** Ensure data makes sense for this operation

```typescript
function initializeWorkspace(projectDir: string, sessionId: string) {
  if (!projectDir) {
    throw new Error('projectDir required for workspace initialization');
  }
  // ... proceed
}
```

### Layer 3: Environment Guards
**Purpose:** Prevent dangerous operations in specific contexts

```typescript
async function gitInit(directory: string) {
  // In tests, refuse git init outside temp directories
  if (process.env.NODE_ENV === 'test') {
    const normalized = normalize(resolve(directory));
    const tmpDir = normalize(resolve(tmpdir()));

    if (!normalized.startsWith(tmpDir)) {
      throw new Error(
        `Refusing git init outside temp dir during tests: ${directory}`
      );
    }
  }
  // ... proceed
}
```

### Layer 4: Debug Instrumentation
**Purpose:** Capture context for forensics

```typescript
async function gitInit(directory: string) {
  const stack = new Error().stack;
  logger.debug('About to git init', {
    directory,
    cwd: process.cwd(),
    stack,
  });
  // ... proceed
}
```

## Applying the Pattern

When independently exposed paths justify this technique:

1. **Trace the data flow** - Where does bad value originate? Where used?
2. **Identify exposed checkpoints** - Determine which paths can bypass the primary check
3. **Add justified checks** - Enforce each affected boundary's contract; add diagnostics when evidence is missing
4. **Verify the protected paths** - Exercise relevant bypass paths and valid inputs using the existing TDD and verification workflows

## Example from Session

Bug: Empty `projectDir` caused `git init` in source code

**Data flow:**
1. Test setup → empty string
2. `Project.create(name, '')`
3. `WorkspaceManager.createWorkspace('')`
4. `git init` runs in `process.cwd()`

**Four layers added:**
- Layer 1: `Project.create()` validates not empty/exists/writable
- Layer 2: `WorkspaceManager` validates projectDir not empty
- Layer 3: `WorktreeManager` refuses git init outside tmpdir in tests
- Layer 4: Stack trace logging before git init

**Reported example result:** All 1847 tests passed and the original pollution
was not reproduced in those checks. This does not establish universal prevention.

## Key Insight

The session example reports reasons for using several layers:
- Different code paths bypassed entry validation
- Mocks bypassed business logic checks
- Edge cases on different platforms needed environment guards
- Debug logging identified structural misuse

Choose additional checks for demonstrated exposure or a governing boundary
contract. Avoid duplicating a guarantee already enforced for all affected paths.
