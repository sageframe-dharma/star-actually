---
id: l2arc
title: L2ARC
type: definition
requires: [arc]
related: [zil-slog]
entry_points:
  - should i add a cache drive
  - what is l2arc
  - zfs ssd cache
  - does l2arc help
summary: >
  The ARC's spillover tier on SSD—every block it caches costs ARC RAM for
  the index, so it's a measured fix for proven ARC misses, not free speed.
---
<!-- depth:1 -->
L2ARC
<!-- depth:2 -->
<!-- provenance: synthesized -->
The forum instinct: spare NVMe + slow pool = add a cache drive, because more
cache is always better. **Actually, L2ARC is not free speed—its index
lives in RAM, so every block cached on the SSD eats a slice of the ARC**,
the cache that's actually fast. On a modest-RAM machine you can end up
trading excellent cache (RAM) for mediocre cache (SSD) and calling it an
upgrade.
<!-- depth:3 -->
<!-- provenance: synthesized -->
The honest decision procedure, in order:

1. **Max out RAM first.** It's the better cache and it needs no index.
2. **Measure.** `arc_summary`—if the ARC hit rate is already high
   (homelabs: it usually is), there is nothing for an L2ARC to catch.
3. Only with real, sustained ARC misses on a working set that fits on the
   SSD: `zpool add tank cache <ssd>`.

Two softeners worth knowing: losing an L2ARC device is harmless (it's pure
cache—the pool doesn't depend on it, unlike a SLOG mid-crash), and modern
OpenZFS supports a persistent L2ARC that survives reboots, fixing the old
cold-cache-every-boot complaint. Neither changes the arithmetic at depth 2.
<!-- depth:4 -->
<!-- provenance: synthesized -->
The confusion neighborhood: L2ARC and SLOG get bought together by the same
impulse ("SSDs make pools fast") and do unrelated jobs—L2ARC serves
re-reads of warm data; a SLOG serves synchronous-write latency and is a
crash log, not a cache. The homelab pattern of carving one SSD into "a bit
of SLOG, a bit of L2ARC" usually means neither was justified by a
measurement.

What actually fixes a slow pool, most often: more RAM (ARC), mirrors instead
of RAIDZ for random-I/O workloads (vdev IOPS), recordsize matched to the
workload, or the pool simply being too full (see The Free-Space Discipline).
L2ARC is the right tool in the narrow case where the working set is bigger
than RAM, smaller than an SSD, and genuinely re-read—a real pattern
(shared build caches, hot media subsets), just rarer than the forums imply.
