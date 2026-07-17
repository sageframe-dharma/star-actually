---
id: replace-disk
title: Replacing a Disk
type: procedure
requires: [zpool-status, resilver]
related: [scrub, raidz-expansion]
entry_points:
  - disk died what do i do
  - how to replace a failed disk
  - zpool replace
  - swap dead drive zfs
summary: >
  The procedure you'll run under stress, made boring: identify by serial,
  replace, watch the resilver, scrub. The real risk is precision, not speed.
---
<!-- depth:1 -->
Replacing a Disk
<!-- depth:2 -->
<!-- provenance: extracted -->
A disk has died. The instinct is either panicked speed or frozen
paralysis. **Actually, a pool that lost a disk is stable and still
serving—the procedure is unhurried, and the danger that actually bites
people is imprecision: pulling the *wrong* disk out of a machine full of
identical-looking drives.** The command itself is one line: `zpool
replace` "is equivalent to attaching new-device, waiting for it to
resilver, and then detaching device" (zpool-replace(8)). Everything around
that one line is about being absolutely sure which physical object you're
touching.

⚠ **DESTRUCTIVE**—verify before running: `zpool replace` wipes and takes
over the new disk, and pulling the wrong disk from a pool that's already
down one can kill the pool. Semantics per zpool-replace(8).
<!-- depth:3 -->
<!-- provenance: extracted -->
The procedure:

1. **Identify beyond doubt.** Map the failed device to a physical serial
   number (`zpool status` names the device; smartctl or /dev/disk/by-id
   gives the serial printed on the label). This step is the whole game—this is why pools should be built with `by-id` paths, not `/dev/sdX`
   names that reshuffle across reboots.
2. **Swap the hardware** (hot-swap bays or a powered-off swap—either is
   fine; the pool imports degraded and waits).
3. **`zpool replace tank <old-device> <new-device>`**—the new disk must
   be at least "the minimum size of all the devices" in the vdev
   (zpool-replace(8)). Resilver begins immediately; the pool serves
   throughout.
4. **Watch it finish** (`zpool status`), then **scrub** to certify the
   whole pool. Note: starting the replace "cancels any in-progress scrub"
   (man page)—resilver first, scrub after, not the reverse.
<!-- depth:4 -->
<!-- provenance: synthesized -->
Judgment calls around the mechanics:

- **Failing vs failed**—a disk that still limps (rising errors, not yet
  dead) can be replaced *while alive*: `zpool replace` with both old and
  new connected reads from the failing disk too, keeping full redundancy
  through the resilver. Strictly better when you have the ports—don't
  pull the sick disk first if you don't have to.
- **The window**—the resilver is your thinnest moment (see Resilvering);
  a RAIDZ1 rebuild across correlated, same-batch survivors is where
  healthy paranoia earns its keep. Have the replacement on the shelf
  *before* the failure; the window starts when the disk dies, not when the
  courier arrives.
- **Spares**—a `spare` vdev automates step 2 for machines you don't
  watch daily; for a watched homelab, the shelf spare plus this procedure
  is usually enough.
- **After it's boring**—the first replacement teaches you your bay
  labeling, your by-id discipline, and your nerves. Do the serial-number
  mapping *now*, on a healthy pool, and tape the printout to the case.
