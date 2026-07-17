---
id: free-space-discipline
title: The Free-Space Discipline
type: concept
requires: [copy-on-write]
related: [snapshot-space, recordsize]
entry_points:
  - how full can a zfs pool get
  - pool slow when full
  - zfs 80 percent rule
  - fragmentation zfs
summary: >
  On ZFS, empty space isn't spare room—it's the workshop floor every change
  is made on. Fill the pool and it gets permanently grumpier.
---
<!-- depth:1 -->
The Free-Space Discipline
<!-- depth:2 -->
<!-- provenance: synthesized -->
Intuition says a nearly-full disk is just a disk with less room—how full
it is and how fast it is are separate questions. On ordinary systems
that's *mostly* true. **Actually, because ZFS never writes over existing
data, every change needs fresh, empty space to land on—even "overwrites,"
even deletions.** A full pool forces ZFS to hunt for scraps of room; new
data gets shredded into whatever gaps exist; and the pool slows down in a
way that doesn't fully recover when you free space later, because the
scattering already happened.

Empty space isn't spare room. It's the workshop floor every change is
made on.
<!-- depth:3 -->
<!-- provenance: synthesized -->
Operating numbers, honestly labeled as heuristics: keep general-purpose
pools **below ~80–85%**; performance-sensitive pools (VMs, databases)
appreciate more slack. Past ~90% the allocator visibly changes character;
at ~100%, deletion itself gets weird—*freeing* space needs CoW writes too
(snapshot destruction is the usual escape because it frees without
writing... unless snapshots are exactly what's pinning everything—see
Snapshots and Disappearing Space).

Watch two numbers: `zpool list` for `CAP` and `FRAG`. FRAG measures
*free-space* fragmentation (how shredded the remaining room is), not file
fragmentation—a high-FRAG, high-CAP pool is one whose future writes are
already compromised. The honest fixes are the blunt ones: grow the pool
(add a vdev), or want less (retention policy, quotas so one dataset can't
eat the floor).
<!-- depth:4 -->
<!-- provenance: synthesized -->
Why this is structural, not a tuning miss: an overwrite-in-place filesystem
at 95% mostly rewrites the blocks files already own—its steady state
barely needs free space. CoW *never* rewrites in place, so its demand for
fresh, preferably-contiguous space is perpetual; the same distrust of
overwrites that buys snapshots-for-free and no-fsck sends the bill here.
There's no configuration that removes the bill—only layouts and habits
that keep it small.

Neighbors: quotas and reservations are the per-dataset tools that keep one
tenant from consuming the shared floor; snapshot retention is the usual
silent filler (`USEDSNAP` grows while everyone stares at `USEDDS`); and
the resilver connection closes the loop—full pools resilver slower,
so the free-space discipline is quietly also failure-window discipline.
