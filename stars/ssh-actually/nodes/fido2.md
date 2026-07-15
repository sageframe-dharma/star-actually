---
id: fido2
title: FIDO2
type: concept
requires: [key-pairs, passwords]
related: [webauthn, passkeys, hardware-security-keys, phishing-resistance]
entry_points: [what is fido2, fido2 vs password, how does fido2 work, fido2 and ssh]
summary: >
  The cryptographic shift for the web—the server verifies a signature, not a
  secret; key-pair cryptography replacing shared secrets everywhere.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
FIDO2

<!-- depth:2 -->
<!-- provenance: extracted -->
**FIDO2** is a standard for cryptographic authentication where the server never learns your secret. The key idea:

> The service verifies a *signature*, not a secret.

<!-- depth:3 -->
<!-- provenance: extracted -->
FIDO2 replaces shared secrets with **key-pair cryptography**. Instead of storing a password that can be stolen, the service stores a public key and asks your authenticator to sign a challenge. Nothing reusable ever travels; nothing stealable ever sits on the server.

You encounter FIDO2 wearing several different outfits:

- **WebAuthn**—the browser API that lets websites use it
- **Passkeys**—discoverable FIDO2 credentials, made user-friendly and synced by platforms
- **Hardware security keys**—FIDO2 with physical enforcement
- **Hardware-backed SSH keys** (`ed25519-sk`)—SSH using FIDO2 hardware as signing devices

The confusion around these names exists because the technologies evolved incrementally, not coherently. They are all one idea.

<!-- depth:4 -->
<!-- provenance: extracted -->
The mental model that keeps the whole landscape coherent:

- **FIDO2** = the cryptographic foundation
- **WebAuthn** = how browsers use it
- **Passkeys** = user-friendly FIDO2
- **Hardware keys** = physical enforcement
- **SSH** = FIDO2 without the browser

SSH predates all of this. It has used key-pair cryptography since the 1990s; the web kept using passwords, then slowly caught up to where SSH already was—with different names and different contexts. SSH already knows the username and doesn't need discovery, so modern SSH simply reuses **FIDO2 hardware keys as signing devices**. That's why hardware SSH keys aren't a "new" technology—they're SSH and FIDO2 meeting in the middle, and why the same YubiKey works for web logins *and* SSH.

Everything modern converges on one principle:

> *Never give the server a secret it can lose.*
