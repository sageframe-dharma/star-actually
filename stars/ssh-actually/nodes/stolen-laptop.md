---
id: stolen-laptop
title: Stolen Laptop
type: scenario
requires: [key-pairs, passphrases]
related: [key-rotation, authorized-keys, recovery-planning]
entry_points: [laptop stolen ssh keys, revoke a compromised ssh key, someone has my private key file]
summary: >
  Disk-key compromise response—assume the key is being brute-forced and
  remove the public key from every authorized_keys now.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Stolen Laptop

<!-- depth:2 -->
<!-- provenance: extracted -->
A machine holding your disk-based private keys is in someone else's hands. If the key has no passphrase, the attacker can impersonate you immediately. If the passphrase is weak, the attacker can brute-force it offline.

<!-- depth:3 -->
<!-- provenance: extracted -->
**Recovery:** immediately remove your public key from all servers' `authorized_keys` files. This is the one move that actually ends the threat—once no server trusts the stolen key, it is worthless regardless of what happens to the passphrase.

What the passphrase did and didn't buy you:

- It **prevents immediate use** if the file is stolen.
- It does **not** prevent offline brute-force attacks, limit guessing attempts, or protect against malware on an unlocked system.

> If someone steals a private key file, they can brute-force the passphrase **offline with unlimited attempts**.

So a strong passphrase (20+ characters) buys you *time* to revoke—not permanent safety. Treat the key as compromised from the moment the machine is gone and use that time.

Related disk-key losses with the same shape:

- **Forgot passphrase**—cannot use the key; generate a new key pair and deploy it. Prevention: store the passphrase in a password manager.
- **Disk corruption/loss**—lose access to all servers using that key; generate a new key pair and deploy (requires existing access or out-of-band auth). Prevention: back up keys to encrypted storage.
