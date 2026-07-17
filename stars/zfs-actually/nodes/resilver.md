---
id: resilver
title: Resilvering
type: concept
requires: [vdev]
related: [scrub, replace-disk, mirror, raidz]
entry_points:
  - what is resilvering
  - resilver vs rebuild
  - how long does resilver take
  - resilver slow
summary: >
  ZFS's rebuild—but it copies live data, not disk sectors, verifying every
  block against its checksum. Emptier pool, shorter rebuild, smaller
  second-failure window.
---
<!-- depth:1 -->
Resilvering
<!-- depth:2 -->
<!-- provenance: extracted -->
A hardware RAID rebuild copies every sector, start to end, because the
controller has no idea which sectors matter. **Actually, ZFS *is* the
filesystem—it knows exactly which blocks are live, so a resilver copies
data, not disk** ("resilvering only examines data that ZFS knows to be out
of date"—zpool-scrub(8)), and verifies each block against its checksum as
it goes. A half-full vdev resilvers in roughly half the time—and the time
matters, because the resilver window is when your margin is thinnest.
<!-- depth:3 -->
<!-- provenance: synthesized -->
Living through one: the pool stays up and serving—a resilver is a
background process, visible in `zpool status` with progress and an
estimate (early estimates lie; trust them only after they settle). The
system deliberately throttles resilver I/O behind live traffic, so a busy
pool resilvers slower. Don't reboot casually mid-resilver—it resumes, but
the window extends.

Vdev geometry sets the character of the event: a **mirror** resilver is a
straight copy from the healthy twin—fast, gentle. A **RAIDZ** resilver
reconstructs the missing disk from *all* survivors, hammering every one of
them for hours or days at exactly the moment redundancy is reduced—correlated disks (same batch, same age) make that a real stress test. This
asymmetry is a load-bearing input to the mirrors-vs-RAIDZ decision.
<!-- depth:4 -->
<!-- provenance: synthesized -->
Placed against its relatives:

- **vs a scrub**—same walk, different scope: scrub reads *everything* to
  find silent damage; resilver reads what's needed to rebuild one member.
  The pairing is standard: resilver to restore redundancy, then scrub to
  verify the whole (see Replacing a Disk).
- **vs sequential rebuild**—the block-tree walk has an honest cost: on a
  very full, fragmented pool it's seek-bound and can be *slower* than a
  dumb sector copy (`zpool replace -s` offers a sequential mode for
  mirrors that trades immediate verification for speed). "Smarter" wins
  most of the time, not always.
- **The window logic**—everything about resilvers feeds one number: how
  long you're exposed to a second failure. Emptier pools, mirror vdevs,
  RAIDZ2-over-RAIDZ1—most healthy-paranoia layout advice is
  resilver-window management by another name.
