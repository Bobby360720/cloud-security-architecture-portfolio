# AFG Enterprise Security Architecture Transformation

**From brownfield assessment to defensible cloud, identity, and information protection architecture.**

An evolving, hands-on enterprise security architecture portfolio using a
fictionalized hybrid Azure organization to connect business requirements,
architectural decisions, security controls, engineering implementation, and
validation evidence across three complementary disciplines:

**Cloud Security · Identity Security · Information Protection · Zero Trust · Azure · Terraform**

> **Current status:** Phase 01 — Azure Landing Zone is complete and validated.
> Phase 02 — Cloud Governance is the next architecture phase.
>
> Phase 00 established the brownfield enterprise assessment baseline.
> Phase 01 translated that baseline into a Terraform-managed Azure Landing Zone
> with validated management-group boundaries, subscription placement,
> brownfield transition patterns, remote state, architecture decisions, and
> implementation evidence.

---

## 1. The Architecture Challenge

AFG Enterprises is a fictionalized enterprise with a hybrid Azure environment
that has evolved through incremental cloud adoption.

The organization has invested in identity, networking, governance, monitoring,
and security tooling. However, inconsistent adoption across production,
non-production, legacy, and shared-platform environments has created
architectural debt.

The transformation addresses eight interconnected challenges spanning cloud
infrastructure, identity, and information protection:

- fragmented governance and overlapping policy assignments;
- inconsistent privileged and workload identity management;
- uneven network segmentation and public exposure;
- gaps in centralized logging and security telemetry;
- incomplete ownership and criticality metadata;
- manual infrastructure configuration and deployment;
- inconsistent data-protection and resilience requirements;
- emerging AI workloads without standardized security governance.

The central architecture question is:

> **How can AFG modernize a brownfield enterprise while establishing
> consistent cloud, identity, and information-protection architecture without
> disrupting business operations?**

---

## 2. Security Architecture Strategy

AFG is organized around three mutually reinforcing architecture pillars.

Each pillar is evaluated against business requirements, operating
responsibilities, risk, implementation cost, architectural trade-offs, and
measurable outcomes rather than against the desire to deploy a particular
technology.

| Pillar | Architecture Questions | Primary Portfolio Evidence |
|---|---|---|
| **Cloud Security** | How should Azure subscriptions, workloads, network boundaries, platform services, and policy guardrails be governed? | Landing-zone designs, Terraform, Azure Policy, risk assessments, ADRs, validation evidence |
| **Identity Security** | How should workforce, privileged, application, and workload identities authenticate, receive access, and be governed? | Entra ID reference patterns, SSO/federation designs, lifecycle and governance models, Entra-versus-Okta evaluation, identity ADRs |
| **Information Protection** | How should sensitive information be classified, accessed, shared, retained, and protected across enterprise services? | Information-classification model, Purview/DLP target designs, ownership model, exception decisions, validation plans |

Architecture leadership is the connecting discipline.

Each major design should document:

- the business problem;
- architecture drivers;
- requirements;
- alternatives considered;
- trade-offs;
- decision authority;
- implementation boundaries;
- control intent;
- validation evidence;
- residual risk;
- conditions requiring reconsideration.

### Scope Control

DevSecOps, API security, network modernization, security operations, and AI
security remain supporting architecture capabilities.

Okta, SailPoint, Azure API Management, and other platforms are evaluated only
when they solve a defined AFG requirement. Their inclusion in the portfolio
does not imply production deployment or production-level expertise unless
supported by validation evidence.

---

## 3. Architecture at a Glance

AFG operates a hybrid enterprise architecture connecting on-premises
infrastructure to Azure through private and enterprise connectivity patterns.

The Phase 01 target Azure Landing Zone separates shared platform capabilities,
business workloads, transitional environments, experimentation, onboarding,
and retirement states.

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

### Platform Boundaries

`Platform` contains shared enterprise capabilities:

- **Connectivity** — enterprise network and connectivity services;
- **Management** — centralized operational and management services;
- **Security** — centralized security platform capabilities.

### Workload and Lifecycle Boundaries

`Landing-Zones` and lifecycle management groups provide distinct governance
boundaries:

- **Corp** — corporate-connected, hybrid, and privately integrated workloads;
- **Online** — independently connected customer- and partner-facing workloads;
- **Legacy** — transitional brownfield workloads requiring temporary exceptions;
- **Sandbox** — experimentation, learning, and representative lab workloads;
- **Onboarding** — temporary placement for new or unclassified subscriptions;
- **Decommissioned** — controlled retirement before subscription cancellation or deletion.

Microsoft Entra ID, Azure Policy, monitoring, security operations, information
protection, automation, and later-phase security controls operate across these
boundaries.

### Current-State Architecture

The detailed brownfield current-state architecture remains documented under
Phase 00.

The portfolio deliberately distinguishes:

```text
Current State
      ↓
Assessment
      ↓
Target Architecture
      ↓
Controlled Implementation
      ↓
Validation Evidence
```

The current-state model is not retroactively rewritten to resemble the target
architecture.

---

## 4. Current Transformation Status

| Phase | Architecture Domain | Status |
|---|---|---|
| Bootstrap | Engineering Foundation | **Complete** |
| 00 | Enterprise Assessment | **Baseline complete** |
| 01 | Azure Landing Zone | **Complete — implemented and validated** |
| 02 | Cloud Governance | **Next** |
| 03 | Enterprise Identity Security | Planned — flagship pillar |
| 04 | Network Modernization | Planned |
| 05 | Security Operations | Planned |
| 06 | DevSecOps | Planned |
| 07 | Information Protection | Planned — flagship pillar |
| 08 | AI Security | Planned |
| 09 | DLV FinTech Platform | Planned |

### Current Focus

The portfolio is transitioning into:

> **Phase 02 — Cloud Governance**

Phase 02 will use the validated Phase 01 management-group and subscription
hierarchy as the governance scope for:

- Azure Policy architecture;
- policy inheritance;
- initiative design;
- exemptions;
- compliance ownership;
- remediation;
- tagging governance;
- policy-as-code;
- governance operations.

Residual Phase 00 review items, where applicable, remain tracked through
GitHub Issues and do not require reopening or redesigning the established
assessment baseline.

Progress is tracked through:

- GitHub Issues;
- GitHub Milestones;
- architecture decision records;
- repository commit history;
- implementation evidence.

---

## 5. What Has Been Engineered

This portfolio contains both architecture documentation and hands-on
implementation.

### Engineering Foundation

The engineering foundation includes:

- Terraform-based Azure infrastructure deployment;
- Azure Storage remote Terraform state;
- GitHub version control;
- Azure DevOps integration;
- workload identity federation for Azure authentication;
- Terraform formatting, validation, and planning;
- environment-specific backend configuration excluded from source control.

### Brownfield Architecture Reconstruction

Phase 00 reconstructed representative existing Azure infrastructure before
target-state architecture changes were introduced.

The reconstruction demonstrated:

- discovery of existing Azure resources;
- Terraform import of existing resources;
- preservation of management-group identifiers;
- inspection of potentially destructive plans;
- state reconciliation;
- non-destructive brownfield adoption.

This work demonstrates that Infrastructure as Code can adopt existing
enterprise infrastructure without requiring a complete greenfield rebuild.

### Azure Landing Zone Transformation

Phase 01 transformed the reconstructed brownfield hierarchy into the target
AFG Azure Landing Zone.

Implemented and validated capabilities include:

- `AFG` enterprise management-group boundary beneath Tenant Root;
- separation of `Platform` and `Landing-Zones`;
- Connectivity, Management, and Security platform boundaries;
- Corp, Online, and Legacy workload archetypes;
- dedicated Sandbox, Onboarding, and Decommissioned lifecycle boundaries;
- retirement of the former Production and Non-Production management groups;
- `Onboarding` configured as the tenant default management group;
- representative platform and brownfield subscription placement;
- Terraform state reconciliation before architecture modification;
- transition of active Terraform ownership from Phase 00 to Phase 01;
- migration of Phase 01 Terraform state to the Azure Storage remote backend;
- preservation of valid brownfield resources and management-group identifiers;
- formal architecture decision records;
- final Terraform desired-state convergence.

### Representative Subscription Placement

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

Brownfield subscriptions were classified using their actual resources,
dependencies, RBAC, policy assignments, locks, ownership, and lifecycle rather
than their names alone.

Representative transitions included:

```text
Connectivity  → Landing-Zones / Legacy
Identity      → Decommissioned
Security      → Decommissioned
sub-sandbox   → Sandbox
Web Apps      → Landing-Zones / Online
```

Final Terraform validation reported:

```text
No changes. Your infrastructure matches the configuration.
```

---

## 6. Completed Architecture Checkpoints

### Phase 00 — Enterprise Assessment

Phase 00 established the brownfield enterprise baseline used by later
architecture phases.

Primary outputs include:

- business context;
- cloud inventory;
- current-state architecture;
- governance maturity assessment;
- findings register;
- enterprise risk register;
- business requirements;
- technical requirements;
- transformation strategy;
- representative Terraform-managed brownfield reconstruction.

Phase 00 answers:

> **What does AFG have today, what architectural weaknesses exist, and what
> requirements must the transformation satisfy?*
[View Phase 00 Assessment](00-enterprise-assessment/README.md) ·
[Explore Engineering Foundation](00-bootstrap/README.md) ·
### Phase 01 — Azure Landing Zone

Phase 01 translated Phase 00 requirements into the target Azure organizational
foundation.

Primary outputs include:

- Azure Landing Zone architecture requirements;
- management-group and subscription architecture;
- workload-placement criteria;
- resource organization standards;
- naming and tagging standards;
- ownership standards;
- subscription lifecycle design;
- brownfield migration strategy;
- Terraform-managed target hierarchy;
- remote state implementation;
- architecture decision records;
- validation evidence.

Phase 01 answers:

> **How should AFG organize Azure so future governance, identity, networking,
> security operations, data protection, DevSecOps, and AI-security controls
> have stable enterprise boundaries?**

Detailed completion status is maintained through GitHub Issues and Milestones
rather than duplicated in this README.
[View Phase 01 Landing Zone](01-azure-landing-zone/README.md) ·
---

## 7. Phase 01 Architecture Decisions

Phase 01 uses a working architecture decision log for detailed decisions and
formal ADRs for decisions that establish durable enterprise standards.

### Formal ADRs

- **ADR-002 — Azure Landing Zone Governance Boundary Model**
- **ADR-003 — Brownfield Subscription Transition Strategy**

These decisions preserve the rationale for:

- the `AFG` enterprise governance boundary;
- Platform and Landing-Zones separation;
- Corp, Online, Legacy, Sandbox, Onboarding, and Decommissioned boundaries;
- incremental brownfield adoption;
- preservation of validated existing resources;
- controlled migration and retirement.

Routine implementation decisions remain documented in the Phase 01 design
artifact rather than being promoted unnecessarily into separate ADRs.

---

## 8. Resource Organization Standards

Phase 01 establishes architecture standards for:

### Management Groups

Management groups represent durable governance boundaries.

They are not intended to model:

- individual applications;
- temporary projects;
- individual teams;
- organizational reporting structures;
- Azure regions alone.

### Subscriptions

Subscription boundaries require an architectural reason such as:

- ownership;
- lifecycle;
- security isolation;
- production/non-production separation;
- connectivity;
- regulatory scope;
- cost accountability;
- blast-radius reduction;
- quota or capacity requirements.

### Resource Groups

Resource groups represent deployment and operational lifecycle boundaries.

They should generally align resources that share:

- ownership;
- application purpose;
- environment;
- deployment lifecycle;
- change management.

### Tags

Tags provide metadata.

They do **not** replace:

- subscription boundaries;
- RBAC;
- Azure Policy;
- network segmentation;
- data-security controls.

Target baseline metadata includes:

- `Environment`;
- `Application`;
- `Owner`;
- `CostCenter`;
- `ManagedBy`;
- `Criticality`.

Conditional metadata may include:

- `DataClassification`;
- `BusinessOwner`;
- `Lifecycle`;
- `Expiry`;
- `ComplianceScope`;
- `RecoveryTier`.

Brownfield resources are normalized incrementally rather than rebuilt or
renamed solely for cosmetic consistency.

---

## 9. Planned Flagship Deliverables

### Phase 03 — Enterprise Identity Security

Planned flagship deliverables include:

- workforce identity reference architecture;
- workload identity patterns;
- Microsoft Entra ID federation and access design;
- identity-governance operating model;
- joiner–mover–leaver architecture;
- privileged-access standards;
- application identity architecture;
- workload identity architecture;
- Entra-versus-Okta decision analysis;
- identity threat model;
- identity architecture decision records.

An Okta implementation lab is optional and must remain clearly separated from
the enterprise target design unless physically implemented and validated.

### Phase 07 — Information Protection

Planned flagship deliverables include:

- business-driven data classification;
- information ownership and stewardship;
- Microsoft Purview target architecture;
- sensitivity-label architecture;
- DLP architecture;
- information-sharing patterns;
- retention patterns;
- exception governance;
- security requirements;
- validation plans;
- residual-risk documentation.

### Phase 09 — DLV FinTech Platform

The DLV FinTech Platform will demonstrate how:

- cloud governance;
- identity security;
- workload identity;
- information protection;
- application security;
- API security;
- infrastructure automation

work together for a representative business workload.

This remains a planned capstone and is not represented as a completed
production platform.

---

## 10. Transformation Methodology

Every phase follows the same architecture lifecycle:

```text
Discover
   ↓
Assess
   ↓
Design
   ↓
Decide
   ↓
Engineer
   ↓
Validate
   ↓
Operate
   ↓
Improve
```

Findings and decisions are connected through a traceability chain:

```text
Observation
   ↓
Finding
   ↓
Risk
   ↓
Requirement
   ↓
Architecture Decision
   ↓
Control
   ↓
Validation
   ↓
Evidence
```

This prevents the portfolio from becoming a disconnected collection of
technology demonstrations.

Each transformation phase should produce a defensible architecture checkpoint
containing:

- architecture drivers;
- requirements;
- decisions;
- implementation changes;
- validation results;
- evidence;
- residual risks;
- lessons learned.

---

## 11. Enterprise Model vs. Physical Lab

The portfolio intentionally distinguishes the full fictionalized enterprise
from the resources physically deployed in the Azure lab.

| Logical Enterprise | Physical Lab |
|---|---|
| Enterprise-scale subscription model | Selected representative subscriptions |
| Representative enterprise resource inventory | Cost-controlled implementation |
| Modeled security and governance gaps | Selectively implemented controls |
| Complete target architecture | Incremental validation checkpoints |
| Enterprise operating model | Representative technical evidence |

### Evidence Classifications

**Modeled**
Part of the representative AFG enterprise scenario.

**Observed**
Discovered directly from the physical Azure lab.

**Validated**
Implemented and tested.

**Planned**
Identified for a future architecture phase.

The enterprise scenario is fictionalized and sanitized.

It does not represent a production customer environment.

---

## 12. Technology and Architecture Domains

| Domain | Technologies and Practices |
|---|---|
| Cloud Platform | Microsoft Azure, management groups, subscriptions, landing zones |
| Cloud Governance | Azure Policy, initiatives, exemptions, tagging, compliance |
| Identity Security | Microsoft Entra ID, RBAC, PIM, SSO/federation, workload identities |
| Information Protection | Microsoft Purview, classification, sensitivity labels, DLP, information governance |
| Infrastructure as Code | Terraform, Bicep |
| Engineering | GitHub, Azure DevOps, CI/CD |
| Network Security | Hub-and-spoke, routing, Azure Firewall, private endpoints, DNS |
| Security Operations | Microsoft Sentinel, Defender for Cloud, Azure Monitor |
| Application and API Security | DevSecOps, API security, Azure API Management |
| Emerging Technology | AI security, threat modeling, secure AI architecture |

Technologies are introduced according to architecture requirements.

Listing a technology does not mean it has been deployed or validated.

---

## 13. Repository Navigation

| Directory | Purpose |
|---|---|
| `00-bootstrap` | Engineering foundation and Terraform bootstrap |
| `00-enterprise-assessment` | Brownfield current-state assessment, findings, risks, and architecture baseline |
| `01-azure-landing-zone` | Completed Azure Landing Zone design, Terraform implementation, ADRs, standards, and validation evidence |
| `02-cloud-governance` | Azure Policy, control inheritance, exemptions, ownership, compliance, and governance operations |
| `03-zero-trust-identity` | Workforce, privileged, application, and workload identity architecture |
| `04-network-modernization` | Network architecture, routing, segmentation, DNS, private connectivity, and egress |
| `05-security-operations` | Monitoring, detection, response, telemetry, and security operations |
| `06-devsecops` | Secure engineering, pipeline security, application security, and deployment controls |
| `07-data-protection` | Information protection, classification, Purview, DLP, and data governance |
| `08-ai-security` | AI security architecture and governance |
| `09-dlv-fintech-platform` | Integrated reference workload and architecture capstone |

---

## 14. Phase 01 Key Artifacts

Phase 01 artifacts include:

| Artifact | Purpose |
|---|---|
| `01-azure-landing-zone/README.md` | Phase overview and status |
| `01-azure-landing-zone/architecture/landing-zone-requirements.md` | Phase 01 architecture requirements |
| `01-azure-landing-zone/architecture/management-group-subscription-design.md` | Target management-group, subscription, placement, lifecycle, and migration design |
| `01-azure-landing-zone/architecture/resource-organization-standards.md` | Resource organization, naming, tagging, ownership, and brownfield-normalization standards |
| `01-azure-landing-zone/decisions/ADR-002-azure-landing-zone-governance-boundary-model.md` | Durable landing-zone governance decision |
| `01-azure-landing-zone/decisions/ADR-003-brownfield-subscription-transition-strategy.md` | Brownfield transformation decision |
| `01-azure-landing-zone/infrastructure-as-code/terraform/` | Active Terraform implementation |
| `01-azure-landing-zone/evidence/phase1-landing-zone-validation.md` | Implementation and validation evidence |

---

## 15. Follow the Progress

The portfolio is developed incrementally.

GitHub provides visibility into the transformation:

- **Issues** track architecture, assessment, and engineering deliverables;
- **Milestones** group work by transformation phase;
- **ADRs** preserve consequential architecture decisions;
- **Commit history** records changes to documentation and code;
- **Evidence artifacts** document implemented and validated outcomes;
- **Releases and tags** can identify completed architecture checkpoints.

Completed work is explicitly distinguished from:

- modeled architecture;
- in-progress work;
- planned capabilities.

---

## About the Architect

**John Hilton Jr.** [Connect on LinkedIn](https://www.linkedin.com/in/johnhilton1/)

Cloud Security Engineer developing enterprise security architecture capability
across:

- Cloud Security;
- Identity Security;
- Information Protection.

The portfolio is grounded in:

- Microsoft Azure;
- Microsoft Entra ID;
- Zero Trust;
- Infrastructure as Code;
- enterprise governance;
- risk-based architecture;
- cross-functional security design.

This portfolio documents the progression from implementing individual
security controls to:

- assessing enterprise environments;
- translating findings into risk;
- defining architecture requirements;
- evaluating alternatives;
- making architecture decisions;
- establishing standards;
- implementing representative controls;
- validating technical outcomes;
- governing enterprise-wide security architecture.

Planned reference designs, vendor evaluations, and modeled enterprise
capabilities are clearly distinguished from hands-on implementation and
validated evidence.

---

## Portfolio Objective

The objective is not to demonstrate the largest possible number of security
tools.

The objective is to demonstrate the ability to:

> **Assess an enterprise, identify material risk, translate business
> requirements into architecture, make defensible technical decisions,
> implement representative controls, validate outcomes, and communicate the
> resulting security architecture clearly.**
```
