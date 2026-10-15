# Phase 1 — Azure Landing Zone

## Objective

Establish the Azure platform foundation required to provide consistent
enterprise governance, predictable subscription placement, workload
separation, lifecycle management, and controlled brownfield adoption.

Phase 1 translates the findings and requirements established during the
enterprise assessment into a representative Azure Landing Zone architecture.

## Architecture Outcome

The Phase 1 target management-group hierarchy is:

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
```

The hierarchy separates shared platform services, standard business workloads,
customer-facing workloads, transitional legacy workloads, experimentation,
unclassified subscriptions, and retirement states.

## Representative Subscription Placement

```text
AFG
├── Platform
│   ├── Connectivity
│   │   └── sub-connectivity-01
│   ├── Management
│   │   └── sub-management-01
│   └── Security
│       └── sub-security-01
│
├── Landing-Zones
│   ├── Corp
│   ├── Online
│   │   └── Web Apps
│   └── Legacy
│       └── Connectivity
│
├── Sandbox
│   ├── sub-sandbox-01
│   └── sub-sandbox
│
├── Onboarding
│
└── Decommissioned
    ├── Identity
    └── Security
```

Subscription placement was based on workload purpose, deployed resources,
governance requirements, RBAC, policy, resource locks, lifecycle, and target
architecture rather than subscription names alone.

## Implemented and Validated

The representative Azure lab validates:

- the `AFG` enterprise management-group boundary;
- Platform and Landing-Zones separation;
- Connectivity, Management, and Security platform boundaries;
- Corp, Online, and Legacy workload archetypes;
- Sandbox isolation;
- `Onboarding` as the default management group for unclassified subscriptions;
- `Decommissioned` as a controlled retirement boundary;
- retirement of the former `Production` and `Non-Production` management groups;
- preservation and reparenting of existing brownfield management groups;
- representative platform subscription placement;
- classification and placement of existing brownfield subscriptions;
- Terraform state reconciliation;
- transition of Terraform ownership from Phase 0 to Phase 1;
- Azure Storage remote Terraform state;
- Terraform desired-state convergence.

Final Terraform validation reported:

```text
No changes. Your infrastructure matches the configuration.
```

## Modeled or Deferred

The representative lab does not physically reproduce the complete modeled AFG
enterprise estate.

The following remain modeled, planned, or deferred:

- full Corp workload subscription population;
- full Online workload implementation;
- `sub-prod-digital-services-01` target naming;
- enterprise Data Platform subscriptions;
- subscription-vending automation;
- detailed Azure Policy implementation;
- detailed identity controls;
- detailed network-security architecture;
- security operations;
- data protection;
- DevSecOps;
- AI security.

## Key Architecture Decisions

Phase 1 resolved the initial landing-zone architecture decisions covering:

- identity subscription strategy;
- Corp versus Online workload placement;
- disaster-recovery subscription strategy;
- enterprise Data Platform boundaries;
- Legacy management-group usage;
- brownfield migration sequencing;
- ADR governance;
- default subscription placement through `Onboarding`.

Detailed decisions are maintained in:

`architecture/management-group-subscription-design.md`

## Key Artifacts

| Artifact | Purpose |
|---|---|
| `architecture/landing-zone-requirements.md` | Phase 1 architecture requirements and Phase 0 drivers |
| `architecture/management-group-subscription-design.md` | Target management-group, subscription, lifecycle, and migration design |
| `infrastructure-as-code/terraform/` | Active Terraform implementation |
| `evidence/phase1-landing-zone-validation.md` | Validation evidence distinguishing implemented state from modeled architecture |

## Phase Status

**Status: Complete — representative Azure Landing Zone foundation implemented and validated.**

## Next Phase

Phase 2 — Cloud Governance

The next phase builds on the validated landing-zone hierarchy by defining
Azure Policy, control inheritance, exemptions, ownership, compliance, and
governance operations.
