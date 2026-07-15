---
id: hardware-pin
title: Hardware PINs
type: definition
requires: [hardware-security-keys]
related: [pins-vs-passphrases, touch-requirement, passphrases]
entry_points: [what is a fido pin, yubikey pin, what happens if I forget my pin, how many pin attempts]
summary: >
  A short code enforced by the device itself—attempt-limited, lockout-on-failure,
  impossible to brute-force offline.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Hardware PINs

<!-- depth:2 -->
<!-- provenance: extracted -->
A short code enforced **by the device itself**, not the computer.

<!-- depth:3 -->
<!-- provenance: extracted -->
Key properties of a hardware PIN:

- Limited attempts
- Enforced inside hardware
- Locks or wipes after failures
- Cannot be brute-forced offline

This is why a short PIN is acceptable where a short passphrase is not: a passphrase protects a *file*, which a thief can attack offline with unlimited attempts. A PIN protects a *physical device* with attempt limits—the enforcement lives in the same tamper-resistant hardware as the secrets.

Setting or changing the PIN (YubiKey example):

```bash
ykman fido access change-pin
```

The forgot-PIN reality: if you forget the PIN, you cannot use the hardware key after the limited attempts run out—the key locks or wipes after too many failures (usually 8 attempts). There is no reset-by-email here; the lockout is the security feature working as designed. Store the PIN securely (a password manager is fine) and have a backup hardware key.
