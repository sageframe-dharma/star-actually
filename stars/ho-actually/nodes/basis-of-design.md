---
id: basis-of-design
title: Basis of Design
type: definition
requires: []
related: [propagation-ledger]
entry_points: [basis of design]
summary: >
  The one file that holds a project's settled design values as explicit numbers, the source of truth everything else builds from.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Basis of Design

<!-- depth:2 -->
<!-- provenance: extracted -->
The one file that holds a project's settled design values as explicit numbers, the source of truth everything else builds from.

<!-- depth:3 -->
<!-- provenance: extracted -->
The single file holding a project's landed design decisions as
explicit numeric parameters — the source of truth the tuners land into, the spikes
validate against, and the implementation ports from. Holds the _frozen_ values at any
moment (the _living_ happens in the **propagation ledger**): the file itself is living —
propagated with named-reason commits only — while each landed value is frozen until a
propagation moves it. Generalizes past visual to any
design parameter, interaction thresholds included. Named from the AEC term of art; not a
"register" (see _architectural register_).

<!-- depth:4 -->
<!-- provenance: extracted -->
**The eight steps.** Recorded from the primary source; the specific decisions are the project's, the
method transfers. […]
