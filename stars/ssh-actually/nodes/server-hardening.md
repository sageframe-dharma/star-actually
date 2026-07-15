---
id: server-hardening
title: Server Hardening
type: concept
requires: [what-ssh-is, key-pairs]
related: [passwords, authorized-keys, permission-denied]
entry_points: [how do I harden ssh, disable password login, should I allow root login, ssh key only access]
summary: >
  Minimum viable server security—passwords off, root off, key-only access,
  sudo for escalation—and why keys structurally beat passwords.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Server Hardening

<!-- depth:2 -->
<!-- provenance: extracted -->
A properly hardened SSH server usually has:

- ❌ password login disabled
- ❌ direct root login disabled
- ✅ SSH key-only access
- ✅ normal user account
- ✅ `sudo` for privilege escalation

<!-- depth:3 -->
<!-- provenance: extracted -->
Why this exact shape?

Passwords:

- can be guessed
- can be phished
- can be reused
- can leak

SSH keys:

- cannot be guessed
- cannot be reused elsewhere
- cannot be brute-forced remotely

Disabling password login removes the entire category of remote guessing attacks. Disabling direct root login means an attacker needs both a working key *and* a way to escalate—`sudo` from a normal account keeps escalation visible and revocable.

<!-- depth:4 -->
<!-- provenance: synthesized -->
Hardening is the server-side half of the key-pair bargain:

- The server stores **only public keys**—its list of who to trust lives in `authorized_keys`, which is why auditing that file *is* auditing access. A hardened server with a stale `authorized_keys` is only half hardened.
- Passwords are the structural weakness the whole arrangement exists to remove: a shared secret the server can lose. Key-only access means there is nothing on the server worth stealing.
- Key-only cuts both ways: get the order right. Deploy your key, **test that key login works**, and only then turn password login off—the same test-before-revoke discipline as key rotation. A permissions mistake that makes SSH silently refuse your key ("Permission denied") on a password-disabled server is a lockout, not an inconvenience.
