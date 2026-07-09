---
id: ssh-agents
title: SSH Agents
type: concept
requires: [key-pairs, passphrases]
related: [agent-forwarding, macos-keychain, ssh-debugging]
entry_points: [what is ssh-agent, why do I keep typing my passphrase, ssh-add, cache ssh passphrase]
summary: >
  The background process that caches unlocked keys for a session so you stop
  retyping passphrases.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
SSH Agents

<!-- depth:2 -->
<!-- provenance: synthesized -->
An **SSH agent** is a background process that holds your unlocked private keys for a **session**, so you type your passphrase once instead of on every connection. `ssh-agent` is the standard one; OS keychains play the same role.

<!-- depth:3 -->
<!-- provenance: extracted -->
**Session** — a period of time during which authentication remains valid.

Agent caching:

- avoids repeated typing
- expires when the session ends
- requires a background process

The working vocabulary is three `ssh-add` commands:

```bash
ssh-add ~/.ssh/id_example   # unlock a key and cache it for the session
ssh-add -l                  # list keys currently loaded in the agent
ssh-add -D                  # remove all keys from the agent
```

<!-- depth:4 -->
<!-- provenance: synthesized -->
The agent is a small idea with long shadows:

- **It's why macOS feels magical.** macOS stores passphrases in Keychain, unlocks them via Touch ID, and auto-loads keys into `ssh-agent`. The invisibility is the agent working, not a different security model — the key still lives on disk.
- **It's what agent forwarding forwards.** Forwarding lets a remote server request signatures from *your local* agent. Convenient across hops — and the reason a compromised intermediate can sign as you for the length of your session. The agent's power is exactly what gets lent.
- **It's the first thing to check when the wrong key wins.** SSH will offer agent-loaded keys during authentication; `ssh-add -l` tells you what's actually loaded, which is a standard early step when debugging why SSH presented a key you didn't expect.
