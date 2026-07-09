---
id: presence-vs-identity
title: Presence vs Identity
type: concept
requires: [touch-requirement]
related: [hardware-pin, mfa, passkeys]
entry_points: [why is touch enough, do I need the biometric yubikey, touch vs fingerprint security key, does my fingerprint go to the server]
summary: >
  Touch proves a human is present now; biometrics prove which human. For
  cryptographic auth, presence is sufficient and identity is optional.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Presence vs Identity

<!-- depth:2 -->
<!-- provenance: extracted -->
This is subtle and important. **Touch** proves a human is present *now* and the action is intentional. **Biometrics** prove *which* human is present. For cryptographic authentication, **presence is sufficient — identity is optional**.

<!-- depth:3 -->
<!-- provenance: extracted -->
The goal of hardware security keys is to **prevent remote, automated, or malware-driven abuse**. Measured against that goal:

Touch proves:

- a human is present
- automation is impossible

Biometrics:

- unlock the device
- do *not* provide cryptographic identity to servers

That's why touch is required, biometrics are optional, and a PIN replaces passphrases cleanly. Touch is enough because **presence**, not identity, is the goal.

<!-- depth:4 -->
<!-- provenance: synthesized -->
This is the answer to "do I need the biometric model?" — the fingerprint reader is purely a **local unlock convenience**; cryptographic guarantees are identical with touch+PIN. Your fingerprint never goes to the server. Nothing about the signature the server verifies changes based on *how* the device was unlocked.

The division of labor:

| Question | Answered by |
| --- | --- |
| Is a human physically there? | Touch |
| Is it someone allowed to use this device? | PIN (or biometric, as convenience) |
| Is it the account holder? | The key pair itself — possession of the device |

The server never asks "which human?" It asks "does the holder of the registered private key approve this action?" — and the signature answers that. Identity, in the biometric sense, was never part of the protocol. This is why touch + PIN equals Bio: the extra sensor changes the unlock experience, not the security model.
