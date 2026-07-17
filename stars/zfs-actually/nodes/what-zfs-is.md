---
id: what-zfs-is
title: What ZFS Is
type: concept
requires: [what-a-filesystem-is]
related: [pool, copy-on-write, checksums, filesystem-landscape]
entry_points:
  - what is zfs
  - is zfs a filesystem
  - what layer is zfs
  - why is zfs different
  - why do people love zfs
summary: >
  Not a filesystem with features—the whole storage stack rebuilt around one
  act of distrust: assume the hardware lies, verify everything, never depend
  on an overwrite.
---
<!-- depth:1 -->
What ZFS Is
<!-- depth:2 -->
<!-- provenance: synthesized -->
You'll want to call ZFS a filesystem, because that's the word the ecosystem
uses. **Actually, ZFS is the entire storage stack in one system.** The jobs
that are normally three separate tools—the filesystem (the ledger that
turns blocks into files), the volume manager (the software that gathers
many disks into one usable space), and the RAID layer (the software that
keeps redundant copies so a dead disk costs nothing)—are merged, on
purpose, into one.

Everything else you'll meet—pools, checksums, snapshots, scrubs—falls out
of one founding assumption: **your hardware is lying to you.** Disks return
wrong data without error, controllers drop writes, power dies mid-operation.
ZFS is what storage looks like when you refuse to trust any of it.
<!-- depth:3 -->
<!-- provenance: synthesized -->
In practice this means you stop juggling tools. The usual parade of
single-purpose utilities—one to partition the disk, one to build the RAID,
one to create volumes, one to format, one config file to mount—simply
isn't there. Two commands cover almost everything:

- **`zpool`**—the physical side: disks, redundancy, health.
- **`zfs`**—the logical side: datasets, properties, snapshots, replication.

You meet ZFS most often without choosing it: Proxmox offers it at install,
TrueNAS is built on it, a homelab guide says "make a pool." Which is exactly
how you end up *operating* ZFS for a year without being able to say what it
is. The commands work whether or not you hold the model—until the first
disk dies or the first pool fills, and then the model is the only thing that
helps.
<!-- depth:4 -->
<!-- provenance: synthesized -->
The traditional stack is a bucket brigade of strangers: the filesystem hands
blocks to a volume manager, which hands them to a RAID layer, which hands
them to disks—and **no layer can check another's work.** RAID will
faithfully mirror corruption it can't detect; a filesystem can't ask RAID
"which of your two copies is right?" because the interface between them has
no words for that question.

People called ZFS's merge a *layering violation*—a serious accusation in
systems design. The retort is that the boundary being violated was the
problem: repair requires one system that both **knows what the data should
be** (checksums, the filesystem's knowledge) and **has another copy to fix it
with** (redundancy, the RAID layer's knowledge). Split those across an
interface and self-healing is structurally impossible.

Nearest kin: **Btrfs** (same convictions, rockier history—its RAID5/6 never
became trustworthy) and **APFS** (took copy-on-write and snapshots, skipped
data checksums and redundancy—the single-device convictions only).
<!-- depth:5 -->
<!-- provenance: synthesized -->
The design reduces to three commitments, each buying the next:

1. **Never overwrite live data.** Every write goes to fresh space; pointers
   flip atomically afterward. The on-disk state is always *some* consistent
   moment—there is no torn middle to repair, which is why there's no fsck.
2. **Checksum everything, and keep the checksum away from the data.** Each
   block's checksum lives in its *parent* block, so the whole pool is a
   Merkle tree up to a root (the uberblock). A disk that silently returns
   wrong bits fails verification on read. Detection is unconditional.
3. **Manage redundancy yourself.** Because ZFS placed the copies, a failed
   checksum isn't just detectable—it's *repairable*, quietly, from the
   copy that verifies. This is self-healing, and it's the payoff the merge
   exists for.

History, briefly: built at Sun for Solaris in the 2000s; Oracle closed it;
the open fork became **OpenZFS**, which is what Linux and FreeBSD run today.
When forum posts contradict each other, check the year—pre-2013 Solaris
lore and pre-2025 "you can never grow RAIDZ" absolutes both linger.
