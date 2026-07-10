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

<!-- depth:4 -->
<!-- provenance: extracted -->
**Ho Overview.** **What it is:** The sequence plan. What hos are needed, in what order, with what dependencies. This is the project arc made concrete — it turns the System Design and README scope into a buildable sequence of bounded sessions.

The Ho Overview is possible precisely because the upstream documents have already made the hard decisions. You can't plan a build order for a system whose architecture is undecided. You can't scope sessions for a project whose boundaries are undefined. The Seed established the core idea. The System Design committed to architecture. The README defined scope. The Ho Overview sequences the execution.

**What it's NOT:** The individual hos themselves. The Ho Overview says "Ho 3 implements the backup workflow: wake, SSH, syncoid, verify, shutdown." It does NOT provide the step-by-step instructions for doing that work. Those come from writing the actual ho using the appropriate template.

**What "done" looks like:**

The Ho Overview should define: […]

<!-- depth:5 -->
<!-- provenance: extracted -->
**The Build Record (K4 Extension).** The public counterpart to the hot file. An **append-only build-record log grafted onto the tail
of the K4 [[kamae-project-framing|ho overview]] (framework/structure/kamae-project-framing.md
§2.4)** — one entry per ho close and per replan checkpoint, each entry shaped as a
state-summary block (§3) with prose around it. Cleaner than the hot file, no hashes or traps:
the human's progress ledger.

It differs from the hot file on three axes:

| | Working-memory file (§4) | Build record (§8) |
|---|---|---|
| **Audience** | the next agent session | the practitioner + future agents |
| **Authority** | hot, mutable, non-canonical | cold, append-only, canonical |
| **Altitude** | dense, tactical, private | narrative, strategic, public |

The build record turns K4 from a pure forward plan into a plan with a running record grown onto
its tail — the forward plan above, the append-only ledger below. It is cold and forward-only:
entries are added, never rewritten. The convention is specified in
[[kamae-project-framing|kamae-project-framing §2.4]]
(framework/structure/kamae-project-framing.md); this document names its role in continuity.

---
