---
id: key-generation
title: Generating Keys
type: procedure
requires: [key-pairs]
related: [key-naming, passphrases, first-key-setup, hardware-key-setup-nonresident]
entry_points: [how to generate an ssh key, ssh-keygen command, change passphrase on existing key, which key algorithm]
summary: >
  ssh-keygen and its choices—algorithm, filename, comment, passphrase—plus changing the passphrase or comment on a key you already have.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Generating Keys

<!-- depth:2 -->
<!-- provenance: synthesized -->
One command—`ssh-keygen`—creates every kind of key pair. The choices that matter are the **algorithm** (`-t ed25519` for disk keys, `-t ed25519-sk` for hardware-backed keys), the **filename** (`-f`), the **comment** (`-C`), and whether to set a **passphrase**.

<!-- depth:3 -->
<!-- provenance: extracted -->
### create a standard ssh key pair

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_example -C "example@laptop"
```

What this does:

- Creates private key: `id_example`
- Creates public key: `id_example.pub`

Options:

- `-t ed25519`—Key algorithm (modern, recommended)
- `-f ~/.ssh/id_example`—Name of key files
- `-C "comment"`—Metadata label (optional but helpful)

When prompted for passphrase:

- Enter strong passphrase (20+ characters) for security
- OR press Enter for no passphrase (convenient but risky)

For hardware-backed keys the algorithm changes to `-t ed25519-sk` (with `-O resident` for resident keys)—the setup procedures for those have their own nodes.

### change passphrase on existing key

```bash
ssh-keygen -p -f ~/.ssh/id_example
```

What this does:

- Re-encrypts the private key with new passphrase
- Does NOT change the key itself
- Public key remains valid

### change comment on existing key

```bash
ssh-keygen -c -f ~/.ssh/id_example
```

What this does:

- Updates the metadata label only
- Does NOT affect authentication
