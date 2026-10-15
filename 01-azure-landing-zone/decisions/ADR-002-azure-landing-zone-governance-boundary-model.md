# ADR-002 — Azure Landing Zone Governance Boundary Model

## Status

Accepted

## Date

2026-10-15

## Context

Phase 0 identified fragmented management-group boundaries, inconsistent
subscription placement, uneven governance inheritance, and weak lifecycle
separation across the modeled AFG Azure estate.

Phase 1 required a management-group architecture that could:

- provide a stable enterprise governance boundary;
- separate shared platform services from business workloads;
- distinguish corporate-connected and independently connected workloads;
- isolate transitional legacy workloads;
- provide controlled boundaries for experimentation, onboarding, and retirement;
- support incremental brownfield adoption;
- avoid modeling the management-group hierarchy as an organizational chart.

The architecture also needed to preserve valid existing Azure resources and
management-group identifiers where practical.

## Decision Drivers

The decision was driven by:

- predictable policy and RBAC inheritance;
- enterprise-scale subscription governance;
- separation of platform and workload responsibilities;
- workload placement based on connectivity and governance requirements;
- controlled brownfield modernization;
- subscription lifecycle management;
- reduction of unmanaged subscriptions directly beneath Tenant Root;
- future compatibility with governance, identity, networking, security,
  data-protection, and DevSecOps architecture phases.

## Options Considered

### Option 1 — Retain the Phase 0 Environment-Based Hierarchy

Retain `Production`, `Non-Production`, `Sandbox`, and `Legacy` beneath
`Landing-Zones`.

This option was rejected because environment-oriented management groups alone
did not provide sufficient separation between workload connectivity archetypes
and would encourage policy differences to be implemented through lower-level
exceptions.

### Option 2 — Create Management Groups Around Applications or Teams

Create management groups based on individual applications, departments,
business units, or resource ownership.

This option was rejected because management groups should represent durable
governance boundaries rather than organizational structures that may change
frequently.

### Option 3 — Establish an Enterprise Governance Boundary with Platform,
Landing-Zone, and Lifecycle Archetypes

Create an `AFG` intermediate enterprise root and organize management groups
around durable governance and workload-placement requirements.

This option was selected.

## Decision

AFG will use the following target management-group architecture:

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