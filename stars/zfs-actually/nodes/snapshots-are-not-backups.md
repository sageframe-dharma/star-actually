---
id: snapshots-are-not-backups
title: Snapshots Are Not Backups
type: concept
requires: [snapshot]
related: [send-recv, sanoid-syncoid, vdev]
entry_points:
  - are snapshots backups
  - do i need backups with zfs
  - is zfs a backup
  - snapshot vs backup
summary: >
  A snapshot lives on the same disks, in the same pool, behind the same
  mistakes as the data. It's the versioning half of a backup strategy;
  replication is the other half.
---
<!-- depth:1 -->
Snapshots Are Not Backups
<!-- depth:2 -->
<!-- provenance: synthesized -->
The feeling is earned: snapshots every hour, every day, every month—you
can bring back anything from any point in time. That's what backups *do*,
so surely you have backups. **Actually, ask one question of anything that
claims to protect you: which disasters does it survive?** A snapshot lives
on the same disks, in the same machine, in the same building, under the
same hands as the data itself. Fire, theft, the whole pool dying, malicious
software that gets full control, one catastrophic mistyped command—the
snapshot dies in every single scenario the word "backup" exists for.

Snapshots answer "the *data* went wrong." Backups answer "the *place* went
wrong." Different questions, and you need answers to both.
<!-- depth:3 -->
<!-- provenance: synthesized -->
What snapshots are, said positively: the **versioning half** of a backup
strategy—recovery from deletion, bad upgrades, corruption-by-software,
your own past self. Instant, free, high-resolution. Most restores you'll
ever perform come from a snapshot, because most disasters are small.

The other half is **replication**: `zfs send` the snapshots to a *different
pool on a different machine* (syncoid on a schedule does exactly this). Now
the failure domains actually separate—and the classic 3-2-1 shape
(three copies, two media, one offsite) maps cleanly onto ZFS: live pool +
snapshots, replicated pool in the house, one leg somewhere else entirely.

The test that keeps everyone honest: **a backup you haven't restored from is
a hypothesis.** Browse the replica's `.zfs/snapshot/`, restore one real file,
once a quarter.
<!-- depth:4 -->
<!-- provenance: synthesized -->
Why smart people get this wrong: the *recovery experience* of a snapshot is
identical to the recovery experience of a backup—you reach into the past,
the file comes back. Identical interface, disjoint failure coverage. The
same conflation, one layer down, is "RAID is a backup": redundancy inside a
vdev survives a disk; it does nothing about the pool, the machine, or the
mistake. Each layer protects against exactly what it protects against:

- **vdev redundancy** → a disk dies
- **snapshots** → the data was wrong
- **replication** → the pool/machine died
- **offsite** → the building did

The stack is only as complete as its weakest *absent* layer—and the
snapshot layer is so pleasant to use that it hides the absence of the two
above it. That comfort is precisely the trap.
