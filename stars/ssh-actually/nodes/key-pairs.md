---
id: key-pairs
title: Key Pairs
type: concept
requires: [what-ssh-is]
related: [signatures, passphrases, trust-boundaries, authorized-keys]
entry_points: [what is a key pair, public vs private key, what is a private key, can I share my public key]
summary: >
  Two mathematically linked keys — private (secret, yours) and public (shared,
  safe) — and the storage rules that follow; the server never learns your secret.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Key Pairs

<!-- depth:2 -->
<!-- provenance: extracted -->
A **key pair** is two mathematically linked keys:

- a **private key** (secret, kept by you)
- a **public key** (shared with others)

The public key can verify that a message was created by the private key **without revealing the private key**.

<!-- depth:3 -->
<!-- provenance: extracted -->
The two halves, precisely:

**Private key** — a secret file that proves your identity. If stolen, it can be used to impersonate you.

**Public key** — a non-secret file used by a server to verify signatures.

The rules that follow:

- The private key **must never be shared**
- The public key **is safe to share**
- The server stores **only public keys**

That last rule is the one people doubt, and it holds: sharing a public key gives away nothing that lets anyone impersonate you.

<!-- depth:4 -->
<!-- provenance: synthesized -->
Everything around key pairs is answering one of two questions:

**How do you prove possession?** By itself a key pair proves nothing — the missing piece is the **signature**: the server sends a challenge, your private key signs it, the public key verifies. That flow is what makes the pair usable.

**Where does the private key live?** This is the real security question, because the answer sets who you must trust:

- On disk (traditional) — protected at rest by a **passphrase**, at the mercy of your OS and anything running on it.
- Inside a hardware key — usable, never extractable.

The public key's home is simpler: the server keeps it in `authorized_keys`, its list of keys it will accept. Losing a public key costs nothing; it can always be re-shared.

<!-- depth:5 -->
<!-- provenance: extracted -->
The core idea, and why it beats passwords structurally:

- The **server never knows your secret**
- Only **you** can prove you have it
- Proof is done via **signatures**

A password is a shared secret known by you *and* the service — it can be stolen from servers, reused, phished, and must be remembered. SSH keys:

- cannot be guessed
- cannot be reused elsewhere
- cannot be brute-forced remotely

Everything modern in authentication — FIDO2, WebAuthn, passkeys, hardware keys — converges on the same idea SSH has run on since the 1990s:

> **Never give the server a secret it can lose.**

The final mental model: SSH proves **possession**, not identity. Servers never store secrets. Hardware keys don't change the crypto — they change **where secrets live**.
