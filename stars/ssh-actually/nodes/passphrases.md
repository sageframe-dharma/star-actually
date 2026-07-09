---
id: passphrases
title: Passphrases
type: concept
requires: [key-pairs]
related: [ssh-agents, pins-vs-passphrases, macos-keychain, trust-boundaries]
entry_points: [should I set a passphrase, what does a passphrase protect, passphrase vs password, forgot my ssh passphrase]
summary: >
  A secret that encrypts a private key at rest — and its honest limits:
  offline brute-force with unlimited attempts.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Passphrases

<!-- depth:2 -->
<!-- provenance: extracted -->
A **passphrase** is a secret used to encrypt a private key **at rest** on disk. It is not a password for a server — it protects the key file itself.

<!-- depth:3 -->
<!-- provenance: extracted -->
What it does:

- prevents immediate use if the file is stolen

What it does **not** do:

- prevent offline brute-force attacks
- limit guessing attempts
- protect against malware on an unlocked system

The important reality:

> If someone steals a private key file, they can brute-force the passphrase **offline with unlimited attempts**.

That's why strength matters — 20+ characters, stored in a password manager. The tradeoff is honest: no passphrase → convenient, unsafe; passphrase → safer, annoying.

And if you forget it: there is no recovery. You cannot use the key. Generate a new key pair and deploy it to your servers — which is exactly why the passphrase belongs in a password manager.

<!-- depth:4 -->
<!-- provenance: synthesized -->
The passphrase sits at the center of three tradeoffs:

- **The annoyance has a fix.** Retyping the passphrase every connection is what **SSH agents** exist for — the agent caches the unlocked key for a session. macOS goes further and makes the whole thing invisible (Keychain + Touch ID), which is convenience, not a stronger boundary.
- **The comparison that clarifies it.** A passphrase protects a *file*, brute-forceable offline with unlimited attempts. A hardware PIN protects a *physical device*, with attempt limits enforced inside the hardware. That asymmetry is why a 6-digit PIN can safely replace a 40-character passphrase.
- **What it says about where you stand.** Needing a passphrase at all is a symptom of the disk-based trust boundary: the secret is a copyable file, so it needs armor. Hardware keys remove the file entirely — and the passphrase with it.
