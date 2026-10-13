# Azure Landing Zone Architecture Requirements

## Purpose

This document defines the architecture requirements for the AFG Azure Landing Zone based on the findings, risks, business requirements, and technical requirements established during Phase 0.

The landing zone shall provide a scalable enterprise foundation for management-group governance, subscription organization, workload separation, shared platform services, lifecycle management, and incremental modernization of the existing brownfield Azure environment.

The Azure landing-zone architecture should support future cross-tenant collaboration, external identity federation, and controlled onboarding of acquired organizations without weakening existing governance boundaries.

## Phase 0 Architecture Drivers

Phase 0 identified governance fragmentation, inconsistent management-group and subscription boundaries, uneven policy inheritance, incomplete ownership standards, and legacy workload governance gaps across the modeled Azure estate.

These conditions create risk because platform controls cannot be applied consistently, subscription placement is not governed by a standard architecture model, and exceptions for legacy or specialized workloads may weaken broader enterprise controls.

Phase 1 therefore establishes the Azure Landing Zone foundation needed to support consistent governance, workload separation, shared platform services, subscription lifecycle management, and incremental modernization.

The landing-zone design is primarily driven by the following Phase 0 concerns:

- R-001 — inconsistent management-group hierarchy and subscription governance.
- R-010 — recovery architecture and resilience requirements that may influence subscription placement.
- R-013 — legacy and hybrid workload governance requiring an incremental modernization path.
- BR-001 — cloud governance must scale as subscriptions and workloads grow.
- BR-010 — modernization must support brownfield adoption without requiring a full greenfield rebuild.

Detailed identity, network security, security operations, data protection, and DevSecOps controls remain within their respective later architecture phases unless a Phase 1 platform boundary is required to support them.

## Architecture Requirements

| ID | Architecture Requirement | Primary Driver |
|---|---|---|
| ALZ-001 | AFG shall establish a standardized management-group hierarchy that provides predictable governance inheritance and separates enterprise platform, workload, sandbox, transitional, and retired environments. | R-001, BR-001 |
| ALZ-002 | AFG shall define subscription placement criteria based on workload purpose, ownership, connectivity, environment, governance requirements, and lifecycle rather than resource type alone. | R-001, BR-001 |
| ALZ-003 | Shared platform services shall be separated from application and business workload subscriptions to provide clear ownership and governance boundaries. | R-001 |
| ALZ-004 | Production and non-production workloads shall use governance boundaries that support appropriate separation of operational risk, access, data handling, and change management. | R-001 |
| ALZ-005 | AFG shall define documented placement criteria for Corp and Online landing zones based primarily on connectivity and routing requirements. | R-001 |
| ALZ-006 | Legacy workloads requiring temporary exceptions shall use a controlled transitional architecture that does not weaken the standard governance baseline for modern workloads. | R-013, BR-010 |
| ALZ-007 | Sandbox subscriptions shall be isolated from production workloads and governed through a separate control and lifecycle model. | R-001 |
| ALZ-008 | AFG shall define a subscription lifecycle covering provisioning, placement, operation, transition, decommissioning, and eventual removal. | BR-001 |
| ALZ-009 | The landing-zone architecture shall provide defined boundaries for centralized identity, management, connectivity, and security platform services where justified by workload and operational requirements. | R-001 |
| ALZ-010 | The target architecture shall support incremental brownfield adoption without requiring existing workloads to be rebuilt solely to conform to the target-state hierarchy. | R-013, BR-010 |

## Constraints and Assumptions

The Phase 1 architecture is based on a brownfield Azure environment rather than a greenfield deployment.

The following constraints and assumptions apply:

- Existing subscriptions and workloads may require staged migration into the target management-group hierarchy.
- Existing production workloads shall not be assumed to be immediately movable without dependency and impact analysis.
- The Tenant Root Group is an existing Azure tenant boundary and is not currently intended to be managed through the Phase 1 Terraform implementation.
- The proposed `AFG` management group is intended to serve as the enterprise governance root beneath the Tenant Root Group.
- Existing management groups and subscriptions may be reused, renamed, moved, or retired where appropriate rather than recreated solely to match the target-state model.
- Legacy and hybrid workloads may require temporary exceptions while modernization work is completed.
- Phase 1 establishes architectural boundaries but does not fully design identity, networking, security operations, DevSecOps, data protection, or AI security controls.
- The lab implementation shall remain representative and cost-conscious rather than attempting to reproduce a full enterprise Azure estate.
- Architecture documented in this phase represents the proposed target state unless explicitly supported by validated lab evidence.

## Architecture Decision Status

The architecture decisions required to implement these requirements were
evaluated during Phase 1 and are recorded in
`management-group-subscription-design.md`.

All initial Phase 1 architecture decisions have been resolved or explicitly
deferred to later-phase detailed design where appropriate.