---
id: managing-resident-credentials
title: Managing Resident Credentials
type: procedure
requires: [resident-keys, slots]
related: [hardware-key-setup-resident, stub, lost-hardware-key]
entry_points: [list keys on yubikey, ykman fido credentials, delete resident key, yubikey slots full]
summary: >
  Housekeeping on the device—ykman list/delete, checking slot usage,
  freeing slots, and the slot-limit recovery path.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Managing Resident Credentials

<!-- depth:2 -->
<!-- provenance: synthesized -->
Resident credentials live on the hardware key itself, so managing them means talking to the device—with `ykman`—not editing files. The housekeeping: list what's stored, delete what you no longer need, free slots when you hit the limit.

<!-- depth:3 -->
<!-- provenance: extracted -->
### list resident credentials on hardware key

```bash
ykman fido credentials list
```

Shows:

- All resident credentials stored on device
- Application names (ssh:)
- User names

Use case: verify which keys are stored, manage slots.

### delete resident credential

```bash
ykman fido credentials delete ssh:username
```

When to use:

- Free up slots
- Remove old access
- Before decommissioning key

**Warning: permanent!** Make sure you don't need this key anymore.

### reached the slot limit

Resident keys are limited by hardware slots (typically 25-32). If you can't create more resident keys:

- **Recovery:** delete old resident keys with `ykman fido credentials delete`
- **Prevention:** use non-resident keys for frequently-changing access
