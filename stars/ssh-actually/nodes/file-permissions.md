---
id: file-permissions
title: SSH File Permissions
type: concept
requires: [key-pairs]
related: [permission-denied, ssh-debugging, deploy-public-key]
entry_points: [ssh file permissions, chmod 600 ssh key, why does ssh care about permissions, authorized_keys permissions]
summary: >
  Why SSH is opinionated about permissions — a readable key is an
  untrustworthy key — the correct numbers on both sides, and the
  home-directory gotcha.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
SSH File Permissions

<!-- depth:2 -->
<!-- provenance: extracted -->
SSH refuses to use a private key if other users could read it. The logic: if the file is readable by others, it might already be compromised. **SSH would rather fail than use a key it can't trust.** The same applies to `authorized_keys` on the server side.

<!-- depth:3 -->
<!-- provenance: extracted -->
### correct permissions (local machine)

```bash
# The .ssh directory itself
chmod 700 ~/.ssh

# Private keys — owner read/write only
chmod 600 ~/.ssh/id_*

# Public keys — owner read/write, others can read
chmod 644 ~/.ssh/id_*.pub

# Config file
chmod 600 ~/.ssh/config

# Known hosts
chmod 644 ~/.ssh/known_hosts
```

### correct permissions (server side)

```bash
# Home directory — must not be writable by others
chmod 755 ~/
# Some servers require 700

# The .ssh directory
chmod 700 ~/.ssh

# Authorized keys file
chmod 600 ~/.ssh/authorized_keys
```

**The home directory matters.** This trips people up. Even if `~/.ssh` and `authorized_keys` have correct permissions, SSH will reject the key if the home directory itself is group-writable or world-writable. This is a server-side `sshd` requirement, not a client-side one.

<!-- depth:4 -->
<!-- provenance: synthesized -->
What this assumes, and where it connects:

- On the server side, if `authorized_keys` or its parent directories are writable by other users, SSH ignores the file entirely — the trust anchor itself must be tamper-proof, not just the secret.
- `ssh-copy-id` sets correct permissions for you; the manual deployment method makes them your job. Keys copied to a new machine arrive with whatever permissions the copy gave them — set them explicitly.
- When permissions are wrong, the failure is **silent**: no error in normal mode, just "Permission denied." The failure mode and its diagnosis path are their own node — this one carries the why and the correct numbers.
