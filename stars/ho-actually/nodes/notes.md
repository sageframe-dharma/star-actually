---
id: notes
title: notes/
type: definition
requires: []
related: [builds-on, ho-process]
entry_points: [notes/]
summary: >
  The folder where findings gathered before a session wait until some later session pulls them in.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
notes/

<!-- depth:2 -->
<!-- provenance: extracted -->
The folder where findings gathered before a session wait until some later session pulls them in.

<!-- depth:3 -->
<!-- provenance: extracted -->
The `ho-process/notes/` location where pre-ho findings live (dated finding
documents) before any ho consumes them via `builds-on:`. A location, not a first-class
artifact type. Its complement is `ideas.md`: **notes/ is evidence behind you; ideas.md is
intentions ahead of you.**

<!-- depth:4 -->
<!-- provenance: extracted -->
**Filenames and Location.** The four framing documents live in the project repo under `ho-process/`, with the README at the repo root.

**Pattern:** `kamae-<N>-<project>-<doctype>.md` for documents 1, 2, and 4. The README (Kamae 3) is the canonical repo-root `README.md` and does *not* take a `kamae-3-` prefix — it ships as the public face of the repository under its standard name.

| Kamae | Document | Path |
|---|---|---|
| 1 | Seed | `ho-process/kamae-1-<project>-seed.md` |
| 2 | System Design | `ho-process/kamae-2-<project>-system-design.md` |
| 3 | README | `README.md` (repo root) |
| 4 | Ho Overview | `ho-process/kamae-4-<project>-ho-overview.md` |

`<project>` is the project's short slug in kebab-case (e.g., `shodo`, `hozo`, `kanyo`). It matches the slug used elsewhere in the project (repo name, package name) so the filenames are predictable from any one of them.

**Per-ho documents** (the Kamae 5 phase) live under `ho-process/hos/` and follow the [[ho-structure|ho filename convention]] (framework/structure/ho-structure.md §3.6): `ho-<number>-<slug>.md`. **Child agent-task specs** live under `ho-process/agent-tasks/` and follow `Ho-<NN>-AT-<NN>.md` (see [[ho-task-decomposition|Ho Task Decomposition]] (framework/structure/ho-task-decomposition.md) §4.2). […]
