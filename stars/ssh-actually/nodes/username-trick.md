---
id: username-trick
title: The git@ Username
type: concept
requires: [git-ssh-authentication]
related: [host-aliases, multiple-github-accounts]
entry_points: [why is the username always git, git@github.com meaning, how does github know who I am]
summary: >
  Why the username is always git — the service identifies you by which key you
  present, not by the username you type.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
The git@ Username

<!-- depth:2 -->
<!-- provenance: extracted -->
The username in `git@github.com` and `git@gitlab.com` is always `git` — for everyone. The service doesn't care about your account username; it cares about **which SSH key you presented**. Your **actual** identity comes from the key, not the username.

<!-- depth:3 -->
<!-- provenance: extracted -->
The pieces:

- The service doesn't care about your **GitHub username**
- It cares about **which SSH key** you presented
- The SSH key is linked to your account
- The `git` user is just a convention

You can watch the key-to-identity lookup happen:

```bash
ssh -T git@github.com
# → Hi username! You've successfully authenticated...
```

You typed `git`; the greeting names *you* — because the key you presented is registered to your account.

One consequence trips up almost everyone eventually: since the username and hostname are identical for every account on the service, **the key is the only thing that distinguishes two accounts**. That's the trap behind multi-account setups — and why the fix (host aliases) works by changing which key gets presented, not the username.
