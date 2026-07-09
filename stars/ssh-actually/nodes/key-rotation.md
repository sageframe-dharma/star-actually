---
id: key-rotation
title: Key Rotation
type: procedure
requires: [key-pairs, authorized-keys]
related: [key-naming, recovery-planning, hardware-keys-ssh]
entry_points: [how often should I rotate ssh keys, do ssh keys expire, replace an ssh key, left a job with keys on machines]
summary: >
  Keys never expire on their own — rotation is a manual discipline: when to do
  it, the test-before-revoke order, and how hardware keys change the calculus.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Key Rotation

<!-- depth:2 -->
<!-- provenance: extracted -->
Replacing an existing SSH key with a new one, either on a planned schedule or in response to a security event. Keys don't expire on their own — SSH has no built-in expiration mechanism. A key generated in 2019 works identically in 2029. This is a feature — and a risk.

<!-- depth:3 -->
<!-- provenance: extracted -->
**When to rotate.**

Event-driven rotation (do it now):

- You suspect a private key was exposed
- A machine with your key was stolen or decommissioned
- You left a job and had keys on work machines
- You changed your security posture (moving from disk-based to hardware-backed)

Scheduled rotation (reasonable cadence):

- Disk-based keys: once a year is practical
- Hardware-backed keys: rotation is less urgent because the key cannot be copied, but rotating when you replace hardware is good practice

**How to rotate.** Rotation means:

1. Generate a new key
2. Deploy the new public key to all servers that need it
3. Test access with the new key
4. Remove the old public key from all servers' `authorized_keys`
5. Delete or archive the old private key locally

The critical step is **3 before 4**. Test before you revoke. Otherwise a mistake in deployment locks you out.

<!-- depth:4 -->
<!-- provenance: extracted -->
Why rotate at all: rotation limits the damage from keys you forgot existed, keys on machines you no longer control, keys whose passphrases may have been compromised without your knowledge, and `authorized_keys` files on servers that have accumulated stale entries.

What most people actually do: nothing. They generate a key once, use it everywhere, and forget about it. This works until it doesn't. **Rotation is insurance — boring until the moment you need it.**

Hardware-backed keys change the rotation calculus:

- The private key cannot be copied, so "key compromise" means physical device compromise
- Non-resident keys: rotation means generating a new key, deploying the new public key, and deleting the old blob
- Resident keys: rotation means generating a new key in a new slot, deploying the new public key, and deleting the old slot entry

Hardware keys don't eliminate the need for rotation. They reduce the urgency.
