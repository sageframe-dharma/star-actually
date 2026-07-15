---
id: first-key-setup
title: First-Time Key Setup
type: procedure
requires: [key-pairs]
related: [key-generation, deploy-public-key, ssh-config-basics, permission-denied]
entry_points: [set up ssh keys for the first time, ssh without a password, quick start ssh key, how do I stop typing my server password]
summary: >
  The end-to-end quick start—generate, deploy with ssh-copy-id, test, add a
  config block; passwordless server access from zero.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
First-Time Key Setup

<!-- depth:2 -->
<!-- provenance: extracted -->
**Goal:** set up SSH key authentication to access a server without typing passwords. You generate a key pair, send the public key to the server, and from then on the server trusts your key instead of asking for passwords.

<!-- depth:3 -->
<!-- provenance: extracted -->
Prerequisites:

- You have an account on a remote server
- You can currently log in with a password
- You're on Linux, macOS, or Windows with OpenSSH

**1. Generate an SSH key pair**

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_myserver -C "$(whoami)@$(hostname)"
```

- Press Enter when prompted for passphrase (or type a strong one)
- Creates `~/.ssh/id_myserver` (private) and `~/.ssh/id_myserver.pub` (public)

**2. Copy public key to server**

```bash
ssh-copy-id -i ~/.ssh/id_myserver.pub username@server-address
```

- Enter your password when prompted
- This is the LAST time you'll need the password

**3. Test it**

```bash
ssh username@server-address
```

- Should log in without password
- May prompt for passphrase if you set one

**4. (Optional) Create SSH config for convenience**

Edit or create `~/.ssh/config`:

```
Host myserver
    HostName server-address
    User username
    IdentityFile ~/.ssh/id_myserver
```

Now you can just type:

```bash
ssh myserver
```

What you just did:

- Generated a cryptographic key pair
- Sent the public key to the server
- Server now trusts your key instead of asking for passwords
- Your private key stays on your laptop
