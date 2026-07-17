---
id: scrub
title: Scrubs
type: concept
requires: [checksums]
related: [resilver, ecc-question, zpool-status]
entry_points:
  - what does scrub do
  - does scrub fix bit rot
  - how often to scrub
  - zpool scrub
summary: >
  A forced read of everything, so checksums can catch silent damage while
  redundancy still exists to repair it. Detection is unconditional; repair
  isn't.
---
<!-- depth:1 -->
Scrubs
<!-- depth:2 -->
<!-- provenance: extracted -->
The word is active—you scrub a thing to clean it—so the naive model
makes scrub the repair process. **Actually, a scrub is a forced read: "a
normal scrub examines all data in the specified pools and verifies each
block's checksum" (zpool-scrub(8)).** Detection was always going to happen
on read; the scrub's contribution is reading the data *nothing else reads*,
so cold corruption is found while the redundancy to fix it still exists.

Repair happens only where a second good copy lives: "for replicated (mirror,
raidz, or draid) devices, ZFS automatically repairs any damage discovered."
Scrub a redundancy-less vdev and ZFS hands you a list of what rotted—named
files, even—and can heal none of it.
<!-- depth:3 -->
<!-- provenance: synthesized -->
The practice: `zpool scrub tank`, online, background, throttled behind real
traffic—expect hours to a day-plus on big HDD pools. **Monthly is the
homelab convention**, usually via a systemd timer or cron a distro already
installed (check before adding a second one). Then read the results in
`zpool status`: `repaired 0B ... with 0 errors` is the sentence you want.
A scrub that repairs a few blocks did its job; a device whose CKSUM count
rises scrub after scrub is announcing its retirement—that, plus a rising
trend, is your early-warning system working.

Why it must be scheduled at all: your hot data self-verifies on every read.
The archive nobody has opened in three years verifies never—unless
something walks it. The scrub is that something.
<!-- depth:4 -->
<!-- provenance: synthesized -->
Boundaries:

- **vs resilver**—same machinery, different scope and occasion: scrub
  reads everything on schedule; resilver reads what's needed to rebuild a
  member after replacement. Sequence them—resilver restores redundancy,
  scrub then certifies the whole pool (and note: starting a replace
  cancels a running scrub, per zpool-replace(8)).
- **vs fsck**—fsck repairs *structure* after crashes, offline, on a
  filesystem that can be inconsistent. CoW made that job obsolete. Scrub
  audits *content* against physics, online. People reach for "it's like
  fsck" and it's nearly the opposite: fsck assumes the software failed;
  scrub assumes the hardware did.
- **The scrub-of-death legend**—scrubbing with bad RAM supposedly
  destroys pools; it doesn't survive inspection (see The ECC Question).
  Scrub with confidence.
