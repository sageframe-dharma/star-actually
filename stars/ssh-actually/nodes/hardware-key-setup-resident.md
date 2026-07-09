---
id: hardware-key-setup-resident
title: Setting Up a Resident Key
type: procedure
requires: [resident-keys]
related: [hardware-key-setup-nonresident, recovery-planning, managing-resident-credentials, hardware-pin]
entry_points: [set up resident ssh key, yubikey resident key howto, ssh-keygen -O resident, backup yubikey setup]
summary: >
  Quick start for resident keys — generate with -O resident, PIN, deploy,
  test, and the critical step everyone skips: the duplicate on a second device.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Setting Up a Resident Key

<!-- depth:2 -->
<!-- provenance: synthesized -->
The setup for hardware-backed SSH where the key lives **inside** the device: generate with `-O resident`, deploy like any key, and — the step that is not optional — create a duplicate resident key on a second hardware key so losing the first one isn't lockout.

<!-- depth:3 -->
<!-- provenance: extracted -->
Prerequisites:

- A FIDO2-capable hardware key (YubiKey 5, YubiKey Bio, similar)
- OpenSSH 8.2+ installed (`ssh -V` to check)
- libfido2 installed (`apt install libfido2-1` on Debian/Ubuntu)

**1. Plug in hardware key**

**2. Generate resident SSH key**

```bash
ssh-keygen -t ed25519-sk -O resident -f ~/.ssh/id_myserver_yk -C "myserver-hw"
```

- Touch key when prompted
- Set a PIN if prompted (highly recommended)
- Creates stub file and stores key on hardware

**3. Deploy to server**

```bash
ssh-copy-id -i ~/.ssh/id_myserver_yk.pub username@server
```

**4. Test it**

```bash
ssh username@server
```

- Enter PIN if required
- Touch key when it flashes
- Should log in

**5. Create SSH config**

Edit `~/.ssh/config`:

```
Host myserver
    HostName server-address
    User username
    IdentityFile ~/.ssh/id_myserver_yk
    IdentitiesOnly yes
```

**Recovery setup (CRITICAL):** on a SECOND hardware key, create a duplicate resident key:

```bash
# With second key plugged in
ssh-keygen -t ed25519-sk -O resident -f ~/.ssh/id_myserver_backup_yk -C "myserver-hw-backup"
ssh-copy-id -i ~/.ssh/id_myserver_backup_yk.pub username@server
```

Store the backup key safely. If you lose your primary key, you can still access the server.

What just happened:

- Private key was generated INSIDE the hardware key
- It never touched your computer
- Stub file on disk is just a pointer
- You can regenerate the stub on any machine: `ssh-keygen -K`
