
## Existing Resource Adoption

The current-state cloud inventory documents a brownfield Terraform adoption
process. Initial planning identified potential replacement of existing
management groups because their immutable Azure identifiers differed from
the identifiers originally represented in Terraform.

The configuration was reconciled with the existing Azure identifiers.
Existing management groups were imported and preserved rather than
destroyed and recreated.

Production, Non-Production, and Sandbox were reparented beneath
Landing Zones. Connectivity and Management were established beneath
Platform, alongside Security.

The three core platform subscriptions were associated with their
respective management groups.

**Evidence:**
- `current-state/cloud-inventory.md`, Key Engineering Finding
- Git commit `facda0a` — Build Phase 0 Azure enterprise hierarchy
- September 27, 2026: live Azure hierarchy inspection and Terraform
  plans returning exit code 0

**Limitation:** The repository documents the import and preservation
process, but the evidence reviewed does not include a pre-import
identifier snapshot or original import logs.
