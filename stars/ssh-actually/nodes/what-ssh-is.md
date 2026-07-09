---
id: what-ssh-is
title: What SSH Is
type: concept
requires: []
related: [key-pairs, git-ssh-authentication, server-hardening]
entry_points: [what is ssh, how does ssh work, what does ssh actually do, why is ssh secure]
summary: >
  SSH is cryptographic proof of identity over a hostile network — the protocol
  assumes someone is listening and someone is impersonating.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
What SSH Is

<!-- depth:2 -->
<!-- provenance: extracted -->
**SSH (Secure Shell)** is a protocol that lets you securely connect to another computer over a network and run commands on it.

<!-- depth:3 -->
<!-- provenance: extracted -->
SSH assumes:

- the network is hostile
- someone may be listening
- someone may try to impersonate you

SSH solves this by requiring **cryptographic proof** before access is granted. SSH normally does **not** use passwords — it uses key-pair cryptography: the server never learns your secret, and only you can prove you have it.

<!-- depth:4 -->
<!-- provenance: synthesized -->
SSH shows up in two roles, and confusing them is where most misunderstanding starts:

- **Server login** (the traditional model) — you get a shell, you run commands, the connection stays open. This is what "hardening a server" is about: passwords off, keys only.
- **Authentication only** (the Git hosting model) — GitHub, GitLab. You never get a shell; you only prove identity, and each git operation is a separate proof. **Same cryptography, different purpose.**

SSH also predates everything it now resembles. It has used key-pair cryptography since the 1990s, while the web kept using passwords; the web slowly caught up to where SSH already was — with different names (FIDO2, WebAuthn, passkeys) and different contexts.

The mental model to keep: SSH proves **possession**, not identity — and servers never store secrets.
