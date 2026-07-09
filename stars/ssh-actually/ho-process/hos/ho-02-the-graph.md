---
created: 2026-07-03
status: complete
type: ho
project: star-actually
ho: ho-02
title: The Graph
builds-on: ho-01-node-schema-and-parser
---

# ho-02 — The Graph

**Goal:** the weave stage. Cross-node validation, backlinks, neighborhoods, and the entry catalog — everything the render stage and the Receptionist consume.

## Scope

**In:** `star_actually.graph` — cross-node validation (every referenced id exists, no self-references, no cycles in `requires`), neighborhood computation (forward = requires-inverse; lateral = related-union; backlinks = all inbound edges), orphan and root-reachability warnings, catalog construction. `star_actually.config` — typed `site.yaml` loader.

**Out:** rendering (ho-03), search (ho-06).

## Decisions made here

- **Dangling references are errors by default, droppable by flag.** The content track runs parallel to the system track, so the graph is legitimately incomplete for weeks. `build_graph(..., allow_dangling=True)` drops unresolved edges and records warnings — the development mode. The default (strict) is what ho-08 integration and deployment use: a broken graph fails the build loudly.
- **`requires` cycles are errors, always.** A prerequisite loop is an editorial bug, not a rendering problem.
- **Orphans warn, never fail.** A node with no inbound edges and no outbound edges is suspicious but legal — the map review (ho-C-final) judges it.
- **Determinism everywhere:** neighborhoods sorted by node id; catalog sorted by id. Same nodes in, byte-identical site out.

## Verification

`make verify` green, coverage ≥90%; exemplar nodes weave with `allow_dangling=True` (their edges point at content-track nodes that don't exist yet — by design); strict mode rejects the same set with errors naming each dangling edge.
