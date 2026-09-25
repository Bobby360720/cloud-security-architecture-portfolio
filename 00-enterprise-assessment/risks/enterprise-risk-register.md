# Enterprise Risk Register

**Organization:** AFG Enterprises (modeled)  
**Assessment:** Phase 0 — Enterprise Assessment  
**Status:** Baseline documented; modeled risks pending validation  
**Risk IDs:** R-001 through R-015

## Purpose

This register documents the consolidated enterprise architecture risks identified during Phase 0. It establishes the risk baseline used to prioritize and trace the cloud-security transformation.

Detailed assessment findings are maintained separately in the Enterprise Findings Register. Multiple findings may contribute to a single enterprise risk.

The SharePoint Enterprise Risk Register is the operational tracking system. This document is the version-controlled architecture baseline.

## Rating Model

Likelihood and Impact use a scale of 1–5.

**Inherent Risk Score = Likelihood × Impact**

| Score | Rating |
|---|---|
| 20–25 | Critical |
| 15–19 | High |
| 8–14 | Medium |
| 1–7 | Low |

The scores below represent the modeled Phase 0 assessment. They have not been independently validated against a production environment.

## Enterprise Risks

| ID | Risk Statement | L | I | Score | Rating | Treatment | Accountable Team | Phase |
|---|---|---:|---:|---:|---|---|---|---|
| R-001 | Fragmented management-group/policy inheritance causes inconsistent enterprise controls. | 4 | 5 | 20 | Critical | Mitigate | Cloud Platform | 1–2 |
| R-002 | Standing or excessive privilege enables unauthorized high-impact change. | 4 | 5 | 20 | Critical | Mitigate | Identity/Security | 3 |
| R-003 | Long-lived workload credentials or excessive API permissions are compromised or abused. | 4 | 5 | 20 | Critical | Mitigate | App/Identity Security | 3/6 |
| R-004 | Unnecessary public exposure increases attack surface. | 4 | 4 | 16 | High | Mitigate | Network/Workload Owners | 4 |
| R-005 | Incomplete telemetry prevents timely detection or investigation. | 4 | 4 | 16 | High | Mitigate | Security Operations | 5 |
| R-006 | Weak exception lifecycle creates permanent unmanaged security debt. | 4 | 4 | 16 | High | Mitigate | Governance/Security | 2 |
| R-007 | Manual configuration causes drift, inconsistent controls, and weak auditability. | 4 | 4 | 16 | High | Mitigate | Platform Engineering | 6 |
| R-008 | Missing ownership/criticality metadata delays remediation and incident response. | 4 | 4 | 16 | High | Mitigate | Cloud Governance | 2 |
| R-009 | Incomplete data classification leads to insufficient protection of sensitive data. | 3 | 5 | 15 | High | Mitigate | Data Governance | 7 |
| R-010 | Inconsistent recovery testing results in failure to meet business recovery needs. | 3 | 5 | 15 | High | Mitigate | Platform/Workload Owners | 1/5 |
| R-011 | Unmanaged detection lifecycle causes alert gaps, noise, or stale controls. | 3 | 4 | 12 | Medium | Mitigate | Security Operations | 5 |
| R-012 | AI adoption exposes sensitive data or introduces unsafe model/agent behavior. | 3 | 5 | 15 | High | Mitigate | AI Governance/Security | 8 |
| R-013 | Legacy/Arc workloads remain outside modern governance patterns. | 3 | 4 | 12 | Medium | Mitigate | Infrastructure/Platform | 1/2/5 |
| R-014 | Inconsistent Defender coverage leaves preventable security blind spots. | 3 | 4 | 12 | Medium | Mitigate | Security Engineering | 5 |
| R-015 | Non-production environments process production-like data without equivalent safeguards. | 3 | 5 | 15 | High | Mitigate | Data/App Owners | 7 |


## Business Impact and Architecture Dependencies

The following table identifies the modeled assets, business capabilities and architecture dependencies associated with each enterprise risk. These relationships represent the Phase 0 architecture assessment and require validation during the relevant delivery phases.

| Risk ID | Affected Assets | Business Capability | Key Architecture Dependencies |
|---|---|---|---|
| R-001 | Azure management groups, subscriptions, Azure Policy assignments and initiatives | Consistent enterprise governance, secure subscription onboarding and compliance management | Approved management-group hierarchy; subscription placement model; policy inheritance and assignment scopes; baseline enforcement and exception processes |
| R-002 | Microsoft Entra ID, privileged groups, Azure RBAC assignments and PIM | Secure privileged administration, identity governance and protection of critical systems | Privileged role inventory; PIM eligibility and activation; least-privilege RBAC; recurring access reviews; emergency-access procedures |
| R-003 | App registrations, service principals, managed identities, application credentials and API permissions | Secure application authentication, workload integration and service continuity | Workload identity inventory and ownership; managed identity or workload federation; credential lifecycle; API permission governance; secure secrets management |
| R-004 | Public IP addresses, internet-facing workloads, Azure PaaS services, VNets, NSGs and private endpoints | Secure application delivery, protection of externally accessible services and controlled network connectivity | Approved ingress architecture; private endpoint and DNS patterns; network segmentation; egress controls; public exposure policies and exception approval |
| R-005 | Azure resources, Azure Monitor Agent, Data Collection Rules, diagnostic settings, Log Analytics and Microsoft Sentinel | Threat detection, incident investigation, operational monitoring and security reporting | Standardized diagnostic settings; AMA and DCR deployment; log collection architecture; telemetry coverage monitoring; approved retention requirements |
| R-006 | Azure Policy exceptions, governance approvals, control deviations and risk acceptance records | Controlled business exceptions, auditable governance decisions and security debt management | Documented exception workflow; accountable exception owners; defined expiration and review dates; approval authority; compensating controls; residual risk reassessment |
| R-007 | Azure infrastructure, Terraform and Bicep configurations, source repositories, CI/CD pipelines and deployment records | Repeatable infrastructure delivery, change management, operational consistency and auditability | Approved IaC standards; version control; deployment identities; peer review; automated policy and security validation; drift detection and change approval |
| R-008 | Azure resources, resource groups, subscriptions, ownership tags, service inventories and remediation records | Resource accountability, incident response, cost allocation and timely remediation | Approved ownership and criticality metadata; tagging standards; resource inventory; ownership assignment process; compliance monitoring and escalation procedures |
| R-009 | Sensitive data repositories, databases, storage accounts, Microsoft Purview and data-processing workloads | Data protection, regulatory compliance, information governance and secure business operations | Approved classification taxonomy; data ownership; sensitive-data discovery; protection requirements by classification; access controls; retention and lifecycle standards |
| R-010 | Tier 1 workloads, backup repositories, recovery services, databases, application dependencies and disaster recovery infrastructure | Business continuity, service availability and recovery within approved business objectives | Business impact analysis; workload criticality classification; approved RTO/RPO; backup architecture; recovery runbooks; dependency mapping; scheduled recovery testing |
| R-011 | Microsoft Sentinel analytics rules, detection content, automation rules, incident workflows and detection repositories | Reliable threat detection, security operations effectiveness and incident response | Detection ownership; detection-as-code; testing and tuning procedures; change approval; version control; detection performance monitoring; retirement criteria |
| R-012 | AI applications, models, agents, prompts, retrieval systems, connected data sources and AI service identities | Secure AI adoption, protection of enterprise information and controlled AI-enabled business processes | AI use-case inventory; data classification; identity and connector permissions; model and agent security reviews; approved data flows; monitoring; AI governance standards |
| R-013 | Azure Arc-enabled servers, legacy subscriptions, hybrid infrastructure, legacy VNets and associated management tooling | Hybrid operations, legacy workload continuity and phased modernization | Legacy and Arc inventory; management-group placement; policy applicability; Azure Arc onboarding; monitoring coverage; network dependency mapping; phased migration and retirement plans |
| R-014 | Microsoft Defender for Cloud plans, Azure subscriptions, protected servers, databases, storage and other eligible workloads | Threat protection, vulnerability visibility, security posture management and incident response | Approved Defender coverage baseline; subscription-level plan configuration; resource eligibility inventory; onboarding procedures; coverage monitoring; documented exceptions |
| R-015 | Non-production subscriptions, development and test databases, storage accounts, application environments and production-derived datasets | Secure software development, testing, protection of sensitive information and regulatory compliance | Data classification; approved non-production data handling; masking or synthetic-data standards; environment isolation; least-privilege access; encryption; retention and disposal controls |

## Risk-Based Remediation Priorities

Remediation priority considers inherent risk severity,
architecture dependencies, business impact and the
approved delivery sequence.

Critical risks do not automatically receive the earliest
implementation phase when prerequisite architecture
controls must be established first.

| Priority | Risks | Delivery Focus |
|---|---|---|
| Foundation | R-001, R-010, R-013 | Landing zone, governance foundations, resilience and hybrid inventory |
| Governance | R-006, R-008 | Policy exceptions and ownership metadata |
| Identity | R-002, R-003 | Privileged access and workload identity |
| Network | R-004 | Public exposure and network security |
| Security Operations | R-005, R-011, R-014 | Telemetry, detection lifecycle and Defender coverage |
| Engineering | R-007 | Repeatable IaC and deployment controls |
| Data Protection | R-009, R-015 | Classification and non-production data protection |
| AI Security | R-012 | AI security governance and controls |

These groups describe implementation sequencing,
not a replacement for inherent risk ratings.
Critical exposures may require interim mitigation
before their primary delivery phase.

### Validation and Ownership

The affected assets and dependencies are modeled architecture assumptions, not confirmed production inventory. The proposed accountable teams in the Enterprise Risks table are responsible for coordinating validation and treatment planning, subject to formal ownership assignment.

Each delivery phase should verify its applicable assets and dependencies, document the business impact, implement approved treatment controls and retain validation evidence. Changes to the modeled assumptions should be reflected in the operational SharePoint Enterprise Risk Register and the Phase 0 Traceability Matrix.

## Risk Ownership

The Accountable Team column identifies the proposed functional owner of each risk. It does not establish individual ownership or formal risk acceptance.

Individual risk owners will be recorded in the SharePoint Enterprise Risk Register when assigned.

## Relationship to Enterprise Findings

The Enterprise Findings Register maintains detailed assessment findings, including:

- **IAM:** IAM-01 through IAM-07
- **Network:** NET-01 through NET-06
- **Security Operations:** SOC-01 through SOC-07

Each numbered finding retains its own identifier and can reference one or more enterprise risks.

The seven cross-domain architecture candidates remain subject to governance review. They are not automatically treated as additional enterprise risks.

## Residual Risk

Residual scores are not assigned in Phase 0 because treatment controls have not yet been validated.

Each delivery phase will reassess its source risks after implementation and validation evidence exists. Residual likelihood, impact, rating and any formal risk acceptance will be maintained in the operational SharePoint register.

## Architecture Traceability

Enterprise risks are linked to architecture findings, security requirements, technical requirements and delivery phases in the [Phase 0 Traceability Matrix](../assessment/traceability-matrix.md).

Risk IDs R-001 through R-015 are the canonical identifiers for this architecture baseline.
