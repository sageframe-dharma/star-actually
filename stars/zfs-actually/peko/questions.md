# Questions—ZFS

*The question/need log. Ordered and append-only; the order IS the learning
path (D9). Simulated arc: authored as Andrew's plausible path from "I operate
ZFS through a skill" to "I can reason about it"—for comparison against his
own live arc.*

---

## Q01 · what even is ZFS   [phase: P1] [status: resolved]
- **Asked:** I keep calling ZFS a filesystem, but I also use it to do RAID-ish things and to carve out volumes for Docker. Which is it? What layer does it live at?
- **Naive model:** ZFS is a filesystem like ext4 or APFS, with a RAID feature bolted on the side, sitting on top of the normal disk stack.
- **Why it felt right:** Every other storage thing I've touched respects the layers—partition, then RAID, then filesystem. Tools have one job.
- **Resolved by:** node `what-zfs-is`
- **Actually:** ZFS is the whole storage stack in one system—volume manager, RAID layer, and filesystem merged on purpose, because the merge is what lets it keep its promises. The "layering violation" everyone complained about is the design.

## Q02 · pool vs dataset vs vdev   [phase: P1] [status: resolved]
- **Asked:** The deploy skill makes "datasets" inside a "pool," and zpool status shows "vdevs." I've been using all three words for a year without being able to define any of them. What's the actual containment hierarchy?
- **Naive model:** Pool = big partition. Dataset = folder with superpowers. Vdev = fancy word for disk.
- **Why it felt right:** That mapping let me operate. Everything I typed worked, so the model never got tested.
- **Resolved by:** node `pool` (and `vdev`, `dataset`)
- **Actually:** Disks form vdevs, vdevs form the pool, datasets carve the pool's one shared space into policy boundaries. None of the three is a partition—nothing has a fixed size anywhere in the stack.

## Q03 · where does redundancy live   [phase: P2] [status: resolved]
- **Asked:** If I have a pool of two mirrors and one lone disk I added later, is my data safe? The pool is "redundant," right?
- **Naive model:** Redundancy is a property of the pool—the pool has parity/copies spread across everything, like one big RAID.
- **Why it felt right:** "Pool" sounds like one homogeneous thing. And mdraid works that way—the array is the unit.
- **Resolved by:** node `vdev`
- **Actually:** Redundancy lives inside each vdev, never between vdevs. The pool stripes across vdevs with zero redundancy at that level—lose any single vdev and the whole pool is gone. That lone disk is a loaded gun pointed at both mirrors.

## Q04 · why so many datasets   [phase: P2] [status: resolved]
- **Asked:** The deploy skill makes a separate dataset per service. Isn't that overkill? On ext4 I'd just make directories.
- **Naive model:** Datasets are like partitions—pre-sized, expensive, something you plan carefully and make few of.
- **Why it felt right:** Everything that looked like a filesystem before had a size and a cost.
- **Resolved by:** node `dataset`
- **Actually:** Datasets are nearly free and have no fixed size—they all share the pool's space. They're the unit of *policy*: per-dataset compression, recordsize, quotas, snapshots, replication. A directory can't be snapshotted or sent; a dataset can. Make many.

## Q05 · what copy-on-write actually means   [phase: P2] [status: resolved]
- **Asked:** People say ZFS is copy-on-write and that this is why it doesn't need fsck. Copy of *what*, on write of *what*?
- **Naive model:** CoW is a safety feature like journaling—it keeps a copy of what you're changing so it can recover if interrupted.
- **Why it felt right:** Journaling was the last "crash safety" mechanism I'd absorbed, so the new one got parsed as a variant of it.
- **Resolved by:** node `copy-on-write`
- **Actually:** ZFS never overwrites a live block, ever. Every write goes to fresh space, then the pointers flip atomically. There's no journal replaying half-finished work—a write either fully happened or never happened. It's not a recovery mechanism; it's the removal of the state that needed recovering.

## Q06 · how can snapshots be free   [phase: P2] [status: resolved]
- **Asked:** Sanoid takes snapshots of everything every hour and the pool doesn't fill up. If a snapshot is a copy of the dataset, where is all that data going?
- **Naive model:** A snapshot is a copy—maybe a clever compressed one, but fundamentally a duplicate that costs what the data costs.
- **Why it felt right:** "Snapshot" sounds like a photograph—a captured duplicate of a moment.
- **Resolved by:** node `snapshot`
- **Actually:** A snapshot copies nothing. It's a named pointer that pins blocks that already exist—creation is instant and free because CoW means old blocks were never going to be overwritten anyway. The cost arrives later, as the live data diverges from the pinned past.

## Q07 · I deleted 100GB and got nothing back   [phase: P2] [status: resolved]
- **Asked:** I cleared a huge pile of build artifacts off a dataset and `zfs list` showed almost no space freed. Deleting is supposed to free space. What is holding it?
- **Naive model:** Deleting files frees their space. That's what deleting *is*.
- **Why it felt right:** Forty years of filesystems have worked that way.
- **Resolved by:** node `snapshot-space`
- **Actually:** Deletion only frees blocks nothing references. Every hourly snapshot still references those artifacts, so the space moved from the dataset's ledger to the snapshots' ledger (`USEDBYSNAP`). The space comes back when the last snapshot pinning it is destroyed—deleting files in the present can't unpin the past.

## Q08 · are my snapshots backups   [phase: P2] [status: resolved]
- **Asked:** Sanoid keeps hourlies, dailies, monthlies on every host. That's a backup regime, right? I could lose anything and roll back.
- **Naive model:** Lots of snapshots at good intervals = backed up.
- **Why it felt right:** Snapshots do the thing backups are *for*—they let you recover yesterday's state. The recovery experience is identical, so the protection felt identical.
- **Resolved by:** node `snapshots-are-not-backups`
- **Actually:** A snapshot lives on the same disks, in the same pool, behind the same controller, in the same building as the data. It shares every failure domain that matters—pool loss, fire, theft, a fat-fingered `zpool destroy`. Snapshots are the *versioning half* of a backup strategy; replication (`zfs send` to another machine) is the *backup half*.

## Q09 · what send/recv actually moves   [phase: P2] [status: resolved]
- **Asked:** Syncoid "replicates" datasets between hosts. Is that rsync with extra steps? Why does everyone act like send/recv is sacred?
- **Naive model:** send/recv is a file-sync tool—it walks the tree, finds changed files, copies them, like rsync.
- **Why it felt right:** Same job description: get this data onto that machine.
- **Resolved by:** node `send-recv`
- **Actually:** send serializes a *snapshot*—an exact, block-level, point-in-time state, properties included—and an incremental send ships only the blocks born between two snapshots, found by birth-time on the block tree, no directory walking, no comparing. rsync approximates sameness; recv *is* sameness. The price: both sides must share a common snapshot, and if it gets destroyed, incrementals are over—full send from zero.

## Q10 · what sanoid and syncoid actually are   [phase: P2] [status: resolved]
- **Asked:** I've been running sanoid and syncoid via the deploy skill's config for a year. What are they actually doing on my behalf?
- **Naive model:** Some kind of unified backup daemon—one system that "does ZFS backups."
- **Why it felt right:** I configured them once, together, in one file, and never looked again. One config, one mental object.
- **Resolved by:** node `sanoid-syncoid`
- **Actually:** Two separate small tools wrapping two ZFS primitives. Sanoid is a policy engine over `zfs snapshot`/`zfs destroy`—take hourlies/dailies/monthlies, prune on schedule. Syncoid is an orchestrator over `zfs send | zfs recv`—find the common snapshot, ship the increment. Neither adds storage machinery of its own; it's all cron-shaped judgment on top of snapshots.

## Q11 · ZFS is eating my RAM   [phase: P2] [status: resolved]
- **Asked:** htop on the Proxmox hosts shows almost all RAM used even when the VMs are light. Is ZFS leaking? Should I cap it?
- **Naive model:** High RAM usage = something is wrong. Free RAM is healthy RAM.
- **Why it felt right:** Every OS dashboard trains you to read the memory bar as a fuel gauge—full is bad.
- **Resolved by:** node `arc`
- **Actually:** That's the ARC, ZFS's adaptive read cache, and it's supposed to be huge—free RAM does nothing for anyone. It yields when applications ask (with some lag, and on Linux the pressure dance is imperfect, hence `zfs_arc_max` on VM hosts). The fuel-gauge reading of the memory bar is the wrong instrument.

## Q12 · should I add a cache SSD   [phase: P2] [status: resolved]
- **Asked:** Old drives are slow; I have a spare NVMe. Everyone on the forums adds an L2ARC. Should I?
- **Naive model:** Cache is free speed. Adding a faster tier can only help.
- **Why it felt right:** In every other context (CPU caches, CDNs), more cache = better. Nobody ever removed a cache to go faster.
- **Resolved by:** node `l2arc`
- **Actually:** L2ARC's index lives in RAM—every cached block on the SSD *costs ARC*, the cache that's actually fast. On a small system you're often trading excellent cache for mediocre cache. The right order: max out RAM first, prove ARC misses are the problem, only then consider L2ARC.

## Q13 · what the SLOG actually is   [phase: P2] [status: resolved]
- **Asked:** Same forums: "add a SLOG to speed up writes." So it's a write cache on fast media—writes land there first, then flush to the pool?
- **Naive model:** SLOG = write buffer. Data flows *through* it on its way to the disks.
- **Why it felt right:** That's what a write cache is everywhere else, and the word "log" didn't register as load-bearing.
- **Resolved by:** node `zil-slog`
- **Actually:** Nothing flows through the SLOG. Writes stage in RAM regardless; the ZIL is a crash-recovery *log* that is written and—in normal operation—never read. It's read exactly once: at import after a crash. And it only exists for *synchronous* writes; async writes (most of a homelab) don't touch it. A SLOG on an all-async workload is a decoration.

## Q14 · RAIDZ is just RAID5, right   [phase: P2] [status: resolved]
- **Asked:** RAIDZ1/2/3 map to RAID5/6/whatever—same parity math, same tradeoffs. So why do the VM people all insist on mirrors?
- **Naive model:** RAIDZ = RAID5 with a Z. And more spindles = more speed, so a wide RAIDZ should be fast.
- **Why it felt right:** The parity arithmetic *is* the same shape, and capacity math is how everyone compares arrays.
- **Resolved by:** node `raidz` (and `mirror`)
- **Actually:** Two real differences. RAIDZ closes RAID5's write hole (CoW + variable-width stripes—no read-modify-write, no torn parity). But each RAIDZ vdev delivers roughly *one disk's worth of IOPS* no matter how wide—every random read touches every data disk. Mirrors scale read IOPS with every disk. RAIDZ for bulk sequential storage; mirrors for VMs and databases. Capacity math and performance math point in opposite directions.

## Q15 · can I grow a RAIDZ later   [phase: P2] [status: resolved]
- **Asked:** If I build a 3-disk RAIDZ1 today, can I add a fourth disk next year when I need space? Or am I locked in?
- **Naive model:** Either "of course, arrays grow" (NAS-appliance intuition) or, after first forum contact, "never, ZFS vdevs are immutable forever."
- **Why it felt right:** Both answers circulate. The forums are full of pre-2025 absolutes.
- **Resolved by:** node `raidz-expansion`
- **Actually:** Since OpenZFS 2.3 (Jan 2025), yes—`zpool attach` can widen a RAIDZ vdev, live. Two catches: existing data keeps its old parity-to-data ratio until rewritten, so reclaimed capacity is less than naive math suggests; and you still can't change *type* (RAIDZ1→RAIDZ2) or shrink. The old absolute is stale, but the planning pressure it created is still mostly good advice.

## Q16 · what is ashift and why the panic   [phase: P2] [status: resolved]
- **Asked:** Guides scream about getting ashift right at creation. It's one number. Why is this one setting treated like pouring a foundation?
- **Naive model:** It's a tunable like the rest—if it's wrong, change it later.
- **Why it felt right:** Nearly everything else in ZFS is a property you can set anytime. The system trains you to expect mutability.
- **Resolved by:** node `ashift`
- **Actually:** Ashift is the sector-size assumption baked into a vdev's on-disk format at creation—"set at vdev creation and it is immutable" (OpenZFS docs). Wrong (ashift=9 on a 4K drive that lies about its sectors), and every small write becomes read-modify-write inside the drive, forever, and the only fix is destroying the vdev. It's the one decision that is actually a foundation pour. Use ashift=12 unless you can prove otherwise.

## Q17 · doesn't compression cost speed   [phase: P2] [status: resolved]
- **Asked:** The deploy skill sets compression=lz4 on everything, including stuff that barely compresses. Shouldn't compression be reserved for compressible data? CPU isn't free.
- **Naive model:** Compression trades CPU for space—a tax you pay only when the space is worth it.
- **Why it felt right:** That was true for decades (gzip on a 90s CPU was a real tax).
- **Resolved by:** node `compression`
- **Actually:** LZ4 is so fast the trade usually *reverses*: compressing costs less time than writing/reading the uncompressed extra bytes, so lz4 is frequently faster than no compression. It early-aborts on incompressible data. It's the OpenZFS default now. The real gotcha is temporal: it only touches newly written blocks—flipping it on rewrites nothing.

## Q18 · recordsize is the disk block size?   [phase: P2] [status: resolved]
- **Asked:** Is recordsize ZFS's version of the 512B/4K sector thing? Why would I tune it per dataset?
- **Naive model:** recordsize = the fixed block size ZFS writes to disk, a hardware-ish constant.
- **Why it felt right:** "Size of the blocks" only had one slot in my head, and sectors occupied it.
- **Resolved by:** node `recordsize`
- **Actually:** recordsize is the *maximum logical block per file*, per dataset, default 128K—a policy knob, not a hardware fact (that's ashift). It matters when apps do small random I/O inside big files: a 16K database page under 128K records means reading/CoW-ing 128K to touch 16K. Match it to the workload's I/O grain (16K for InnoDB, 1M for media), and remember it applies to new files only.

## Q19 · dedup sounds free   [phase: P2] [status: resolved]
- **Asked:** ZFS checksums every block anyway—dedup seems like it comes along for free. My VMs share most of their OS blocks. Turn it on?
- **Naive model:** The checksums already exist, so noticing duplicates is nearly free space savings.
- **Why it felt right:** The mechanism genuinely does reuse the checksum work—the inference wasn't crazy, it just ignored where the table lives.
- **Resolved by:** node `dedup`
- **Actually:** Dedup needs the table of every written block's hash *in RAM on the write path*—hundreds of bytes per block, forever, and when it spills, every write goes disk-random-slow. The RAM it eats buys more storage than dedup saves in almost every homelab case. Compression captures most of the win for none of the tax. (OpenZFS 2.3's fast dedup softens the cliff; it doesn't repeal the math.)

## Q20 · do I need ECC or ZFS eats my data   [phase: P2] [status: resolved]
- **Asked:** The forums say running ZFS without ECC RAM is reckless—the "scrub of death" will corrupt everything. My hosts are consumer boards. Am I sitting on a time bomb?
- **Naive model:** ZFS is *more* dangerous than other filesystems without ECC, because scrubs "correct" good data with bad RAM.
- **Why it felt right:** It's repeated with total confidence in every homelab thread, and it has the shape of expert knowledge—counterintuitive, specific, scary.
- **Resolved by:** node `ecc-question`
- **Actually:** Matt Ahrens (ZFS co-creator): "There's nothing special about ZFS that requires/encourages the use of ECC RAM more so than any other filesystem." The scrub-of-death mechanism doesn't survive inspection—a repair write requires a checksum *match* on the reconstructed data, which bad RAM can't fake by accident. ECC is good, for every filesystem equally. ZFS without ECC is still safer than ext4 without ECC.

## Q21 · does scrub fix bit rot   [phase: P2] [status: resolved]
- **Asked:** Sanoid's ecosystem assumes monthly scrubs. Is the scrub what protects me from bit rot—does running it *fix* things?
- **Naive model:** Scrub = the repair process. Checksums are just how it finds what to repair. One mechanism, "scrubbing."
- **Why it felt right:** The word is active—you scrub something to clean it.
- **Resolved by:** node `scrub` (and `checksums`)
- **Actually:** Detection and repair are separate powers. Checksums (always on, every read) *detect* corruption everywhere. *Repair* needs a second good copy—mirror, RAIDZ parity, copies=2. A scrub is just a forced read of everything, so corruption in cold data gets found while redundancy still exists to fix it. Scrub a redundancy-less vdev and ZFS tells you what rotted; it can't heal any of it.

## Q22 · a disk died, now what   [phase: P2] [status: resolved]
- **Asked:** zpool status shows DEGRADED and a dead disk. My honest instinct was to shut everything down and read for three hours. What's the actual move?
- **Naive model:** DEGRADED means the pool is dying/half-broken; touching it might tip it over. Panic-shaped caution.
- **Why it felt right:** Red words in status output mean crisis in every other system I run.
- **Resolved by:** node `replace-disk` (and `zpool-status`)
- **Actually:** DEGRADED means the design is *working*—redundancy absorbed the failure and the pool is serving normally with less margin. The move is unhurried and boring: identify the disk by serial, `zpool replace`, watch the resilver, scrub after. The real risks are precision risks—replacing the wrong disk, or a second failure during the resilver window—which is why you move deliberately, not fast.

## Q23 · resilver vs rebuild   [phase: P2] [status: resolved]
- **Asked:** Why does ZFS have its own word for rebuilding? Is a resilver just a rebuild with branding?
- **Naive model:** Same thing: copy every sector from the survivors to the new disk, start to end.
- **Why it felt right:** Hardware RAID and mdraid literally do that.
- **Resolved by:** node `resilver`
- **Actually:** ZFS is the filesystem, so it knows which blocks are *live*—a resilver copies data, not disk, and verifies every block against its checksum as it goes. Half-full pool = roughly half the rebuild time = half the second-failure window. (The trade: it walks the block tree, so on a very full, fragmented pool it's seek-bound and can be slower than a dumb sequential rebuild.)

## Q24 · why isn't any of this in fstab   [phase: P2] [status: resolved]
- **Asked:** I went to check how my datasets mount and fstab is empty. Where does mounting even happen? What do I edit?
- **Naive model:** Filesystems mount via /etc/fstab. That file is the source of truth; ZFS must generate entries into it somehow.
- **Why it felt right:** Decades of Linux muscle memory—mount configuration lives in fstab, full stop.
- **Resolved by:** node `mountpoints`
- **Actually:** ZFS mounts itself. The mountpoint is a *property of the dataset*, stored in the pool, inherited down the tree—`zfs set mountpoint=` is the edit, `zfs mount -a` at import does the work. The config travels *with the data*: export the pool, import it on another machine, everything mounts where it should. fstab describes storage to the OS; ZFS pools carry their own description.

## Q25 · is my data trapped in this machine   [phase: P2] [status: resolved]
- **Asked:** If a host motherboard dies, are the pools recoverable, or is there machine-specific state I need to be backing up? Where does the pool's "definition" live?
- **Naive model:** Array/mount configuration lives somewhere in the OS (a config file, like mdadm.conf)—lose the OS, face a painful reconstruction.
- **Why it felt right:** mdraid and hardware RAID both keep essential config off-disk (or in a controller). Controllers dying and taking arrays with them is a classic horror story.
- **Resolved by:** node `pool-import-export`
- **Actually:** The pool's entire self-description—layout, properties, mountpoints, dataset tree—lives *on the member disks* as labels. Any machine with OpenZFS can `zpool import` the disks and get everything, mounts included. The host keeps only a convenience cachefile. Dead motherboard = move disks, import, done. The data was never married to the machine.

## Q26 · why does a full pool get slow   [phase: P2] [status: resolved]
- **Asked:** Rule-of-thumb says don't fill a pool past ~85–90%. My instinct says a 95%-full disk is just a disk with less room—why would *speed* care?
- **Naive model:** Fullness costs capacity, not performance. Slow-when-full is a UI myth.
- **Why it felt right:** For read-mostly workloads on ordinary filesystems it mostly *is* a myth.
- **Resolved by:** node `free-space-discipline`
- **Actually:** CoW makes free space a *working resource*: every write—including "overwrites" and even deletions—needs fresh contiguous-ish space to land. A full pool means allocation works harder, writes fragment, and the pool's steady state degrades (and fragmentation doesn't undo when you free space later). Free space isn't headroom; it's the workshop floor CoW operates on.

## Q27 · rollback ate my snapshots   [phase: P2] [status: resolved]
- **Asked:** I assumed rollback was a cursor I could move around the timeline—roll back to Tuesday, look around, roll forward to Thursday. That's not what happened, is it?
- **Naive model:** Snapshots form a timeline you can move along freely in both directions; rollback is navigation.
- **Why it felt right:** VM snapshots in Proxmox feel exactly like that—jump anywhere, nothing is lost.
- **Resolved by:** node `rollback`
- **Actually:** Rollback is demolition, not navigation: rolling back to Tuesday *destroys* everything after Tuesday—later snapshots, later data, permanently (`-r` confirms rather than protects). There is no roll forward. The nondestructive way to look at the past is `zfs clone` (a writable branch) or the snapshot's hidden `.zfs/snapshot/` directory. Rollback is for "the present is wrong, discard it," nothing gentler.

## Q28 · what Proxmox actually did to my disks   [phase: P2] [status: resolved]
- **Asked:** Proxmox "uses ZFS"—but my VM disks aren't files I can see, and there's an rpool I never made. What did the installer actually set up, and what are these zvols?
- **Naive model:** Proxmox stores VM disks as image files (qcow2-ish) on a ZFS filesystem it made somewhere.
- **Why it felt right:** VirtualBox/ESXi habits—a VM disk is a big file you can locate and copy.
- **Resolved by:** node `proxmox-zfs` (and `zvol`)
- **Actually:** Proxmox carves each VM disk out of the pool as a *zvol*—a dataset that presents as a raw block device instead of a filesystem. No file, no image format, no filesystem-in-a-file overhead; and each VM disk is individually snapshottable/sendable like any dataset. The rpool is the installer's pool for the OS itself. My "datasets and services" model and Proxmox's "zvols and VMs" model are the same machinery wearing two faces.

---

*The entries below arrived after handoff, from the first reader test of the
built site. They are the reader's questions, not the practitioner's—and Q29
is the finding that forced the boundary correction.*

## Q29 · the reader isn't me   [phase: P4] [status: resolved]
- **Asked:** (first reader test of the site) "There's still no initial base—what even IS a filesystem? This feels confusing. We need to be able to start from absolute basics."
- **Naive model:** The P0 boundary assumed the reader shares the practitioner's starting point: someone already *operating* ZFS who lacks the model. The instance's ground floor was set at "What ZFS Is," which silently assumes the reader knows what a filesystem is, what RAID is, what a volume manager is.
- **Why it felt right:** The arc's origin story was "I run ZFS through automation and don't hold the model"—so every node was aimed at that person. Authoring from your own arrival is the default failure of expertise: the boundary of your own confusion feels like the boundary of everyone's.
- **Resolved by:** node `what-a-filesystem-is` (new root), plus `filesystem-history`, `filesystem-landscape`, and the "Start from zero" chain
- **Actually:** A `*, Actually` serves *arrivals*, and arrivals don't share your history. The root must sit at the true ground floor—the reader who needs altitude can climb; the reader who doesn't can search past it. Reader agency includes the reader who knows nothing yet.

## Q30 · what is a filesystem, actually   [phase: P4] [status: resolved]
- **Asked:** What even is a filesystem? I've formatted drives and seen NTFS and ext4 in dropdowns, but I couldn't define the thing.
- **Naive model:** "My files are on the disk"—the disk somehow inherently contains files and folders.
- **Why it felt right:** Every interface shows files as *things in a place*; nothing in daily computing ever exposes the bookkeeping layer.
- **Resolved by:** node `what-a-filesystem-is`
- **Actually:** The disk holds only numbered blocks and has no idea what a file is. The filesystem is the ledger that invents files, names, and folders on top of anonymous blocks—lose the ledger and the blocks remain, meaning nothing.

## Q31 · why are there so many filesystems   [phase: P4] [status: resolved]
- **Asked:** FAT32, NTFS, ext4, APFS, ZFS—why does this keep happening? Are the old ones just bad?
- **Naive model:** Filesystems are versions—newer replaces older, and the old ones persist out of laziness.
- **Why it felt right:** That's how most software works; "why hasn't everyone upgraded" is usually a fair question.
- **Resolved by:** node `filesystem-history` (and `filesystem-landscape`)
- **Actually:** Filesystem history is a chain of disasters and answers—simple ledgers lost to crashes, journaling answered crashes, the integrity generation (ZFS) answered lying hardware. Each older generation survives exactly where its trade-offs still fit: FAT32 rules camera cards *because* simplicity is the feature there. They're not versions; they're different answers to different disasters.

## Q32 · plain words in the wrong order are still arcane   [phase: P4] [status: resolved]
- **Asked:** (reader test, round three) "This is so awkward: 'You'll want to call ZFS a filesystem, because that's the word the ecosystem uses. Actually, ZFS is the entire storage stack…' Do you see the learning path there?"
- **Naive model:** "Clear and additive" means plain vocabulary—swap jargon for everyday words and the surface is fixed. A sentence can open with the author's conclusion as long as the words in it are simple.
- **Why it felt right:** The jargon was the visible offense, so removing jargon looked like the whole cure. But a plain-worded sentence that starts from the author's conclusion still strands the reader—they have the words and not the ground.
- **Resolved by:** the walk shape, applied to every depth-2 surface (heard-word → define it → anchor it in lived experience → then the correction)
- **Actually:** Additive means *ordered*, not merely plain: start from the word or belief the reader already carries, define it in the same breath, anchor it in something they've lived (FAT32 on a USB stick), and only then fire the "actually." Each sentence hands the next its footing—the correction lands *because* the ground was laid. A depth-2 that opens with the author's framing is a lecture; one that opens with the reader's is a path.
