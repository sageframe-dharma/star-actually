---
id: zil-slog
title: ZIL and SLOG
type: concept
requires: [copy-on-write]
related: [arc, l2arc]
entry_points:
  - what is the zil
  - what is a slog
  - is slog a write cache
  - do i need a slog
  - sync writes slow
summary: >
  Not a fast lane for writes—a diary of promises, written constantly and
  read exactly once: after a crash. A SLOG just moves the diary to a faster
  drive, and only promise-me-now writes ever use it.
---
<!-- depth:1 -->
ZIL and SLOG
<!-- depth:2 -->
<!-- provenance: extracted -->
Some programs, before they continue, demand a promise: *"confirm this is
safely on disk—now."* The **ZIL** (ZFS Intent Log) is the diary where ZFS
records those promises the instant it makes them. Here's the part everyone
gets backwards: the diary is **written constantly and, in normal life,
never read at all.** It's read exactly once—when the machine starts up
after a crash, to make good on promises made just before the lights went
out ("On system startup, ZFS reads the ZIL and replays any pending
transactions"—Klara). Data does not travel *through* it on the way to
disk; it is insurance, not a fast lane.

A **SLOG** is nothing more than that diary moved onto a fast dedicated
drive. Every pool already has the diary without one, kept on the pool's
own disks.
<!-- depth:3 -->
<!-- provenance: extracted -->
The part that decides whether you should care: **only synchronous writes
touch the ZIL.** An async write (most writes—file copies, media, general
homelab traffic) is acknowledged from RAM and flows to the pool in the next
transaction group; "neither the ZIL nor the SLOG make a difference with
pending asynchronous writes… if you don't have any applications that use
synchronous writes, you don't need a SLOG" (Klara).

Sync writes—databases honoring fsync, NFS exports, VMs whose guests demand
durability—must be on stable storage *before* ZFS acknowledges. Without a
SLOG that means a hurried write to the ZIL area of your spinning pool per
fsync; latency suffers. A SLOG (low-latency, power-loss-protected SSD—Optane-class ideally) absorbs exactly that. Check whether you even have the
problem: `zilstat`, or watch pool latency while a sync-heavy workload runs.
<!-- depth:4 -->
<!-- provenance: synthesized -->
Placed against its false siblings:

- **vs a write cache**—RAM is the write cache (dirty data waiting in the
  transaction group). The ZIL is durability *insurance on the
  acknowledgment*, not a stop on the data path.
- **vs L2ARC**—read-side spillover cache; loss is harmless. Losing a SLOG
  is harmless *except* if it dies together with a crash before replay—the
  one window where the log was about to be needed. Cheap consumer SSDs
  without power-loss protection quietly fail the job description.
- **vs `sync=disabled`**—the tempting benchmark cheat: acknowledge sync
  writes as if durable. The performance of a SLOG for free, paid for with
  the exact guarantee the application asked for. Fine for scratch data you
  can regenerate; a lie anywhere durability was the point.
<!-- depth:5 -->
<!-- provenance: synthesized -->
Why does a CoW filesystem with atomic transaction groups need a log at all?
Because txgs commit every few seconds, and a sync write can't wait seconds—the contract is "durable *now*." The ZIL bridges the gap: a minimal record
of the acknowledged operation lands on stable storage immediately, while the
real write travels the normal CoW path in its txg. When the txg commits, the
log records become garbage without ever being read—the happy path discards
the log continuously.

So the ZIL is the deliberate exception to "everything flows through the
tree": a small, forward-only side channel purchased solely so that fsync can
return in device-latency time instead of txg time. Understanding that makes
the SLOG sizing folklore obvious—it holds seconds of sync writes, not
gigabytes of data (a few GB is plenty), and its virtue is latency, not
bandwidth.
