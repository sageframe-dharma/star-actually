---
id: ecc-question
title: The ECC Question
type: concept
requires: [checksums]
related: [scrub]
entry_points:
  - do i need ecc ram for zfs
  - scrub of death
  - zfs without ecc
  - is non ecc ram dangerous
summary: >
  "ZFS without special error-checking memory will eat your data" is the
  loudest myth in ZFS—it doesn't survive inspection, per the co-creator
  himself.
---
<!-- depth:1 -->
The ECC Question
<!-- depth:2 -->
<!-- provenance: extracted -->
First, the term: **ECC memory** is a pricier kind of computer memory,
common in servers, that catches its own rare internal errors; ordinary
computers use memory that doesn't. The claim you'll meet arrives with total
confidence: running ZFS on ordinary memory is reckless—its self-repair
process, fed by faulty memory, will "fix" your good data into garbage. The
claim has the *shape* of expert knowledge: specific, counterintuitive,
scary. **Actually, here's Matt Ahrens, co-creator of ZFS: "There's nothing
special about ZFS that requires/encourages the use of ECC RAM more so than
any other filesystem."** ECC memory is good engineering—for every system
equally. ZFS on an ordinary computer is still *safer* than an ordinary
filesystem on that same computer, because everything ZFS checks is still
being checked.
<!-- depth:3 -->
<!-- provenance: extracted -->
Why the "scrub of death" fails on inspection: for a scrub to overwrite good
data, the repair path has to *accept* a corrupted reconstruction—and
acceptance requires the reconstruction to **match its checksum**. Random RAM
corruption producing data that happens to hash correctly is a hash
collision by accident—odds so remote they aren't a scenario, they're a
rounding error (the jrs-s.net analysis walks the arithmetic). Bad RAM makes
a scrub *fail to repair* things, loudly; it doesn't convert the repair
machinery into a corruption engine. The myth requires the safety system to
be the weapon, and the safety system checks its own work.
<!-- depth:4 -->
<!-- provenance: synthesized -->
The calibrated position, since both extremes are wrong:

- **What non-ECC actually risks** (on any filesystem): data corrupted in
  RAM *before* ZFS checksums it is checksummed-as-corrupted—written
  wrong, verified wrong forever. Checksums guard the disk boundary, not
  the memory above it. This is real, rare, and filesystem-agnostic.
- **What ECC buys**: closing that gap. On an always-on server doing work
  you care about, ECC is worth having—the boring, universal argument,
  which was never ZFS-specific.
- **Why the myth persists**: it flatters its holder (secret knowledge),
  it's unfalsifiable in the small (nobody's homelab runs the control), and
  it got institutionalized by forum culture repeating a worst-case sketch
  as a mechanism. Its function now is mostly gatekeeping—"your hardware
  isn't worthy of ZFS"—which is exactly backwards: the machines that
  can't have ECC benefit *most* from a filesystem that verifies.
