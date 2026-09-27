
# Phase 0 Terraform Baseline Validation

**Validation date:** September 27, 2026  
**Terraform version:** 1.16.3  
**Scope:** Bootstrap infrastructure and Phase 0 Azure management-group hierarchy  
**Environment:** Physical Azure lab supporting the fictionalized AFG enterprise assessment

## Validation Summary

Both Terraform configurations passed formatting and configuration
validation. Both normal Terraform plans returned exit code 0 with
no proposed infrastructure changes.

| Validation | Bootstrap | Enterprise Assessment |
|---|---|---|
| Terraform formatting | Passed | Passed |
| Terraform validation | Passed | Passed |
| Remote state access | Confirmed | Confirmed |
| Resources tracked | 4 | 12 |
| Normal Terraform plan | No changes | No changes |
| Plan exit code | 0 | 0 |

The 16 tracked resources comprise four bootstrap resources,
nine management groups, and three subscription associations.

## Verified Management-Group Hierarchy

The deployed Azure hierarchy was inspected using Azure CLI and
compared with the Terraform configuration.

| Parent | Child management groups |
|---|---|
| Tenant Root Group | Platform, Landing Zones |
| Platform | Security, Connectivity, Management |
| Landing Zones | Production, Non-Production, Sandbox, Legacy |

All nine management groups are tracked in Terraform state.

The Platform and Landing Zones branches were inspected in Azure.
Their Terraform configurations omit explicit parent identifiers,
and both normal Terraform plans returned no changes.

The parent values in the shared Azure output were redacted;
the exact Tenant Root Group relationship was therefore not
independently established from that output.

## Core Platform Subscription Associations

| Management group | Subscription | Result |
|---|---|---|
| Security | sub-security-01 | Verified |
| Connectivity | sub-connectivity-01 | Verified |
| Management | sub-management-01 | Verified |

All three associations were observed in the deployed Platform
hierarchy and are tracked in Terraform state.

## Existing Resource Adoption

The current-state cloud inventory documents a brownfield Terraform
adoption process. Initial planning identified potential replacement
of existing management groups because their immutable Azure
identifiers differed from the identifiers originally represented
in Terraform.

The configuration was reconciled with the existing Azure identifiers.
Existing management groups were imported and preserved rather than
destroyed and recreated.

Production, Non-Production, and Sandbox were reparented beneath
Landing Zones. Connectivity and Management were established beneath
Platform, alongside Security.

The three core platform subscriptions were associated with their
respective management groups.

**Evidence:**
- `../current-state/cloud-inventory.md`, Key Engineering Finding
- Git commit `facda0a` — Build Phase 0 Azure enterprise hierarchy
- September 27, 2026: live Azure hierarchy inspection and Terraform
  plans returning exit code 0

**Limitation:** The repository documents the import and preservation
process, but the evidence reviewed does not include a pre-import
identifier snapshot or original import logs.

## State Refresh Observations

Both configurations were inspected using refresh-only Terraform
plans.

The bootstrap refresh-only plan reported an empty tag map on
the Terraform state resource group.

The enterprise refresh-only plan reported subscription membership
updates for the Security, Connectivity, and Management groups.

Subsequent normal Terraform plans returned exit code 0 for both
configurations. No infrastructure changes were proposed.

The refresh-only differences were observed but were not applied
as separate state updates during this validation.

## Deployment Considerations

1. Preserve existing management-group identifiers when modifying
   the Terraform configuration.
2. Review every Terraform plan before applying changes.
3. Maintain separate remote state keys for bootstrap and
   enterprise-assessment configurations.
4. Protect remote state with appropriate Azure RBAC and
   Microsoft Entra authentication.
5. Validate management-group hierarchy and subscription placement
   after any governance configuration change.
6. Keep modeled enterprise resources separate from the physical
   Azure lab baseline.

## Teardown Considerations

The bootstrap storage account and its state container are persistent
dependencies. They must not be included in routine lab teardown.

Management groups and platform subscription associations may also
be shared dependencies. Do not destroy them automatically.

Before any teardown:

- Identify resources owned exclusively by the temporary lab.
- Review the Terraform destroy plan and its dependencies.
- Confirm that no shared subscriptions or management groups
  would be affected.
- Preserve remote state and any required validation evidence.
- Require explicit approval before removing persistent governance
  or bootstrap resources.

## Validation Limitations

The results establish that the Terraform-managed Phase 0 lab
configuration matched the deployed Azure resources at the time
of testing.

They do not demonstrate that the wider modeled AFG enterprise
inventory has been deployed or that its security controls have
been operationally validated.

Historical preservation of management-group identifiers is
documented in the repository but has not been independently
verified against pre-import identifier records.
