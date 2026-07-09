---
id: hardware-key-capabilities
title: Hardware Key Capabilities
type: concept
requires: [hardware-security-keys]
related: [webauthn, passkeys, hardware-keys-ssh, slots]
entry_points: [what can a yubikey do, which yubikey should I buy, yubikey security key vs 5 series, does the blue yubikey do ssh]
summary: >
  The conceptual capability map — OTP, FIDO/U2F, WebAuthn, passkeys, SSH signing,
  PIV, OpenPGP — and how real models combine them.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Hardware Key Capabilities

<!-- depth:2 -->
<!-- provenance: extracted -->
Modern hardware keys can support multiple independent roles. What follows is a **conceptual capability map**, not marketing tiers — different models enable different *combinations* of the same underlying capabilities.

<!-- depth:3 -->
<!-- provenance: extracted -->
The capability map:

| Capability | What it does | Why it matters |
| --- | --- | --- |
| 2FA (OTP) | Generates rotating codes | Better than SMS |
| FIDO/U2F | Cryptographic challenge-response | Phishing resistant |
| WebAuthn | Browser-based cryptographic login | Passwordless |
| Passkey storage | Stores discoverable credentials | Cross-device login |
| SSH signing | Signs SSH challenges | No private keys on disk |
| Touch requirement | Enforces presence | Stops automation |
| PIN enforcement | Rate-limited access | Stronger than passphrases |
| Biometric unlock (optional) | Local identity check | Convenience layer |

Using YubiKey as an example (not endorsement) — a simplified conceptual lineup:

| Feature / Capability | Security Key (blue) | 5 Series | Bio |
| --- | --- | --- | --- |
| Touch (presence check) | ✔ | ✔ | ✔ |
| PIN (device-enforced) | ✔ | ✔ | ✔ |
| OTP (TOTP / HOTP) | ✖ | ✔ | ✖ |
| WebAuthn (FIDO2 / U2F) | ✔ | ✔ | ✔ |
| Passkeys (resident creds) | ✔ (limited) | ✔ | ✔ |
| SSH (ed25519-sk) | ✔ | ✔ | ✔ |
| PIV / Smart Card (X.509) | ✖ | ✔ | ✖ |
| OpenPGP | ✖ | ✔ | ✖ |
| Biometrics (fingerprint) | ✖ | ✖ | ✔ |

Important clarifications:

- The **Security Key (blue)** *does* support SSH (`ed25519-sk`) and passkeys, but **only via FIDO2/WebAuthn**. It does not support OTP, PIV, or OpenPGP.
- **Passkeys = resident FIDO2 credentials**, which are **slot-limited** on all keys (lower limits on Security Key models).
- **SSH works on all three**, because it uses FIDO2 as a signing oracle (not PIV).
- **Biometrics** are purely a local unlock convenience; cryptographic guarantees are identical with touch+PIN.

All of these still rely on the same foundation: hardware isolation, non-exportable secrets, signature-based authentication.
