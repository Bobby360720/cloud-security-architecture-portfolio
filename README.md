# Enterprise Cloud Security Architecture Transformation

**From brownfield assessment to validated enterprise cloud security architecture.**

An evolving, hands-on architecture portfolio demonstrating how to assess, design, engineer, secure and modernize a hybrid enterprise Azure environment.

**Microsoft Azure · Cloud Security Architecture · Zero Trust · Terraform · Cloud Governance · DevSecOps**

**Current status:** Phase 0 — Enterprise Assessment (in progress)

[View current assessment](00-enterprise-assessment/README.md) · [Explore engineering foundation](00-bootstrap/README.md) · [Track progress](../../issues) · [Connect on LinkedIn](https://www.linkedin.com/in/johnhilton1/)

---

## 1. The Architecture Challenge

AFG Enterprises is a fictionalized enterprise with a hybrid Azure environment that has evolved through incremental cloud adoption.

The organization has invested in identity, networking, governance, monitoring and security tooling. However, inconsistent adoption across production, non-production and legacy environments has created architectural debt.

The transformation addresses eight interconnected challenges:

* Fragmented governance and overlapping policy assignments.
* Inconsistent privileged and workload identity management.
* Uneven network segmentation and public exposure.
* Gaps in centralized logging and security telemetry.
* Incomplete ownership and criticality metadata.
* Manual infrastructure configuration and deployment.
* Inconsistent data protection and resilience requirements.
* Emerging AI workloads without standardized security governance.

**The central question:** How do we transform an existing enterprise into a consistently governed, secure and repeatable cloud environment without disrupting business operations?

## 2. Architecture at a Glance

AFG operates a hybrid enterprise architecture connecting on-premises infrastructure to Azure through private connectivity.

The logical architecture separates shared platform services from workload landing zones.

Platform services provide connectivity, management and security capabilities. Landing zones organize production, non-production, sandbox and legacy workloads.

Microsoft Entra ID, Azure Policy, monitoring, security operations and automation operate across these boundaries.

![AFG Enterprises Current-State Architecture](00-enterprise-assessment/diagrams/images/current-state-architecture.png)

### Current-State Architecture

The detailed diagram is maintained in the [Phase 0 architecture documentation](00-enterprise-assessment/current-state/current-state-architecture.md).

The architecture is deliberately assessed as an existing brownfield environment rather than presented as an ideal greenfield deployment.

## 3. Current Transformation Status

| Phase     | Architecture domain    | Status      |
| --------- | ---------------------- | ----------- |
| Bootstrap | Engineering foundation | Complete    |
| 00        | Enterprise Assessment  | In progress |
| 01        | Azure Landing Zone     | Planned     |
| 02        | Cloud Governance       | Planned     |
| 03        | Zero Trust Identity    | Planned     |
| 04        | Network Modernization  | Planned     |
| 05        | Security Operations    | Planned     |
| 06        | DevSecOps              | Planned     |
| 07        | Data Protection        | Planned     |
| 08        | AI Security            | Planned     |
| 09        | DLV FinTech Platform   | Planned     |

**Current focus:** Complete the Phase 0 assessment, document architectural risks and requirements, and establish the baseline for Phase 1.

Progress is tracked through [GitHub Issues](../../issues) and [Milestones](../../milestones). Engineering changes are recorded in the repository's commit history.

## 4. What Has Been Engineered

This portfolio contains both architecture documentation and hands-on implementation.

### Engineering foundation

The initial engineering foundation includes:

* Terraform-based Azure infrastructure deployment.
* Azure Storage remote Terraform state.
* GitHub version control.
* Azure DevOps integration.
* Workload identity federation for Azure authentication.
* Terraform formatting, validation and planning.

### Brownfield architecture reconstruction

Phase 0 has established a Terraform-managed organizational hierarchy with nine management groups beneath Tenant Root.

The reconstruction includes discovery of existing Azure resources, import into Terraform state, inspection of potentially destructive changes, preservation of existing management-group identifiers and non-destructive hierarchy reconciliation.

Three core platform subscriptions are represented through Terraform subscription associations:

* `sub-connectivity-01`
* `sub-management-01`
* `sub-security-01`

This work demonstrates how Infrastructure as Code can adopt and manage existing enterprise infrastructure rather than requiring a complete rebuild.

[Explore Phase 0 Terraform](00-enterprise-assessment/terraform/)

## 5. Current Phase — Enterprise Assessment

**Objective:** Establish a defensible current-state architecture before designing the target state.

| Deliverable                               | Status         |
| ----------------------------------------- | -------------- |
| Terraform engineering foundation          | Complete       |
| Management-group reconstruction           | Complete       |
| Cloud inventory                           | Documented     |
| Current-state architecture assessment     | Drafted        |
| Current-state architecture diagram        | In progress    |
| Identity assessment                       | Pending review |
| Network assessment                        | Pending review |
| Security operations assessment            | Pending review |
| Security governance maturity              | Pending review |
| Enterprise risk register                  | Pending review |
| Architecture requirements                 | Pending review |
| Traceability and transformation decisions | Pending review |
| Phase 0 checkpoint                        | Pending        |

### Featured architecture documents

* [Cloud Inventory](00-enterprise-assessment/current-state/cloud-inventory.md) — logical enterprise resources, physical lab boundaries, ownership and governance findings.
* [Current-State Architecture](00-enterprise-assessment/current-state/current-state-architecture.md) — architectural planes, dependencies, weaknesses and constraints.
* [Transformation Strategy ADR](00-enterprise-assessment/decisions/ADR-001-transformation-strategy.md) — phased transformation decisions.

The completion status of each deliverable is maintained through GitHub Issues.

## 6. Transformation Methodology

Every phase follows the same architecture lifecycle:

**Discover → Assess → Design → Decide → Engineer → Validate → Operate → Improve**

Findings and decisions are connected through a traceability chain:

**Observation → Finding → Risk → Requirement → Architecture Decision → Control → Validation → Evidence**

This prevents the portfolio from becoming a disconnected collection of technology demonstrations.

Each transformation phase is intended to produce a documented architecture checkpoint, including design decisions, implementation changes, validation results and lessons learned.

## 7. Enterprise Model vs. Physical Lab

The portfolio intentionally distinguishes the full fictionalized enterprise from the resources deployed in the physical Azure lab.

| Logical enterprise                                 | Physical lab                                   |
| -------------------------------------------------- | ---------------------------------------------- |
| Twelve-subscription enterprise model               | Selected platform subscriptions                |
| Representative enterprise-scale resource inventory | Cost-controlled implementation                 |
| Modeled security and governance gaps               | Selectively implemented and validated controls |
| Complete transformation architecture               | Incremental engineering checkpoints            |

**Evidence classifications**

* **Modeled:** Part of the representative AFG enterprise scenario.
* **Observed:** Discovered directly from the physical lab.
* **Validated:** Implemented and tested.
* **Planned:** Identified for a future phase.

The enterprise scenario is fictionalized and sanitized. It does not represent a production customer environment.

## 8. Technology and Architecture Domains

| Domain                 | Technologies and practices                                    |
| ---------------------- | ------------------------------------------------------------- |
| Cloud platform         | Microsoft Azure, management groups, subscriptions             |
| Identity               | Microsoft Entra ID, RBAC, PIM, workload identity              |
| Governance             | Azure Policy, tagging, compliance, architecture standards     |
| Infrastructure as Code | Terraform, Bicep                                              |
| Engineering            | GitHub, Azure DevOps, CI/CD                                   |
| Network security       | Hub-and-spoke, Azure Firewall, private endpoints              |
| Security operations    | Microsoft Sentinel, Defender for Cloud, Azure Monitor         |
| Data protection        | Key Vault, classification, encryption, Microsoft Purview      |
| Emerging technology    | AI security, threat modeling, secure application architecture |

Technologies are introduced and validated according to the needs of each transformation phase.

## 9. Repository Navigation

| Directory                                             | Purpose                                            |
| ----------------------------------------------------- | -------------------------------------------------- |
| [00-bootstrap](00-bootstrap/)                         | Engineering foundation and Terraform bootstrap     |
| [00-enterprise-assessment](00-enterprise-assessment/) | Current-state assessment and architecture baseline |
| [01-azure-landing-zone](01-azure-landing-zone/)       | Landing-zone transformation                        |
| [02-cloud-governance](02-cloud-governance/)           | Policy, governance and compliance                  |
| [03-zero-trust-identity](03-zero-trust-identity/)     | Workforce, privileged and workload identity        |
| [04-network-modernization](04-network-modernization/) | Network architecture and segmentation              |
| [05-security-operations](05-security-operations/)     | Monitoring, detection and response                 |
| [06-devsecops](06-devsecops/)                         | Secure engineering and deployment                  |
| [07-data-protection](07-data-protection/)             | Data security architecture                         |
| [08-ai-security](08-ai-security/)                     | AI security architecture                           |
| [09-dlv-fintech-platform](09-dlv-fintech-platform/)   | Reference application platform                     |

## 10. Follow the Progress

The portfolio is developed incrementally. GitHub provides visibility into the architecture transformation:

* [Issues](../../issues) track assessment and engineering deliverables.
* [Milestones](../../milestones) group work by transformation phase.
* [Commit history](../../commits/main/) records changes to documentation and code.
* Releases and tags will identify completed architecture checkpoints.

Completed work is distinguished from in-progress and planned capabilities. Architecture decisions and engineering evidence are published as the project develops.

---

## About the Architect

**John Hilton Jr.**

Cloud Security Engineer focused on enterprise cloud security architecture, Azure governance, Zero Trust, Infrastructure as Code and secure platform engineering.

This portfolio demonstrates the progression from implementing individual security controls to designing, governing and validating enterprise-wide security architecture.

[LinkedIn](https://www.linkedin.com/in/johnhilton1/) · [GitHub](https://github.com/Bobby360720)
