---
name: replay-procedure
description: "Validate and dispatch a recorded UI procedure to an explicitly registered computer-use adapter. Dry-run by default and adapter-dependent."
---
# replay-procedure
Route: `@computer-use-agent /computer-use:replay-procedure`. `-Apply` requires `adapterStatus=CONFIRMED` and an explicit adapter script; otherwise it HALTs rather than pretending computer control exists.
