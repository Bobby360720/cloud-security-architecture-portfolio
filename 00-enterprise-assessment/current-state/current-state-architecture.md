# Current-State Architecture

## Overview

AFG operates a hybrid enterprise estate connecting on-premises
infrastructure to Azure through private enterprise connectivity. Azure
workloads are distributed across platform, production, non-production,
sandbox, legacy, and disaster-recovery purposes.

The architecture contains many appropriate building blocks, but
governance consistency varies between modern and legacy workloads.

## Logical Architecture

### Identity Plane

Microsoft Entra ID provides enterprise identity. Conditional Access and
PIM exist, but privileged-access and workload-identity governance are
not yet uniform.

### Governance Plane

Management groups and Azure Policy exist, but overlapping assignments
and transitional subscription placement reduce predictability.

### Connectivity Plane

Hub-and-spoke networking, ExpressRoute, Azure Firewall, NSGs, private
endpoints, and private DNS are present. Adoption is uneven across older
workloads.

### Workload Plane

The estate contains VMs, Arc-enabled servers, App Services, Function
Apps, APIs, Logic Apps, container workloads, storage, and database
services.

### Security Plane

Defender for Cloud, Sentinel, Log Analytics, Azure Monitor, AMA, and
DCRs provide security visibility. Coverage and lifecycle management
require normalization.

### Delivery Plane

Azure DevOps, Git, Bicep, Terraform, and CI/CD exist, but manual
configuration and team-specific patterns remain.

## Architectural Weaknesses

1.  Governance scope does not always align with workload purpose.
2.  Secure platform patterns are not uniformly inherited.
3.  Identity lifecycle maturity varies by identity type.
4.  Network trust is more restrictive for newer workloads than legacy
    ones.
5.  Logging requirements are not consistently enforced.
6.  Data sensitivity is not reliably represented in platform metadata.
7.  Deployment automation is not yet the universal path.
8.  Exceptions and residual risk are not managed through one consistent
    lifecycle.

## Architecture Constraint

The transformation must modernize governance without requiring a
disruptive greenfield rebuild. Existing workloads will migrate toward
target patterns incrementally.
