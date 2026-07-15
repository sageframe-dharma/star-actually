---
id: cross-session-continuity
title: cross-session continuity
type: definition
requires: []
related: [devlog, forward-only, hot-cold, state-memory, state-summary-block, working-memory-handoff]
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
the one holding it. Continuity is *implicit* everywhere—the cold record (git, Reflect, the
build record) carries the thread as a side effect of being well-kept—and *explicit* in one
place: the **state memory (Kamae 6)**, always present, with the universal **state-summary
block** at its top and the **working-memory handoff** body grown by event-gated accretion.
Kept honest by the freshness, **hot / cold**, and graduated-compaction disciplines. Promoted
from the pālana pilot.

<!-- depth:4 -->
<!-- provenance: extracted -->
**The Problem the Framework Leaves.** The Ho System's answer to continuity across sessions is *documents as memory*. A fresh agent
arrives with no context and reads its way in: the README, the system design, the ho overview,
the relevant ho, the code. The bounded-session discipline keeps each session in clean context;
the [[devlog|Reflect phase]] (framework/structure/devlog.md) banks what each ho learned; the
forward-only principle keeps the record honest; `builds-on:` frontmatter gives the reading
order. That model works—and it rests on an assumption the framework never states out loud:
**a human carries the thread.** The practitioner remembers the last session, holds the
architectural intent, drives planning mode, and is the watching presence that catches drift.
The [[operating-discipline|operating discipline]] (practitioner/operating-discipline.md) names
this directly—*"the practitioner is the continuity,"* *"the presence is the verification."*

Remove the human from between sessions and two roles the whole model rests on vanish: **holding
intent across sessions**, and **being the verification presence**. The
pālana pilot—the first fully autonomous Ho build ([[continuity-discipline|5.3]]
(examples/palana-autonomous/continuity-discipline.md))—ran a multi-session build where the
agent's context window was wiped between sessions and the agent itself had to reconstitute the
entire build state from written artifacts alone. It evolved a system to fill exactly that gap.
This document promotes the load-bearing parts of that system into doctrine. […]
