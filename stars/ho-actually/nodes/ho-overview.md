---
id: ho-overview
title: ho overview
type: definition
requires: []
related: [build-record, kamae, phase]
entry_points: [ho overview]
summary: >
  The build's directional plan, grouping the planned steps into themed clusters with checkpoints and named milestones.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
ho overview

<!-- depth:2 -->
<!-- provenance: extracted -->
The build's directional plan, grouping the planned steps into themed clusters with checkpoints and named milestones.

<!-- depth:3 -->
<!-- provenance: extracted -->
The Kamae 4 document: the build's directional plan — phases first, hos
within phases, decisions inline with the ho that resolves them, replan checkpoints, release
tags at phase boundaries. A living document; the map, not the territory.

<!-- depth:4 -->
<!-- provenance: extracted -->
**Ho Overview.** **What it is:** The sequence plan. What hos are needed, in what order, with what dependencies. This is the project arc made concrete — it turns the System Design and README scope into a buildable sequence of bounded sessions.

The Ho Overview is possible precisely because the upstream documents have already made the hard decisions. You can't plan a build order for a system whose architecture is undecided. You can't scope sessions for a project whose boundaries are undefined. The Seed established the core idea. The System Design committed to architecture. The README defined scope. The Ho Overview sequences the execution.

**What it's NOT:** The individual hos themselves. The Ho Overview says "Ho 3 implements the backup workflow: wake, SSH, syncoid, verify, shutdown." It does NOT provide the step-by-step instructions for doing that work. Those come from writing the actual ho using the appropriate template.

**What "done" looks like:**

The Ho Overview should define: […]
