---
id: deploy-public-key
title: Deploying a Public Key
type: procedure
requires: [key-pairs, authorized-keys]
related: [first-key-setup, file-permissions, permission-denied]
entry_points: [ssh-copy-id, add my key to a server, manually add key to authorized_keys, deploy public key]
summary: >
  Getting your public key onto the server—ssh-copy-id, the manual
  authorized_keys method, and the permissions that must accompany it.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Deploying a Public Key

<!-- depth:2 -->
<!-- provenance: extracted -->
Deploying means getting your **public** key into the server's `authorized_keys` file so the server trusts it. `ssh-copy-id` does it automatically—logs in with your current auth method, appends the key, sets correct permissions. You can also do it by hand.

<!-- depth:3 -->
<!-- provenance: extracted -->
### automatic

```bash
ssh-copy-id -i ~/.ssh/id_example.pub user@server
```

What this does:

- Logs in with current auth method
- Appends public key to `~/.ssh/authorized_keys` on server
- Sets correct permissions

### manual

When to use: `ssh-copy-id` unavailable, or you need manual control.

On the server:

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys
# Paste ENTIRE contents of id_example.pub (one line)
chmod 600 ~/.ssh/authorized_keys
```

### hardware-backed keys

Same as regular keys:

```bash
ssh-copy-id -i ~/.ssh/key_yk.pub user@server
```

**The server doesn't care that it's hardware-backed.**

### test it

```bash
ssh user@server
```

Success indicators: logs in without password prompt (may ask for passphrase if set), no errors.
