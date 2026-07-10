---
id: state-summary-block
title: state-summary block
type: definition
requires: []
related: [cross-session-continuity]
entry_points: [state-summary block]
summary: >
  A short, fixed four-line status — done, next, blockers, and how far along — written at the end of every work session.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
state-summary block

<!-- depth:2 -->
<!-- provenance: extracted -->
A short, fixed four-line status — done, next, blockers, and how far along — written at the end of every work session.

<!-- depth:3 -->
<!-- provenance: extracted -->
The four-field block emitted at every ho close and every session end:
COMPLETED, NEXT, ACTION ITEMS / BLOCKS, PROJECT LIFECYCLE. Fixed labels and fixed order, so it is
both human-glanceable and machine-parseable — the universal minimum of **cross-session
continuity** and a hook surface for automation.
