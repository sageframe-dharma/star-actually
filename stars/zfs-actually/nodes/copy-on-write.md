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
  ZFS never overwrites a live block—every write lands on fresh space and
  pointers flip atomically. Not a safety feature; the ontology everything
  else stands on.
---
<!-- depth:1 -->
Copy-on-Write
<!-- depth:2 -->
<!-- provenance: synthesized -->
The naive parse of "copy-on-write" is a safety feature—something like
journaling, keeping a copy in case a change goes wrong. **Actually,
copy-on-write means ZFS never overwrites a live block, ever.** When you
"change" a file, ZFS writes new blocks somewhere fresh, then atomically flips
pointers so the new blocks become the truth. The old blocks aren't defended
or recovered—they're simply never touched.

The consequence: at every instant, the on-disk state is *some* complete,
consistent moment. A write either fully happened or never happened. There is
no torn middle—which is why there's no fsck, and no journal replaying
half-finished work.
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
