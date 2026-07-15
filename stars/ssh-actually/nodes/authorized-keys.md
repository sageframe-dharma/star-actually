---
id: authorized-keys
title: authorized_keys
type: definition
requires: [key-pairs]
related: [deploy-public-key, server-hardening, key-rotation, permission-denied]
entry_points: [what is authorized_keys, where does the server store my key, how does the server know my key, audit ssh access]
summary: >
  The server-side trust anchor—the file of public keys a server will accept,
  and the discipline of auditing it.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
authorized_keys

<!-- depth:2 -->
<!-- provenance: synthesized -->
`~/.ssh/authorized_keys` is the file on the server that lists the public keys the server will accept for your account. The server stores **only public keys**—this file is where. Every key pair that can log you in has its public half on exactly this list.

<!-- depth:3 -->
<!-- provenance: extracted -->
Two ways your public key gets there:

**Automatic**—`ssh-copy-id` logs in with your current auth method, appends the public key to `~/.ssh/authorized_keys` on the server, and sets correct permissions:

```bash
ssh-copy-id -i ~/.ssh/id_example.pub user@server
```

**Manual**—when `ssh-copy-id` is unavailable, on the server:

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys
# Paste ENTIRE contents of id_example.pub (one line)
chmod 600 ~/.ssh/authorized_keys
```

One key per line, the whole line. The permissions are not optional—if the file or its parent directories are writable by other users, SSH ignores it entirely.

<!-- depth:4 -->
<!-- provenance: synthesized -->
Because `authorized_keys` is the trust anchor, most access discipline reduces to editing it:

- **Audit regularly.** `cat ~/.ssh/authorized_keys`—remove old or unknown keys. Every line is a standing grant of access; stale entries are keys you forgot existed.
- **Rotation ends here.** Replacing a key means deploying the new public key, testing it, *then* removing the old line from every server's `authorized_keys`. Test before you revoke.
- **Compromise response starts here.** Laptop stolen? Immediately remove that public key from all servers' `authorized_keys` files—that is the revocation mechanism; there is no other.
- **Comments earn their keep.** A public key's comment (`username@device-year-purpose`) is what lets you tell lines apart when the audit happens years later.

The file rewards the same habit as the rest of a hardened server: it should say exactly what you mean, and nothing you've forgotten.
