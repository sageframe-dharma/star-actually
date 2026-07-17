---
id: filesystem-history
title: A Short History of Filesystems
type: concept
requires: [what-a-filesystem-is]
related: [filesystem-landscape, copy-on-write]
entry_points:
  - history of filesystems
  - why are there so many filesystems
  - what is journaling
  - how did filesystems evolve
  - what came before zfs
summary: >
  Fifty years in one story: each generation of filesystems answers the
  previous generation's disaster—ending (so far) at the generation ZFS
  opened, which stopped trusting the disk itself.
---
<!-- depth:1 -->
A Short History of Filesystems
<!-- depth:2 -->
<!-- provenance: synthesized -->
Filesystem history looks like a parade of product names—FAT, ext2, NTFS,
ZFS. **Actually, it's a chain of disasters and answers.** Three generations,
each built to survive the failure that ruined the one before:

1. **Simple ledgers** (1970s–80s: FAT, early Unix filesystems). Fast and
   tiny. But lose power mid-write and the ledger itself ends up
   half-updated—scrambled records, orphaned files, a repair tool run at
   every boot, and sometimes real loss.
2. **Journaling** (1990s: NTFS, ext3, XFS). Before touching the ledger,
   write a short note—a *journal* entry—saying what you're about to do.
   After a crash, replay the notes. The ledger stays honest. This
   generation still runs most of the world.
3. **Integrity** (2000s onward: ZFS first at full scale, then Btrfs and
   Apple's APFS). Journaling protects the ledger from *crashes*—but it
   still trusts whatever the disk returns. This generation assumes the
   hardware itself can lie, and verifies everything.
<!-- depth:3 -->
<!-- provenance: synthesized -->
You can date any filesystem you meet by which disaster it answers:

- **FAT32 / exFAT** (generation 1) still rule USB sticks and camera
  cards—not out of nostalgia, but because when every device must read
  every stick, *simplicity is the feature*.
- **ext4, XFS, NTFS** (generation 2) are the workhorses under most Linux
  and Windows machines today: journaled, fast, thoroughly debugged, and
  still fundamentally trusting of the disk.
- **ZFS, Btrfs, APFS** (generation 3) each took the new assumptions
  somewhere different: ZFS to servers and many disks, APFS to the SSD in
  your Mac, Btrfs into the mainline Linux kernel.

The practical takeaway is calm: the older generations aren't wrong or
obsolete—each survives exactly where its trade-offs fit. But when a machine
holds years of data that must stay verifiably intact, generation 3 is the
one built for that job.
<!-- depth:4 -->
<!-- provenance: synthesized -->
The fine print that sorts real understanding from a timeline:

- **Journaling protects the ledger, not your data.** Most journaling
  filesystems journal only the *bookkeeping* (metadata), not file
  contents—a crash can still leave a file's contents half-written even
  though the records are tidy. "Crash-consistent" and "your data is
  intact" are different promises, and the gap between them is exactly
  where generation 3 begins.
- **The fsck ritual**—the repair tool that checked whole disks at
  boot—shaped a generation of habits. Journaling made it rare; the
  copy-on-write design (next stop on this trail) made it structurally
  unnecessary: a ledger that is never edited in place can't be caught
  half-edited.
- **Why generation 3 took until the 2000s**: verifying everything costs
  memory and computation that 1980s hardware couldn't spare, and the
  silent-corruption problem only became visible at scale—when you hold
  enough terabytes for long enough, "the disk sometimes returns wrong
  bytes without any error" stops being folklore and starts being a
  statistic.
