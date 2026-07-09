---
id: host-key-changed
title: Host Key Changed
type: troubleshooting
requires: [known-hosts]
related: [ssh-debugging, permission-denied]
entry_points: [remote host identification has changed, host key verification failed, ssh-keygen -R, server rebuilt ssh warning]
summary: >
  The scary warning decoded — legitimate causes (rebuilt server, reused IP)
  versus the attack it exists to catch, and the ssh-keygen -R fix.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Host Key Changed

<!-- depth:2 -->
<!-- provenance: synthesized -->
SSH refuses to connect and warns that the remote host's identification has changed. `~/.ssh/known_hosts` stores server fingerprints to prevent **MITM attacks** (man-in-the-middle — someone intercepting your connection and impersonating the server), and this warning means the server you reached is presenting a different fingerprint than the one on record.

<!-- depth:3 -->
<!-- provenance: extracted -->
When the change is legitimate:

- Server was rebuilt
- Server OS reinstalled
- IP address reused

The fix — remove the stale entry from `known_hosts`:

```bash
ssh-keygen -R server-name
ssh-keygen -R 192.0.2.10
```

Then reconnect. You'll get the first-connection prompt again:

```
The authenticity of host 'server (192.0.2.10)' can't be established.
ED25519 key fingerprint is SHA256:abc123...
Are you sure you want to continue connecting (yes/no)?
```

What to do:

1. Verify fingerprint via out-of-band method (ask admin, check documentation)
2. Type `yes` if fingerprint matches
3. Server added to known_hosts

**Security note:** typing `yes` blindly defeats MITM protection. The warning exists precisely to catch the case where the "changed" server is actually an attacker in the middle — if you can't explain *why* the key changed (no rebuild, no reinstall, no IP reuse you know of), stop and verify before you clear the entry.
