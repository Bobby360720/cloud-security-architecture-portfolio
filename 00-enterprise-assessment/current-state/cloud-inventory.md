# Cloud Inventory

> **Portfolio note:** This inventory is fictionalized and sanitized for the AFG Enterprises Cloud Security Architecture Portfolio. Names, counts, identifiers, addresses, and operational details are representative only and do not describe a real production environment.

## Purpose

This document provides a current-state inventory of the AFG Enterprises Azure estate during **Phase 0 — Enterprise Assessment**.

The goal is to establish:

- what cloud assets exist;
- where they are located;
- who owns them;
- how they are grouped;
- which services are security-relevant;
- where governance gaps exist;
- which areas require deeper assessment in later phases.

This inventory is intentionally architecture-focused rather than exhaustive. It is designed to support risk identification, governance planning, and target-state design.

---

## Executive Summary

AFG Enterprises operates a hybrid Azure environment with workloads distributed across production, non-production, security, shared services, networking, and sandbox subscriptions.

The environment has grown organically and includes a mix of newer cloud-native services and legacy workloads.

### Current-State Highlights

| Area | Current State |
|---|---|
| Azure tenants | 1 |
| Management groups | 6 |
| Azure subscriptions | 12 |
| Azure regions in use | 4 |
| Azure VMs | 38 |
| Azure Arc-enabled servers | 214 |
| Storage accounts | 67 |
| Key Vaults | 18 |
| App Services | 24 |
| Function Apps | 16 |
| SQL resources | 19 |
| VNets | 31 |
| Private Endpoints | 42 |
| Public IP addresses | 27 |
| Log Analytics workspaces | 8 |
| Microsoft Sentinel workspaces | 2 |
| Defender for Cloud | Partially standardized |
| Azure Policy assignments | 74 |
| Application registrations | 146 |
| Managed identities | 91 |

### Primary Inventory Concerns

- subscription ownership is inconsistently documented;
- management-group placement does not fully reflect business criticality;
- tagging coverage is incomplete;
- public exposure exists across several workloads;
- diagnostic settings are inconsistent;
- workload identity ownership is uneven;
- security controls vary by subscription;
- some resources remain dependent on manual configuration;
- legacy and cloud-native workloads follow different operational standards.

---

# 1. Tenant and Management Group Inventory

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

## Current Management Group Hierarchy

```text
Tenant Root
│
├── Platform
│   ├── Connectivity
│   ├── Management
│   └── Security
│
├── Landing-Zones
│   ├── Production
│   └── Non-Production
│
├── Sandbox
│
└── Legacy
```

### Current-State Observations

- The hierarchy exists but is not consistently used as the primary governance boundary.
- Several older subscriptions remain under transitional or legacy placement.
- Policy assignment exists at multiple scopes, increasing the risk of duplication.
- Production and non-production separation is improving but not yet fully normalized.
- Subscription onboarding is not yet completely automated.

---

# 2. Subscription Inventory

| Subscription | Purpose | Environment | Criticality | Primary Owner | Management Group | Governance Status |
|---|---|---|---|---|---|---|
| sub-prod-apps-01 | Enterprise applications | Production | Tier 1 | Application Platform | Production | Partial |
| sub-prod-apps-02 | Business applications | Production | Tier 1 | Application Platform | Production | Partial |
| sub-prod-data-01 | Data services | Production | Tier 1 | Data Platform | Production | Developing |
| sub-nonprod-apps-01 | Development/test | Non-Production | Tier 3 | Application Platform | Non-Production | Partial |
| sub-nonprod-data-01 | Data development | Non-Production | Tier 3 | Data Platform | Non-Production | Developing |
| sub-connectivity-01 | Hub networking | Platform | Tier 1 | Network Engineering | Connectivity | Strong |
| sub-management-01 | Monitoring/automation | Platform | Tier 1 | Cloud Platform | Management | Strong |
| sub-security-01 | Security tooling | Platform | Tier 1 | Security Engineering | Security | Strong |
| sub-shared-services-01 | Shared infrastructure | Platform | Tier 2 | Cloud Platform | Platform | Partial |
| sub-sandbox-01 | Engineering sandbox | Sandbox | Tier 4 | Cloud Platform | Sandbox | Limited |
| sub-legacy-01 | Legacy migrated workloads | Legacy | Tier 2 | Infrastructure | Legacy | Weak |
| sub-dr-01 | Recovery services | Production support | Tier 1 | Cloud Platform | Production | Partial |

### Key Findings

- Two subscriptions do not have clearly defined secondary owners.
- Legacy subscription governance is materially weaker than the modern platform subscriptions.
- Business criticality is not consistently reflected in metadata.
- Several policy assignments are duplicated at subscription scope.
- Sandbox controls are intentionally lighter but require clearer boundaries.

---

# 3. Regional Footprint

| Azure Region | Primary Usage | Approx. Share | Notes |
|---|---|---:|---|
| Central US | Primary workload region | 52% | Main application footprint |
| East US 2 | Secondary workload region | 28% | Secondary production and SaaS integration |
| West US 3 | Engineering / test | 14% | Non-production and lab workloads |
| South Central US | DR / specialized services | 6% | Recovery and limited legacy usage |

### Governance Concerns

- Not all subscriptions enforce approved-region policy.
- Some legacy resources exist outside preferred deployment patterns.
- Region selection is not consistently tied to documented resilience requirements.

---

# 4. Compute Inventory

## Azure Virtual Machines

| Category | Count | Notes |
|---|---:|---|
| Windows Server | 24 | Mix of application and utility servers |
| Linux | 14 | Primarily application and integration workloads |
| Total Azure VMs | 38 | Includes production and non-production |

### VM Governance Observations

- Patch orchestration is inconsistent across legacy workloads.
- Some VMs use locally managed configuration.
- Managed identity adoption is incomplete.
- Backup coverage is high but not universal.
- Diagnostic settings are not standardized across all VMs.

## Azure Arc-Enabled Servers

| Category | Count |
|---|---:|
| Windows | 182 |
| Linux | 32 |
| Total Arc-enabled servers | 214 |

### Arc Observations

- Arc onboarding is broad but governance maturity varies.
- Azure Monitor Agent coverage is high.
- DCR association requires normalization.
- Tagging quality differs between Azure-native and Arc-enabled resources.
- Some Arc servers lack clear application ownership metadata.

---

# 5. Platform-as-a-Service Inventory

| Resource Type | Count | Security Notes |
|---|---:|---|
| App Services | 24 | Mixed private/public exposure |
| Function Apps | 16 | Several still use app secrets |
| API Management instances | 3 | Central API gateway pattern emerging |
| Logic Apps | 21 | Identity and connector review required |
| Container Apps | 6 | Newer platform pattern |
| AKS clusters | 2 | Requires dedicated workload security review |

### Primary Concerns

- Public network access varies by application.
- Authentication patterns are not fully standardized.
- Some applications still rely on client secrets.
- Private endpoint adoption is incomplete.
- Diagnostic settings differ across services.

---

# 6. Data and Storage Inventory

## Storage

| Resource Type | Count | Notes |
|---|---:|---|
| Storage accounts | 67 | Mixed workload and platform usage |
| Data Lake Storage Gen2 | 8 | Data platform workloads |
| File shares | 19 | Application and legacy integration |
| Blob-heavy accounts | 31 | Application/document storage |

### Storage Governance Concerns

- Public access is disabled on most but not all accounts.
- Private endpoint adoption varies.
- Data classification is incomplete.
- Retention standards differ between business units.
- Some accounts lack clear data-owner metadata.

## Databases

| Resource Type | Count |
|---|---:|
| Azure SQL Databases | 13 |
| SQL Managed Instances | 3 |
| Cosmos DB accounts | 3 |
| Total database platforms | 19 |

### Database Concerns

- Classification maturity varies.
- Key ownership is not consistently documented.
- Network access patterns differ by workload generation.
- Non-production data handling requires stronger governance.

---

# 7. Key Management and Secrets

| Resource Type | Count |
|---|---:|
| Key Vaults | 18 |
| Managed HSM | 1 |
| Managed identities | 91 |
| Application registrations | 146 |
| Enterprise applications | 173 |

### Key and Credential Findings

- Managed identity adoption is increasing but not universal.
- Several application registrations still use client secrets.
- Secret expiration ownership is inconsistently documented.
- Some application registrations have no clearly documented business owner.
- Permission reviews are not performed on a uniform lifecycle.
- High-privilege API permissions require deeper assessment.

---

# 8. Network Inventory

| Resource Type | Count |
|---|---:|
| Virtual Networks | 31 |
| Subnets | 146 |
| Network Security Groups | 118 |
| Azure Firewalls | 2 |
| Application Gateways | 4 |
| Load Balancers | 6 |
| Private Endpoints | 42 |
| Public IP addresses | 27 |
| ExpressRoute circuits | 4 |
| Private DNS zones | 36 |

### Current-State Network Model

AFG uses a hybrid hub-and-spoke design, but implementation maturity varies by subscription.

### Network Governance Concerns

- Some workloads remain directly exposed to the internet.
- Private endpoint use is inconsistent.
- NSG rules require normalization and ownership review.
- DNS governance is centralized only for newer workloads.
- Egress-control standards are incomplete.
- Legacy subscriptions contain network patterns that do not align with current standards.

---

# 9. Security Operations Inventory

## Microsoft Sentinel

| Item | Count |
|---|---:|
| Sentinel-enabled workspaces | 2 |
| Analytics rules | 96 |
| Automation rules | 18 |
| Workbooks | 12 |
| Watchlists | 9 |

## Microsoft Defender for Cloud

| Capability | Status |
|---|---|
| CSPM | Enabled |
| Defender for Servers | Broad coverage |
| Defender for Storage | Partial |
| Defender for SQL | Enabled for critical workloads |
| Defender for Key Vault | Partial |
| Defender for Containers | Limited |
| Regulatory compliance dashboard | Enabled |

### Security Operations Concerns

- Centralized monitoring exists but coverage differs by data source.
- Detection ownership is not consistently recorded.
- Analytics-rule lifecycle management is developing.
- Defender plan coverage is inconsistent across subscriptions.
- Recommendations are not always tied to remediation owners.

---

# 10. Monitoring and Logging Inventory

| Capability | Count / Status |
|---|---|
| Log Analytics workspaces | 8 |
| Azure Monitor Agent | Broad deployment |
| Data Collection Rules | 23 |
| Diagnostic Settings | Inconsistent |
| Activity Logs forwarded | Majority of subscriptions |
| Entra logs forwarded | Yes |
| NSG flow telemetry | Partial |
| Key Vault auditing | Majority |
| PaaS diagnostic coverage | Partial |

### Primary Logging Gaps

- not all security-relevant resources use standard diagnostic settings;
- DCR associations are inconsistent;
- retention varies across workspaces;
- some legacy resources lack complete telemetry;
- centralized standards exist conceptually but are not universally enforced.

---

# 11. Governance and Policy Inventory

| Item | Count |
|---|---:|
| Azure Policy assignments | 74 |
| Custom policy definitions | 29 |
| Policy initiatives | 11 |
| Management-group assignments | 31 |
| Subscription-level assignments | 43 |

### Policy Areas Currently Covered

- tagging;
- allowed regions;
- storage security;
- TLS requirements;
- network controls;
- Key Vault configuration;
- diagnostics;
- managed identities;
- Defender configuration;
- resource restrictions.

### Governance Concerns

- assignments exist at overlapping scopes;
- several policies remain permanently in Audit;
- exception handling is not standardized;
- ownership of some custom policies is unclear;
- remediation tasks are not consistently tracked;
- policy code is not yet universally managed through CI/CD.

---

# 12. Identity and Access Inventory

| Area | Current State |
|---|---|
| Entra ID | Central identity provider |
| Group-based RBAC | Common but not universal |
| PIM | Available and partially adopted |
| Access Reviews | Selective usage |
| Conditional Access | Broadly deployed |
| Break-glass accounts | Present |
| Workload identities | Mixed maturity |
| Entitlement management | Early adoption |

### Identity Governance Concerns

- some privileged roles remain standing assignments;
- direct user RBAC assignments still exist;
- workload-identity ownership is incomplete;
- access reviews are not consistent across all privileged groups;
- entitlement lifecycle management is not yet the default access model.

---

# 13. Resource Tagging and Ownership

## Target Enterprise Tags

| Tag | Purpose |
|---|---|
| `Environment` | Production / NonProduction / Sandbox |
| `Application` | Workload or service name |
| `Owner` | Responsible technical owner |
| `BusinessUnit` | Business organizational owner |
| `CostCenter` | Financial accountability |
| `Criticality` | Tier 1–4 |
| `DataClassification` | Public / Internal / Confidential / Restricted |
| `ManagedBy` | Platform / Application / Security / Network |

## Current Tagging Coverage

| Area | Estimated Coverage |
|---|---:|
| Environment | 91% |
| Application | 76% |
| Owner | 63% |
| Business Unit | 69% |
| Cost Center | 72% |
| Criticality | 41% |
| Data Classification | 27% |

### Key Finding

Tagging currently supports cost and operational use cases better than security-governance use cases.

---

# 14. Backup and Resilience Inventory

| Capability | Current State |
|---|---|
| Recovery Services Vaults | 9 |
| VM backup | Broad |
| SQL backup | Service-native |
| Geo-redundant storage | Selective |
| DR subscription | Present |
| Recovery testing | Inconsistent |
| Documented RTO/RPO | Partial |

### Resilience Governance Concerns

- recovery requirements are not defined consistently for all Tier 1 workloads;
- restoration testing is not performed on a uniform cadence;
- ownership of recovery procedures varies;
- resilience architecture is stronger for infrastructure than for some PaaS workloads.

---

# 15. DevSecOps and Automation Inventory

| Capability | Current State |
|---|---|
| Azure DevOps | Primary engineering platform |
| Git repositories | Established |
| Bicep | Growing adoption |
| Terraform | Selective use |
| CI/CD | Established for application teams |
| Policy as Code | Early maturity |
| IaC security scanning | Partial |
| Secret scanning | Partial |
| Automated compliance gates | Limited |

### Key Findings

- platform configuration is still partly manual;
- pipeline security controls vary by team;
- reusable secure pipeline templates are limited;
- policy and infrastructure deployments need stronger standardization;
- pre-deployment validation is inconsistent.

---

# 16. Data Protection Inventory

| Capability | Current State |
|---|---|
| Encryption at rest | Broadly enabled |
| Encryption in transit | Standard requirement |
| Customer-managed keys | Selective |
| Microsoft Purview | Available |
| DLP | Primarily Microsoft 365 |
| Azure data classification | Developing |
| Retention standards | Business-unit dependent |

### Data Governance Concerns

- cloud resource security cannot always be mapped to data sensitivity;
- data ownership is not uniformly documented;
- customer-managed key requirements are not standardized by classification;
- non-production data handling requires more explicit controls.

---

# 17. AI Workload Inventory

| Item | Current State |
|---|---|
| Approved enterprise AI services | Limited |
| AI proof-of-concepts | Several |
| Azure OpenAI usage | Controlled pilot |
| AI security baseline | Not yet formalized |
| AI threat model | Not standardized |
| Prompt/data handling standard | Developing |

### Primary AI Governance Risks

- sensitive-data leakage;
- unmanaged proofs of concept;
- identity and tool over-permissioning;
- RAG authorization gaps;
- prompt injection;
- incomplete monitoring;
- unclear model and data ownership.

---

# 18. High-Level Current-State Findings

## Critical

1. Privileged and workload identity governance is inconsistent.
2. Security governance controls are not uniformly inherited or enforced.
3. Application credential ownership and lifecycle management require improvement.

## High

4. Public exposure is not consistently governed.
5. Diagnostic and telemetry coverage is incomplete.
6. Policy assignments are fragmented across scopes.
7. Data classification is insufficient for risk-based protection.
8. Configuration remains partly dependent on manual deployment.

## Medium

9. Tagging and ownership metadata are incomplete.
10. Recovery testing is inconsistent.
11. Detection engineering lifecycle management needs formalization.
12. Azure Arc governance differs from Azure-native governance.

---

# 19. Transformation Mapping

| Current-State Gap | Transformation Phase |
|---|---|
| Management-group inconsistency | Phase 1 — Azure Landing Zone |
| Subscription placement | Phase 1 — Azure Landing Zone |
| Policy fragmentation | Phase 2 — Cloud Governance |
| Tagging/ownership | Phase 2 — Cloud Governance |
| Privileged access | Phase 3 — Zero Trust Identity |
| Workload credentials | Phase 3 / Phase 6 |
| Public exposure | Phase 4 — Network Modernization |
| Network segmentation | Phase 4 — Network Modernization |
| Telemetry gaps | Phase 5 — Security Operations |
| Detection lifecycle | Phase 5 — Security Operations |
| Manual deployment | Phase 6 — DevSecOps |
| Policy as Code | Phase 6 — DevSecOps |
| Data classification | Phase 7 — Data Protection |
| DLP/retention | Phase 7 — Data Protection |
| AI governance | Phase 8 — AI Security |

---

# 20. Phase 0 Inventory Conclusion

The inventory confirms that AFG Enterprises has already adopted many Azure security and management capabilities.

The primary challenge is not a lack of technology.

The primary challenge is **consistency, governance, ownership, automation, enforcement, and measurable control effectiveness across the enterprise estate**.

This inventory establishes the baseline for the remaining Phase 0 artifacts:

- current-state architecture;
- security-governance maturity assessment;
- enterprise risk register;
- business/security/technical requirements;
- remediation priorities;
- transformation roadmap.

The next architecture activity is to convert these inventory findings into a prioritized security-governance risk register and target-state requirements.
