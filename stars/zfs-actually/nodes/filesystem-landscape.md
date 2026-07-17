---
id: filesystem-landscape
title: The Filesystem Landscape
type: concept
requires: [what-a-filesystem-is]
related: [filesystem-history, what-zfs-is]
entry_points:
  - zfs vs ext4
  - zfs vs btrfs
  - zfs vs ntfs
  - which filesystem should i use
  - comparable filesystems
  - alternatives to zfs
summary: >
  The filesystems you actually meet—ext4, XFS, NTFS, APFS, Btrfs—one honest
  line each, and the specific combination ZFS offers that the others don't.
---
<!-- depth:1 -->
The Filesystem Landscape
<!-- depth:2 -->
<!-- provenance: synthesized -->
"Which filesystem is best?" is the naive question, and the internet will
happily fight about it forever. **Actually, filesystems are tools for
different jobs, and the real question is "what does each one promise?"**
Most of the familiar ones promise: *your records will survive a crash*.
ZFS promises something stronger and rarer: *your data will be verified,
and if a copy exists, repaired*—across many disks, as one system. Nothing
else in wide use makes that full promise; one system (Btrfs) makes most of
it. That difference, not speed or popularity, is what you're choosing when
you choose ZFS.
<!-- depth:3 -->
<!-- provenance: synthesized -->
The roster, one honest line each:

- **ext4** — the Linux default. Journaled, fast, two decades of debugging.
  Trusts the disk completely. The right answer for most single-disk Linux
  machines.
- **XFS** — ext4's heavy-duty sibling (the default on Red Hat systems);
  excels at large files and parallel work. Same trust in the disk.
- **NTFS** — Windows' filesystem since the 90s. Journaled, capable, and
  not really a choice—it's what Windows is.
- **APFS** — Apple's modern filesystem. Shares real DNA with ZFS
  (copy-on-write, snapshots) but skips data checksums and multi-disk
  redundancy: it's the single-SSD-in-a-laptop distillation of the ideas.
- **Btrfs** — the closest relative: ZFS's convictions (checksums,
  snapshots, multi-disk pools) rebuilt inside the mainline Linux kernel.
  Mature for single disks and mirrors; its RAID5/6-style parity modes
  never became trustworthy, which is the caveat that keeps it second.
- **exFAT / FAT32** — the interchange formats. No journal, no ownership,
  no promises; readable by everything. Perfect for a camera card,
  unthinkable for your archive.
<!-- depth:4 -->
<!-- provenance: synthesized -->
What ZFS uniquely combines—each piece exists somewhere else; the
*combination* is the offer:

- **Verification** (checksums on all data) — Btrfs yes; ext4/XFS/NTFS/APFS
  no.
- **Repair from redundancy** (self-healing across disks) — Btrfs
  partially; nothing else even attempts it.
- **Whole-stack scope** (one system managing disks, redundancy, and
  files) — traditionally three separate tools everywhere else.
- **Snapshots and replication as first-class verbs** — APFS and Btrfs
  have snapshots; ZFS's send/receive replication is the piece the others
  lack or approximate.

And the honest costs, so the comparison isn't a sales pitch: ZFS wants
memory (its cache is a feature, not a leak), lives outside the mainline
Linux kernel for licensing reasons (an extra installation step, not a
quality verdict), and asks you to learn a real mental model—which is,
after all, why this site exists. When the machine is one laptop with one
SSD, ext4 or APFS is genuinely the better fit. When the machine is where
your data *lives*, the combination above is the argument.
