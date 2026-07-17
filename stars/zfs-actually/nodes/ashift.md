---
id: ashift
title: Ashift
type: concept
requires: [vdev]
related: [first-pool, recordsize]
entry_points:
  - what is ashift
  - ashift 9 vs 12
  - can i change ashift
  - 4k sectors zfs
  - ashift wrong
summary: >
  ZFS's recorded guess about a disk's true cell size—made once, when a disk
  team is created, and permanent forever. The one setting a wrong guess
  makes unfixable. Use 12.
---
<!-- depth:1 -->
Ashift
<!-- depth:2 -->
<!-- provenance: extracted -->
Disks secretly do all their work in fixed-size cells (called *sectors*),
and **ashift** is ZFS's recorded guess about how big a disk's cells really
are. Nearly everything in ZFS can be changed later; **ashift is the
exception—it's decided once, when a team of disks is created, and can
never be changed** ("it is set at vdev creation and it is immutable"—
OpenZFS docs). The two values you'll see: ashift=9 means tiny old-style
512-byte cells; ashift=12 means the modern 4-kilobyte kind.

That's why the guides scream about one small number: it's the single
decision in ZFS that is actually a foundation pour.
<!-- depth:3 -->
<!-- provenance: synthesized -->
The failure mode: modern drives have 4K physical sectors, but many *report*
512 for compatibility. Trust the lie and you get ashift=9 on 4K hardware—and every sub-4K write becomes a read-modify-write cycle *inside the drive*,
forever, invisibly, on every vdev member. The pool works; it's just
permanently slower, and the only exit is destroying and rebuilding the vdev.

The practice is blunt: **`zpool create -o ashift=12`** unless you can prove
your drives are truly 512-native (almost nothing you'd buy today is).
ashift=12 on a genuinely-512 drive costs a little slack space; ashift=9 on a
4K drive costs performance permanently. The asymmetry does the deciding.
Check an existing pool with `zdb -C tank | grep ashift`—better to know
than to wonder.
<!-- depth:4 -->
<!-- provenance: synthesized -->
Where it sits among its neighbors:

- **vs recordsize**—the two "block size" ideas. Ashift is the physical
  floor per vdev, immutable; recordsize is the logical ceiling per dataset,
  changeable at will. When someone says "block size" about ZFS, make them
  say which.
- **Per vdev, not per pool**—every vdev added over the pool's life makes
  its own ashift decision (modern ZFS detects 4K correctly most of the
  time, but "most of the time" is doing load-bearing work—pass the flag).
- **Why it can't change**—an honest limitation, honestly derived:
  ashift shapes how every block pointer in the vdev addresses the disk.
  Changing it would mean rewriting the vdev's every allocation—which is
  just "rebuild the vdev" wearing a friendlier name. ZFS declines to
  pretend otherwise.

⚠ **Destructive context**—ashift is set by `zpool create` / `zpool add` /
`zpool attach`, commands that repartition disks. Triple-check device names
before running them; see Your First Pool.
