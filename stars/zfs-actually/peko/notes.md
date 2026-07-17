# Notes—ZFS

_Last rewritten: P4 · handoff_

## What ZFS turned out to be

The subject looked like "a filesystem with features" and turned out to be one
argument, applied everywhere: **your hardware is lying to you, so verify
everything and never depend on an overwrite completing.** Every piece that
seemed like a separate feature—checksums, copy-on-write, snapshots, scrubs,
send/recv—is a consequence of that argument. The learning arc kept
collapsing "features" into corollaries, which is why the graph is smaller
than the man pages suggest it should be.

The load-bearing structural fact, and the one my operating year never taught
me: **the vdev, not the pool, is the unit of redundancy and therefore of
failure.** The pool stripes across vdevs with nothing between them. Every
serious layout decision—mirrors vs RAIDZ, whether that lone disk is
acceptable, what a resilver window means—is a vdev decision. Q03 was the
hinge of the whole arc.

The second hinge: **copy-on-write is not a safety feature, it's the ontology.**
Once "no live block is ever overwritten" landed, snapshots (pins on existing
blocks), the free-space discipline (free space is CoW's workshop, not
headroom), send/recv (block-birth-time diffs), and rollback's destructiveness
all stopped needing to be memorized.

## Which naive models fell

The full ledger is questions.md; the ones that changed my behavior:

- *"The pool is redundant"* → redundancy is per-vdev; audit layouts, not pools.
- *"Snapshots ≈ backups"* → same failure domain; sanoid is versioning, syncoid
  is the backup, and the offsite leg is the part that counts.
- *"SLOG is a write cache" / "L2ARC is free speed"* → both are conditional
  tools for measured problems (sync writes; proven ARC misses), not upgrades.
- *"DEGRADED = crisis"* → DEGRADED is the design working; the response is
  deliberate, not fast.
- *"Rollback is timeline navigation"* → rollback is demolition; clones and
  `.zfs/snapshot/` are navigation.
- *"ZFS needs ECC or it eats data"* → nothing ZFS-specific; the scrub-of-death
  mechanism doesn't survive inspection (Ahrens, S03).

## What I now hold operationally

My own infrastructure finally parses: the deploy skill's per-service datasets
are policy boundaries (Q04); sanoid/syncoid are thin judgment over two
primitives I can now run by hand (Q10); Proxmox's zvols are the same machinery
presenting as block devices (Q28); and the pools would survive the death of
any host because they carry their own description (Q25).

## Genuinely open

- **Encryption**—native ZFS encryption (and raw sends of encrypted
  datasets) never came up because my pools don't use it. Parked; candidate
  nodes if the homelab adopts it.
- **dRAID**—deliberately out of boundary (P0): appliance-scale, not
  homelab-scale.
- **Tuning depth**—recordsize/ARC tuning beyond the homelab cases (real
  database hosts) noted in S05 but not internalized past depth 4.
- The RAIDZ-expansion parity-ratio caveat is carried at medium confidence
  (S02)—worth a primary-source vet if it ever becomes load-bearing.
