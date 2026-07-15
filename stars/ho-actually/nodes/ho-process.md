---
id: ho-process
title: ho-process/
type: definition
requires: []
related: [kamae, readme]
entry_points: [ho-process/]
summary: >
  The project folder that holds the methodology's working artifacts—the framing documents, the session records, and the task specs.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
ho-process/

<!-- depth:2 -->
<!-- provenance: extracted -->
The project folder that holds the methodology's working artifacts—the framing documents, the session records, and the task specs.

<!-- depth:3 -->
<!-- provenance: extracted -->
The project directory holding the Ho System's artifacts: the Kamae
documents, `hos/`, `agent-tasks/`, and any project-specific layers (`learning/`, `notes/`,
`ideas.md`). The README lives at repo root, not here.

<!-- depth:4 -->
<!-- provenance: extracted -->
**Filenames and Location.** The single-instance Kamae documents live in the project repo under `ho-process/`, with the README at the repo root.

**Pattern:** `kamae-<N>-<project>-<doctype>.md` for documents 1, 2, 4, and 6. The README (Kamae 3) is the canonical repo-root `README.md` and does *not* take a `kamae-3-` prefix—it ships as the public face of the repository under its standard name.

| Kamae | Document | Path |
|---|---|---|
| 1 | Seed | `ho-process/kamae-1-<project>-seed.md` |
| 2 | System Design | `ho-process/kamae-2-<project>-system-design.md` |
| 3 | README | `README.md` (repo root) |
| 4 | Ho Overview | `ho-process/kamae-4-<project>-ho-overview.md` |
| 6 | State Memory | `ho-process/kamae-6-<project>-state-memory.md` (§2.7) |

`<project>` is the project's short slug in kebab-case (e.g., `shodo`, `hozo`, `kanyo`). It matches the slug used elsewhere in the project (repo name, package name) so the filenames are predictable from any one of them.

**Per-ho documents** (the Kamae 5 phase) live under `ho-process/hos/` and follow the [[ho-structure|ho filename convention]] (framework/structure/ho-structure.md §3.6): `ho-<number>-<slug>.md`. **Child agent-task specs** live under `ho-process/agent-tasks/` and follow `Ho-<NN>-AT-<NN>.md` (see [[ho-task-decomposition|Ho Task Decomposition]] (framework/structure/ho-task-decomposition.md) §4.2). […]
