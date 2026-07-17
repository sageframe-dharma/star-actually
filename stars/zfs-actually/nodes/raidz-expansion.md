---
id: raidz-expansion
title: RAIDZ Expansion
type: definition
requires: [raidz]
related: [vdev]
entry_points:
  - can i add a disk to raidz
  - grow raidz
  - raidz expansion
  - expand vdev
summary: >
  Adding one more disk to an existing RAIDZ team—impossible for a decade,
  possible since early 2025, with fine print about how much space you
  actually get back.
---
<!-- depth:1 -->
RAIDZ Expansion
<!-- depth:2 -->
<!-- provenance: extracted -->
Can you add one more disk to an existing RAIDZ team when you need more
room? Two confident answers circulate: "of course—storage grows" (what
store-bought boxes teach) and "never—ZFS locks the team size forever" (a
decade of forum truth). **Actually, both are stale: since early 2025
(OpenZFS version 2.3), you can "add new devices to an existing RAIDZ pool,
increasing storage capacity without downtime"** (release notes)—one
command, while everything keeps running.

When reading ZFS advice, check the date. This feature made years of
confident guidance obsolete overnight, and the forums have long memories.
<!-- depth:3 -->
<!-- provenance: synthesized -->
The caveats that keep it from being magic:

- **Existing data keeps its old parity-to-data ratio.** Expansion reflows
  blocks across the new width, but stripes written as 3-wide keep 3-wide
  economics until naturally rewritten—so reclaimed capacity is less than
  the naive math promises, converging only as data churns. *(Carried at
  medium confidence from the feature's design discussion—vet against a
  primary source before it bears operational weight.)*
- **Type is still fixed.** RAIDZ1 cannot become RAIDZ2 in place; parity
  level remains a creation-time decision.
- **No shrink.** Width goes up only.
- The expansion itself is a long, resilver-like background reflow.

The planning consequence: expansion is a real escape hatch for "I need one
more disk of room," not a substitute for choosing vdev shape deliberately at
creation—the pressure the old absolute created was mostly good pressure.
