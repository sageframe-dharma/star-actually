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
  Sounds free because checksums already exist—actually a standing RAM tax
  on every write, forever, that loses to plain compression in almost every
  homelab.
---
<!-- depth:1 -->
Deduplication
<!-- depth:2 -->
<!-- provenance: extracted -->
The reasoning feels airtight: ZFS already checksums every block, so noticing
duplicates should be nearly free—flip it on, especially with all these
similar VMs. **Actually, dedup requires the table of every written block's
hash to be consulted on every write—which means held in RAM—and each
entry costs "slightly more than 320 bytes of memory" (OpenZFS docs),
forever, per unique block.** When the table outgrows RAM, "each cache miss
will require reading a random block from disk"—writes go random-read slow,
which is the storage equivalent of walking with your shoelaces tied
together.
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
