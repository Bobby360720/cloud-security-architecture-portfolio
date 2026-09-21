This is a **good skeleton**, but compared with the cloud inventory we just completed, it is too compressed for the main Phase 0 architecture assessment. I would keep your six-plane concept—it's strong—but expand it into a document that shows **relationships, boundaries, dependencies, architectural debt, and design implications**.

Most importantly, I would **not change your architecture story**. I would deepen it.

Here is the completed version I recommend for `current-state-architecture.md`:

````markdown
# Current-State Architecture Assessment

> **Portfolio note:** This architecture assessment is fictionalized and
> sanitized for the AFG Enterprises Cloud Security Architecture Portfolio.
> It represents a realistic enterprise architecture scenario and does not
> describe a real production environment.

---

## 1. Purpose

This document assesses the current-state architecture of AFG Enterprises
during **Phase 0 — Enterprise Assessment**.

The Cloud Inventory establishes **what exists**.

This assessment establishes:

- how those components relate to one another;
- where architectural and trust boundaries exist;
- how platform services support workloads;
- how security controls cross architectural boundaries;
- where architectural debt has accumulated;
- which dependencies create enterprise risk;
- which constraints must be considered during transformation;
- which findings become design inputs for later phases.

The objective is not to design the target state during Phase 0.

The objective is to establish a defensible understanding of the existing
architecture before making transformation decisions.

---

# 2. Assessment Scope

The assessment evaluates the architecture across six primary planes:

1. Identity
2. Governance
3. Connectivity
4. Workload
5. Security and Management
6. Delivery and Automation

Data protection and resilience are evaluated as cross-cutting concerns because
they span multiple architectural planes.

The assessment uses the same distinction established in the Cloud Inventory:

- **Logical Enterprise Environment** — the complete fictionalized AFG
  enterprise architecture.
- **Physical Architecture Lab** — selected architecture components implemented
  in Azure to validate designs and engineering patterns.

Not every logical enterprise resource is physically instantiated in the lab.

---

# 3. Executive Architecture Summary

AFG Enterprises operates a hybrid, Azure-first architecture connecting
traditional enterprise infrastructure with Azure platform and workload
services.

The environment contains many appropriate architectural building blocks:

- Microsoft Entra ID;
- management groups;
- Azure Policy;
- centralized platform subscriptions;
- hub-and-spoke networking;
- private enterprise connectivity;
- Azure Firewall;
- private endpoints;
- Microsoft Defender for Cloud;
- Microsoft Sentinel;
- Azure Monitor;
- Azure Arc;
- Infrastructure as Code;
- CI/CD.

The principal weakness is therefore not the absence of modern technology.

The architectural problem is that these capabilities have been introduced at
different times, under different operating models, and with different levels
of enforcement.

As a result, architectural maturity varies significantly between:

- platform and workload subscriptions;
- production and non-production environments;
- cloud-native and legacy workloads;
- human and workload identities;
- centrally managed and application-managed resources;
- automated and manually configured infrastructure.

The environment can therefore be characterized as **capability-rich but
inconsistently governed**.

The transformation must standardize how these capabilities operate together
without requiring a disruptive greenfield rebuild.

---

# 4. High-Level Logical Architecture

```text
                         Users / Administrators
                                  │
                                  ▼
                         Microsoft Entra ID
                                  │
                    Identity / Authentication
                                  │
                                  ▼
┌───────────────────────────────────────────────────────────┐
│                     Azure Tenant                          │
│                                                           │
│  ┌──────────────────── Platform ───────────────────────┐  │
│  │                                                     │  │
│  │  Connectivity     Management       Security         │  │
│  │       │               │                │            │  │
│  │       └──────── Shared Platform Services ───────────┤  │
│  │                                                     │  │
│  └─────────────────────────────────────────────────────┘  │
│                          │                                │
│                          ▼                                │
│  ┌──────────────── Landing-Zones ──────────────────────┐  │
│  │                                                     │  │
│  │  Production   Non-Production   Sandbox   Legacy     │  │
│  │                                                     │  │
│  │  Applications │ Data │ Compute │ PaaS │ Storage    │  │
│  │                                                     │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                           │
└───────────────────────────────────────────────────────────┘
                 │                         │
                 │                         │
         Hybrid Connectivity        Security Telemetry
                 │                         │
                 ▼                         ▼
       On-Premises / Arc              Sentinel /
          Infrastructure            Defender / Monitor
````

Cross-cutting architectural concerns include:

```text
Identity
Governance
Policy
Network Security
Observability
Data Protection
Resilience
Automation
Security Operations
```

No single architectural plane can therefore be assessed independently.

---

# 5. Azure Organizational Architecture

The Azure organizational model separates platform capabilities from workload
landing zones.

```text
Tenant Root Group
│
├── Platform
│   ├── Connectivity
│   │   └── sub-connectivity-01
│   ├── Management
│   │   └── sub-management-01
│   ├── Security
│   │   └── sub-security-01
│   └── sub-shared-services-01
│
└── Landing-Zones
    ├── Production
    │   ├── sub-prod-apps-01
    │   ├── sub-prod-apps-02
    │   ├── sub-prod-data-01
    │   └── sub-dr-01
    ├── Non-Production
    │   ├── sub-nonprod-apps-01
    │   └── sub-nonprod-data-01
    ├── Sandbox
    │   └── sub-sandbox-01
    └── Legacy
        └── sub-legacy-01
```

This structure establishes two important architectural boundaries.

### Platform Boundary

Platform subscriptions provide shared capabilities that support the wider
enterprise.

These include:

* connectivity;
* monitoring;
* security services;
* shared infrastructure.

### Landing-Zone Boundary

Landing zones contain business workloads and separate workloads according to
environment, purpose, and governance requirements.

This separation provides a foundation for policy inheritance and delegated
ownership.

However, organizational structure alone does not guarantee consistent
governance.

Policy, identity, logging, network, and deployment standards must align with
the hierarchy for the model to provide effective control.

---

# 6. Identity Plane

Microsoft Entra ID provides the primary enterprise identity and trust plane.

The identity architecture supports:

* workforce identities;
* privileged administrators;
* service principals;
* managed identities;
* application registrations;
* enterprise applications;
* Conditional Access;
* Privileged Identity Management;
* group-based access;
* emergency-access accounts.

## Current-State Pattern

```text
User / Administrator
        │
        ▼
Microsoft Entra ID
        │
        ├── Conditional Access
        ├── MFA
        ├── Groups
        ├── PIM
        └── RBAC
                │
                ▼
        Azure Resources
```

Workload identity follows multiple patterns:

```text
Application
    │
    ├── Managed Identity
    │
    ├── Service Principal
    │
    └── Client Secret / Credential
            │
            ▼
       Azure Resource
```

## Architectural Weakness

Identity governance maturity varies according to identity type.

Human identity controls are more mature than workload identity governance.

Key weaknesses include:

* standing privileged assignments;
* direct user RBAC assignments;
* inconsistent access-review coverage;
* incomplete workload-identity ownership;
* continued use of application secrets;
* inconsistent credential lifecycle management.

### Design Implication

Phase 3 must treat identity as an architectural control plane rather than
simply an authentication service.

---

# 7. Governance Plane

Azure management groups and Azure Policy provide the foundation of the
governance architecture.

The intended control hierarchy is:

```text
Tenant
  │
  ▼
Management Group
  │
  ▼
Subscription
  │
  ▼
Resource Group
  │
  ▼
Resource
```

Higher-level controls should be inherited whenever practical.

## Current-State Weakness

The environment contains policy assignments at both management-group and
subscription scopes.

This creates:

* overlapping controls;
* duplicated assignments;
* inconsistent enforcement;
* unclear policy ownership;
* permanent Audit-mode controls;
* inconsistent remediation;
* configuration drift.

The problem is therefore not simply insufficient policy.

The architectural problem is **fragmented control ownership and inconsistent
inheritance**.

### Design Implication

Phase 2 must rationalize controls into reusable enterprise initiatives with
clear scope, ownership, exceptions, enforcement, and remediation models.

---

# 8. Connectivity Plane

AFG uses a hybrid hub-and-spoke network architecture.

The connectivity plane includes:

* ExpressRoute;
* hub VNets;
* spoke VNets;
* Azure Firewall;
* Network Security Groups;
* Application Gateways;
* load balancers;
* private endpoints;
* private DNS;
* public IP addresses.

Conceptually:

```text
                    Internet
                       │
                Controlled Ingress
                       │
                       ▼
                Azure Edge / Gateway
                       │
                       ▼
On-Premises ─────── Hub Network
     │                 │
ExpressRoute           ├──────────┐
     │                 │          │
     └─────────────────┘          │
                                  ▼
                             Spoke VNets
                                  │
                      ┌───────────┼───────────┐
                      ▼           ▼           ▼
                   Apps         Data       Services
```

## Architectural Weakness

The enterprise does not apply this model uniformly.

Newer workloads increasingly use:

* private endpoints;
* centralized DNS;
* controlled ingress;
* stronger segmentation.

Legacy workloads retain patterns involving:

* direct public exposure;
* inconsistent NSG configuration;
* decentralized DNS;
* weaker egress control;
* older connectivity assumptions.

This produces multiple generations of network trust architecture within the
same enterprise.

### Design Implication

Phase 4 must normalize network trust boundaries without assuming every
workload can be immediately redesigned.

---

# 9. Workload Plane

The workload plane contains both infrastructure and platform services.

Major workload classes include:

* Azure Virtual Machines;
* Azure Arc-enabled servers;
* App Services;
* Function Apps;
* Logic Apps;
* API Management;
* Container Apps;
* AKS;
* storage services;
* Azure SQL;
* SQL Managed Instance;
* Cosmos DB.

This creates a heterogeneous workload architecture.

Traditional infrastructure requires controls around:

* operating-system lifecycle;
* patching;
* endpoint security;
* backup;
* configuration management.

PaaS workloads require greater emphasis on:

* workload identity;
* private connectivity;
* application configuration;
* data protection;
* platform diagnostics;
* API authorization.

Container workloads introduce additional concerns around:

* image security;
* workload identity;
* runtime protection;
* secrets;
* admission controls;
* supply-chain security.

A single security pattern therefore cannot adequately govern every workload
type.

---

# 10. Security and Management Plane

Security and operational visibility are provided through:

* Microsoft Defender for Cloud;
* Microsoft Sentinel;
* Azure Monitor;
* Log Analytics;
* Azure Monitor Agent;
* Data Collection Rules;
* diagnostic settings;
* Azure Activity Logs;
* Entra telemetry.

Conceptually:

```text
Azure / Hybrid Resources
          │
          ├── Platform Logs
          ├── Security Events
          ├── Identity Events
          └── Performance Telemetry
                    │
                    ▼
              Azure Monitor
                    │
             Log Analytics
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
      Sentinel        Defender for Cloud
          │                   │
          └─────────┬─────────┘
                    ▼
             Security Operations
```

## Architectural Weakness

Centralized tooling exists, but telemetry collection is inconsistent.

This creates a distinction between:

**having centralized security tooling**

and

**having consistently observable workloads**.

Current weaknesses include:

* inconsistent diagnostic settings;
* uneven DCR association;
* incomplete PaaS telemetry;
* varying retention;
* inconsistent Defender coverage;
* incomplete detection ownership.

### Design Implication

Phase 5 must define observability as an architectural requirement rather than
an optional resource configuration.

---

# 11. Delivery and Automation Plane

Azure DevOps and Git provide the primary engineering workflow.

Infrastructure deployment includes:

* Terraform;
* Bicep;
* manual Azure configuration;
* application CI/CD pipelines.

The desired engineering lifecycle is:

```text
Design
  │
  ▼
Code
  │
  ▼
Version Control
  │
  ▼
Validate
  │
  ▼
Plan
  │
  ▼
Review / Approval
  │
  ▼
Deploy
  │
  ▼
Verify
  │
  ▼
Operate
```

The current estate has not universally reached this model.

Manual configuration and team-specific deployment patterns remain.

This increases:

* configuration drift;
* deployment inconsistency;
* review difficulty;
* recovery complexity;
* audit complexity.

### Design Implication

Phase 6 must make secure, repeatable deployment the preferred operational
path rather than treating automation as an optional engineering enhancement.

---

# 12. Data Protection and Resilience

Data protection crosses the identity, network, workload, and governance
planes.

Existing capabilities include:

* encryption at rest;
* encryption in transit;
* Key Vault;
* Managed HSM;
* Microsoft Purview;
* DLP;
* backup;
* geo-redundant storage;
* disaster recovery.

However, technical controls cannot always be mapped reliably to business data
sensitivity.

Incomplete classification and ownership metadata limit the ability to apply
risk-based controls consistently.

Resilience maturity also varies by workload.

Infrastructure workloads generally have stronger established recovery
patterns than some newer PaaS architectures.

### Design Implication

Later transformation phases must connect:

```text
Data Classification
        │
        ▼
Business Criticality
        │
        ▼
Security Requirements
        │
        ▼
Technical Controls
        │
        ▼
Recovery Requirements
```

---

# 13. Cross-Domain Dependencies

The current-state assessment identifies several dependencies that prevent
architecture domains from being treated independently.

| Dependency                       | Architectural Effect                                             |
| -------------------------------- | ---------------------------------------------------------------- |
| Management groups → Policy       | Organizational hierarchy determines governance inheritance       |
| Identity → Workloads             | Authentication and authorization determine workload trust        |
| Identity → DevSecOps             | Pipelines require secure workload identities                     |
| Network → PaaS                   | Private access depends on DNS and endpoint architecture          |
| Data classification → Governance | Protection requirements depend on understanding data sensitivity |
| Monitoring → Security Operations | Detection quality depends on telemetry coverage                  |
| Tagging → Operations             | Ownership and criticality metadata drive accountability          |
| Criticality → Resilience         | Recovery requirements depend on business importance              |
| IaC → Governance                 | Repeatable deployment reduces configuration drift                |
| Governance → Security Operations | Policy findings require ownership and remediation                |

These relationships are significant because improving one domain can fail if
its upstream dependency remains unresolved.

---

# 14. Architectural Debt

The environment contains several categories of architectural debt.

### Organizational Debt

* inconsistent ownership;
* fragmented responsibility;
* incomplete backup ownership;
* inconsistent exception management.

### Governance Debt

* overlapping policy assignments;
* inconsistent enforcement;
* duplicated subscription-level controls;
* incomplete remediation.

### Identity Debt

* standing privileges;
* direct RBAC assignments;
* unmanaged credential lifecycle;
* incomplete workload ownership.

### Network Debt

* legacy public exposure;
* inconsistent segmentation;
* incomplete egress control;
* uneven private endpoint adoption.

### Observability Debt

* incomplete diagnostics;
* inconsistent DCR associations;
* variable retention;
* uneven security telemetry.

### Engineering Debt

* manual deployment;
* inconsistent pipeline controls;
* limited reusable patterns;
* incomplete Policy as Code.

### Data Debt

* incomplete classification;
* inconsistent ownership;
* variable retention;
* inconsistent protection requirements.

Architectural debt is therefore distributed across the system rather than
isolated to a single Azure service.

---

# 15. Risk Concentrations

The architecture assessment identifies several areas where multiple weaknesses
intersect.

## Workload Identity

Application secrets, inconsistent ownership, permission lifecycle, and
privileged API access combine to create concentrated identity risk.

## Legacy Workloads

Legacy networking, manual configuration, weaker governance, and incomplete
telemetry combine to produce higher operational and security risk.

## Public Exposure

Internet accessibility becomes more significant when combined with
inconsistent diagnostics, identity patterns, and application ownership.

## Governance Fragmentation

Duplicated policy, inconsistent inheritance, unclear exceptions, and manual
remediation reduce confidence that enterprise standards are consistently
enforced.

These areas should receive greater attention during requirements development
and transformation planning.

---

# 16. Current-State Architectural Weaknesses

The major current-state weaknesses are:

1. Governance scope does not always align with workload purpose.
2. Secure platform patterns are not uniformly inherited.
3. Identity lifecycle maturity varies by identity type.
4. Network trust is more restrictive for newer workloads than legacy ones.
5. Logging requirements are not consistently enforced.
6. Data sensitivity is not reliably represented in platform metadata.
7. Deployment automation is not yet the universal path.
8. Exceptions and residual risk are not managed through one consistent
   lifecycle.
9. Architectural ownership is not uniformly represented in metadata.
10. Platform capabilities exist, but their adoption and enforcement vary
    across the enterprise.

---

# 17. Architecture Constraints

The transformation must operate within several constraints.

### Brownfield Environment

The enterprise cannot assume a clean greenfield deployment.

Existing workloads, subscriptions, identities, network dependencies, and
operational processes must continue functioning during transformation.

### Incremental Migration

Existing workloads will move toward target-state patterns incrementally.

### Business Continuity

Security improvements cannot introduce unacceptable disruption to Tier 1
business services.

### Hybrid Dependencies

On-premises and Azure dependencies must coexist throughout the transformation.

### Legacy Compatibility

Some workloads cannot immediately adopt modern cloud-native patterns.

### Cost

Architectural controls must provide security value proportional to their
operational and financial cost.

### Operational Capacity

The target architecture must be supportable by the teams responsible for
operating it.

---

# 18. Current-State Architecture Principles

The assessment produces several principles that should constrain future
design decisions.

### 1. Understand Before Transforming

Existing architecture must be discovered and understood before it is
redesigned.

### 2. Preserve Before Replacing

Brownfield resources should be adopted or migrated where practical rather
than unnecessarily recreated.

### 3. Inherit Controls by Default

Enterprise controls should be applied at the highest appropriate scope.

### 4. Minimize Standing Privilege

Privileged access should be temporary and auditable where supported.

### 5. Prefer Workload Identity Over Stored Credentials

Managed identity and federated identity patterns should replace persistent
secrets where practical.

### 6. Private Access Should Be the Preferred Pattern

Public exposure should require an explicit architectural reason.

### 7. Observability Is a Platform Requirement

Security-relevant resources must produce appropriate telemetry.

### 8. Infrastructure Should Be Reproducible

Architecture should increasingly be represented through version-controlled
code.

### 9. Security Controls Must Have Owners

Controls without ownership, lifecycle, remediation, and exception processes
cannot be considered fully operational.

### 10. Transformation Must Be Incremental

Target-state architecture must provide migration paths for existing workloads.

---

# 19. Phase 0 Engineering Validation

Selected portions of the architecture have been physically validated in the
portfolio lab.

Validated components include:

* Platform management-group hierarchy;
* Landing-Zones management-group hierarchy;
* Connectivity management group;
* Management management group;
* Security management group;
* Production management group;
* Non-Production management group;
* Sandbox management group;
* Legacy management group;
* core platform subscription placement;
* Terraform management of the hierarchy;
* brownfield Terraform import;
* resource reparenting;
* Terraform plan inspection;
* non-destructive reconciliation.

The broader enterprise architecture remains logically modeled and will be
validated selectively as later transformation phases are implemented.

---

# 20. Phase 1 Design Inputs

Phase 0 does not prescribe the complete target architecture.

It establishes the requirements that Phase 1 must address.

Phase 1 — Azure Landing Zone must evaluate:

* management-group responsibilities;
* subscription vending and lifecycle;
* platform subscription boundaries;
* workload landing-zone patterns;
* policy inheritance boundaries;
* platform ownership;
* resource organization;
* naming and tagging requirements;
* deployment standards;
* environment separation;
* migration paths for existing subscriptions;
* integration with later identity, network, governance, and security controls.

Later phases will address domain-specific transformation.

```text
Phase 0 — Enterprise Assessment
          │
          ▼
Phase 1 — Azure Landing Zone
          │
          ▼
Phase 2 — Cloud Governance
          │
          ▼
Phase 3 — Zero Trust Identity
          │
          ▼
Phase 4 — Network Modernization
          │
          ▼
Phase 5 — Security Operations
          │
          ▼
Phase 6 — DevSecOps
          │
          ▼
Phase 7 — Data Protection
          │
          ▼
Phase 8 — AI Security
```

---

# 21. Conclusion

AFG Enterprises possesses many of the technologies required for a mature
Azure security architecture.

The principal architectural challenge is that those capabilities do not yet
operate as a consistently governed system.

Identity, networking, governance, monitoring, security operations, data
protection, and deployment automation have matured at different rates.

The result is an environment in which modern architectural patterns coexist
with legacy practices and inconsistent control enforcement.

The transformation therefore should not begin by replacing technology.

It should begin by creating a consistent architectural system around the
technology already present.

Phase 0 establishes that baseline.

Phase 1 will use this assessment to design the Azure Landing Zone foundation
upon which subsequent governance, identity, network, security operations,
DevSecOps, data-protection, and AI-security improvements can be implemented.

````
