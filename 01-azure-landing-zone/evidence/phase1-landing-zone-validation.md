# Phase 1 Azure Landing Zone Validation

## Purpose

This document records validation evidence for the representative Phase 1
Azure Landing Zone implementation.

The validation confirms that selected elements of the AFG target-state
management-group and subscription architecture were implemented and tested
in the physical Azure lab.

This evidence does not imply that every modeled enterprise subscription,
workload, policy, or later-phase control has been deployed.

## Validation Scope

Phase 1 validation covers:

- target management-group hierarchy;
- preservation of existing platform management groups;
- retirement of obsolete environment-based management groups;
- representative platform subscription placement;
- brownfield subscription classification and placement;
- default management group configuration;
- Terraform state reconciliation and ownership transition;
- Azure remote backend migration;
- Terraform desired-state validation.

The following remain modeled rather than physically deployed:

- full Corp workload subscription population;
- full Online workload subscription population;
- enterprise Data Platform subscriptions;
- digital-services workload implementation;
- subscription-vending automation;
- detailed Azure Policy controls;
- later-phase identity, networking, security operations, data protection,
  DevSecOps, and AI controls.

## 1. Management-Group Hierarchy Validation

### Expected Target State

```text
Tenant Root Group
└── AFG
    ├── Platform
    │   ├── Connectivity
    │   ├── Management
    │   └── Security
    │
    ├── Landing-Zones
    │   ├── Corp
    │   ├── Online
    │   └── Legacy
    │
    ├── Sandbox
    ├── Onboarding
    └── Decommissioned

## 5. Terraform Ownership Transition

Phase 0 Terraform was used to reconstruct and validate the brownfield
management-group hierarchy.

After the Phase 0 baseline was reconciled, active Terraform ownership was
transitioned from:

01-azure-landing-zone/infrastructure-as-code/terraform/

## 7. Default Management Group

AFG uses `Onboarding` as the tenant default management group for subscriptions
created outside the governed subscription-vending process.

The purpose of `Onboarding` is to provide a controlled temporary boundary for
subscriptions whose ownership, business purpose, connectivity model, data
requirements, or final target placement have not yet been classified.

Approved subscription vending should place subscriptions directly into their
intended target management group rather than routing them through
`Onboarding`.

### Validation Method

```bash
ROOT_MG=$(az account show --query tenantId -o tsv)

az account management-group hierarchy-settings list \
  --name "$ROOT_MG" \
  --query "value[].{DefaultManagementGroup:defaultManagementGroup,RequireAuthorizationForGroupCreation:requireAuthorizationForGroupCreation}" \
  -o jsonc

  ## 7. Default Management Group

AFG uses `Onboarding` as the tenant default management group for subscriptions
created outside the governed subscription-vending process.

The purpose of `Onboarding` is to provide a controlled temporary boundary for
subscriptions whose ownership, business purpose, connectivity model, data
requirements, or final target placement have not yet been classified.

Approved subscription vending should place subscriptions directly into their
intended target management group rather than routing them through
`Onboarding`.

### Validation Method

```bash
ROOT_MG=$(az account show --query tenantId -o tsv)

az account management-group hierarchy-settings list \
  --name "$ROOT_MG" \
  --query "value[].{DefaultManagementGroup:defaultManagementGroup,RequireAuthorizationForGroupCreation:requireAuthorizationForGroupCreation}" \
  -o jsonc

  ## 10. Terraform Desired-State Validation

### Result

**Status: Validated**

Terraform reported:

```text
No changes. Your infrastructure matches the configuration.