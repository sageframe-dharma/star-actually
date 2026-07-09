---
id: key-naming
title: Naming Keys
type: concept
requires: [key-pairs]
related: [key-generation, blob, multiple-github-accounts]
entry_points: [how should I name ssh keys, ssh key naming convention, what is the ssh key comment, id_rsa vs custom names]
summary: >
  Names are for humans, not computers — clarity, intent, and scope in key
  filenames, plus why the comment field earns its keep.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Naming Keys

<!-- depth:2 -->
<!-- provenance: extracted -->
When you create SSH keys, naming them clearly helps you (and others) understand their purpose. What matters: **clarity** (can you tell what the key is for?), **intent** (does the name reflect the key's purpose?), and **scope** (is it clear where this key should be used?). Names are for humans, not computers.

<!-- depth:3 -->
<!-- provenance: extracted -->
Common naming patterns:

```
Disk-based keys:       ~/.ssh/id_purpose
                       id_github, id_homelab, id_work, id_personal_vps

Hardware-backed keys:  ~/.ssh/purpose_yk
                       github_yk, gitlab_work_yk, production_servers_yk
```

The `_yk` suffix clearly indicates hardware-backed, prevents confusion with disk keys, and makes backup decisions easier. But any clear, consistent system works.

What *doesn't* matter: matching filenames across machines, keeping names secret, or following someone else's convention if you have your own system.

Why naming matters in practice:

- **For blobs** (non-resident hardware keys): you must preserve these files. Clear names help you identify what you're backing up — losing a blob means generating a new key.
- **For human sanity**: when you have 5+ keys, unclear names create confusion. `id_rsa` tells you nothing about purpose; `github_personal_yk` tells you everything.

For public keys, the filename doesn't matter (they're deployed to servers) — the **comment inside the public key** matters more:

```
ssh-ed25519 AAAA... tyro@laptop-2024-github
```

A good comment format is `username@device-year-purpose`. It helps identify keys in server logs, makes `authorized_keys` management easier, and is useful when you have multiple keys.

The key insight: **names are for humans, not computers**. Make them useful to future-you.
