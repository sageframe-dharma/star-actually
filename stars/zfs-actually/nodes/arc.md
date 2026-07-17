---
id: arc
title: The ARC
type: concept
requires: [what-zfs-is]
related: [l2arc, zil-slog]
entry_points:
  - zfs is eating my ram
  - why is my memory full
  - what is the arc
  - should i limit arc
  - zfs ram usage
summary: >
  ZFS's reading cache—the reason your machine's memory looks full, and why
  that's the system working, not leaking.
---
<!-- depth:1 -->
The ARC
<!-- depth:2 -->
<!-- provenance: synthesized -->
You check a ZFS machine's system monitor, see nearly all the memory in use
on a quiet day, and conclude something is broken. **Actually, that's the
ARC—ZFS's reading cache—and it is supposed to be huge.** The ARC keeps
recently and frequently read data parked in memory, where fetching it again
is thousands of times faster than going back to the disks. Memory sitting
empty helps no one; ZFS puts it to work—and gives it back when your
programs genuinely need it.

The correction under the correction: the memory bar you've read as a fuel
gauge all your life is the wrong instrument here. Full is the healthy state.
<!-- depth:3 -->
<!-- provenance: synthesized -->
Reading it honestly: `arc_summary` (or `arcstat`) instead of htop. The number
that matters is the **hit rate**—a warm homelab ARC serving in the high-90s
percent is why the pool feels faster than its spinning disks have any right
to be.

The one legitimate reason to cap it: **VM hosts.** The ARC's give-it-back
dance with the Linux kernel is imperfect and slightly laggy, and VMs
allocating big chunks of RAM can collide with it. That's why Proxmox
installations conventionally set `zfs_arc_max` to a fixed budget (Proxmox
itself defaults to a capped ARC on new installs). On a pure storage box,
leave it alone—capping ARC "to keep RAM free" is buying nothing with your
cache.
<!-- depth:4 -->
<!-- provenance: synthesized -->
Its neighbors, and the traps between them:

- **The page cache**—Linux's own file cache, which ordinary filesystems
  use and which htop *doesn't* alarm you about (it hides under
  "available"). ZFS's separate ARC accounting is why identical caching reads
  as a crisis on ZFS and as normal on ext4. Same behavior, scarier
  bookkeeping.
- **L2ARC**—the ARC's spillover tier on SSD. Not more ARC: every L2ARC
  block costs real ARC RAM for its index (see L2ARC before buying).
- **The ZIL/SLOG**—the write-side sibling in name only; it's a crash log,
  not a cache. "ARC for reads, SLOG for writes" is a symmetry your brain
  wants and the system doesn't have.
<!-- depth:5 -->
<!-- provenance: synthesized -->
Why "adaptive," and why ZFS didn't just use the page cache. A plain LRU
cache has a famous failure: one large sequential read (a backup job, a media
scan) flushes everything warm. The ARC runs **two lists—recently used and
frequently used—and moves the boundary between them continuously**, using
ghost lists (records of recent evictions) to notice which list it should
have trusted more. Scan-resistant by construction: the backup job churns the
recency list while the frequency list keeps your hot working set pinned.

The separate-cache design is Solaris heritage, but the argument survived the
port: ZFS wants to cache *its own* blocks (checksummed, compressed—the ARC
holds them compressed, stretching effective capacity) under its own eviction
policy, rather than inherit LRU behavior tuned for a different filesystem's
assumptions. The price is the double-accounting weirdness and the
give-it-back lag on Linux; the payoff is a cache that survives workloads
that flatten an LRU.
