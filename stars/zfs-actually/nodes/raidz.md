---
id: raidz
title: RAIDZ
type: concept
requires: [vdev]
related: [mirror, raidz-expansion, resilver]
entry_points:
  - raidz vs raid5
  - what is raidz
  - raidz1 vs raidz2
  - is raidz slow
  - how many disks raidz
summary: >
  Parity redundancy that fixed RAID5's write hole—but a RAIDZ vdev delivers
  roughly one disk of IOPS no matter how wide. Bulk storage, not VM storage.
---
<!-- depth:1 -->
RAIDZ
<!-- depth:2 -->
<!-- provenance: synthesized -->
"RAIDZ is RAID5 with a Z" is half right, and each half matters. The parity
arithmetic is the same shape—RAIDZ1/2/3 survive one/two/three disk
failures per vdev. **Actually, two things separate it. RAIDZ closed RAID5's
write hole** (the crash-between-data-and-parity corruption that haunted
hardware RAID)—CoW and variable-width stripes mean no read-modify-write
and no torn parity, ever. **And a RAIDZ vdev delivers roughly one disk's
worth of random IOPS, no matter how many disks are in it**—the fact the
capacity math hides and the performance math is ruled by.
<!-- depth:3 -->
<!-- provenance: synthesized -->
Choosing within the family:

- **RAIDZ1**—one parity disk. With today's drive sizes, a resilver reads
  many TB from every survivor for hours or days; a second failure or read
  error in that window costs data. Fine for genuinely rebuildable bulk;
  nervous territory for anything else.
- **RAIDZ2**—the homelab default for bulk storage vdevs (classic shape:
  6–8 disks). Two-failure tolerance is what makes the resilver window
  boring instead of frightening.
- **RAIDZ3**—for wide vdevs and long resilvers at scales most homelabs
  don't reach.

Use it where it's strong: media libraries, backup targets, archives—big
sequential reads and writes, where bandwidth is fine and IOPS don't matter.
Keep VMs and databases off it (that's what mirror vdevs are for).
<!-- depth:4 -->
<!-- provenance: synthesized -->
Its standing confusions:

- **"More spindles = faster"**—true across *vdevs*, false within a RAIDZ:
  every random read touches every data disk in the stripe, so the vdev
  moves as one unit at one disk's cadence. Width buys capacity and
  bandwidth, not IOPS.
- **vs mirrors**—the recurring decision. Capacity efficiency vs IOPS,
  slow reconstructive resilvers vs fast copy resilvers, rigidity vs
  flexibility. The workload decides; wanting one pool to do both jobs well
  is how people end up disappointed.
- **Growth**—the old absolute "you can never expand a RAIDZ" died in
  OpenZFS 2.3 (see RAIDZ Expansion), but width is still mostly a
  creation-time decision, and type (Z1→Z2) still can't change in place.
<!-- depth:5 -->
<!-- provenance: synthesized -->
The write hole, and how CoW dissolves it: RAID5 updates in place—write
data, then parity—so a crash between the two leaves a stripe whose parity
lies, silently, discovered only when a rebuild reconstructs garbage from it.
Battery-backed controllers existed to paper over exactly this. RAIDZ never
updates a stripe in place: each logical block becomes its own
**variable-width stripe** (data + parity sized to fit), written whole to
fresh space and committed by the same atomic pointer flip as everything else
in ZFS. No stripe is ever half-new; the transaction either points at it or
doesn't.

Variable width is also *why* the IOPS ceiling: one logical block spans the
vdev's data disks, so one random read is a coordinated act by all of them—the stripe is the unit of retrieval. And it explains the odd capacity
arithmetic (parity overhead varies with block size—small blocks carry
proportionally more parity), which is why RAIDZ capacity calculators hedge
where mirror math is exact. Every RAIDZ quirk traces back to the same
design move: making the stripe a creature of the write, not of the disk
layout.
