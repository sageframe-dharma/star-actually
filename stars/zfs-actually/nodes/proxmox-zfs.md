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
  What the installer actually built: an rpool for the OS, zvols per VM disk,
  and an ARC that shares RAM with your VMs—the homelab's most common ZFS,
  decoded.
---
<!-- depth:1 -->
ZFS Under Proxmox
<!-- depth:2 -->
<!-- provenance: extracted -->
This is how most homelabs run ZFS for years without meeting it: Proxmox
offered "ZFS" at install, VMs appeared, storage worked. The naive model—VM disks are image files on a filesystem somewhere—sends you hunting for
qcow2 files that don't exist. **Actually, Proxmox carved each VM disk
directly from the pool as a zvol** (a block device, not a file), and the
mysterious `rpool` is just the pool the installer made for the OS itself.
*(Operational source: the practitioner's own Proxmox Docker hosts run
exactly this stack.)*
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
