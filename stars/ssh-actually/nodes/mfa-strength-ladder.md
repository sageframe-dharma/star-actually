---
id: mfa-strength-ladder
title: The MFA Strength Ladder
type: concept
requires: [mfa]
related: [one-time-codes, passkeys, hardware-security-keys, phishing-resistance]
entry_points: [which mfa is strongest, ranking of 2fa methods, is sms worse than an authenticator app, email link login security]
summary: >
  The worst-to-best ranking — email link → SMS → TOTP → enterprise tokens →
  biometrics+WebAuthn → passkeys → hardware keys — and why each tier sits
  where it does.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
The MFA Strength Ladder

<!-- depth:2 -->
<!-- provenance: extracted -->
A rough ordering of MFA methods from worst to best, ranked by one question: **how hard is it for a motivated, competent attacker — who already knows your username — to successfully impersonate you?**

<!-- depth:3 -->
<!-- provenance: extracted -->
The ladder, worst to best:

| # | Method | Why it sits here |
| --- | --- | --- |
| 1 | **Email link** | Email accounts are often already compromised, logged in on many devices, and themselves protected by weak or reused credentials. If an attacker controls your email, this "factor" collapses entirely. |
| 2 | **SMS code** | Vulnerable to SIM-swapping, carrier attacks, interception, and social engineering. The phone *number* — not the physical device — is the security anchor: a fundamental design flaw. |
| 3 | **Authenticator app (TOTP)** | Codes are short-lived and not transmitted over the network, but still **phishable and replayable** — an attacker who tricks you into entering the code can immediately use it. |
| 4 | **Enterprise time-based tokens** | Short validity windows, device management, logging, rapid revocation — but usually still code-based, so real-time phishing remains possible. |
| 5 | **Biometrics (local) + WebAuthn** | The biometric doesn't authenticate you to the service — it unlocks a local authenticator, which proves identity cryptographically. The biometric never leaves the device. |
| 6 | **Passkeys** | Passwords eliminated entirely; authentication by cryptographic signature, not shared secrets. Phishing-resistant, device-bound — but the platform controls creation, syncing, and recovery. |
| 7 | **Hardware security keys** | Secrets never leave the hardware, authentication requires physical touch, attempts are rate-limited, and phishing fails because the device verifies the service before signing anything. |

<!-- depth:4 -->
<!-- provenance: extracted -->
The ladder is really two ladders with a cliff between them. Rungs 1–4 are all **code-based**: something is generated, you type it, and whatever you can type, you can be tricked into typing. Rungs 5–7 are **signature-based**: nothing is typed, so phishing has nothing to capture.

As you move down the list:

- Shared secrets disappear
- Phishing stops working
- Remote-only attacks fail
- Physical presence becomes required

> The strongest systems remove **what can be copied**, **what can be guessed**, and **what can be tricked** — and replace them with cryptographic proof tied to real hardware.
