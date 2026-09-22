# Cloud Inventory

> **Portfolio note:** This inventory is fictionalized and sanitized for the
> AFG Enterprises Cloud Security Architecture Portfolio. Names, counts,
> identifiers, addresses, and operational details are representative only and
> do not describe a real production environment.

---

## Purpose

This document provides the current-state cloud inventory for AFG Enterprises
during **Phase 0 — Enterprise Assessment**.

The purpose of the inventory is to establish:

- what cloud assets exist;
- where they are located;
- who owns them;
- how they are organized;
- which services are security-relevant;
- where governance and operational gaps exist;
- which findings require deeper assessment;
- which findings drive later transformation phases.

This inventory is intentionally architecture-focused rather than an exhaustive
configuration-management database.

It establishes the baseline required for risk identification, architectural
decision-making, governance planning, and target-state design.

---

## Inventory Scope and Representation

This portfolio uses two related but distinct representations of the environment.

### Logical Enterprise Environment

The **logical enterprise environment** represents the complete AFG Enterprises
architecture used throughout the portfolio.

It contains:

- one Microsoft Entra tenant;
- nine management groups below Tenant Root;
- twelve logical Azure subscriptions;
- production and non-production workloads;
- centralized platform services;
- hybrid infrastructure;
- security operations capabilities;
- identity and access services;
- data platforms;
- DevSecOps capabilities;
- legacy workloads;
- emerging AI workloads.

The logical environment is intentionally larger than the physical lab so that
enterprise-scale architecture, governance, security, and operating-model
decisions can be evaluated realistically.

### Physical Architecture Lab

The **physical architecture lab** implements selected portions of the logical
enterprise environment in Azure.

The lab is used to:

- validate architectural decisions;
- test Terraform configurations;
- exercise brownfield adoption patterns;
- validate management-group design;
- test subscription placement;
- implement governance controls;
- validate security architecture patterns;
- produce engineering evidence.

The currently instantiated core platform subscriptions are:

- `sub-connectivity-01`;
- `sub-management-01`;
- `sub-security-01`.

Additional logical subscriptions remain part of the enterprise architecture
without requiring every workload or subscription to remain continuously
deployed.

This allows the portfolio to demonstrate enterprise-scale architecture while
keeping the physical lab financially and operationally sustainable.

---

## Evidence Classification

Inventory information is classified using the following evidence model.

| Classification | Meaning |
|---|---|
| **Observed** | Directly discovered from the physical Azure lab or engineering environment |
| **Modeled** | Part of the fictionalized AFG Enterprises scenario |
| **Validated** | A modeled architecture, configuration, or control that has been implemented and tested in the physical lab |
| **Planned** | A capability identified for implementation or validation in a later transformation phase |

Examples:

| Architecture Element | Evidence Status |
|---|---|
| Management-group hierarchy | Validated |
| Core platform subscription placement | Validated |
| Terraform management-group deployment | Validated |
| Twelve-subscription enterprise model | Modeled |
| Enterprise workload counts | Modeled |
| Azure Landing Zone governance controls | Planned / later-phase validation |
| Zero Trust identity improvements | Planned / later-phase validation |

This distinction prevents the logical enterprise scenario from being
misrepresented as the exact size of the physical lab.

---

# 1. Executive Summary

AFG Enterprises operates a hybrid, Azure-first environment consisting of a
logical twelve-subscription Azure estate organized beneath an enterprise
management-group hierarchy.

The environment has grown over time and contains a combination of:

- cloud-native workloads;
- traditional infrastructure;
- Azure Arc-connected systems;
- centralized platform services;
- security tooling;
- legacy workloads;
- emerging DevSecOps practices;
- developing AI capabilities.

The primary architectural challenge is not the absence of cloud or security
technology.

The challenge is achieving consistent:

- governance;
- ownership;
- identity controls;
- network controls;
- telemetry;
- automation;
- policy enforcement;
- data protection;
- lifecycle management;
- measurable control effectiveness.

## Current-State Highlights

| Area | Current State | Evidence |
|---|---:|---|
| Azure tenants | 1 | Modeled |
| Management groups below Tenant Root | 9 | Validated structure |
| Logical Azure subscriptions | 12 | Modeled |
| Core physical lab subscriptions | 3 | Validated |
| Azure regions in enterprise model | 4 | Modeled |
| Azure VMs | 38 | Modeled |
| Azure Arc-enabled servers | 214 | Modeled |
| Storage accounts | 67 | Modeled |
| Key Vaults | 18 | Modeled |
| App Services | 24 | Modeled |
| Function Apps | 16 | Modeled |
| SQL resources | 19 | Modeled |
| VNets | 31 | Modeled |
| Private Endpoints | 42 | Modeled |
| Public IP addresses | 27 | Modeled |
| Log Analytics workspaces | 8 | Modeled |
| Microsoft Sentinel workspaces | 2 | Modeled |
| Defender for Cloud | Partially standardized | Modeled |
| Azure Policy assignments | 74 | Modeled |
| Application registrations | 146 | Modeled |
| Managed identities | 91 | Modeled |

## Primary Inventory Concerns

- subscription ownership is inconsistently documented;
- secondary ownership is not consistently defined;
- governance maturity varies across workload classes;
- tagging coverage is incomplete;
- public exposure exists across several workloads;
- diagnostic settings are inconsistent;
- workload identity ownership is uneven;
- security controls vary by subscription;
- some resources remain dependent on manual configuration;
- legacy and cloud-native workloads follow different operational standards;
- policy assignments exist at overlapping scopes;
- enterprise controls are not consistently inherited.

---

# 2. Tenant and Management-Group Inventory

## Azure Tenant

| Attribute | Value |
|---|---|
| Tenant name | AFG Enterprises |
| Tenant type | Enterprise |
| Primary identity provider | Microsoft Entra ID |
| Cloud operating model | Hybrid / Azure-first |
| Primary productivity platform | Microsoft 365 |
| Primary SIEM | Microsoft Sentinel |
| Primary CSPM/CWPP | Microsoft Defender for Cloud |

## Current-State Management-Group Hierarchy

```text
Tenant Root Group
│
├── Platform
│   │
│   ├── Connectivity
│   │   └── sub-connectivity-01
│   │
│   ├── Management
│   │   └── sub-management-01
│   │
│   ├── Security
│   │   └── sub-security-01
│   │
│   └── sub-shared-services-01
│
└── Landing-Zones
    │
    ├── Production
    │   ├── sub-prod-apps-01
    │   ├── sub-prod-apps-02
    │   ├── sub-prod-data-01
    │   └── sub-dr-01
    │
    ├── Non-Production
    │   ├── sub-nonprod-apps-01
    │   └── sub-nonprod-data-01
    │
    ├── Sandbox
    │   └── sub-sandbox-01
    │
    └── Legacy
        └── sub-legacy-01
````

### Architectural Boundary

Tenant Root is treated as an existing tenant-level boundary and is not created
or lifecycle-managed by the Phase 0 Terraform configuration.

Terraform manages the portfolio hierarchy beneath that boundary.

This establishes a deliberate separation between:

* tenant ownership;
* platform organization;
* workload landing zones;
* Terraform-managed architecture.

---

# 3. Brownfield Reconstruction

Phase 0 treats the environment as a **brownfield architecture**, rather than
assuming that Terraform created every existing Azure resource.

During Terraform adoption, several management groups already existed in Azure
but were not represented in Terraform state.

The reconstruction process therefore followed this sequence:

```text
Discover Existing Environment
        │
        ▼
Compare Azure with Terraform State
        │
        ▼
Identify Existing Unmanaged Resources
        │
        ▼
Import Existing Management Groups
        │
        ▼
Generate Terraform Plan
        │
        ▼
Inspect Proposed Changes
        │
        ▼
Reconcile Configuration with Existing IDs
        │
        ▼
Reparent Existing Resources Where Required
        │
        ▼
Associate Platform Subscriptions
        │
        ▼
Validate Desired State
```

## Key Engineering Finding

Initial Terraform planning identified potential resource replacement caused by
differences between existing immutable management-group identifiers and
normalized identifiers originally represented in configuration.

Rather than destroying and recreating those resources, the Terraform
configuration was reconciled with the existing Azure identifiers.

Existing management groups were imported and preserved.

Production, Non-Production, and Sandbox were reparented beneath
`Landing-Zones`.

Connectivity and Management were established beneath `Platform`, alongside
Security.

The physical platform subscriptions were then associated with their respective
management groups.

This demonstrates an important brownfield architecture principle:

> Existing infrastructure should be discovered, understood, and reconciled
> before destructive normalization is considered.

Terraform planning was used as an architectural validation control rather than
simply as a deployment mechanism.

---

# 4. Subscription Inventory

## Logical Enterprise Subscription Model

| Subscription             | Purpose                 | Environment        | Criticality | Primary Owner        | Management Group | Governance |
| ------------------------ | ----------------------- | ------------------ | ----------- | -------------------- | ---------------- | ---------- |
| `sub-prod-apps-01`       | Enterprise applications | Production         | Tier 1      | Application Platform | Production       | Partial    |
| `sub-prod-apps-02`       | Business applications   | Production         | Tier 1      | Application Platform | Production       | Partial    |
| `sub-prod-data-01`       | Data services           | Production         | Tier 1      | Data Platform        | Production       | Developing |
| `sub-dr-01`              | Recovery services       | Production Support | Tier 1      | Cloud Platform       | Production       | Partial    |
| `sub-nonprod-apps-01`    | Development/test        | Non-Production     | Tier 3      | Application Platform | Non-Production   | Partial    |
| `sub-nonprod-data-01`    | Data development        | Non-Production     | Tier 3      | Data Platform        | Non-Production   | Developing |
| `sub-connectivity-01`    | Hub networking          | Platform           | Tier 1      | Network Engineering  | Connectivity     | Strong     |
| `sub-management-01`      | Monitoring/automation   | Platform           | Tier 1      | Cloud Platform       | Management       | Strong     |
| `sub-security-01`        | Security tooling        | Platform           | Tier 1      | Security Engineering | Security         | Strong     |
| `sub-shared-services-01` | Shared infrastructure   | Platform           | Tier 2      | Cloud Platform       | Platform         | Partial    |
| `sub-sandbox-01`         | Engineering sandbox     | Sandbox            | Tier 4      | Cloud Platform       | Sandbox          | Limited    |
| `sub-legacy-01`          | Legacy workloads        | Legacy             | Tier 2      | Infrastructure       | Legacy           | Weak       |

## Physical Lab Implementation

The physical lab currently validates the three core platform subscriptions:

```text
Platform
├── Connectivity
│   └── sub-connectivity-01
│
├── Management
│   └── sub-management-01
│
└── Security
    └── sub-security-01
```

These subscriptions validate the organizational architecture without requiring
all twelve logical enterprise subscriptions to be physically maintained.

## Subscription Findings

* No logical subscription currently tracks a standardized secondary owner.
* Tier 1 workloads require stronger continuity-of-ownership requirements.
* Legacy governance is weaker than the modern platform model.
* Business criticality is not consistently reflected in resource metadata.
* Policy assignments exist at overlapping scopes.
* Sandbox controls require explicit boundaries.
* Subscription placement should support policy inheritance rather than
  subscription-by-subscription control duplication.

---

# 5. Regional Footprint

| Azure Region     | Primary Usage             | Approx. Share | Notes                                     |
| ---------------- | ------------------------- | ------------: | ----------------------------------------- |
| Central US       | Primary workload region   |           52% | Main application footprint                |
| East US 2        | Secondary workload region |           28% | Secondary production and SaaS integration |
| West US 3        | Engineering/test          |           14% | Non-production and lab workloads          |
| South Central US | DR/specialized services   |            6% | Recovery and limited legacy usage         |

## Governance Concerns

* approved-region policy is not universally enforced;
* some legacy resources exist outside preferred deployment patterns;
* region selection is not consistently tied to documented resilience
  requirements.

---

# 6. Compute Inventory

## Azure Virtual Machines

| Category       |  Count | Notes                                           |
| -------------- | -----: | ----------------------------------------------- |
| Windows Server |     24 | Application and utility servers                 |
| Linux          |     14 | Primarily application and integration workloads |
| **Total**      | **38** | Production and non-production                   |

### VM Governance Observations

* patch orchestration is inconsistent across legacy workloads;
* some VMs use locally managed configuration;
* managed identity adoption is incomplete;
* backup coverage is high but not universal;
* diagnostic settings are not standardized.

## Azure Arc-Enabled Servers

| Category  |   Count |
| --------- | ------: |
| Windows   |     182 |
| Linux     |      32 |
| **Total** | **214** |

### Arc Observations

* Arc onboarding is broad;
* governance maturity varies;
* Azure Monitor Agent coverage is high;
* Data Collection Rule association requires normalization;
* tagging quality differs between Azure-native and Arc-enabled resources;
* some Arc servers lack clear application ownership metadata.

---

# 7. Platform-as-a-Service Inventory

| Resource Type  | Count | Security Observation                            |
| -------------- | ----: | ----------------------------------------------- |
| App Services   |    24 | Mixed private/public exposure                   |
| Function Apps  |    16 | Some workloads still use application secrets    |
| API Management |     3 | Central gateway pattern emerging                |
| Logic Apps     |    21 | Identity and connector review required          |
| Container Apps |     6 | Emerging platform pattern                       |
| AKS clusters   |     2 | Dedicated workload security assessment required |

## Primary Concerns

* public network access varies by workload;
* authentication patterns are inconsistent;
* client secrets remain in use;
* private endpoint adoption is incomplete;
* diagnostic configuration varies by service.

---

# 8. Data and Storage Inventory

## Storage

| Resource Type          | Count | Notes                              |
| ---------------------- | ----: | ---------------------------------- |
| Storage accounts       |    67 | Mixed workload/platform usage      |
| Data Lake Storage Gen2 |     8 | Data-platform workloads            |
| File shares            |    19 | Application and legacy integration |
| Blob-heavy accounts    |    31 | Application/document storage       |

### Storage Governance Concerns

* public access is disabled on most but not all accounts;
* private endpoint adoption varies;
* data classification is incomplete;
* retention standards differ;
* some resources lack clearly identified data owners.

## Databases

| Resource Type                |  Count |
| ---------------------------- | -----: |
| Azure SQL Databases          |     13 |
| SQL Managed Instances        |      3 |
| Cosmos DB accounts           |      3 |
| **Total database platforms** | **19** |

### Database Concerns

* classification maturity varies;
* key ownership is inconsistently documented;
* network access patterns differ by workload generation;
* non-production data handling requires stronger governance.

---

# 9. Key Management and Workload Identity

| Resource Type             | Count |
| ------------------------- | ----: |
| Key Vaults                |    18 |
| Managed HSM               |     1 |
| Managed identities        |    91 |
| Application registrations |   146 |
| Enterprise applications   |   173 |

## Findings

* managed identity adoption is increasing but not universal;
* several application registrations still use client secrets;
* credential-expiration ownership is inconsistent;
* some applications lack clearly documented business owners;
* permission reviews do not follow a uniform lifecycle;
* high-privilege API permissions require deeper assessment.

---

# 10. Network Inventory

| Resource Type           | Count |
| ----------------------- | ----: |
| Virtual Networks        |    31 |
| Subnets                 |   146 |
| Network Security Groups |   118 |
| Azure Firewalls         |     2 |
| Application Gateways    |     4 |
| Load Balancers          |     6 |
| Private Endpoints       |    42 |
| Public IP addresses     |    27 |
| ExpressRoute circuits   |     4 |
| Private DNS zones       |    36 |

## Current-State Network Model

AFG uses a hybrid hub-and-spoke networking model, but implementation maturity
varies by workload and subscription.

## Network Governance Concerns

* some workloads remain directly exposed to the internet;
* private endpoint use is inconsistent;
* NSG rules require normalization and ownership review;
* DNS governance is centralized primarily for newer workloads;
* egress-control standards are incomplete;
* legacy network patterns do not consistently align with modern standards.

---

# 11. Security Operations Inventory

## Microsoft Sentinel

| Item                        | Count |
| --------------------------- | ----: |
| Sentinel-enabled workspaces |     2 |
| Analytics rules             |    96 |
| Automation rules            |    18 |
| Workbooks                   |    12 |
| Watchlists                  |     9 |

## Microsoft Defender for Cloud

| Capability                      | Status             |
| ------------------------------- | ------------------ |
| CSPM                            | Enabled            |
| Defender for Servers            | Broad coverage     |
| Defender for Storage            | Partial            |
| Defender for SQL                | Critical workloads |
| Defender for Key Vault          | Partial            |
| Defender for Containers         | Limited            |
| Regulatory compliance dashboard | Enabled            |

## Security Operations Concerns

* monitoring coverage differs by data source;
* detection ownership is inconsistently recorded;
* analytics-rule lifecycle management is developing;
* Defender coverage varies across subscriptions;
* recommendations are not consistently tied to remediation owners.

---

# 12. Monitoring and Logging Inventory

| Capability               | Count / Status            |
| ------------------------ | ------------------------- |
| Log Analytics workspaces | 8                         |
| Azure Monitor Agent      | Broad deployment          |
| Data Collection Rules    | 23                        |
| Diagnostic Settings      | Inconsistent              |
| Activity Logs forwarded  | Majority of subscriptions |
| Entra logs forwarded     | Yes                       |
| NSG flow telemetry       | Partial                   |
| Key Vault auditing       | Majority                  |
| PaaS diagnostic coverage | Partial                   |

## Primary Logging Gaps

* diagnostic settings are not standardized;
* DCR associations are inconsistent;
* retention varies across workspaces;
* some legacy resources lack complete telemetry;
* centralized standards are not universally enforced.

---

# 13. Governance and Policy Inventory

| Item                           | Count |
| ------------------------------ | ----: |
| Azure Policy assignments       |    74 |
| Custom policy definitions      |    29 |
| Policy initiatives             |    11 |
| Management-group assignments   |    31 |
| Subscription-level assignments |    43 |

## Existing Policy Areas

* tagging;
* allowed regions;
* storage security;
* TLS requirements;
* network controls;
* Key Vault configuration;
* diagnostics;
* managed identities;
* Defender configuration;
* resource restrictions.

## Governance Concerns

* assignments exist at overlapping scopes;
* several policies remain permanently in Audit;
* exception handling is not standardized;
* ownership of some custom policies is unclear;
* remediation tasks are inconsistently tracked;
* policy code is not universally managed through CI/CD.

---

# 14. Identity and Access Inventory

| Area                           | Current State                 |
| ------------------------------ | ----------------------------- |
| Microsoft Entra ID             | Central identity provider     |
| Group-based RBAC               | Common but not universal      |
| Privileged Identity Management | Available / partially adopted |
| Access Reviews                 | Selective                     |
| Conditional Access             | Broadly deployed              |
| Emergency-access accounts      | Present                       |
| Workload identities            | Mixed maturity                |
| Entitlement Management         | Early adoption                |

## Identity Governance Concerns

* some privileged roles remain standing assignments;
* direct user RBAC assignments exist;
* workload identity ownership is incomplete;
* access reviews are inconsistent across privileged groups;
* entitlement lifecycle management is not the default access model.

---

# 15. Resource Tagging and Ownership

## Target Enterprise Tags

| Tag                  | Purpose                                       |
| -------------------- | --------------------------------------------- |
| `Environment`        | Production / NonProduction / Sandbox          |
| `Application`        | Workload or service                           |
| `Owner`              | Responsible technical owner                   |
| `BusinessUnit`       | Organizational owner                          |
| `CostCenter`         | Financial accountability                      |
| `Criticality`        | Tier 1–4                                      |
| `DataClassification` | Public / Internal / Confidential / Restricted |
| `ManagedBy`          | Platform / Application / Security / Network   |

## Current Tagging Coverage

| Area                | Estimated Coverage |
| ------------------- | -----------------: |
| Environment         |                91% |
| Application         |                76% |
| Owner               |                63% |
| Business Unit       |                69% |
| Cost Center         |                72% |
| Criticality         |                41% |
| Data Classification |                27% |

### Finding

Tagging currently supports financial and operational requirements more
effectively than security-governance requirements.

---

# 16. Backup and Resilience Inventory

| Capability               | Current State  |
| ------------------------ | -------------- |
| Recovery Services Vaults | 9              |
| VM backup                | Broad          |
| SQL backup               | Service-native |
| Geo-redundant storage    | Selective      |
| DR subscription          | Present        |
| Recovery testing         | Inconsistent   |
| Documented RTO/RPO       | Partial        |

## Resilience Concerns

* recovery requirements are inconsistent for Tier 1 workloads;
* restoration testing does not follow a uniform cadence;
* recovery-procedure ownership varies;
* resilience maturity is stronger for infrastructure than for some PaaS
  workloads.

---

# 17. DevSecOps and Automation Inventory

| Capability                 | Current State                     |
| -------------------------- | --------------------------------- |
| Azure DevOps               | Primary engineering platform      |
| Git repositories           | Established                       |
| Bicep                      | Growing adoption                  |
| Terraform                  | Selective use                     |
| CI/CD                      | Established for application teams |
| Policy as Code             | Early maturity                    |
| IaC security scanning      | Partial                           |
| Secret scanning            | Partial                           |
| Automated compliance gates | Limited                           |

## Findings

* platform configuration remains partly manual;
* pipeline controls vary by team;
* reusable secure pipeline templates are limited;
* policy and infrastructure deployment require stronger standardization;
* pre-deployment validation is inconsistent.

---

# 18. Data Protection Inventory

| Capability                | Current State           |
| ------------------------- | ----------------------- |
| Encryption at rest        | Broadly enabled         |
| Encryption in transit     | Standard requirement    |
| Customer-managed keys     | Selective               |
| Microsoft Purview         | Available               |
| DLP                       | Primarily Microsoft 365 |
| Azure data classification | Developing              |
| Retention standards       | Business-unit dependent |

## Data Governance Concerns

* cloud security controls cannot always be mapped to data sensitivity;
* data ownership is not uniformly documented;
* customer-managed-key requirements are not standardized by classification;
* non-production data requires more explicit controls.

---

# 19. AI Workload Inventory

| Item                            | Current State    |
| ------------------------------- | ---------------- |
| Approved enterprise AI services | Limited          |
| AI proof-of-concepts            | Several          |
| Azure OpenAI usage              | Controlled pilot |
| AI security baseline            | Not formalized   |
| AI threat model                 | Not standardized |
| Prompt/data handling standard   | Developing       |

## Primary AI Governance Risks

* sensitive-data leakage;
* unmanaged proofs of concept;
* identity and tool over-permissioning;
* RAG authorization gaps;
* prompt injection;
* incomplete monitoring;
* unclear model and data ownership.

---

# 20. High-Level Current-State Findings

## Critical

1. Privileged and workload identity governance is inconsistent.
2. Security governance controls are not uniformly inherited or enforced.
3. Application credential ownership and lifecycle management require
   improvement.

## High

4. Public exposure is not consistently governed.
5. Diagnostic and telemetry coverage is incomplete.
6. Policy assignments are fragmented across scopes.
7. Data classification is insufficient for risk-based protection.
8. Configuration remains partly dependent on manual deployment.

## Medium

9. Tagging and ownership metadata are incomplete.
10. Recovery testing is inconsistent.
11. Detection-engineering lifecycle management requires formalization.
12. Azure Arc governance differs from Azure-native governance.

---

# 21. Transformation Traceability

Phase 0 findings provide direct inputs into subsequent transformation phases.

| Current-State Finding                          | Transformation Phase            |
| ---------------------------------------------- | ------------------------------- |
| Management-group and subscription architecture | Phase 1 — Azure Landing Zone    |
| Platform/workload separation                   | Phase 1 — Azure Landing Zone    |
| Policy fragmentation                           | Phase 2 — Cloud Governance      |
| Tagging and ownership                          | Phase 2 — Cloud Governance      |
| Privileged access                              | Phase 3 — Zero Trust Identity   |
| Workload credentials                           | Phase 3 / Phase 6               |
| Public exposure                                | Phase 4 — Network Modernization |
| Network segmentation                           | Phase 4 — Network Modernization |
| Telemetry gaps                                 | Phase 5 — Security Operations   |
| Detection lifecycle                            | Phase 5 — Security Operations   |
| Manual deployment                              | Phase 6 — DevSecOps             |
| Policy as Code                                 | Phase 6 — DevSecOps             |
| Data classification                            | Phase 7 — Data Protection       |
| DLP and retention                              | Phase 7 — Data Protection       |
| AI governance                                  | Phase 8 — AI Security           |

---

# 22. Phase 0 Inventory Conclusion

The inventory demonstrates that AFG Enterprises has already adopted many Azure
security, management, monitoring, and identity capabilities.

The primary challenge is not a lack of technology.

The primary challenge is achieving **consistent governance, ownership,
automation, enforcement, and measurable control effectiveness across the
enterprise estate**.

Phase 0 therefore does not immediately attempt to redesign every identified
weakness.

Instead, it establishes a defensible baseline by:

1. discovering the current environment;
2. documenting the logical enterprise architecture;
3. distinguishing modeled architecture from physically validated components;
4. reconstructing the organizational hierarchy;
5. adopting existing brownfield resources into Terraform where appropriate;
6. validating platform subscription placement;
7. identifying security and governance gaps;
8. establishing traceability between findings and later transformation phases.

The inventory now provides input into the remaining Phase 0 architecture
artifacts:

* current-state architecture assessment;
* identity current-state assessment;
* network current-state assessment;
* security-operations current-state assessment;
* security-governance maturity assessment;
* enterprise risk register;
* business, security, and technical requirements;
* architecture decision records;
* transformation roadmap.

The next architecture activity is to translate these inventory findings into
the broader **current-state architecture assessment**, identifying the
relationships, dependencies, control boundaries, architectural debt, and risks
that will drive the Phase 1 Azure Landing Zone design.

