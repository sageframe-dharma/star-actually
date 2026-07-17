---
id: compression
title: Compression
type: concept
requires: [dataset]
related: [recordsize, dedup]
entry_points:
  - should i enable compression
  - is compression slow
  - lz4 zfs
  - zfs compression ratio
summary: >
  LZ4 is so fast the old space-vs-CPU trade runs backward—compression on is
  the default posture, and it often makes the pool faster.
---
<!-- depth:1 -->
Compression
<!-- depth:2 -->
<!-- provenance: extracted -->
The inherited model: compression trades CPU for space—a tax you pay only
when the space is worth it. **Actually, with LZ4 the trade usually runs
backward: compressing costs less time than reading and writing the extra
uncompressed bytes would**, so compression frequently makes the pool
*faster*. It early-aborts on incompressible data (media files cost you
almost nothing), and it's the OpenZFS default posture—"set
compression=lz4 on your pools' root datasets so that all datasets inherit it
unless you have a reason not to enable it" (OpenZFS docs).

Your 90s-CPU intuition about gzip was correct *then*. The hardware moved;
the intuition didn't.
<!-- depth:3 -->
<!-- provenance: synthesized -->
Operating it:

- Set once at the top (`zfs set compression=lz4 tank`), let inheritance
  carry it down. On current OpenZFS, `compression=on` means lz4 already.
- Check what it's buying: `zfs get compressratio tank/...`—text, logs,
  and databases commonly land 1.5–3×; already-compressed media sits at
  1.0× and cost you a rounding error to check.
- **zstd** is the deliberate upgrade: better ratios than lz4 for more CPU,
  tunable levels (`compression=zstd-3`). Worth it on datasets that are
  compressible, written moderately, and read a lot—archives, logs. lz4
  remains the right default reflex.

The temporal gotcha (same rule as every ZFS property): it applies to **newly
written blocks only**. Flipping it on rewrites nothing—old data stays
uncompressed until something rewrites it. Don't be puzzled by a 1.0× ratio
on a dataset that was full before you enabled it.
<!-- depth:4 -->
<!-- provenance: synthesized -->
Boundaries worth holding:

- **vs dedup**—the two get mentioned together as "space features" and
  deserve opposite reflexes: compression is nearly-free and default-on;
  dedup is a standing RAM tax and default-off. Compression also quietly
  captures much of what people hope dedup will give them (all those similar
  text blocks compress well) for none of the cost.
- **vs recordsize**—compression works per record, so larger records give
  the compressor more to chew on; a 1M-recordsize archive dataset
  compresses meaningfully better than the same bytes at 128K. The two knobs
  are teammates on archive-shaped data.
- **Where not to bother**—datasets that are purely already-compressed
  media *can* be set `compression=off` for tidiness, but the early-abort
  makes the savings mostly aesthetic. The reflex "off for performance" is
  the one to unlearn.
