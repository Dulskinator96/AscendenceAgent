# Keep Quasar's machine profile separately attributed

Quasar is a distinct machine context (the user's brother's PC, reported hostname `AURORA`, local Windows profile `mxz`), so its hardware evidence and AI handoff instructions are recorded in a dedicated profile rather than being folded into the user's own device record; this boundary prevents agents from transferring capabilities, assumptions, or operational instructions between different computers.

## Status

Accepted for the Quasar handoff baseline.

## Considered options

- **Keep Quasar details in a general user profile:** rejected because machine ownership and hardware context could be conflated.
- **Record only a short hardware summary:** rejected because future agents also need provenance, unknowns, and operational guardrails.
- **Maintain a dedicated, evidence-based machine profile:** chosen to keep attribution explicit and updates traceable in version control.

## Consequences

- Future agents must verify they are working on Quasar before applying machine-specific instructions.
- Unknown specifications remain explicitly unknown until new evidence is collected.
- The profile requires deliberate updates when hardware or configuration changes.
- This record documents a data-boundary and handoff decision; it does not authorize system changes or assert that the machine has been independently inspected.
