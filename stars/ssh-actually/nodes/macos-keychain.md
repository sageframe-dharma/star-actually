---
id: macos-keychain
title: macOS Keychain Integration
type: concept
requires: [ssh-agents]
related: [passphrases, trust-boundaries, hardware-security-keys]
entry_points: [why doesn't my mac ask for my passphrase, ssh touch id, UseKeychain, is my mac key hardware backed]
summary: >
  Why SSH feels invisible on macOS—Keychain, Touch ID, and an auto-loaded
  agent. Feels like hardware security; is actually disk security plus OS trust.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
macOS Keychain Integration

<!-- depth:2 -->
<!-- provenance: extracted -->
macOS stores passphrases in Keychain, unlocks them via Touch ID / Face ID, and auto-loads keys into `ssh-agent`. The result: it **feels like hardware security**, but it is actually **disk-based security + OS trust**. The private key still lives on disk.

<!-- depth:3 -->
<!-- provenance: extracted -->
The behavior is driven by two macOS-specific options in `~/.ssh/config`:

```
UseKeychain yes          # Store passphrase in Keychain
AddKeysToAgent yes       # Auto-add to ssh-agent
```

With these set, you type the passphrase once; after that, Keychain supplies it and the agent caches the unlocked key. This is the same session-caching mechanism SSH supports everywhere—`ssh-agent` and OS keychains—which avoids repeated typing, expires when the session ends, and requires a background process. macOS just wires it all together so smoothly that the passphrase seems to vanish.

<!-- depth:4 -->
<!-- provenance: synthesized -->
The trap in the convenience is a **trust-boundary misread**. Touch ID before an SSH connection looks exactly like touching a hardware key—but the two prove different things. On a Mac, the fingerprint unlocks the *Keychain entry that holds your passphrase*; the private key is an ordinary encrypted file on disk, and anything with sufficient access to your unlocked OS can reach it. With a hardware key, the secret physically cannot leave the device.

So the boundary you are trusting is the operating system, not a physical object:

- **Disk key + Keychain**—you trust macOS, everything running on it, and your disk encryption. Convenient, reasonable for most people, but a compromised machine compromises the key.
- **Hardware key**—you trust a physical object that will sign but never export. A compromised machine can *use* the key while it's plugged in and touched, but can never copy it.

If you want the security that the Touch ID prompt *feels* like it's giving you, that's what hardware-backed keys are for.
