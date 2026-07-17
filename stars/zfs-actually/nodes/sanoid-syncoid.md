---
id: sanoid-syncoid
title: Sanoid and Syncoid
type: concept
requires: [snapshot, send-recv]
related: [snapshot-space, proxmox-zfs]
entry_points:
  - what is sanoid
  - what is syncoid
  - automated zfs snapshots
  - zfs backup automation
  - snapshot policy
summary: >
  Not one "backup system"—two small helpers: sanoid takes and prunes
  snapshots on a schedule; syncoid ships them to another machine. Both just
  automate things you can do by hand.
---
<!-- depth:1 -->
Sanoid and Syncoid
<!-- depth:2 -->
<!-- provenance: extracted -->
A snapshot routine that actually protects you—taken every hour, old ones
cleaned out, fresh copies shipped to another machine—is a chore no human
keeps up by hand at three in the morning. So most serious ZFS setups run
two small helper tools, usually installed together and easily mistaken for
one thing called "the backup system." **Actually, they're two separate
helpers, each automating one job you can do yourself.** **Sanoid** is the
snapshot-taker: "a policy-driven snapshot management tool" (its README)—it
takes snapshots on a schedule (hourly, daily, monthly) and deletes old
ones according to rules you set. **Syncoid** is the shipper: it
"facilitates the asynchronous incremental replication of ZFS filesystems"—
it finds the last moment both machines share, and sends over only what's
new since.

Neither adds any storage machinery of its own. They're scheduling and
judgment layered on top of snapshots and send/receive—which is why
understanding those two ideas *is* understanding these tools.
<!-- depth:3 -->
<!-- provenance: extracted -->
The working setup (the practitioner's homelab runs exactly this shape):
`/etc/sanoid/sanoid.conf` assigns each dataset a template—
```
[tank/services/postgres]
  use_template = production   # hourlies pruned in days; frequent history
[tank/media]
  use_template = archive      # weekly, kept for months; slow history
```
—and a timer runs `sanoid --cron`. Separately, a scheduled
`syncoid --recursive tank/services backup-host:vault/services` replicates.
Two decisions worth making deliberately rather than by default: retention
*per dataset* (churn-heavy data accrues snapshot rent fast—see Snapshots
and Disappearing Space), and replication cadence per dataset (how much
history are you willing to lose—that's your real RPO, in systems terms:
the age of the newest copy elsewhere when disaster hits).
<!-- depth:4 -->
<!-- provenance: synthesized -->
The relationship that bites when misunderstood: **sanoid's pruning and
syncoid's incrementals share the snapshot chain.** Incremental replication
needs a common snapshot on both ends; a retention policy that destroys it
forces the next replication to start from zero. Design retention and
replication as one system (syncoid's own sync snapshots exist to hold the
reference point)—and treat hand-deleting snapshots under a policy engine
as off-limits; change the policy instead.

Automation's quiet cost, named once: a year of these tools working
flawlessly is a year of never being forced to learn what they do—the
naive models survive *because* nothing fails. Run the primitives by hand
once (`zfs snapshot`, `zfs send -i ... | zfs recv`), and the config file
stops being an incantation. Then let the robots have it back.
