---
id: ssh-debugging
title: Debugging SSH
type: troubleshooting
requires: [ssh-config-basics]
related: [permission-denied, ssh-agents, known-hosts, identities-only]
entry_points: [debug ssh connection, ssh -vvv how to read, why is ssh using the wrong key, check ssh server logs]
summary: >
  The diagnostic toolkit as a workflow—verbose output, config resolution,
  agent inspection, and server-side logs, each answering a different question.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Debugging SSH

<!-- depth:2 -->
<!-- provenance: synthesized -->
SSH failures are rarely mysterious once you ask the right tool. Four tools cover almost every case: **verbose output** (`ssh -v`) shows what the client tried and where it failed, **config resolution** (`ssh -G`) shows what configuration actually applied, **agent inspection** (`ssh-add -l`) shows which keys are loaded, and **server-side logs** show why the server said no.

<!-- depth:3 -->
<!-- provenance: extracted -->
### Watch the connection

```bash
ssh -v user@server      # Basic verbosity
ssh -vv user@server     # More detail
ssh -vvv user@server    # Maximum detail
```

Look for: which keys are being tried, the authentication method used, and where failures occur.

### Check what config resolved

```bash
ssh -G hostname
```

Shows all resolved options, which config rules matched, and the final values used. Use case: debugging unexpected SSH behavior—this is how you find out SSH is using a different key than you think.

### Inspect the agent

```bash
ssh-add -l
```

Shows all keys currently loaded in the agent. Add a key with `ssh-add ~/.ssh/id_example` (cache passphrase for session); clear everything with `ssh-add -D`.

### Read the server's side (requires existing access)

```bash
sudo tail -20 /var/log/auth.log
# or on some systems:
sudo journalctl -u sshd -n 20
```

The server will log exactly why it rejected the key.

<!-- depth:4 -->
<!-- provenance: synthesized -->
The workflow is a funnel—each tool narrows where the problem lives:

| Question | Tool | Points toward |
| --- | --- | --- |
| Is SSH even using the config block I wrote? | `ssh -G hostname` | Config matching, wrong `Host` pattern |
| Which key did it actually offer? | `ssh -vvv` | `IdentityFile` mistakes; add `IdentitiesOnly yes` if SSH is cycling through every key ("too many authentication failures") |
| Is the key loaded and unlocked? | `ssh-add -l` | Agent problems—key never added, agent not running |
| Client says fine, server says no? | server auth logs | Permissions and ownership on the server side—the silent-refusal territory of "Permission denied" |

Two supporting checks for hardware-backed setups: `ssh -V` (hardware keys require OpenSSH 8.2+) and `lsusb | grep -i yubikey` to verify the device is detected at all.

The habit worth building: **read the verbose output before changing anything.** Most "my key doesn't work" problems announce their cause in `ssh -vvv`—a key not tried, a file ignored for bad permissions, a config block that never matched.
