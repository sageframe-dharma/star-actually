---
id: system-design
title: system design (Kamae 2)
type: definition
requires: []
related: [kamae, seed, kamae-addendum, basis-of-design]
entry_points: [system design, kamae 2]
summary: >
  The document that settles how the system works—its parts, connections, and technology choices—before any code is written.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
system design (Kamae 2)

<!-- depth:2 -->
<!-- provenance: extracted -->
The document that settles how the system works—its parts, connections, and technology choices—before any code is written.

<!-- depth:3 -->
<!-- provenance: extracted -->
The Kamae 2 document: the structured technical vision—major
components and how they connect, data flow, technology stack with rationale, deployment
model, scope boundaries. Turns the seed's architectural opinions into decisions, each
traceable to the seed's core idea; no implementation details (those belong to individual
hos). Frozen once committed—superseded by dated addenda (kamae-N.M), never edited in
place.

<!-- depth:4 -->
<!-- provenance: extracted -->
**System Design.** **What it is:** The structured technical vision. How the system works, what the major components are, how they connect, what technology choices anchor the architecture. Written for someone who needs to understand _what you're building_ at a systems level.

The System Design takes the seed's architectural opinions and turns them into decisions. The seed says "I think I need a database and a web frontend, and here's why." The System Design says "PostgreSQL, FastAPI, here's the data model, here's how the components connect." Every decision should be traceable back to the seed's core idea—if an architectural choice doesn't serve the project's stated purpose, it needs justification or removal.

**What it's NOT:** Implementation details. The System Design says "the controller sends a Wake-on-LAN packet, waits for SSH, runs syncoid, and shuts down the remote machine." It does NOT say "use paramiko with a 120-second timeout and poll every 5 seconds." Those decisions happen in individual hos.

**What "done" looks like:**

Someone reading this document should understand:

- The system architecture (major components and how they interact)
- Data flow (what goes in, what comes out, what's stored where)
- Technology stack (languages, frameworks, key libraries—with rationale)
- Deployment model (where does this run, how is it accessed)
- Scope boundaries (what's v1, what's future, what's explicitly out)

A good System Design includes at least one architecture diagram (even ASCII art) showing the major components and their relationships. […]
