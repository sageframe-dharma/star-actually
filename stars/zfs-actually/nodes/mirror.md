---
id: mirror
title: Mirrors
type: concept
requires: [vdev]
related: [raidz, resilver]
entry_points:
  - mirror vs raidz
  - should i use mirrors
  - zfs mirror
  - mirrors for vms
summary: >
  Two-plus disks holding identical copies—half your capacity for the best
  IOPS, the fastest resilvers, and the most flexible growth. The
  workhorse layout for VM and database pools.
---
<!-- depth:1 -->
Mirrors
<!-- depth:2 -->
<!-- provenance: synthesized -->
A **mirror vdev** is two (or more) disks holding identical copies of every
block. Capacity math makes it look like the naive option—you "lose" half
your disks. **Actually, the capacity you give up buys the three things
parity can't sell you**: reads served by any member (IOPS scale with disk
count), resilvers that are a straight copy from a healthy twin, and vdevs
you can grow, split, and rearrange with the least ceremony in ZFS.
<!-- depth:3 -->
<!-- provenance: synthesized -->
Where mirrors are simply the right answer: **pools whose workload is random
I/O—VMs, databases, container volumes.** The pool stripes across vdevs, so
six disks as three mirror vdevs gives roughly 3× write IOPS and 6× read
IOPS of a single disk; the same six as one RAIDZ2 gives roughly 1× (see
RAIDZ for why). This is the whole "mirrors for VMs" folk wisdom, derived.

Operations worth knowing exist: `zpool attach` converts a lone disk into a
mirror (the retroactive fix for a single-disk-vdev regret) or adds a third
member to a pair—and resilvering a mirror is reading one healthy disk,
not reconstructing from the whole vdev. Growth path: replace both members
with bigger disks one resilver at a time, or add another mirror vdev to the
pool.
<!-- depth:4 -->
<!-- provenance: synthesized -->
Against its alternatives honestly:

- **vs RAIDZ**—mirrors pay in capacity (50% at two-way); RAIDZ pays in
  IOPS and inflexibility. Sequential bulk storage (media, backups) doesn't
  feel RAIDZ's costs, which is why the split verdict—mirrors for random,
  RAIDZ for bulk—keeps being the answer.
- **The two-way honesty clause**—a 2-disk mirror survives *one* failure,
  and the resilver window after that failure is a no-redundancy window (a
  read error during it costs data). Three-way mirrors exist precisely for
  data where that window is unacceptable.
- **vs "RAID1 is a backup"**—a mirror faithfully replicates your
  mistakes in real time. It survives a disk; it does not survive you (see
  Snapshots Are Not Backups for the full stack of what-protects-what).
