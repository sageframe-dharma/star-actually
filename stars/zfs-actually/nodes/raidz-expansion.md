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
  Since OpenZFS 2.3 you can widen a RAIDZ vdev live—with caveats: old data
  keeps its old parity ratio, and type still can't change.
---
<!-- depth:1 -->
RAIDZ Expansion
<!-- depth:2 -->
<!-- provenance: extracted -->
Two absolutes circulate: "of course arrays grow" (appliance intuition) and
"ZFS RAIDZ can never grow" (a decade of forum truth). **Actually, both are
stale: since OpenZFS 2.3 (January 2025), RAIDZ expansion lets you "add new
devices to an existing RAIDZ pool, increasing storage capacity without
downtime"** (release notes)—`zpool attach` a disk to a RAIDZ vdev and it
widens, live, while the pool serves.

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
