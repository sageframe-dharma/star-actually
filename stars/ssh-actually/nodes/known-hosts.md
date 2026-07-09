---
id: known-hosts
title: Known Hosts
type: concept
requires: [what-ssh-is]
related: [signatures, host-key-changed, ssh-debugging]
entry_points: [what is known_hosts, authenticity of host can't be established, should I type yes, ssh fingerprint check]
summary: >
  The other direction of trust — you verify the server. Fingerprints, the
  first-connection prompt, and MITM protection.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Known Hosts

<!-- depth:2 -->
<!-- provenance: extracted -->
`~/.ssh/known_hosts` stores server fingerprints. Its purpose: prevent MITM attacks — someone impersonating the server you meant to reach — by verifying server identity on every connection.

<!-- depth:3 -->
<!-- provenance: extracted -->
The first connection to a new server is where the file earns its keep:

```
The authenticity of host 'server (192.0.2.10)' can't be established.
ED25519 key fingerprint is SHA256:abc123...
Are you sure you want to continue connecting (yes/no)?
```

What to do:

1. Verify the fingerprint via an out-of-band method (ask the admin, check documentation)
2. Type `yes` if the fingerprint matches
3. The server is added to `known_hosts`

**Typing `yes` blindly defeats MITM protection.** The prompt is the one moment you're actually being asked to establish trust; after that, SSH checks automatically.

Housekeeping:

```bash
cat ~/.ssh/known_hosts                 # see stored fingerprints
ssh-keygen -H -f ~/.ssh/known_hosts    # hash entries (obscures which servers you visit)
```

<!-- depth:4 -->
<!-- provenance: synthesized -->
SSH trust runs in both directions, and `known_hosts` is the half most people never think about:

- `authorized_keys` on the server answers *"should I trust this client?"*
- `known_hosts` on your machine answers *"is this really the server I think it is?"*

Both use the same mechanism — the server holds a key pair too, and proves possession by signature; the fingerprint you stored is how your client recognizes its public key. Without this check, someone between you and the server could impersonate it and quietly relay everything you type.

Which is why the scary warning — `REMOTE HOST IDENTIFICATION HAS CHANGED` — deserves a moment of respect before you fix it. Legitimate causes exist (server rebuilt, OS reinstalled, IP reused), and `ssh-keygen -R hostname` clears the stale entry. But the warning exists to catch exactly the attack this file defends against; verify before you delete.
