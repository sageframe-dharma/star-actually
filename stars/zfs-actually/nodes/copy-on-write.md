---
id: copy-on-write
title: Copy-on-Write
type: concept
requires: [what-zfs-is]
related: [snapshot, free-space-discipline, checksums]
entry_points:
  - what is copy on write
  - what is cow
  - why does zfs not need fsck
  - does zfs overwrite data
  - why are snapshots cheap
summary: >
  ZFS never writes over existing data—every change lands on fresh space
  first, then takes effect in one clean switch. The habit everything else
  stands on.
---
<!-- depth:1 -->
Copy-on-Write
<!-- depth:2 -->
<!-- provenance: synthesized -->
When an ordinary system saves a change, it writes the new version on top
of the old one, right where it sat. That's the obvious approach, and it
carries a hidden bet: that nothing goes wrong *mid-write*. Lose power at
the wrong instant and the old version is half-destroyed while the new one
is half-written—the ugly middle that older systems needed repair tools
for.

**Copy-on-write is ZFS's refusal to ever make that bet: existing data is
never written over. Ever.** When you "change" a file, ZFS writes the new
version onto fresh, empty space, and then—in one clean, instant switch—
makes it the official one. So at every moment, what's on disk is *some*
complete, correct state. A change either fully happened or never happened;
there is nothing half-done to repair, which is why no repair pass exists.
<!-- depth:3 -->
<!-- provenance: synthesized -->
You feel CoW everywhere before you can name it:

- **Snapshots are instant and free**—old blocks were never going to be
  overwritten, so "keep the past" is just "don't garbage-collect these yet."
- **Power loss stops being scary**—pull the plug mid-write; on import the
  pool is simply *at* the last committed moment. No repair pass.
- **Free space is a working resource**—even overwrites and deletions need
  fresh space to land, which is why a nearly-full CoW pool degrades (see
  The Free-Space Discipline).
- **Sequential writes fragment over time**—rewrite the middle of a file
  and the new blocks live elsewhere; the file's layout scatters. The steady
  state of a busy CoW pool is honest fragmentation managed by caching.
<!-- depth:4 -->
<!-- provenance: synthesized -->
What it gets confused with:

- **Journaling** (ext4, XFS): a journal records intentions, then performs
  overwrites in place, and replays intentions after a crash. Repair
  machinery for a dangerous act. CoW removes the dangerous act—there's
  nothing to replay.
- **The other CoWs**: APFS and Btrfs share the discipline (APFS without data
  checksums); qcow2 does it at the image-file level; even `cp
  --reflink` is CoW at the file level. The idea won. ZFS's version is
  distinctive for being welded to checksums and redundancy.
- **"CoW is slow"**: half-true, workload-shaped. Random-rewrite workloads
  (VM images, databases) pay real fragmentation costs—that's the true part
  and why recordsize and mirrors matter there. For most everything else the
  cost is noise against the durability purchased.
<!-- depth:5 -->
<!-- provenance: synthesized -->
The mechanism, one level down. The pool's block pointers form a tree. To
modify a leaf block, ZFS writes the new leaf to fresh space; the parent that
points at it must change, so a new parent is written too—and so on, new
blocks rippling up to the root. The root pointer (the **uberblock**) is then
updated in one atomic step. That single flip is the commit: before it, the
old tree is the truth; after it, the new one is. Crash at any moment and one
of the two is what you have—never a blend.

Writes batch into **transaction groups** (txgs) that commit every few
seconds, so the ripple amortizes across many changes. Blocks freed by a
commit return to the allocator only when nothing references them—and
"nothing references them" is exactly the accounting that snapshots hook into
by holding references. Snapshot, rollback, clone, even send: all of them are
just different ways of pointing at trees that CoW was already producing.
