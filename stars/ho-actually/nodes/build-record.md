---
id: build-record
title: build record
type: definition
requires: []
related: [forward-only, ho-overview, replan-checkpoint, state-summary-block, working-memory-handoff]
entry_points: [build record]
summary: >
  A running, add-only list at the bottom of the build plan recording what each step actually finished and where the build stands.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
build record

<!-- depth:2 -->
<!-- provenance: extracted -->
A running, add-only list at the bottom of the build plan recording what each step actually finished and where the build stands.

<!-- depth:3 -->
<!-- provenance: extracted -->
The append-only log grafted onto the tail of the K4 **ho overview**: one
entry per ho close and per replan checkpoint, each shaped as a **state-summary block**, never
rewritten. Cold and forward-only — the human-facing, canonical ledger of what a build actually
did, the counterpart to the *hot* **working-memory handoff**.
