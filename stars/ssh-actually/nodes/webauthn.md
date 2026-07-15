---
id: webauthn
title: WebAuthn
type: concept
requires: [fido2]
related: [passkeys, hardware-security-keys, phishing-resistance]
entry_points: [what is webauthn, webauthn vs fido2, how do browsers do passwordless login]
summary: >
  The browser API that lets websites use FIDO2—the bridge between web pages
  and authenticators, phishing-resistant by design.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
WebAuthn

<!-- depth:2 -->
<!-- provenance: extracted -->
**WebAuthn** is the browser API that allows websites to use FIDO2. It runs in browsers, talks to authenticators (phones, laptops, hardware keys), and is **phishing-resistant by design**.

<!-- depth:3 -->
<!-- provenance: extracted -->
WebAuthn is the bridge layer: a web page can't talk to a hardware key or a secure enclave directly, so the browser and operating system do it on the page's behalf, performing **cryptographic authentication** with a local authenticator and handing back only a signature.

This is how Google, GitHub, Apple, and Microsoft implement modern passwordless login.

One subtlety worth keeping: when you unlock a login with a fingerprint or face, the biometric does **not** authenticate you to the remote service. It unlocks the local authenticator, which then uses WebAuthn to prove identity cryptographically. The biometric never leaves the device.
