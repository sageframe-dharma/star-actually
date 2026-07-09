---
created: 2026-07-03
status: draft — practitioner review pending
type: node-map
project: star-actually
ho: ho-C1
---

# \*, Actually — Node Map (ho-C1)

The editorial architecture for decomposing the two source documents into the knowledge graph. **60 nodes** across 10 clusters. Three nodes already exist (`agent-forwarding`, `blob`, `permission-denied`); they appear below with their frozen edges (additions marked).

Conventions used in this map:

- `depth_levels` — planned depth ceiling (the parser computes the real value from the authored body; this is the editorial target).
- `scope` — the ONE mental model the node carries.
- `provenance` — expected mix: `mostly-extracted` | `mixed` | `mostly-synthesized`.
- `source` — "Guide §N" = *SSH, Keys, and Hardware Security — A Human Guide*; "Ref" = *SSH Commands and Configuration Reference*.

Requires-graph note: `what-ssh-is` is the declared root (`requires: []`). One deliberate second zero-requires node exists — `passwords` — because the modern-auth cluster is conceptually prior to SSH, not downstream of it, and many readers will arrive asking about passwords/MFA directly. It is reachable laterally and feeds five requires-edges forward. Flagged for practitioner review; if a single-root invariant is wanted, give `passwords` `requires: [what-ssh-is]`.

---

## Cluster 1 — Foundations (6 nodes)

The spine. Everything else hangs off these.

```yaml
id: what-ssh-is
title: "What SSH Is"
type: concept
depth_levels: 4
scope: "SSH is cryptographic proof of identity over a hostile network — the protocol assumes someone is listening and someone is impersonating."
requires: []
related: [key-pairs, git-ssh-authentication, server-hardening]
entry_points: ["what is ssh", "how does ssh work", "what does ssh actually do", "why is ssh secure"]
source: "Guide §1"
provenance: "mostly-extracted"
```

```yaml
id: key-pairs
title: "Key Pairs"
type: concept
depth_levels: 5
scope: "Two mathematically linked keys — private (secret, yours) and public (shared, safe) — and the storage rules that follow; the server never learns your secret."
requires: [what-ssh-is]
related: [signatures, passphrases, trust-boundaries, authorized-keys]
entry_points: ["what is a key pair", "public vs private key", "what is a private key", "can I share my public key"]
source: "Guide §2, §5"
provenance: "mostly-extracted"
```

```yaml
id: signatures
title: "Signatures"
type: concept
depth_levels: 5
scope: "The challenge–sign–verify flow — proof of possession that never reveals the secret. The missing piece that makes key pairs usable."
requires: [key-pairs]
related: [fido2, hardware-security-keys, known-hosts]
entry_points: ["what is a cryptographic signature", "how does ssh prove identity", "challenge response", "how does the server verify me"]
source: "Guide §3, §13 Diagram 1"
provenance: "mostly-extracted"
```

```yaml
id: trust-boundaries
title: "Trust Boundaries"
type: concept
depth_levels: 4
scope: "Where the secret lives determines who you must trust — disk trusts your OS, hardware trusts a physical object, forwarding lends trust away. The unifying \"where secrets live\" model."
requires: [key-pairs]
related: [passphrases, hardware-security-keys, agent-forwarding, state]
entry_points: ["where does my ssh key live", "who can steal my key", "where do secrets live", "what am I trusting"]
source: "Guide §5, §7, §11 intro, §13 Diagram 2"
provenance: "mostly-synthesized"
```

```yaml
id: server-hardening
title: "Server Hardening"
type: concept
depth_levels: 4
scope: "Minimum viable server security — passwords off, root off, key-only access, sudo for escalation — and why keys structurally beat passwords."
requires: [what-ssh-is, key-pairs]
related: [passwords, authorized-keys, permission-denied]
entry_points: ["how do I harden ssh", "disable password login", "should I allow root login", "ssh key only access"]
source: "Guide §4"
provenance: "mostly-extracted"
```

```yaml
id: authorized-keys
title: "authorized_keys"
type: definition
depth_levels: 4
scope: "The server-side trust anchor — the file of public keys a server will accept, and the discipline of auditing it."
requires: [key-pairs]
related: [deploy-public-key, server-hardening, key-rotation, permission-denied]
entry_points: ["what is authorized_keys", "where does the server store my key", "how does the server know my key", "audit ssh access"]
source: "Guide §5; Ref Part A, Security Best Practices"
provenance: "mixed"
```

---

## Cluster 2 — Keys on Disk: Local Machine Practice (6 nodes)

Disk-based key life: protection at rest, caching, hygiene.

```yaml
id: passphrases
title: "Passphrases"
type: concept
depth_levels: 4
scope: "A secret that encrypts a private key at rest — and its honest limits: offline brute-force with unlimited attempts. Includes the forgot-passphrase recovery reality."
requires: [key-pairs]
related: [ssh-agents, pins-vs-passphrases, macos-keychain, trust-boundaries]
entry_points: ["should I set a passphrase", "what does a passphrase protect", "passphrase vs password", "forgot my ssh passphrase"]
source: "Guide §6; Ref What Can Go Wrong (disk)"
provenance: "mostly-extracted"
```

```yaml
id: ssh-agents
title: "SSH Agents"
type: concept
depth_levels: 4
scope: "The background process that caches unlocked keys for a session so you stop retyping passphrases — including the session concept and ssh-add basics."
requires: [key-pairs, passphrases]
related: [agent-forwarding, macos-keychain, ssh-debugging]
entry_points: ["what is ssh-agent", "why do I keep typing my passphrase", "ssh-add", "cache ssh passphrase"]
source: "Guide §6 (session caching); Ref Part D (ssh-add -l/-D)"
provenance: "mostly-extracted"
```

```yaml
id: macos-keychain
title: "macOS Keychain Integration"
type: concept
depth_levels: 4
scope: "Why SSH feels invisible on macOS — Keychain + Touch ID + auto-loaded agent. Feels like hardware security; is disk security plus OS trust."
requires: [ssh-agents]
related: [passphrases, trust-boundaries, hardware-security-keys]
entry_points: ["why doesn't my mac ask for my passphrase", "ssh touch id", "UseKeychain", "is my mac key hardware backed"]
source: "Guide §7; Ref Part C (UseKeychain, AddKeysToAgent)"
provenance: "mostly-extracted"
```

```yaml
id: file-permissions
title: "SSH File Permissions"
type: concept
depth_levels: 4
scope: "Why SSH is opinionated about permissions (a readable key is an untrustworthy key), the correct numbers on both sides, and the home-directory gotcha."
requires: [key-pairs]
related: [permission-denied, ssh-debugging, deploy-public-key]
entry_points: ["ssh file permissions", "chmod 600 ssh key", "why does ssh care about permissions", "authorized_keys permissions"]
source: "Ref Part F"
provenance: "mostly-extracted"
```

```yaml
id: key-naming
title: "Naming Keys"
type: concept
depth_levels: 3
scope: "Names are for humans — clarity, intent, scope. Conventions (id_purpose, purpose_yk) and why the comment field earns its keep."
requires: [key-pairs]
related: [key-generation, blob, multiple-github-accounts]
entry_points: ["how should I name ssh keys", "ssh key naming convention", "what is the ssh key comment", "id_rsa vs custom names"]
source: "Guide §14; Ref Naming Conventions"
provenance: "mostly-extracted"
```

```yaml
id: key-rotation
title: "Key Rotation"
type: procedure
depth_levels: 4
scope: "Keys never expire on their own — rotation as manual discipline: when (event vs schedule), the test-before-revoke order, and how hardware changes the calculus."
requires: [key-pairs, authorized-keys]
related: [key-naming, recovery-planning, hardware-keys-ssh]
entry_points: ["how often should I rotate ssh keys", "do ssh keys expire", "replace an ssh key", "left a job with keys on machines"]
source: "Guide §14a"
provenance: "mostly-extracted"
```

---

## Cluster 3 — SSH Beyond Servers: The Git Hosting Model (4 nodes)

Authentication without a shell; identity from the key.

```yaml
id: git-ssh-authentication
title: "Git over SSH"
type: concept
depth_levels: 4
scope: "The authentication-only model — no shell, no session; each git operation is a fresh cryptographic proof of identity. Same cryptography, different purpose."
requires: [what-ssh-is, key-pairs]
related: [username-trick, phishing-resistance, hardware-key-setup-nonresident]
entry_points: ["how does github ssh work", "why does git use ssh", "git clone ssh vs https", "does github give me a shell"]
source: "Guide §8"
provenance: "mostly-extracted"
```

```yaml
id: username-trick
title: "The git@ Username"
type: concept
depth_levels: 3
scope: "Why the username is always `git` — the service identifies you by which key you present, not by the username you type."
requires: [git-ssh-authentication]
related: [host-aliases, multiple-github-accounts]
entry_points: ["why is the username always git", "git@github.com meaning", "how does github know who I am"]
source: "Guide §8 (The Username Trick)"
provenance: "mostly-extracted"
```

```yaml
id: host-aliases
title: "Host Aliases"
type: concept
depth_levels: 4
scope: "Host is a label you control, HostName is where the connection goes — SSH config as named connection instructions, not a hostname routing table."
requires: [ssh-config-basics]
related: [username-trick, multiple-github-accounts, config-wildcards]
entry_points: ["ssh host alias", "host vs hostname ssh config", "can host be a made-up name", "nickname for ssh server"]
source: "Guide §8b (The Solution, The Mental Model); Ref Example 1a"
provenance: "mostly-extracted"
```

```yaml
id: multiple-github-accounts
title: "Multiple Accounts, One Service"
type: scenario
depth_levels: 4
scope: "The two-accounts trap — same host, same username, different keys — and the alias-based way out, including clone-URL changes and updating existing remotes."
requires: [git-ssh-authentication, host-aliases]
related: [username-trick, identities-only, key-naming]
entry_points: ["two github accounts one machine", "personal and work github ssh", "wrong github account authenticating", "git remote set-url alias"]
source: "Guide §8b; Ref Example 1a"
provenance: "mostly-extracted"
```

---

## Cluster 4 — Multi-Hop SSH (3 nodes)

Reaching machines behind machines.

```yaml
id: agent-forwarding          # EXISTS — edges frozen, none added
title: "Agent Forwarding"
type: concept
depth_levels: 5
scope: "Let a remote server request signatures from your local agent — the key stays home but its power travels; anyone with root on the intermediate can sign as you."
requires: [ssh-agents, key-pairs, ssh-config-basics]
related: [proxy-jump, trust-boundaries, hardware-keys-ssh]
entry_points: ["ssh forwarding", "forward agent", "multi-hop ssh", "ssh from server to server"]
source: "Guide §8a"
provenance: "mixed (authored)"
```

```yaml
id: proxy-jump
title: "ProxyJump"
type: concept
depth_levels: 5
scope: "Route through an intermediate as a dumb TCP relay — it never sees your key, never talks to your agent, cannot act as you. The better answer to multi-hop."
requires: [ssh-config-basics]
related: [agent-forwarding, jump-host-config, trust-boundaries]
entry_points: ["what is proxyjump", "ssh -J", "ssh through a jump host safely", "proxyjump vs agent forwarding"]
source: "Guide §8a (Option 3)"
provenance: "mostly-extracted"
```

```yaml
id: jump-host-config
title: "Configuring Jump Hosts"
type: procedure
depth_levels: 3
scope: "The bastion pattern in ~/.ssh/config — ProxyJump blocks, wildcarded environment groups, transparent `ssh prod-db1` through a bastion."
requires: [proxy-jump, ssh-config-basics]
related: [config-wildcards, agent-forwarding]
entry_points: ["configure a bastion in ssh config", "proxyjump config example", "ssh through bastion automatically"]
source: "Ref Part C (jump host), Example 2"
provenance: "mostly-extracted"
```

---

## Cluster 5 — The Modern Authentication Landscape (9 nodes)

The map: how passwords, OTP, FIDO2, WebAuthn, passkeys, and MFA fit together — and where SSH sits.

```yaml
id: modern-auth-landscape
title: "The Modern Auth Landscape"
type: concept
depth_levels: 4
scope: "The map — passwords → OTP → FIDO2/WebAuthn → passkeys → hardware keys all converge on one idea: never give the server a secret it can lose. SSH did it first."
requires: [key-pairs, passwords]
related: [fido2, passkeys, mfa-strength-ladder, hardware-security-keys]
entry_points: ["how do passkeys mfa and hardware keys fit together", "map of modern authentication", "how does ssh relate to webauthn", "why do these all feel related"]
source: "Guide §9 (Big Picture, How These Fit, Mental Model), §13 Diagram 5"
provenance: "mostly-extracted"
```

```yaml
id: passwords
title: "Passwords"
type: concept
depth_levels: 3
scope: "The shared-secret baseline — the server knows your secret, so it can lose it; everything else in modern auth exists because of this flaw."
requires: []
related: [one-time-codes, phishing-resistance, server-hardening, passphrases]
entry_points: ["why are passwords weak", "what is a shared secret", "why replace passwords"]
source: "Guide §9 (Passwords)"
provenance: "mostly-extracted"
```

```yaml
id: one-time-codes
title: "One-Time Codes"
type: concept
depth_levels: 4
scope: "OTP/TOTP/SMS as layered defense on top of shared secrets — rotating codes help, but they remain phishable and replayable, and the secret still lives on a server."
requires: [passwords]
related: [mfa, mfa-strength-ladder, phishing-resistance]
entry_points: ["what is totp", "are authenticator apps secure", "why is sms 2fa bad", "can otp codes be phished"]
source: "Guide §9 (OTP), §10 items 1–4"
provenance: "mostly-extracted"
```

```yaml
id: mfa
title: "Multi-Factor Authentication"
type: concept
depth_levels: 3
scope: "Proof comes in categories — know, have, are — and MFA means requiring more than one; includes the credential/factor vocabulary."
requires: [passwords]
related: [one-time-codes, mfa-strength-ladder, hardware-security-keys]
entry_points: ["what is mfa", "what counts as a factor", "something you know have are", "what is 2fa"]
source: "Guide §9 (Definitions), §10 intro"
provenance: "mostly-extracted"
```

```yaml
id: mfa-strength-ladder
title: "The MFA Strength Ladder"
type: concept
depth_levels: 4
scope: "The worst-to-best ranking — email link → SMS → TOTP app → enterprise tokens → biometrics+WebAuthn → passkeys → hardware keys — and *why* each tier sits where it does."
requires: [mfa]
related: [one-time-codes, passkeys, hardware-security-keys, phishing-resistance]
entry_points: ["which mfa is strongest", "ranking of 2fa methods", "is sms worse than an authenticator app", "email link login security"]
source: "Guide §10"
provenance: "mostly-extracted"
```

```yaml
id: fido2
title: "FIDO2"
type: concept
depth_levels: 4
scope: "The cryptographic shift for the web — the server verifies a signature, not a secret; key-pair cryptography replacing shared secrets everywhere."
requires: [key-pairs, passwords]
related: [webauthn, passkeys, hardware-security-keys, phishing-resistance]
entry_points: ["what is fido2", "fido2 vs password", "how does fido2 work", "fido2 and ssh"]
source: "Guide §9 (FIDO2)"
provenance: "mostly-extracted"
```

```yaml
id: webauthn
title: "WebAuthn"
type: concept
depth_levels: 3
scope: "The browser API that lets websites use FIDO2 — the bridge between web pages and authenticators, phishing-resistant by design."
requires: [fido2]
related: [passkeys, hardware-security-keys, phishing-resistance]
entry_points: ["what is webauthn", "webauthn vs fido2", "how do browsers do passwordless login"]
source: "Guide §9 (WebAuthn), §10 item 5"
provenance: "mostly-extracted"
```

```yaml
id: passkeys
title: "Passkeys"
type: concept
depth_levels: 4
scope: "User-friendly FIDO2 — discoverable credentials, synced by platforms, phishing-resistant; the tradeoff is that the platform controls creation, sync, and recovery."
requires: [fido2, webauthn]
related: [hardware-security-keys, trust-boundaries, mfa-strength-ladder]
entry_points: ["what is a passkey", "passkey vs password", "passkey vs hardware key", "who controls my passkeys"]
source: "Guide §9 (Passkeys), §10 item 6"
provenance: "mostly-extracted"
```

```yaml
id: phishing-resistance
title: "Phishing Resistance"
type: concept
depth_levels: 4
scope: "Why cryptographic auth defeats phishing — there is nothing to type, nothing to replay; the authenticator verifies the service before signing. The lateral thread tying SSH, FIDO2, and hardware keys together."
requires: [passwords]
related: [fido2, webauthn, git-ssh-authentication, hardware-security-keys]
entry_points: ["what does phishing resistant mean", "why can't ssh keys be phished", "can 2fa codes be phished", "phishing proof login"]
source: "Synthesized across Guide §8–§11 (recurring theme)"
provenance: "mostly-synthesized"
```

---

## Cluster 6 — Hardware Security Keys (6 nodes)

What the physical object actually does.

```yaml
id: hardware-security-keys
title: "Hardware Security Keys"
type: concept
depth_levels: 5
scope: "A physically enforced boundary where secrets can be used but never stolen — generate inside, store non-exportably, sign without exposing. A cryptographic co-processor, not a USB password."
requires: [key-pairs, fido2]
related: [trust-boundaries, hardware-keys-ssh, passkeys, touch-requirement]
entry_points: ["what is a yubikey", "what does a hardware security key do", "how does a security key work", "can a yubikey be copied"]
source: "Guide §11 (definition, capabilities 1–4, takeaway)"
provenance: "mostly-extracted"
```

```yaml
id: hardware-key-capabilities
title: "Hardware Key Capabilities"
type: concept
depth_levels: 3
scope: "The conceptual capability map — OTP, FIDO/U2F, WebAuthn, passkey storage, SSH signing, PIV, OpenPGP — and how models (Security Key, 5 Series, Bio) combine them."
requires: [hardware-security-keys]
related: [webauthn, passkeys, hardware-keys-ssh, slots]
entry_points: ["what can a yubikey do", "which yubikey should I buy", "yubikey security key vs 5 series", "does the blue yubikey do ssh"]
source: "Guide §11 (capability map, YubiKey lineup)"
provenance: "mostly-extracted"
```

```yaml
id: touch-requirement
title: "The Touch Requirement"
type: definition
depth_levels: 3
scope: "A physical press before any cryptographic operation — proves a human is present and the action is intentional; makes automation and remote abuse impossible."
requires: [hardware-security-keys]
related: [presence-vs-identity, hardware-pin]
entry_points: ["why do I have to touch my yubikey", "what does the touch prove", "hardware key flashing"]
source: "Guide §11 (Touch)"
provenance: "mostly-extracted"
```

```yaml
id: hardware-pin
title: "Hardware PINs"
type: definition
depth_levels: 3
scope: "A short code enforced by the device itself — attempt-limited, lockout-on-failure, impossible to brute-force offline; includes the forgot-PIN lockout reality."
requires: [hardware-security-keys]
related: [pins-vs-passphrases, touch-requirement, passphrases]
entry_points: ["what is a fido pin", "yubikey pin", "what happens if I forget my pin", "how many pin attempts"]
source: "Guide §11 (PIN); Ref (ykman change-pin, forgot-PIN scenario)"
provenance: "mostly-extracted"
```

```yaml
id: presence-vs-identity
title: "Presence vs Identity"
type: concept
depth_levels: 4
scope: "The subtle point — touch proves a human is present now; biometrics prove which human. For cryptographic auth, presence is sufficient and identity is optional. Why touch+PIN equals Bio."
requires: [touch-requirement]
related: [hardware-pin, mfa, passkeys]
entry_points: ["why is touch enough", "do I need the biometric yubikey", "touch vs fingerprint security key", "does my fingerprint go to the server"]
source: "Guide §11 (Presence vs identity, Touch vs biometrics), §9 (Touch vs Biometrics)"
provenance: "mostly-extracted"
```

```yaml
id: pins-vs-passphrases
title: "PINs vs Passphrases"
type: concept
depth_levels: 3
scope: "A passphrase protects a file (offline brute-forceable, unlimited attempts); a PIN protects a physical device (rate-limited, hardware-enforced). Why PIN replaces passphrase safely."
requires: [hardware-pin, passphrases]
related: [hardware-keys-ssh, trust-boundaries]
entry_points: ["pin vs passphrase", "is a short pin really safe", "why is a 6 digit pin ok but a short passphrase not"]
source: "Guide §12c, §11 (Why PIN beats passphrase)"
provenance: "mostly-extracted"
```

---

## Cluster 7 — Hardware Keys for SSH (8 nodes)

Where authentication memory lives: state, slots, resident, non-resident.

```yaml
id: hardware-keys-ssh
title: "Hardware Keys for SSH"
type: concept
depth_levels: 5
scope: "Hardware-backed SSH doesn't change the cryptography — it changes where authentication state is allowed to exist, splitting it between disk and device (ed25519-sk, FIDO2 as signing oracle)."
requires: [hardware-security-keys, key-pairs]
related: [state, slots, agent-forwarding, choosing-an-approach]
entry_points: ["ssh with a yubikey", "what is ed25519-sk", "why does hardware ssh feel weird", "hardware backed ssh keys"]
source: "Guide §12 (intro + section), §13 Diagram 2; Ref Part B intro"
provenance: "mostly-extracted"
```

```yaml
id: state
title: "State"
type: definition
depth_levels: 3
scope: "Anything that must be remembered for authentication to keep working — lose it and auth fails, copy it and auth can be stolen; you cannot eliminate state, only choose where it lives."
requires: [hardware-keys-ssh]
related: [slots, trust-boundaries, resident-vs-non-resident]
entry_points: ["what is authentication state", "what must be remembered for ssh to work", "where does auth state live"]
source: "Guide §12 (Definition: State)"
provenance: "mostly-extracted"
```

```yaml
id: slots
title: "Slots"
type: definition
depth_levels: 3
scope: "Small, protected storage locations inside the hardware key — intentionally scarce, because limiting stored secrets limits blast radius and forces safer designs."
requires: [hardware-keys-ssh, state]
related: [resident-keys, managing-resident-credentials]
entry_points: ["what is a slot on a yubikey", "how many keys fit on a hardware key", "why are slots limited"]
source: "Guide §12 (Definition: Slot, Why slots are limited)"
provenance: "mostly-extracted"
```

```yaml
id: non-resident-keys
title: "Non-Resident SSH Keys"
type: concept
depth_levels: 5
scope: "The key that is stored nowhere — derived on demand inside the hardware from master secret + blob; unlimited keys, but you guarantee continuity by preserving the blob."
requires: [hardware-keys-ssh, state]
related: [blob, resident-keys, hardware-key-setup-nonresident]
entry_points: ["what is a non-resident key", "where is my sk key stored", "the key isn't on the hardware?", "unlimited hardware ssh keys"]
source: "Guide §12a, §13 Diagram 3"
provenance: "mostly-extracted"
```

```yaml
id: resident-keys
title: "Resident SSH Keys"
type: concept
depth_levels: 5
scope: "The key the hardware remembers — generated and stored entirely inside the device, discoverable, survives disk loss; the cost is a scarce slot."
requires: [hardware-keys-ssh, state]
related: [stub, slots, non-resident-keys, hardware-key-setup-resident]
entry_points: ["what is a resident key", "ssh key that survives a wiped laptop", "discoverable credential ssh", "-O resident meaning"]
source: "Guide §12b, §13 Diagram 3"
provenance: "mostly-extracted"
```

```yaml
id: blob                      # EXISTS — edges frozen; ADD related: recovery-planning
title: "Blob"
type: definition
depth_levels: 4
scope: "The non-secret file a non-resident key needs to reconstruct its private key — not a secret, but lose it and the key is gone forever."
requires: [non-resident-keys]
related: [stub, hardware-security-keys, key-pairs, recovery-planning]
entry_points: ["blob file", "sk key file", "what is the file on disk for a hardware key"]
source: "Guide §12a"
provenance: "mixed (authored)"
```

```yaml
id: stub
title: "Stub"
type: definition
depth_levels: 3
scope: "The regenerable pointer — a small non-secret file that tells SSH which resident key to use; delete it freely, regenerate anywhere with `ssh-keygen -K`."
requires: [resident-keys]
related: [blob, new-machine-setup, hardware-keys-ssh]
entry_points: ["what is a stub file", "ssh-keygen -K", "regenerate ssh key files", "deleted my sk key file"]
source: "Guide §12b, §13 Diagram 4; Ref Part B (regenerate stubs)"
provenance: "mostly-extracted"
```

```yaml
id: resident-vs-non-resident
title: "Resident vs Non-Resident"
type: concept
depth_levels: 4
scope: "The decision surface — permanence vs scalability: resident trades slots for survivability (servers), non-resident trades blob-custody for unlimited keys (GitHub). State survivability, not strength."
requires: [resident-keys, non-resident-keys]
related: [choosing-an-approach, state, slots, recovery-planning]
entry_points: ["resident or non-resident", "which hardware key type should I use", "resident vs non-resident comparison", "blob vs stub"]
source: "Guide §12d, §13 Diagrams 3–4; Ref QS2 decision table"
provenance: "mostly-extracted"
```

---

## Cluster 8 — SSH Configuration (5 nodes)

The config file as a system, plus server identity.

```yaml
id: ssh-config-basics
title: "SSH Config Basics"
type: concept
depth_levels: 4
scope: "~/.ssh/config as named connection instructions — Host, HostName, User, Port, IdentityFile — turning flag soup into `ssh myserver`."
requires: [what-ssh-is]
related: [identities-only, config-wildcards, host-aliases, first-key-setup]
entry_points: ["what is ssh config", "how to set up ~/.ssh/config", "stop typing ssh flags", "ssh nickname for server"]
source: "Ref Part C (basic structure, examples), Before/After section; Guide glossary (Host, HostName, User, Port)"
provenance: "mostly-extracted"
```

```yaml
id: identities-only
title: "IdentitiesOnly"
type: definition
depth_levels: 3
scope: "Force SSH to present only the keys you named — prevents SSH trying every key you own and the \"too many authentication failures\" it causes."
requires: [ssh-config-basics]
related: [multiple-github-accounts, ssh-debugging, config-wildcards]
entry_points: ["what does identitiesonly do", "too many authentication failures", "ssh tries wrong key"]
source: "Ref Part C (Why IdentitiesOnly matters), SSH config security"
provenance: "mostly-extracted"
```

```yaml
id: config-wildcards
title: "Config Patterns and Wildcards"
type: concept
depth_levels: 3
scope: "Matching semantics — wildcards, per-network blocks, `Host *` global defaults, most-specific-match wins; plus the useful-options toolbox (keep-alives, forwards)."
requires: [ssh-config-basics]
related: [jump-host-config, identities-only, host-aliases]
entry_points: ["ssh config wildcards", "different keys for different networks", "Host * defaults", "which config block wins"]
source: "Ref Part C (networks example, useful options, ssh -G)"
provenance: "mostly-extracted"
```

```yaml
id: known-hosts
title: "Known Hosts"
type: concept
depth_levels: 4
scope: "The other direction of trust — you verify the server. Fingerprints, the first-connection prompt (and why typing yes blindly defeats it), MITM protection."
requires: [what-ssh-is]
related: [signatures, host-key-changed, ssh-debugging]
entry_points: ["what is known_hosts", "authenticity of host can't be established", "should I type yes", "ssh fingerprint check"]
source: "Ref Parts D–E"
provenance: "mostly-extracted"
```

```yaml
id: host-key-changed
title: "Host Key Changed"
type: troubleshooting
depth_levels: 3
scope: "The scary warning decoded — legitimate causes (rebuilt server, reused IP) vs the attack it exists to catch, and the ssh-keygen -R fix."
requires: [known-hosts]
related: [ssh-debugging, permission-denied]
entry_points: ["remote host identification has changed", "host key verification failed", "ssh-keygen -R", "server rebuilt ssh warning"]
source: "Ref Part D (remove host), Part E (remove changed host key)"
provenance: "mostly-extracted"
```

---

## Cluster 9 — Procedures: Getting Set Up (8 nodes)

The action layer. Each assumes the concepts, delivers the steps.

```yaml
id: choosing-an-approach
title: "Choosing an Approach"
type: concept
depth_levels: 4
scope: "The decision guide — disk key with passphrase vs resident vs non-resident, by situation (getting started, max security, many servers, git hosting); recommendations table."
requires: [key-pairs]
related: [resident-vs-non-resident, hardware-keys-ssh, passphrases, first-key-setup]
entry_points: ["which ssh key setup should I use", "do I need a hardware key", "disk key or hardware key", "best ssh setup for github"]
source: "Ref \"Which Approach Should You Use?\" (decision trees, recommendations)"
provenance: "mostly-extracted"
```

```yaml
id: key-generation
title: "Generating Keys"
type: procedure
depth_levels: 3
scope: "ssh-keygen and its choices — algorithm (-t ed25519 / ed25519-sk), filename, comment, passphrase decision; plus changing passphrase and comment on existing keys."
requires: [key-pairs]
related: [key-naming, passphrases, first-key-setup, hardware-key-setup-nonresident]
entry_points: ["how to generate an ssh key", "ssh-keygen command", "change passphrase on existing key", "which key algorithm"]
source: "Ref Part A"
provenance: "mostly-extracted"
```

```yaml
id: first-key-setup
title: "First-Time Key Setup"
type: procedure
depth_levels: 3
scope: "The end-to-end quick start — generate, deploy with ssh-copy-id, test, add a config block; passwordless server access from zero."
requires: [key-pairs]
related: [key-generation, deploy-public-key, ssh-config-basics, permission-denied]
entry_points: ["set up ssh keys for the first time", "ssh without a password", "quick start ssh key", "how do I stop typing my server password"]
source: "Ref Quick Start 1"
provenance: "mostly-extracted"
```

```yaml
id: deploy-public-key
title: "Deploying a Public Key"
type: procedure
depth_levels: 3
scope: "Getting your public key onto the server — ssh-copy-id, the manual authorized_keys method, and the permissions that must accompany it."
requires: [key-pairs, authorized-keys]
related: [first-key-setup, file-permissions, permission-denied]
entry_points: ["ssh-copy-id", "add my key to a server", "manually add key to authorized_keys", "deploy public key"]
source: "Ref Part A (deploy automatic/manual), Part B (deploy hardware key)"
provenance: "mostly-extracted"
```

```yaml
id: hardware-key-setup-resident
title: "Setting Up a Resident Key"
type: procedure
depth_levels: 3
scope: "Quick start for resident keys — generate with -O resident, PIN, deploy, test, and the critical step everyone skips: the duplicate key on a second device."
requires: [resident-keys]
related: [hardware-key-setup-nonresident, recovery-planning, managing-resident-credentials, hardware-pin]
entry_points: ["set up resident ssh key", "yubikey resident key howto", "ssh-keygen -O resident", "backup yubikey setup"]
source: "Ref Quick Start 2a"
provenance: "mostly-extracted"
```

```yaml
id: hardware-key-setup-nonresident
title: "Setting Up a Non-Resident Key"
type: procedure
depth_levels: 3
scope: "Quick start for non-resident keys — generate ed25519-sk, register with GitHub/GitLab, config block, test; and the blob-backup obligation that comes with it."
requires: [non-resident-keys]
related: [hardware-key-setup-resident, blob, git-ssh-authentication, key-naming]
entry_points: ["yubikey with github", "set up non-resident ssh key", "hardware key for git", "ed25519-sk github setup"]
source: "Ref Quick Start 2b"
provenance: "mostly-extracted"
```

```yaml
id: managing-resident-credentials
title: "Managing Resident Credentials"
type: procedure
depth_levels: 3
scope: "Housekeeping on the device — ykman list/delete, checking slot usage, freeing slots, and the slot-limit recovery path."
requires: [resident-keys, slots]
related: [hardware-key-setup-resident, stub, lost-hardware-key]
entry_points: ["list keys on yubikey", "ykman fido credentials", "delete resident key", "yubikey slots full"]
source: "Ref Part B (ykman list/delete), What Can Go Wrong (slot limit)"
provenance: "mostly-extracted"
```

```yaml
id: new-machine-setup
title: "New Machine Setup"
type: procedure
depth_levels: 3
scope: "Fresh laptop, restore access — the three workflows side by side: regenerate stubs (resident), restore blobs (non-resident), restore keys + fix permissions (disk)."
requires: [key-pairs, ssh-config-basics]
related: [stub, blob, file-permissions, first-key-setup]
entry_points: ["ssh on a new laptop", "restore ssh access new machine", "migrate ssh keys", "fresh install ssh setup"]
source: "Ref Workflow: Setting Up New Machine"
provenance: "mostly-extracted"
```

---

## Cluster 10 — Troubleshooting and Recovery (5 nodes)

When it breaks, and planning for when it breaks.

```yaml
id: permission-denied         # EXISTS — edges frozen; ADD related: file-permissions, ssh-debugging
title: "Permission Denied"
type: troubleshooting
depth_levels: 4
scope: "The most common SSH failure and its diagnosis path — SSH silently refuses keys with wrong file permissions; no error, just \"Permission denied.\""
requires: [key-pairs]
related: [ssh-config-basics, known-hosts, ssh-agents, file-permissions, ssh-debugging]
entry_points: ["permission denied publickey", "key doesn't work", "ssh rejects my key", "file permissions ssh"]
source: "Ref Part F"
provenance: "mixed (authored)"
```

```yaml
id: ssh-debugging
title: "Debugging SSH"
type: troubleshooting
depth_levels: 4
scope: "The diagnostic toolkit as a workflow — ssh -v/-vv/-vvv (which keys tried, where it fails), ssh -G (what config resolved), agent inspection, server-side auth logs."
requires: [ssh-config-basics]
related: [permission-denied, ssh-agents, known-hosts, identities-only]
entry_points: ["debug ssh connection", "ssh -vvv how to read", "why is ssh using the wrong key", "check ssh server logs"]
source: "Ref Part D, Part F (diagnosing), Part C (ssh -G)"
provenance: "mixed"
```

```yaml
id: lost-hardware-key
title: "Lost Hardware Key"
type: scenario
depth_levels: 4
scope: "The recovery playbook when the device is gone — why non-resident loss is an inconvenience and resident-without-backup is total lockout; what the thief can and cannot do."
requires: [resident-vs-non-resident]
related: [recovery-planning, blob, stub, managing-resident-credentials]
entry_points: ["lost my yubikey", "hardware key stolen what now", "yubikey broke can I recover", "locked out resident key"]
source: "Ref What Can Go Wrong (hardware-backed scenarios)"
provenance: "mostly-extracted"
```

```yaml
id: stolen-laptop
title: "Stolen Laptop"
type: scenario
depth_levels: 3
scope: "Disk-key compromise response — assume the key is being brute-forced, remove the public key from every authorized_keys now; what the passphrase did and didn't buy you."
requires: [key-pairs, passphrases]
related: [key-rotation, authorized-keys, recovery-planning]
entry_points: ["laptop stolen ssh keys", "revoke a compromised ssh key", "someone has my private key file"]
source: "Ref What Can Go Wrong (disk-based scenarios)"
provenance: "mostly-extracted"
```

```yaml
id: recovery-planning
title: "Recovery Planning"
type: concept
depth_levels: 4
scope: "Always have a path back — the two-hardware-keys rule, blob backups, out-of-band access, and testing recovery before you need it. Security you can't recover from is fragility."
requires: [key-pairs]
related: [lost-hardware-key, stolen-laptop, key-rotation, resident-vs-non-resident]
entry_points: ["ssh backup strategy", "do I need two yubikeys", "how do I not lock myself out", "test recovery process"]
source: "Ref Critical Safety Rules, Security Best Practices, Summary Checklist"
provenance: "mixed"
```

---

## Summary Table

| # | id | type | depths | cluster |
|---|----|------|--------|---------|
| 1 | what-ssh-is | concept | 4 | 1 Foundations |
| 2 | key-pairs | concept | 5 | 1 Foundations |
| 3 | signatures | concept | 5 | 1 Foundations |
| 4 | trust-boundaries | concept | 4 | 1 Foundations |
| 5 | server-hardening | concept | 4 | 1 Foundations |
| 6 | authorized-keys | definition | 4 | 1 Foundations |
| 7 | passphrases | concept | 4 | 2 Local Practice |
| 8 | ssh-agents | concept | 4 | 2 Local Practice |
| 9 | macos-keychain | concept | 4 | 2 Local Practice |
| 10 | file-permissions | concept | 4 | 2 Local Practice |
| 11 | key-naming | concept | 3 | 2 Local Practice |
| 12 | key-rotation | procedure | 4 | 2 Local Practice |
| 13 | git-ssh-authentication | concept | 4 | 3 Git Model |
| 14 | username-trick | concept | 3 | 3 Git Model |
| 15 | host-aliases | concept | 4 | 3 Git Model |
| 16 | multiple-github-accounts | scenario | 4 | 3 Git Model |
| 17 | agent-forwarding † | concept | 5 | 4 Multi-Hop |
| 18 | proxy-jump | concept | 5 | 4 Multi-Hop |
| 19 | jump-host-config | procedure | 3 | 4 Multi-Hop |
| 20 | modern-auth-landscape | concept | 4 | 5 Modern Auth |
| 21 | passwords | concept | 3 | 5 Modern Auth |
| 22 | one-time-codes | concept | 4 | 5 Modern Auth |
| 23 | mfa | concept | 3 | 5 Modern Auth |
| 24 | mfa-strength-ladder | concept | 4 | 5 Modern Auth |
| 25 | fido2 | concept | 4 | 5 Modern Auth |
| 26 | webauthn | concept | 3 | 5 Modern Auth |
| 27 | passkeys | concept | 4 | 5 Modern Auth |
| 28 | phishing-resistance | concept | 4 | 5 Modern Auth |
| 29 | hardware-security-keys | concept | 5 | 6 Hardware Keys |
| 30 | hardware-key-capabilities | concept | 3 | 6 Hardware Keys |
| 31 | touch-requirement | definition | 3 | 6 Hardware Keys |
| 32 | hardware-pin | definition | 3 | 6 Hardware Keys |
| 33 | presence-vs-identity | concept | 4 | 6 Hardware Keys |
| 34 | pins-vs-passphrases | concept | 3 | 6 Hardware Keys |
| 35 | hardware-keys-ssh | concept | 5 | 7 Hardware SSH |
| 36 | state | definition | 3 | 7 Hardware SSH |
| 37 | slots | definition | 3 | 7 Hardware SSH |
| 38 | non-resident-keys | concept | 5 | 7 Hardware SSH |
| 39 | resident-keys | concept | 5 | 7 Hardware SSH |
| 40 | blob † | definition | 4 | 7 Hardware SSH |
| 41 | stub | definition | 3 | 7 Hardware SSH |
| 42 | resident-vs-non-resident | concept | 4 | 7 Hardware SSH |
| 43 | ssh-config-basics | concept | 4 | 8 Configuration |
| 44 | identities-only | definition | 3 | 8 Configuration |
| 45 | config-wildcards | concept | 3 | 8 Configuration |
| 46 | known-hosts | concept | 4 | 8 Configuration |
| 47 | host-key-changed | troubleshooting | 3 | 8 Configuration |
| 48 | choosing-an-approach | concept | 4 | 9 Procedures |
| 49 | key-generation | procedure | 3 | 9 Procedures |
| 50 | first-key-setup | procedure | 3 | 9 Procedures |
| 51 | deploy-public-key | procedure | 3 | 9 Procedures |
| 52 | hardware-key-setup-resident | procedure | 3 | 9 Procedures |
| 53 | hardware-key-setup-nonresident | procedure | 3 | 9 Procedures |
| 54 | managing-resident-credentials | procedure | 3 | 9 Procedures |
| 55 | new-machine-setup | procedure | 3 | 9 Procedures |
| 56 | permission-denied † | troubleshooting | 4 | 10 Troubleshooting |
| 57 | ssh-debugging | troubleshooting | 4 | 10 Troubleshooting |
| 58 | lost-hardware-key | scenario | 4 | 10 Troubleshooting |
| 59 | stolen-laptop | scenario | 3 | 10 Troubleshooting |
| 60 | recovery-planning | concept | 4 | 10 Troubleshooting |

† = node already exists; edges frozen (additions noted inline).

**Type census:** concept 33 · definition 9 · procedure 10 · scenario 3 · troubleshooting 5.

---

## Edge-Count Sanity Check

- **Nodes:** 60
- **requires edges:** 80 (mean 1.3/node; max 3 — no node exceeds the 0–4 cap)
- **related edges:** 201 directed references (mean 3.4/node; max 5 — cap respected)
- **Closure:** every id appearing in any `requires` or `related` list resolves to a node in this map — verified mechanically (script-parsed all YAML blocks; zero dangling references).
- **Acyclicity:** the `requires` graph is a DAG — verified mechanically (topological sort succeeds; zero cycles).
- **Zero-requires nodes:** `what-ssh-is` (declared root) and `passwords` (deliberate, flagged above for practitioner review).
- **Forward reachability:** every node except the two zero-requires nodes is in the forward neighborhood chain of the root or of `passwords`; `passwords` itself is reachable laterally (from `server-hardening`, `passphrases` via related).
- **Existing-node integrity:** all ten ids referenced by the three pre-existing nodes (`ssh-agents`, `key-pairs`, `ssh-config-basics`, `proxy-jump`, `trust-boundaries`, `hardware-keys-ssh`, `non-resident-keys`, `stub`, `hardware-security-keys`, `known-hosts`) exist in the map.

---

## Guide Content Deliberately NOT Given a Node

| Content | Disposition | Why |
|---|---|---|
| Private Key / Public Key (glossary defs, Guide §5) | Folded into `key-pairs` depths 2–3 | Halves of one mental model; standalone nodes would force three hops through one idea. **Hardest call in the map — see review flags.** |
| Session (glossary) | Folded into `ssh-agents` | Only meaningful in the caching context; trivial alone |
| Comment (glossary) | Folded into `key-naming` + `key-generation` | Metadata detail, not a model |
| Biometrics (glossary) | Folded into `presence-vs-identity` | The node IS the interesting claim about biometrics |
| Cryptographic Secret, Secure Storage (Guide §11 defs) | Folded into `hardware-security-keys` depths 3–5 | Sub-parts of the "physically enforced boundary" model |
| Authentication, Credential, Factor (Guide §9 defs) | Folded into `mfa` depth 2–3 | Vocabulary for one model, not three models |
| Email link, SMS OTP, enterprise tokens (Guide §10 items 1,2,4) | Folded into `mfa-strength-ladder` (+ `one-time-codes`) | Rungs of one ladder; splitting destroys the comparative model |
| Host, HostName, User, Port, IdentityFile (glossary) | Folded into `ssh-config-basics` depth 2–3 | Fields of one structure; `identities-only` and `host-aliases` are the two that carry independent weight |
| Guide §13 (Visual Diagrams) | Distributed as depth-layer material | Diagrams are renderings of models owned by other nodes (D1→signatures, D2→trust-boundaries, D3/D4→resident/non-resident/blob/stub, D5→modern-auth-landscape) |
| YubiKey lineup table (Guide §11) | Inside `hardware-key-capabilities` depth 3 | Example instance of the capability map, not its own model |
| Ref "Before/After: SSH Config Impact" | Inside `ssh-config-basics` depth 3 | Motivation for the same model |
| Ref "Security Best Practices" | Distributed (`key-naming`, `identities-only`, `recovery-planning`, `authorized-keys`, `hardware-pin`) | A checklist spanning many models; no model of its own |
| Ref "Summary Checklist", "Additional Resources" | Distributed / dropped | Procedural scaffolding and external links, not knowledge |
| Forgot-passphrase, forgot-PIN scenarios (Ref) | Folded into `passphrases` / `hardware-pin` depth 3 + `recovery-planning` | Each is one paragraph of consequence within an existing model |
| ssh -T account testing (Ref) | Inside `multiple-github-accounts` and setup procedures | A verification step, not a standalone procedure |
| Guide §15 (pointer to the Reference) | Dropped | Cross-document plumbing; the graph replaces it |

---

## Decomposition Batch Plan (ho-C2 … ho-C7)

57 nodes to author (60 minus 3 existing). Ordered so every batch's `requires` targets exist by the end of that batch; early batches carry the spine. Existing nodes' prerequisites (`agent-forwarding`, `permission-denied`, `blob`) are fully satisfied by end of ho-C4.

| Ho | Theme | Nodes (n) |
|---|---|---|
| **ho-C2** | **The spine** — root + core concepts every other cluster leans on | what-ssh-is, key-pairs, signatures, trust-boundaries, server-hardening, authorized-keys, passphrases, ssh-agents, ssh-config-basics, known-hosts (10) |
| **ho-C3** | **Modern auth landscape** — self-contained cluster; unlocks the hardware chain via fido2 | passwords, modern-auth-landscape, one-time-codes, mfa, mfa-strength-ladder, fido2, webauthn, passkeys, phishing-resistance (9) |
| **ho-C4** | **Hardware: device + SSH core** — completes deps of existing `blob` node | hardware-security-keys, hardware-key-capabilities, touch-requirement, hardware-pin, presence-vs-identity, pins-vs-passphrases, hardware-keys-ssh, state, slots, non-resident-keys, resident-keys (11) |
| **ho-C5** | **Config, git model, multi-hop** — the lateral fabric | stub, resident-vs-non-resident, identities-only, config-wildcards, host-aliases, git-ssh-authentication, username-trick, multiple-github-accounts, proxy-jump, jump-host-config (10) |
| **ho-C6** | **Procedures** — the action layer; all concept prerequisites now exist | choosing-an-approach, key-generation, first-key-setup, deploy-public-key, hardware-key-setup-resident, hardware-key-setup-nonresident, managing-resident-credentials, new-machine-setup, file-permissions (9) |
| **ho-C7** | **Troubleshooting, recovery, hygiene** — leaves of the graph | key-naming, key-rotation, macos-keychain, ssh-debugging, host-key-changed, lost-hardware-key, stolen-laptop, recovery-planning (8) |

Within-batch ordering matters twice: in ho-C2, author `what-ssh-is` → `key-pairs` before their dependents; in ho-C5, author `host-aliases` before `multiple-github-accounts`.

---

## Flags for Practitioner Review

1. **`passwords` has `requires: []`** — a second requires-root. Deliberate (conceptually prior to SSH; heavy question-entry traffic), but it breaks a single-root invariant if you want one.
2. **Private/public key folded into `key-pairs`** — the alternative was three nodes (`key-pairs`, `private-key`, `public-key`). Folding won on the one-model principle, but these are the two heaviest glossary terms folded anywhere. Cheap to split later if depth 2–3 of `key-pairs` feels overloaded.
3. **`file-permissions` (concept) vs `permission-denied` (troubleshooting)** — intentional overlap: one carries *why SSH cares + the correct numbers*, the other carries *the failure and diagnosis path*. Decomposition agents must keep the boundary clean.
4. **`resident-vs-non-resident` exists despite both member nodes carrying tradeoffs at depth 4** — kept because it is the decision surface the Reference's decision guide points at; its depth 4 should stay comparative, not repeat the members.
