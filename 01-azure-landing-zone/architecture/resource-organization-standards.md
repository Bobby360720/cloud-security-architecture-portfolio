# Resource Organization, Naming, Tagging, and Ownership Standards

## Purpose

This document defines the Phase 1 resource-organization standards for the AFG Azure Landing Zone.

The standard establishes consistent rules for:

* Resource organization
* Azure resource naming
* Tagging
* Ownership
* Lifecycle accountability

These standards support the Phase 1 landing-zone architecture without duplicating the detailed governance controls that will be defined in Phase 2.

---

## 1. Design Principles

AFG will use the following organizational principles:

* **Durable Hierarchy:** Management groups represent durable governance and policy-inheritance boundaries.
* **Clear Boundaries:** Subscriptions represent meaningful isolation, ownership, lifecycle, cost, or security boundaries.
* **Operational Grouping:** Resource groups represent deployment and operational-management boundaries.
* **Contextual Naming:** Resource names communicate technical purpose and operational context.
* **Metadata Separation:** Tags provide business and operational metadata but do not provide security isolation.
* **Organizational Decoupling:** Resource organization should remain stable when team names or reporting structures change.
* **Architectural Justification:** New boundaries require an architectural justification rather than preference alone.
* **Pragmatic Brownfield Adoption:** Brownfield resources should be normalized incrementally rather than renamed or rebuilt solely for cosmetic consistency.

---

## 2. Resource Organization Model

AFG organizes Azure resources using the following hierarchy:

```text
Management Group
       ↓
Subscription
       ↓
Resource Group
       ↓
Azure Resource

```

### 2.1 Management Groups

Management groups define enterprise governance boundaries.

**Standard Management Groups:**

* Platform
* Landing-Zones / Corp
* Landing-Zones / Online
* Landing-Zones / Legacy
* Sandbox
* Onboarding
* Decommissioned

Management groups must **not** be created solely for:

* Individual applications
* Individual development teams
* Azure regions
* Temporary projects
* Organizational-chart structure

### 2.2 Subscriptions

A separate subscription requires one or more material architecture drivers.

**Valid Drivers:**

* Distinct ownership
* Workload lifecycle
* Production / non-production separation
* Privileged administration
* Security isolation
* Regulatory or contractual scope
* Network-routing requirements
* Cost accountability
* Azure service limits or quotas
* Blast-radius reduction
* Independent recovery requirements

A separate subscription should **not** be created when the requirement can be adequately satisfied using:

* Resource groups
* Azure Role-Based Access Control (RBAC)
* Azure Policy
* Virtual network controls
* Tags
* Workload-level configuration

### 2.3 Resource Groups

Resource groups should contain resources that share a meaningful operational lifecycle. Resources within a resource group should generally share aligned:

* Ownership
* Deployment lifecycle
* Change management process
* Environment tier
* Application or platform purpose

Resource groups must not be used as substitutes for subscription-level security or governance boundaries.

---

## 3. Naming Standard

Azure resource names should communicate:

1. Resource type
2. Workload or service
3. Environment (where relevant)
4. Region (where operationally useful)
5. Instance or uniqueness identifier (where required)

### General Pattern

```text
<resource-type>-<service>-<environment>-<region>-<instance>

```

> **Note:** Not every resource requires every component.

Names must remain:

* Concise
* Predictable
* Readable
* Automation-friendly
* Independent of individual employee names
* Independent of temporary team structures

---

## 4. Standard Resource Prefixes

| Azure Resource | Prefix | Example |
| --- | --- | --- |
| Resource Group | `rg` | `rg-edm-dev` |
| Virtual Network | `vnet` | `vnet-edm-dev-cus-01` |
| Subnet | `snet` | `snet-app` |
| Network Security Group | `nsg` | `nsg-edm-app-dev` |
| Route Table | `rt` | `rt-edm-dev` |
| Public IP | `pip` | `pip-edm-dev-01` |
| Network Interface | `nic` | `nic-edm-vm-01` |
| Virtual Machine | `vm` | `vm-edm-dev-01` |
| Key Vault | `kv` | `kv-edm-dev-01` |
| Storage Account | `st` | `stedmdev01` |
| Log Analytics Workspace | `law` | `law-platform-sec-01` |
| Application Insights | `appi` | `appi-edm-dev` |
| Function App | `func` | `func-edm-dev-01` |
| App Service Plan | `asp` | `asp-edm-dev-01` |
| Managed Identity | `id` | `id-edm-function-dev` |
| Private Endpoint | `pe` | `pe-edm-kv-dev` |
| Private DNS Zone Link | `pdnslink` | `pdnslink-edm-hub` |

Azure resources with restrictive naming rules (such as Storage Accounts, which disallow hyphens and enforce character limits) may use an abbreviated format while preserving the same naming intent.

---

## 5. Subscription Naming

Target subscription names should communicate purpose rather than generic resource types.

### Examples

* `sub-connectivity-01`
* `sub-management-01`
* `sub-security-01`
* `sub-sandbox-01`
* `sub-prod-digital-services-01`
* `sub-prod-data-platform-01`
* `sub-nonprod-data-platform-01`

Subscription names must not be treated as authoritative evidence of actual workload purpose. Brownfield subscriptions must be assessed based on deployed resources, dependencies, ownership, and lifecycle before placement or renaming.

---

## 6. Resource Group Naming

### Recommended Pattern

```text
rg-<service>-<environment>[-<region>][-<instance>]

```

### Examples

* `rg-edm-dev`
* `rg-digital-services-prod-eus2`
* `rg-data-platform-prod-cus-01`

A resource group should normally represent a workload or platform component with a shared lifecycle.

---

## 7. Tagging Standard

Tags provide business, financial, operational, and lifecycle metadata.

Tags **do not** replace:

* Management-group boundaries
* Subscription boundaries
* Azure RBAC
* Azure Policy
* Network segmentation
* Data-security controls

### 7.1 Baseline Tags

The following tags form the target baseline for supported Azure resources:

| Tag | Purpose |
| --- | --- |
| `Environment` | Identifies lifecycle environment such as `Production`, `NonProduction`, `Sandbox`, or `Shared` |
| `Application` | Identifies the application, platform, or business service |
| `Owner` | Identifies the accountable technical owner or owning group |
| `CostCenter` | Supports financial accountability and chargeback/showback |
| `ManagedBy` | Identifies the management method such as `Terraform`, `PlatformTeam`, or `Manual` |
| `Criticality` | Identifies workload importance or service tier |

### 7.2 Conditional Tags

The following tags are applied when relevant:

| Tag | Purpose |
| --- | --- |
| `DataClassification` | Identifies data sensitivity requirements |
| `BusinessOwner` | Identifies accountable business ownership |
| `Lifecycle` | Identifies `Active`, `Transitional`, `Decommissioning`, or other lifecycle states |
| `Expiry` | Provides an expiration date for temporary resources (`YYYY-MM-DD`) |
| `ComplianceScope` | Identifies applicable regulatory or contractual scope |
| `RecoveryTier` | Identifies recovery requirements where defined |

### 7.3 Temporary and Sandbox Resources

Temporary resources must include sufficient metadata to support automated or routine cleanup:

```ini
Environment = Sandbox
Lifecycle   = Temporary
Expiry      = <defined expiration>
Owner       = <accountable owner>
ManagedBy   = Terraform

```

---

## 8. Ownership Model

Every production or shared-platform subscription must have clear ownership. AFG distinguishes the following ownership roles:

| Role | Accountability |
| --- | --- |
| **Business Owner** | Accountable for business purpose, value, and business risk |
| **Technical Owner** | Accountable for workload operation and technical lifecycle |
| **Platform Owner** | Accountable for shared platform capabilities where applicable |
| **Security Owner** | Accountable for security requirements, exceptions, and security oversight where applicable |
| **Cost Owner** | Accountable for budget, consumption, and financial ownership |

One person or team may fulfill multiple roles where appropriate, but accountability must remain explicit.

---

## 9. Minimum Subscription Metadata

Every active subscription must be able to answer:

1. What business or platform capability does the subscription support?
2. Who is the business owner?
3. Who is the technical owner?
4. What environment does it support?
5. What management group should it inherit governance from?
6. What data sensitivity or compliance requirements apply?
7. What active exceptions exist?
8. Who owns the cost?
9. What is the expected lifecycle?
10. What is the retirement or transition plan?

A subscription that cannot answer these questions represents a governance gap and must be flagged for review.

---

## 10. Brownfield Adoption

Existing brownfield resources are not required to be renamed solely to conform to this standard. AFG prioritizes actions in the following order:

1. Correct governance placement
2. Documented ownership
3. Risk reduction
4. Lifecycle classification
5. Automation and policy compliance
6. Naming normalization where practical

New resources must follow the target standard. Existing resources should be normalized during planned lifecycle events, migrations, modernizations, or redevelopment where the operational benefit justifies the change.

---

## 11. Exceptions

Naming, tagging, or organizational exceptions may be required because of:

* Azure service naming limitations
* Legacy application dependencies
* Vendor requirements
* Migration constraints
* Regulatory requirements
* Temporary transition states

All exceptions must document:

* Requirement being waived
* Reason / justification
* Accountable owner
* Assessed risk
* Compensating control (where required)
* Expected remediation or review date

Detailed exception governance will be addressed in Phase 2.

---

## 12. Validation and Phase Boundary

Phase 1 validates the organizational model and representative implementation.

**Demonstrated Capabilities in Phase 1:**

* Management-group placement
* Subscription placement
* Brownfield classification
* Representative Terraform-managed resources
* Lifecycle boundaries
* Ownership and placement reasoning

Phase 1 does not claim enterprise-wide enforcement of every naming or tagging standard. Azure Policy enforcement, compliance reporting, remediation, exemption governance, and policy-as-code implementation are deferred to Phase 2.

---

## 13. Traceability

### Requirements Supported

* **ALZ-001:** Standardized management-group hierarchy
* **ALZ-002:** Subscription organization
* **ALZ-003:** Platform / workload separation
* **ALZ-007:** Sandbox isolation
* **ALZ-008:** Subscription lifecycle
* **ALZ-010:** Incremental brownfield adoption

### Related Artifacts

* `landing-zone-requirements.md`
* `management-group-subscription-design.md`
* `../decisions/ADR-002-azure-landing-zone-governance-boundary-model.md`
* `../decisions/ADR-003-brownfield-subscription-transition-strategy.md`
* `../evidence/phase1-landing-zone-validation.md`