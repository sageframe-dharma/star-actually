---
id: mutability
title: mutability (living / frozen / sealed)
type: concept
requires: []
related: [dogfood, reflect, seed, supersedes]
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
final, never changes (closed hos, sidequests, addenda, dogfood findings, devlogs/Reflect,
executed ATs, propagation-ledger commits); a future document may _respond_ but nothing
supersedes it in force. Forward-only governs frozen and sealed; living is the declared exception.

<!-- depth:4 -->
<!-- provenance: extracted -->
**Mutability regimes (cross-cutting).** Not every artifact has the same mutability. The corpus practices one axis with three
values — **living | frozen | sealed** — and naming them removes a recurring ambiguity in
forward-only's application: forward-only governs how *frozen* and *sealed* change
(supersede forward, never edit), while *living* is the declared exception (edited in place).

| Value | Applies to | Rule |
|---|---|---|
| **living** | README (kamae-3), ho overview (kamae-4), seed (kamae-1, see note), the Basis of Design (2.11) | Edited in place as the project evolves. Overview edits are forward-looking only: dead numbers stay dead, checkpoint outcomes get recorded, historical entries aren't rewritten. "Small frequent updates beat large rare ones" (sharibako kamae-4). |
| **frozen** | System design (kamae-2) | Not edited in place; changed only by a superseding addendum. Body preserved as-authored; a reader's-note pointer at the top names the addenda; the addenda carry the change (sharibako kamae-2 + 2.1 + 2.2). Thaw-able through the addendum mechanism, and still governs the build. |
| **sealed** | Closed hos, sidequests, addenda, dogfood findings, devlogs/Reflect, executed ATs, propagation-ledger commits | Final — never changes. Typographical fixes only; anything that changes what the document *said* belongs in a new document. A future document may *respond* (forward-only), but nothing supersedes it in force — it is already history. | […]
