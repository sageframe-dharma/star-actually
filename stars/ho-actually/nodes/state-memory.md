---
id: state-memory
title: state memory (Kamae 6)
type: definition
requires: []
related: [ho-process, hot-cold, kamae, state-summary-block, working-memory-handoff]
entry_points: [state memory]
summary: >
  One always-present file per project holding where the build is, so any new session can pick it up.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
state memory (Kamae 6)

<!-- depth:2 -->
<!-- provenance: extracted -->
One always-present file per project holding where the build is, so any new session can pick it up.

<!-- depth:3 -->
<!-- provenance: extracted -->
The project's living cross-session memory: the sixth Kamae link, a
single always-present file (`ho-process/kamae-6-<project>-state-memory.md`) that a returning
session reads first to get back into stance. Carries the **state-summary block** at its top
(always) and the **working-memory handoff** body beneath, grown by event-gated accretion —
sections switch on as the build first needs them. Private by default, published only by
closeout election; hot and non-canonical; kept honest by the freshness and **hot / cold**
rules and by graduated compaction.

<!-- depth:4 -->
<!-- provenance: extracted -->
**Kamae 6: State Memory.** **What it is:** The build's living cross-session memory — one per project, always present, written continuously as the build runs. The four framing documents (§§2.1–2.4) get the *project* into stance once; the per-ho documents (§2.5) get each *session* into stance; the State Memory is how a *returning* session gets back into stance after its context is wiped. It is the first thing a fresh agent reads to reconstitute where the build is, without re-deriving it from the whole chain. Alone among the six links it is *living and reflexive* — never "done" until the project is, and holding the running state of the other five so a new session can pick them up. […]
