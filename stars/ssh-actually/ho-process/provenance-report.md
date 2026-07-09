---
created: 2026-07-04
status: awaiting practitioner sign-off
type: provenance-report
project: star-actually
ho: ho-C-final
---

# ho-C-final — Graph Review and Provenance Report

**The review surface for the content sign-off.** Extracted layers are the
practitioner's own words, trimmed and reflowed — skim them. Synthesized
layers are new connective prose written during decomposition — read them.
Once signed off, provenance markers are stripped from the node files.

## The graph

- **60 nodes**, strict validation clean (no dangling edges, no
  requires-cycles, no orphans)
- Types: 37 concept, 8 definition, 9 procedure, 3 scenario, 3 troubleshooting
- Depth ceilings: 24 nodes stop at 3, 28 nodes stop at 4, 8 nodes stop at 5
- **224 authored layers total; 37 synthesized (16%), 187 extracted**

## Synthesized layers — the review reading list

| Node | Depth | Read it at |
| --- | --- | --- |
| agent-forwarding | 4 | `/n/agent-forwarding/?d=4` |
| authorized-keys | 2 | `/n/authorized-keys/?d=2` |
| authorized-keys | 4 | `/n/authorized-keys/?d=4` |
| choosing-an-approach | 2 | `/n/choosing-an-approach/?d=2` |
| choosing-an-approach | 4 | `/n/choosing-an-approach/?d=4` |
| file-permissions | 4 | `/n/file-permissions/?d=4` |
| hardware-key-setup-nonresident | 2 | `/n/hardware-key-setup-nonresident/?d=2` |
| hardware-key-setup-resident | 2 | `/n/hardware-key-setup-resident/?d=2` |
| host-key-changed | 2 | `/n/host-key-changed/?d=2` |
| key-generation | 2 | `/n/key-generation/?d=2` |
| key-pairs | 4 | `/n/key-pairs/?d=4` |
| known-hosts | 4 | `/n/known-hosts/?d=4` |
| lost-hardware-key | 2 | `/n/lost-hardware-key/?d=2` |
| lost-hardware-key | 4 | `/n/lost-hardware-key/?d=4` |
| macos-keychain | 4 | `/n/macos-keychain/?d=4` |
| managing-resident-credentials | 2 | `/n/managing-resident-credentials/?d=2` |
| multiple-github-accounts | 4 | `/n/multiple-github-accounts/?d=4` |
| new-machine-setup | 2 | `/n/new-machine-setup/?d=2` |
| passkeys | 4 | `/n/passkeys/?d=4` |
| passphrases | 4 | `/n/passphrases/?d=4` |
| phishing-resistance | 2 | `/n/phishing-resistance/?d=2` |
| phishing-resistance | 3 | `/n/phishing-resistance/?d=3` |
| phishing-resistance | 4 | `/n/phishing-resistance/?d=4` |
| presence-vs-identity | 4 | `/n/presence-vs-identity/?d=4` |
| proxy-jump | 5 | `/n/proxy-jump/?d=5` |
| recovery-planning | 2 | `/n/recovery-planning/?d=2` |
| recovery-planning | 4 | `/n/recovery-planning/?d=4` |
| server-hardening | 4 | `/n/server-hardening/?d=4` |
| signatures | 4 | `/n/signatures/?d=4` |
| ssh-agents | 2 | `/n/ssh-agents/?d=2` |
| ssh-agents | 4 | `/n/ssh-agents/?d=4` |
| ssh-config-basics | 4 | `/n/ssh-config-basics/?d=4` |
| ssh-debugging | 2 | `/n/ssh-debugging/?d=2` |
| ssh-debugging | 4 | `/n/ssh-debugging/?d=4` |
| trust-boundaries | 2 | `/n/trust-boundaries/?d=2` |
| trust-boundaries | 3 | `/n/trust-boundaries/?d=3` |
| what-ssh-is | 4 | `/n/what-ssh-is/?d=4` |

## Entry-point coverage (seed §3 example questions)

| Seed question | Landing node |
| --- | --- |
| "What is SSH?" | what-ssh-is |
| "How do I juggle three GitHub SSH logins?" | multiple-github-accounts |
| "At what point do I need a physical auth key?" | choosing-an-approach / hardware-security-keys |
| "Resident vs non-resident, actually?" | resident-vs-non-resident |
| "Permission denied (publickey)?" | permission-denied |

Every layer in the corpus carries a provenance marker. ✓
