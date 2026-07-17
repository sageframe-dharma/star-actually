---
id: proxmox-zfs
title: ZFS Under Proxmox
type: scenario
requires: [zvol]
related: [sanoid-syncoid, dataset, arc]
entry_points:
  - proxmox zfs
  - what is rpool
  - proxmox vm disks zfs
  - proxmox storage explained
summary: >
  What the Proxmox installer actually built: a pool for the operating
  system, a raw virtual disk per VM, and a cache that shares memory with
  your machines—the most common accidental ZFS, decoded.
---
<!-- depth:1 -->
ZFS Under Proxmox
<!-- depth:2 -->
<!-- provenance: extracted -->
**Proxmox** is a popular system for running virtual machines—computers
simulated in software—on one physical box, and it offers ZFS during
installation. This is how most home servers end up running ZFS for years
without their owners ever meeting it: click yes, machines appear, storage
works. The natural assumption—each virtual machine's disk is a big file
sitting in a folder somewhere—sends you hunting for files that don't
exist. **Actually, Proxmox carves each virtual machine's disk straight
from the pool** (a zvol—a slice of the pool pretending to be a real
disk), and the mysterious `rpool` is just the pool the installer made for
the operating system itself. *(Operational source: the practitioner's own
Proxmox hosts run exactly this stack.)*
<!-- depth:3 -->
<!-- provenance: extracted -->
Decoding a typical host:

- `zpool status`—`rpool` (the installer's, often a mirror of the boot
  disks) plus any pool you added. All the vdev/scrub/status reasoning from
  this site applies verbatim.
- `zfs list`—`rpool/ROOT/...` (the OS), `rpool/data/vm-103-disk-0` and
  friends (zvols, one per VM disk), and on a services host, datasets like
  `tank/services/<name>` per deployed service—filesystem face and
  block-device face of the same pool, side by side.
- **The RAM ledger**—the ARC and your VMs share physical RAM, and the
  give-it-back dance is imperfect on a VM host; this is the one place
  capping `zfs_arc_max` is orthodox rather than superstition (see The
  ARC). Budget it deliberately: RAM = VMs + ARC cap + host slack.
- Proxmox's own VM snapshots ride the same machinery—but sanoid
  policies on the zvols and syncoid replication offsite are what turn
  "snapshots exist" into a strategy (see Sanoid and Syncoid).
<!-- depth:4 -->
<!-- provenance: synthesized -->
The two models reconciled—the point of this node: "datasets for services"
and "zvols for VMs" felt like different systems when learned separately.
They're one pool wearing two faces per consumer type: containers and
services want filesystems (datasets—snapshot boundaries per service);
VMs want disks (zvols—block semantics per guest). Policy, retention,
replication, scrubs: identical underneath.

Two Proxmox-specific edges worth respecting: **double-CoW**—a guest
running ZFS/btrfs (or qcow2-on-ZFS) on top of a zvol amplifies every
write; give guests ext4/XFS unless you have a reason. And **thin zvols
overcommit the pool**—five VMs each promised 100GB on a 300GB pool works
until they all mean it; the free-space discipline gets *less* forgiving
when the claimants are machines (see The Free-Space Discipline).
