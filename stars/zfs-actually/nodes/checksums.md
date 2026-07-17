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
  A tiny fingerprint for every piece of data, re-checked on every read—so
  a lying disk gets caught in the act. Noticing damage is guaranteed;
  fixing it needs a spare copy.
---
<!-- depth:1 -->
Checksums
<!-- depth:2 -->
<!-- provenance: synthesized -->
A **checksum** is a tiny fingerprint computed from a piece of data. ZFS
fingerprints everything it writes, and every time it reads anything back,
it re-computes the fingerprint and compares. Why bother? Because **disks
sometimes lie**: they age, they glitch, and they can hand back subtly wrong
data while reporting that everything is fine. Storage systems that keep
duplicate copies but no fingerprints can't even tell which copy is the
right one. With fingerprints, wrong data gets caught the moment anything
touches it.

Hold two powers apart, because everything downstream depends on the split:
**noticing damage is guaranteed, everywhere, always. Fixing damage requires
a spare copy to fix it from.** Fingerprints without spare copies can only
tell you what you lost—they can't give it back.
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
