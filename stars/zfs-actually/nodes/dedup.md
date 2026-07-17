---
id: dedup
title: Deduplication
type: concept
requires: [checksums]
related: [compression, arc]
entry_points:
  - should i enable dedup
  - zfs dedup ram
  - dedup worth it
  - fast dedup
summary: >
  Storing each duplicate piece of data only once—sounds free, actually
  costs a standing memory tax on every write, forever. Plain compression
  wins in almost every home setup.
---
<!-- depth:1 -->
Deduplication
<!-- depth:2 -->
<!-- provenance: extracted -->
**Deduplication** means storing each identical piece of data only once,
however many times it appears. The reasoning for turning it on feels
airtight: ZFS already fingerprints everything it writes, so *noticing*
duplicates should be nearly free. **Actually, noticing isn't the cost—
remembering is.** Dedup requires a directory of every piece ever written,
consulted on every single write, which means kept in fast memory: a few
hundred bytes per entry ("slightly more than 320 bytes of memory"—OpenZFS
docs), forever. When that directory outgrows memory, every write has to go
ask the slow disks first—the storage equivalent of walking with your
shoelaces tied together.
<!-- depth:3 -->
<!-- provenance: synthesized -->
Run the arithmetic before the feature: a few TB of unique 128K blocks is
already multiple GB of dedup table that must stay resident—RAM that was
being your ARC. In almost every homelab, **the RAM dedup consumes would buy
more value as cache than dedup saves as space**, and plain lz4 compression
already captures much of the same win (similar blocks compress well) for
approximately zero cost.

Where it genuinely pays: high-duplication, high-value-per-TB data—dozens
of near-identical VM golden images, certain backup corpora—on machines
specced for it. If you're not sure you're that case, you aren't. Estimate
first: `zdb -S tank` simulates the dedup ratio without committing to
anything. Under ~2×, close the tab.
<!-- depth:4 -->
<!-- provenance: extracted -->
Placed honestly:

- **vs compression**—same aisle ("space features"), opposite reflexes:
  compression default-on, dedup default-off. If you want one sentence:
  compression is free money; dedup is a mortgage.
- **Fast dedup (OpenZFS 2.3)**—"a major performance upgrade to the
  original OpenZFS deduplication functionality" (release notes): smarter,
  smaller, prunable tables. It softens the cliff; it does not repeal the
  arithmetic. The decision procedure above survives it intact.
- **The permanence trap**—`dedup=off` stops *new* dedup, but existing
  deduped blocks keep the table alive until that data is destroyed. It's a
  feature you can regret at leisure and un-regret only by rewriting data.
- **Block cloning**—modern ZFS can reflink copies (`cp` on the same pool
  sharing blocks without any table), which quietly serves the most common
  "I have copies" case for free. Much of what people wanted dedup for, it
  now delivers by default.
