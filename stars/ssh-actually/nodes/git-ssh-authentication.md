---
id: git-ssh-authentication
title: Git over SSH
type: concept
requires: [what-ssh-is, key-pairs]
related: [username-trick, phishing-resistance, hardware-key-setup-nonresident]
entry_points: [how does github ssh work, why does git use ssh, git clone ssh vs https, does github give me a shell]
summary: >
  The authentication-only model—no shell, no session; each git operation is
  a fresh cryptographic proof of identity. Same cryptography, different purpose.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Git over SSH

<!-- depth:2 -->
<!-- provenance: extracted -->
With GitHub, GitLab, and similar services, SSH is used as **authentication, not login**. You never get a shell—you only prove identity, the service decides what you can access based on that identity, and each git operation is a separate authentication.

<!-- depth:3 -->
<!-- provenance: extracted -->
Two models, one protocol.

**The traditional model (server login):** you get a shell, you run commands, you browse the filesystem, the connection stays open.

**The git hosting model (authentication only):** no shell, ever. You prove identity; the service does the rest.

When you run:

```bash
git clone git@github.com:user/repo.git
```

behind the scenes:

1. Git opens an SSH connection to `github.com`
2. You prove identity using your SSH key
3. GitHub checks: "Does this key have access to this repo?"
4. If yes → sends repository data
5. Connection closes

No shell. No commands. Just **cryptographic proof of identity**.

<!-- depth:4 -->
<!-- provenance: extracted -->
Why this model is powerful:

- No passwords ever transmitted
- No credentials to steal from GitHub's servers
- Phishing-resistant—you're not typing anything

**Same cryptography—different purpose.** This is why learning SSH well matters even if you never manage servers: every time you push code, you're using SSH authentication.

The model has a distinctive fingerprint: because the service identifies you by *which key you presented*, the username in the URL is always just `git`—your actual identity comes from the key, not the username. And because authentication is a signature, not a typed secret, this is the same phishing-resistant shape that FIDO2 brought to the web—modern setups go one step further and back the git key with a hardware device.
