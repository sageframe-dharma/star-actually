---
id: mfa
title: Multi-Factor Authentication
type: concept
requires: [passwords]
related: [one-time-codes, mfa-strength-ladder, hardware-security-keys]
entry_points: [what is mfa, what counts as a factor, something you know have are, what is 2fa]
summary: >
  Proof comes in categories — know, have, are — and MFA means requiring more
  than one. Includes the credential/factor vocabulary used everywhere else.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Multi-Factor Authentication

<!-- depth:2 -->
<!-- provenance: extracted -->
**MFA (Multi-Factor Authentication)** is requiring proof from more than one **factor** — more than one *category* of evidence: something you **know** (password, PIN), something you **have** (phone, hardware key), something you **are** (biometric).

<!-- depth:3 -->
<!-- provenance: extracted -->
The vocabulary, since it's used everywhere:

- **Authentication** — proving that you are who you claim to be.
- **Credential** — any secret or cryptographic material used to authenticate (password, key, token, etc.).
- **Factor** — a *category* of proof: something you know, have, or are.

The category distinction is what makes MFA meaningful: a factor is a *kind* of proof, not another copy of the same kind. And not all combinations are equal — "MFA" covers everything from an email link (weakest) to a hardware security key (strongest), which is why the strength *ladder* matters as much as the factor count.
