---
id: new-machine-setup
title: New Machine Setup
type: procedure
requires: [key-pairs, ssh-config-basics]
related: [stub, blob, file-permissions, first-key-setup]
entry_points: [ssh on a new laptop, restore ssh access new machine, migrate ssh keys, fresh install ssh setup]
summary: >
  Fresh laptop, restore access — three workflows side by side: regenerate
  stubs (resident), restore blobs (non-resident), restore keys + permissions (disk).
---

<!-- depth:1 -->
<!-- provenance: extracted -->
New Machine Setup

<!-- depth:2 -->
<!-- provenance: synthesized -->
Fresh laptop, and you need your SSH access back. The workflow depends on where your authentication state lives: **resident** keys regenerate their stubs from the hardware, **non-resident** keys restore their blobs from backup, **disk-based** keys restore the keys themselves — and then the permissions must be fixed.

<!-- depth:3 -->
<!-- provenance: extracted -->
### if using resident hardware keys

```bash
# 1. Plug in hardware key

# 2. Regenerate stubs
ssh-keygen -K

# 3. Move stubs to ~/.ssh
mv ssh_*.pub ~/.ssh/
mv ssh_* ~/.ssh/

# 4. Rename to meaningful names (optional)
mv ~/.ssh/ssh_rk_... ~/.ssh/production_yk

# 5. Test
ssh production-server
```

### if using non-resident hardware keys

```bash
# 1. Restore blob files from backup
# (blobs should be in your encrypted backup)

cp backup/github_yk ~/.ssh/
cp backup/gitlab_yk ~/.ssh/

# 2. Restore or recreate SSH config
cp backup/config ~/.ssh/

# 3. Test
ssh -T git@github.com
```

### if using disk-based keys

```bash
# 1. Restore private keys from encrypted backup
cp backup/id_* ~/.ssh/

# 2. Set correct permissions
chmod 600 ~/.ssh/id_*
chmod 644 ~/.ssh/id_*.pub

# 3. Restore SSH config
cp backup/config ~/.ssh/
chmod 600 ~/.ssh/config

# 4. Test
ssh server
```
