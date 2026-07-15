---
id: pins-vs-passphrases
title: PINs vs Passphrases
type: concept
requires: [hardware-pin, passphrases]
related: [hardware-keys-ssh, trust-boundaries]
entry_points: [pin vs passphrase, is a short pin really safe, why is a 6 digit pin ok but a short passphrase not]
summary: >
  A passphrase protects a file (offline brute-forceable, unlimited attempts);
  a PIN protects a physical device (rate-limited, hardware-enforced).
---

<!-- depth:1 -->
<!-- provenance: extracted -->
PINs vs Passphrases

<!-- depth:2 -->
<!-- provenance: extracted -->
A passphrase protects a *file*. A PIN protects a *physical device* with attempt limits. With hardware keys, the PIN replaces the passphrase **safely**.

<!-- depth:3 -->
<!-- provenance: extracted -->
The comparison, spelled out:

**Passphrase:**

- protects a file
- brute-forceable offline

If someone steals a private key file, they can brute-force the passphrase **offline with unlimited attempts**—on their hardware, at their pace, with no lockout.

**PIN:**

- enforced by hardware
- rate-limited
- requires the physical device
- requires presence

An attacker with your PIN but not your device has nothing. An attacker with your device but not your PIN gets a handful of guesses before the key locks or wipes. There is no offline attack, because the thing being guessed against is tamper-resistant hardware, not a file that can be copied and hammered forever.

This is why a 6-digit PIN on a hardware key is stronger in practice than a short passphrase on a disk key: the strength was never in the code's length—it's in *what enforces the guessing rules*.
