---
id: sidequest
title: sidequest
type: definition
requires: []
related: [dogfood, graded-eval, phase, supersedes]
entry_points: [sidequest]
summary: >
  A bounded, detachable line of work inside a project, with its own folder, numbering, and its own check that it worked.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
sidequest

<!-- depth:2 -->
<!-- provenance: extracted -->
A bounded, detachable line of work inside a project, with its own folder, numbering, and its own check that it worked.

<!-- depth:3 -->
<!-- provenance: extracted -->
A bounded, severable capability _arc_ inside a project: its own folder, its
own phase-overview (`type: ho-overview-phase`), local letter-prefixed numbering (ho-A1…), an
explicit `supersedes:` against the main overview (bidirectional), its own validation pass
(in shodo's case, an eval). It is _work_, an arc—the counterpart to the dogfood finding's record. (The earlier "sidequest =
emergent record" definition was a mislabeling, now corrected—those files are dogfood
findings.)

<!-- depth:4 -->
<!-- provenance: extracted -->
**Sidequest.** **Purpose:** a bounded, severable capability chain *inside* a project—a full
feature/build developed within the project that wants its own ordered arc without
becoming a separate project ("the work is a capability, not a separate project—no
separate seed, system design, or README," shodo Subproject-A phase overview). It is
*work*, an arc—not a record. shodo's ingest/harvest engine (Subproject-A-Harvester)
is the canonical example.
**Structural signature:**

- Its own folder under `ho-process/hos/` (`Subproject-A-Harvester/`)
- Its own phase-overview document: `type: ho-overview-phase`, `stage: kamae-4`,
 `subproject:` field—a mini-Kamae-4 fragment with local scope
- Local ho numbering with a letter prefix (ho-A1 … ho-A5)
- An explicit `supersedes:` clause against the specific main-kamae-4 bullet the
 sidequest overtakes, plus a documented cascade reading order
- Its own validation pass (in shodo's case, an eval) and release-tag consequences […]
