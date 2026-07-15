---
id: hardware-key-setup-nonresident
title: Setting Up a Non-Resident Key
type: procedure
requires: [non-resident-keys]
related: [hardware-key-setup-resident, blob, git-ssh-authentication, key-naming]
entry_points: [yubikey with github, set up non-resident ssh key, hardware key for git, ed25519-sk github setup]
summary: >
  Quick start for non-resident keys—generate ed25519-sk, register with
  GitHub/GitLab, config block, test—and the blob-backup obligation.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Setting Up a Non-Resident Key

<!-- depth:2 -->
<!-- provenance: synthesized -->
The setup for hardware-backed SSH where keys are **derived on demand** rather than stored: generate an `ed25519-sk` key, register the public key with the service, and take on the one obligation that comes with it—the blob file must be preserved.

<!-- depth:3 -->
<!-- provenance: extracted -->
Prerequisites:

- A FIDO2-capable hardware key (YubiKey 5, YubiKey Bio, similar)
- OpenSSH 8.2+ installed (`ssh -V` to check)
- libfido2 installed (`apt install libfido2-1` on Debian/Ubuntu)

**1. Plug in hardware key**

**2. Generate non-resident SSH key**

```bash
ssh-keygen -t ed25519-sk -f ~/.ssh/id_github_yk -C "github-hw"
```

- Touch key when prompted
- Set PIN if prompted
- Creates blob file (required for authentication)

**3. Add to GitHub/GitLab**

Copy public key:

```bash
cat ~/.ssh/id_github_yk.pub
```

- Go to GitHub Settings → SSH and GPG keys
- Click "New SSH key"
- Paste the contents
- Save

**4. Create SSH config**

Edit `~/.ssh/config`:

```
Host github.com
    IdentityFile ~/.ssh/id_github_yk
    IdentitiesOnly yes
```

**5. Test it**

```bash
ssh -T git@github.com
```

- Touch key when prompted
- Should see: "Hi username! You've successfully authenticated..."

What just happened:

- Hardware key can derive unlimited private keys from blobs
- Blob file must be preserved (back it up!)
- Each service gets its own blob
- No slot limit

**Critical:** back up your blob files! They're not secrets, but losing them means generating new keys.
