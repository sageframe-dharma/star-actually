---
id: mutability
title: mutability (living / frozen / sealed)
type: concept
requires: []
related: [dogfood, hot-cold, kamae, reflect, seed, state-memory, supersedes]
entry_points: [mutability]
summary: >
  The scale of how much an artifact may change over its life — living (revised freely), frozen (changed only by override), or sealed (never again).
---

<!-- depth:1 -->
<!-- provenance: extracted -->
mutability (living / frozen / sealed)

<!-- depth:2 -->
<!-- provenance: extracted -->
The scale of how much an artifact may change over its life — living (revised freely), frozen (changed only by override), or sealed (never again).

<!-- depth:3 -->
<!-- provenance: extracted -->
The axis naming how an artifact changes over its
life. **living** — revised in place (README, overview, seed by dated revision, the Basis of
Design). **frozen** — not edited in place, changed only by a superseding addendum (system
design); thaw-able through the addendum mechanism, still governs the build. **sealed** —
final, the text never changes (closed hos, sidequests, addenda, dogfood findings,
devlogs/Reflect, executed ATs, propagation-ledger commits, sealed decisions); reopening carries
gravity — a sealed record is history (a future document may _respond_, nothing supersedes it in
force), a sealed decision's force yields only to a deliberate, recorded supersession.
Forward-only governs frozen and sealed; living is the declared exception — and the **state
memory (Kamae 6)** is living *and non-canonical*: the hot posture.

<!-- depth:4 -->
<!-- provenance: extracted -->
**Mutability regimes (cross-cutting).** Not every artifact has the same mutability. The corpus practices one axis with three
values — **living | frozen | sealed** — and naming them removes a recurring ambiguity in
forward-only's application: forward-only governs how *frozen* and *sealed* change
(supersede forward, never edit), while *living* is the declared exception (edited in place). […]
