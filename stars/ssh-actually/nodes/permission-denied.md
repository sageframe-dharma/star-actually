---
id: permission-denied
title: Permission Denied
type: troubleshooting
requires: [key-pairs]
related: [ssh-config-basics, known-hosts, ssh-agents, file-permissions, ssh-debugging]
entry_points: [permission denied publickey, key doesn't work, ssh rejects my key, file permissions ssh]
summary: >
  The most common SSH failure, and the diagnosis path: SSH silently refuses
  keys with wrong file permissions — no error, just "Permission denied."
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Permission Denied

<!-- depth:2 -->
<!-- provenance: extracted -->
SSH is opinionated about file permissions. If permissions are wrong, SSH **silently refuses to use the key** — no error message in normal mode, just "Permission denied." This is the single most common cause of "my key doesn't work" problems.

<!-- depth:3 -->
<!-- provenance: extracted -->
Why SSH cares: if a private key file is readable by other users, it might already be compromised. SSH would rather fail than use a key it can't trust. The same applies to `authorized_keys` on the server — if the file or its parent directories are writable by others, SSH ignores it entirely.

Fix all permissions at once, locally:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/*
chmod 644 ~/.ssh/*.pub
chmod 644 ~/.ssh/known_hosts
```

And on the server:

```bash
chmod 755 ~/
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

**The home directory matters.** Even if `~/.ssh` and `authorized_keys` are correct, the server rejects the key if your home directory is group- or world-writable. Server-side `sshd` requirement, and it trips people up constantly.

<!-- depth:4 -->
<!-- provenance: extracted -->
When key auth fails silently, the diagnosis path is:

1. **Verbose output:** `ssh -vvv user@server` — look for lines containing "Permissions", "ignored", or "bad ownership".
2. **Server-side logs** (requires existing access): `sudo tail -20 /var/log/auth.log` or `sudo journalctl -u sshd -n 20`. The server logs exactly why it rejected the key.
3. **Ownership:** `ls -la ~/.ssh/` — everything should be owned by your user. Root-owned files in `~/.ssh` are a common artifact of running `ssh-keygen` with `sudo`.

Common patterns:

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| "Permission denied (publickey)" | Private key is 644 instead of 600 | `chmod 600 ~/.ssh/id_*` |
| Works locally, not from new machine | Forgot permissions after copying | Run the fix-all commands |
| Works as root, not as user | `authorized_keys` owned by root | `chown user:user ~/.ssh/authorized_keys` |
| Suddenly stops working | Home directory permissions changed | `chmod 755 ~/` on the server |
| Works on one server, not another | Different `sshd` strictness (`StrictModes`) | Check server-side `/etc/ssh/sshd_config` |
