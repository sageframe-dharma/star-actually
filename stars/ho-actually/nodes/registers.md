---
id: registers
title: architectural register / executable register
type: concept
requires: []
related: [agent-task, basis-of-design, ho-document]
entry_points: [architectural register / executable register]
summary: >
  The two levels a single thought is written at: the reasoning a person reads, and the exact instructions the executor follows.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
architectural register / executable register

<!-- depth:2 -->
<!-- provenance: extracted -->
The two levels a single thought is written at: the reasoning a person reads, and the exact instructions the executor follows.

<!-- depth:3 -->
<!-- provenance: extracted -->
The two cognitive registers a single
architectural thought is written in: the **architectural register** (the ho document —
decisions, reasoning, reflection, read by humans) and the **executable register** (the
agent task — exact files, changes, verification, read by the executor). The word
_register_ in the framework means this cognitive altitude; the design source-of-truth file
is the **Basis of Design**, not a "register."

<!-- depth:4 -->
<!-- provenance: extracted -->
**The Two Registers.** A ho document operates at the **architectural register**. It carries decisions, the
reasoning behind them, deferred discoveries, and post-execution reflection. It is read
by humans — the practitioner, future maintainers, anyone trying to understand why the
system is the way it is. Its content is durable: it survives the project and gets
revisited years later.

An agent task operates at the **executable register**. It carries exact files, exact
changes, exact acceptance criteria, exact verification commands. It is read primarily
by an autonomous coding agent — and secondarily by the practitioner reviewing the
agent's output. Its content is operational: once the work is committed and verified,
the task's job is done.

Mixing the registers in one document damages both. The architectural reasoning gets
buried under schemas and signatures; the executable spec gets diluted by paragraphs of
context the agent doesn't need. Extraction resolves the conflict structurally: each
document speaks in one voice, and the relationship between them is preserved by
explicit binding.
