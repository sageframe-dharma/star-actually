# ZFS, Actually

The ZFS mental model as a navigable [`*, Actually`](https://star-actually.sageframe.net)
knowledge graph—for the person who met ZFS sideways (Proxmox, TrueNAS, a
homelab guide) and has been typing commands they don't own.

This is not a manual. The [OpenZFS documentation](https://openzfs.github.io/openzfs-docs/)
is the manual, and it's good. This is the layer the manual can't carry: the
naive models a smart newcomer walks in with, named and corrected—*"a pool is
a big partition"* (it isn't), *"snapshots are backups"* (they aren't),
*"SLOG is a write cache"* (it's a crash log). Every node answers one question a
person actually arrives wondering, at the depth they ask for.

## Layout

```
site.yaml     ← the domain boundary: title, root node, chains
nodes/        ← the graph—one question-shaped concept per file
peko/         ← the learning arc that produced this instance (questions,
                sources, notes, state)—the confusion-map, preserved
tests/        ← content facts, exercised through the engine
```

## Build

The build engine is the domain-blind
[`star-actually`](https://github.com/sageframe-no-kaji/star-actually) package,
pinned by tag in `pyproject.toml`.

```
make install    # uv sync
make validate   # parse nodes, weave the graph, check it's sound
make build      # render dist/
make serve      # build + serve locally
make verify     # lint + typecheck + test
```

## Provenance

Every depth layer carries a provenance marker: `extracted` (vetted against a
source logged in `peko/sources.md`) or `synthesized` (written from the
learning arc, not yet vetted line-by-line against a spine source). Destructive
operations (`zpool create`, `zpool replace`, `zfs rollback`) are hazard-marked
in the content and grounded in the OpenZFS man pages.
