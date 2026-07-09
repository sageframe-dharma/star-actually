---
id: release-tag
title: release tag
type: definition
requires: []
related: [phase]
entry_points: [release tag]
summary: >
  A tagged commit marking the end of a build stage, forcing a done/not-done call and leaving a rollback point.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
release tag

<!-- depth:2 -->
<!-- provenance: extracted -->
A tagged commit marking the end of a build stage, forcing a done/not-done call and leaving a rollback point.

<!-- depth:3 -->
<!-- provenance: extracted -->
The tagged commit at a phase boundary (v0.1 … v1.0): each completed phase
produces a release, forcing a "done" judgment and a rollback point.
