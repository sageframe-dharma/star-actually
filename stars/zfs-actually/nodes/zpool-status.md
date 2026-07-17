---
id: zpool-status
title: Reading zpool status
type: procedure
requires: [pool]
related: [scrub, replace-disk, vdev]
entry_points:
  - zpool status degraded
  - how to read zpool status
  - what does degraded mean
  - checksum errors zpool status
  - is my pool healthy
summary: >
  The pool's one health report—and DEGRADED means the design is working,
  not that the pool is dying. How to read it without panic.
---
<!-- depth:1 -->
Reading zpool status
<!-- depth:2 -->
<!-- provenance: synthesized -->
`zpool status` is the command that shows the pool's health report. Scary
capitalized words in a report mean crisis in most of computing, so
**DEGRADED** reads as "half-broken—touching it might tip it over."
**Actually, DEGRADED means the design is working: a disk failed, the spare
copies absorbed it, and the pool is running normally with less safety
margin than before.** The report itself is a calm document—what state
things are in, what caused it, and almost always an explicit recommended
next step, written right there in an `action:` line. It tells you what to
do; the skill is believing it.
<!-- depth:3 -->
<!-- provenance: synthesized -->
The reading order:

1. **`state:`**—`ONLINE` (healthy), `DEGRADED` (redundancy absorbed
   something; act deliberately), `FAULTED`/`UNAVAIL` (pool-level trouble—*now* it's serious).
2. **`status:` and `action:`**—plain-English diagnosis and the
   recommended move. Start there, not the forums.
3. **The device tree**—indentation is the vdev structure (this is also
   your layout audit—a bare disk at vdev level is a single point of
   failure hiding in plain sight). Each line: state plus **READ / WRITE /
   CKSUM** error counts.
4. **The `scan:` line**—last scrub/resilver and its result.

Reading the error columns: READ/WRITE are I/O failures (dying disk, or the
perennially guilty cable); CKSUM means the device returned wrong *data*—silent corruption, caught. A handful, once, cleared with `zpool clear` and
watched: reasonable. A count that climbs after clearing: that disk (or
cable) is telling you something—swap the cheap cable before condemning
the expensive disk.
<!-- depth:4 -->
<!-- provenance: synthesized -->
What the panic-model gets wrong, structurally: DEGRADED is not an unstable
state sliding toward loss—it's a *stable* state with reduced margin. The
correct response is neither speed nor paralysis but **deliberateness**: the
real risks in a degraded pool are precision risks (replacing the *wrong*
disk—see Replacing a Disk) and window risks (a second failure during the
resilver—see Resilvering). Rushing serves the first risk; freezing serves
the second.

One habit upgrade: don't wait for a bad day to read this output. `zpool
status` on a healthy pool, regularly—or wired into monitoring (the `-x`
flag exists exactly for scripts: silence when all pools are healthy)—is
how DEGRADED becomes a Tuesday instead of an event.
