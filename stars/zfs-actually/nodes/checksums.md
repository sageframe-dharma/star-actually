---
id: checksums
title: Checksums
type: concept
requires: [what-zfs-is]
related: [scrub, ecc-question, copy-on-write]
entry_points:
  - how does zfs detect corruption
  - what is bit rot
  - does raid protect my data
  - how does self healing work
  - checksum error zfs
summary: >
  Every block verified on every read, with the checksum stored apart from the
  data—detection is unconditional; repair needs a second good copy.
---
<!-- depth:1 -->
Checksums
<!-- depth:2 -->
<!-- provenance: synthesized -->
The naive model: "RAID protects my data, and corruption announces itself as
errors." **Actually, disks lie silently**—they return wrong bits while
reporting success—and traditional RAID can't even ask which of its copies
is right. ZFS checksums every block and verifies on **every read**, so wrong
data cannot travel: it's caught the moment anything touches it.

Hold the two powers apart, because everything downstream depends on the
split: **checksums detect, unconditionally. Repair requires a second good
copy**—a mirror, RAIDZ parity. Detection without redundancy tells you what
you lost; it can't give it back.
<!-- depth:3 -->
<!-- provenance: extracted -->
Where you meet them: `zpool status` has three error columns—READ, WRITE,
**CKSUM**. A rising CKSUM count means a device returned data that failed
verification: silent corruption, caught in the act. With redundancy present,
ZFS already repaired it from the good copy ("For replicated (mirror, raidz,
or draid) devices, ZFS automatically repairs any damage discovered"—zpool-scrub(8)) and the count is your notification. Persistent CKSUM errors
on one disk mean a dying disk or a bad cable—SATA cables are the classic
false villain, cheap to swap first.

A scrub is this same verification, forced over *everything*, including cold
data nothing has read in years—so corruption gets found while the
redundancy to fix it still exists.
<!-- depth:4 -->
<!-- provenance: synthesized -->
What this replaces and what it neighbors:

- **Traditional RAID** mirrors bytes, not truth. Feed it silent corruption
  and it mirrors the corruption faithfully; ask it which side of a
  disagreement is right and the interface has no such question. Checksums
  are the missing arbiter—this is what "self-healing" actually is:
  detection (checksum) plus a decidable repair (the copy that verifies).
- **Bit rot** is the phenomenon checksums exist for—media degrading in
  place, cosmic-ray flips, firmware lies. Rare per-block, near-certain at
  pool-scale over years.
- **The ECC question**—checksums verify the *disk's* honesty; RAM sits
  above them. The panic version of that observation is mostly myth, but the
  layering is real (see The ECC Question).
<!-- depth:5 -->
<!-- provenance: synthesized -->
The structural trick is *where* checksums live: not beside the data (a disk
that corrupts a block would corrupt its adjacent checksum just as happily)
but **in the parent block pointer**. Every pointer carries the checksum of
what it points to, so verification walks downward: trust the parent, check
the child, descend. Each pool-wide commit produces a new root, so the whole
pool is a **Merkle tree**—the root (uberblock) transitively vouches for
every byte below it.

This is the same construction as Git and blockchains, deployed for the same
reason: tamper-evidence, where the tamperer is physics. It also makes the
checksum *self-verifying in context*—a corrupted checksum fails one level
up, so there's no chicken-and-egg. Default algorithm fletcher4 (fast,
error-detecting); sha256 when cryptographic strength is wanted (dedup).
Overhead: single-digit CPU percent, unconditional—ZFS considers reading
without verifying to be a category error, and after your first caught CKSUM
error, so will you.
