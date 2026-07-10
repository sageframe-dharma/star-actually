---
id: cross-session-continuity
title: cross-session continuity
type: definition
requires: []
related: [hot-cold, state-memory, state-summary-block, working-memory-handoff]
entry_points: [cross-session continuity]
summary: >
  Keeping track of where a build is between work sessions, especially when no person is there to remember it.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
cross-session continuity

<!-- depth:2 -->
<!-- provenance: extracted -->
Keeping track of where a build is between work sessions, especially when no person is there to remember it.

<!-- depth:3 -->
<!-- provenance: extracted -->
Carrying a build's thread across sessions when the human is not
the one holding it. Continuity is *implicit* everywhere — the cold record (git, Reflect, the
build record) carries the thread as a side effect of being well-kept — and *explicit* in one
place: the **state memory (Kamae 6)**, always present, with the universal **state-summary
block** at its top and the **working-memory handoff** body grown by event-gated accretion.
Kept honest by the freshness, **hot / cold**, and graduated-compaction disciplines. Promoted
from the pālana pilot.
