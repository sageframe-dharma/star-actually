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
  "ZFS without ECC eats your data" is the loudest myth in homelab ZFS—the
  scrub-of-death mechanism doesn't survive inspection, per the co-creator
  himself.
---
<!-- depth:1 -->
The ECC Question
<!-- depth:2 -->
<!-- provenance: extracted -->
The claim arrives with total confidence: running ZFS on non-ECC RAM is
reckless—a scrub with bad memory will "correct" your good data into
garbage, pool-wide. It has the *shape* of expert knowledge: specific,
counterintuitive, scary. **Actually, here's Matt Ahrens, co-creator of ZFS:
"There's nothing special about ZFS that requires/encourages the use of ECC
RAM more so than any other filesystem."** ECC is good engineering—for
every filesystem equally. ZFS on consumer RAM is still *safer* than ext4 on
the same RAM, because everything ZFS verifies is still being verified.
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
