---
id: first-pool
title: Your First Pool
type: procedure
requires: [vdev, dataset, ashift]
related: [compression, mirror, raidz, mountpoints]
entry_points:
  - how to create a pool
  - zpool create
  - set up zfs
  - first zfs setup
summary: >
  The creation decisions in the order they lock in: vdev shape and ashift are
  forever, everything else is a property. One command, four judgments.
---
<!-- depth:1 -->
Your First Pool
<!-- depth:2 -->
<!-- provenance: synthesized -->
Guides present `zpool create` as setup—type it, get storage, move on.
**Actually, that one command makes the only decisions in ZFS you can't
revise: the vdev shape and the ashift.** Everything else—compression,
mountpoints, quotas, datasets—is a property you can change over morning
coffee. The discipline is knowing which decisions are the foundation pour
and giving them the ten deliberate minutes they deserve.

⚠ **DESTRUCTIVE**—`zpool create` repartitions the named devices. A typo'd
device name destroys a disk's contents. Verify with `ls -l
/dev/disk/by-id/` before running.
<!-- depth:3 -->
<!-- provenance: extracted -->
The shape of the command, judgments annotated:

```
zpool create -o ashift=12 \
  -O compression=lz4 -O atime=off \
  tank mirror ata-DISK1-SERIAL ata-DISK2-SERIAL
```

1. **Vdev shape** (`mirror ...` / `raidz2 ...`)—permanent. Random-I/O
   workloads → mirrors; bulk sequential → RAIDZ2 (the whole argument lives
   in Mirrors and RAIDZ).
2. **`ashift=12`**—permanent; don't let ZFS trust a lying drive ("set at
   vdev creation and it is immutable"—OpenZFS docs).
3. **By-id device names**—not permanent, but the cheapest gift to the
   future you who'll someday map a dead disk to a physical serial (see
   Replacing a Disk).
4. **`-O compression=lz4`** (and `atime=off`—write amplification for a
   timestamp nobody reads)—changeable later, but properties only touch
   *new* writes, so setting them at birth is the one time they cover
   everything.

Then immediately make datasets—the pool root is a policy anchor, not a
place to put files: `zfs create tank/services`, and policy boundaries per
thing you'll snapshot or tune separately.
<!-- depth:4 -->
<!-- provenance: synthesized -->
The judgment calls behind the incantation:

- **Whole disks, not partitions**—standard practice; ZFS partitions the
  disk itself and everyone can see it's ZFS's.
- **One pool unless physics differ**—an SSD pool and an HDD pool make
  sense side by side; two HDD pools on one box usually just split your
  free space into two smaller problems.
- **Name it plainly**—`tank` is the community's `foo`; anything works,
  you'll type it forever.
- **The test that beats reading**: before trusting real data to it, kill
  it once. Create the pool, write files, snapshot, yank a mirror member,
  watch DEGRADED, replace, resilver, scrub. Twenty minutes, and every
  status line in this site becomes something your hands have seen. Then
  build it for real.
