![alt text](<Copper A Auburn financial logo.png>)
# AFG Enterprise Security Architecture Transformation

**From brownfield assessment to defensible cloud, identity, and secure platform engineering architecture.**

An evolving, hands-on enterprise architecture portfolio using **AFG Enterprises**, a fictionalized Azure-first financial-technology enterprise, to connect business requirements, security risks, architecture decisions, technical controls, engineering implementation, and validation evidence.

**Primary pillars:** Cloud Security Architecture · Identity & Zero Trust Architecture · Secure Platform Engineering

**Technology focus:** Microsoft Azure · Microsoft Entra ID · Terraform · Azure Policy · GitHub Actions · DevSecOps

> **Current status (November 2026):** Phase 00 established the enterprise assessment baseline. Phase 01 implemented and validated a Terraform-managed Azure Landing Zone. **Phase 02 — Cloud Governance is in progress.** Later phases and proposed platform capabilities remain planned unless a linked evidence artifact demonstrates otherwise.
>
> **Portfolio direction:** Secure Platform Engineering replaces Information Protection as the third primary pillar. Information protection remains an essential cross-cutting control domain; existing findings, risks, requirements, and compliance obligations are not retired by this change.

---

## 1. The Architecture Challenge

AFG has evolved through incremental hybrid and Azure cloud adoption. Inconsistent practices across production, non-production, legacy, and shared-platform environments have introduced architectural debt.

The transformation addresses interconnected challenges:

- Fragmented governance, overlapping Azure Policy assignments, and inconsistent standards.
- Inconsistent workforce, privileged, application, and workload identity management.
- Uneven network segmentation, connectivity controls, and exposure management.
- Gaps in centralized telemetry, detection, and security operations.
- Incomplete resource ownership, business criticality, and lifecycle metadata.
- Manual infrastructure configuration and inconsistent deployment controls.
- Data protection, regulatory, resilience, and recovery requirements that are not uniformly applied.
- Emerging application and AI workloads without repeatable platform security guardrails.

**Central architecture question:**

> How can AFG modernize a brownfield enterprise and provide secure, reusable cloud platform capabilities while governing identity, reducing material risk, and minimizing business disruption?

## 2. Architecture Strategy: Three Primary Pillars

| Pillar | Architecture question | Portfolio evidence |
|---|---|---|
| **Cloud Security Architecture** | How should Azure organization, network boundaries, workloads, security services, and policy guardrails be designed and governed? | Enterprise assessment, Azure Landing Zone, Terraform infrastructure, Azure Policy architecture, risk-to-control traceability, ADRs, and validation |
| **Identity & Zero Trust Architecture** | How should workforce, privileged, application, and workload identities authenticate, obtain access, and be governed across trust boundaries? | Microsoft Entra ID reference patterns, role and privileged-access designs, federation, Conditional Access, workload identity, lifecycle requirements, and threat models |
| **Secure Platform Engineering** | How can AFG make secure deployment the repeatable default through shared services, automated controls, and clear operating ownership? | Reusable Terraform patterns, GitHub Actions/CI-CD security checks, policy-as-code, secure application and API reference deployments, workload guardrails, operations, and deployment evidence |

### How the pillars work together

Cloud Security Architecture defines enterprise boundaries, requirements, and guardrails. Identity & Zero Trust defines access and trust relationships. Secure Platform Engineering makes approved patterns repeatable and testable through automation, reusable infrastructure, secure deployment workflows, and operational standards.

### Cross-cutting capabilities

- **Information protection and privacy:** Data classification, encryption, secrets management, access restrictions, retention, sharing, DLP, and applicable regulatory obligations. These remain in scope as risk-based requirements, not a standalone flagship implementation program.
- **Network modernization:** Segmentation, routing, DNS, controlled ingress/egress, and private connectivity.
- **Security operations and resilience:** Telemetry, detection, response, recovery, and operational evidence.
- **Application/API and AI security:** Threat modeling, Azure API Management where justified, secure application design, AI access controls, and model/data governance.
- **Enterprise risk and compliance:** Control ownership, exceptions, residual-risk acceptance, testing, and measurable outcomes.

DevSecOps and policy-as-code are **core Secure Platform Engineering practices**, rather than peripheral technology demonstrations.

### Architecture decision standards

Significant designs identify the business problem, requirement, relevant finding and risk, alternatives, trade-offs, decision authority, implementation boundary, control intent, evidence, residual risk, and conditions for reconsideration. Vendor selection is requirement-driven. Mentioning a platform does not indicate an approved enterprise decision or a validated implementation.

## 3. Architecture at a Glance

AFG models hybrid enterprise connectivity and an Azure Landing Zone with separate platform, workload, and subscription lifecycle boundaries.

```text
Tenant Root Group
└── AFG
    ├── Platform
    │   ├── Connectivity
    │   ├── Management
    │   └── Security
    ├── Landing-Zones
    │   ├── Corp
    │   ├── Online
    │   └── Legacy
    ├── Sandbox
    ├── Onboarding
    └── Decommissioned
```

- **Platform:** Shared connectivity, operations, and security capabilities.
- **Corp:** Corporate-connected and privately integrated workloads.
- **Online:** Independently connected customer- and partner-facing workloads.
- **Legacy:** Transitional brownfield workloads under controlled exception handling.
- **Sandbox:** Representative experiments and cost-controlled lab deployments.
- **Onboarding:** Temporary classification and placement of incoming subscriptions.
- **Decommissioned:** Controlled retirement before cancellation or deletion.

The current-state model remains separate from the target design; later implementation does not retroactively change earlier assessment evidence.

## 4. Transformation Roadmap

| Phase | Domain | Status | Relationship to pillars |
|---|---|---|---|
| Bootstrap | Engineering foundation | Complete | Terraform, repository, authentication, and deployment foundations |
| 00 | Enterprise assessment | Baseline complete | Business context, findings, risks, requirements, current state |
| 01 | Azure Landing Zone | Implemented and validated | Cloud platform foundation and governance boundaries |
| 02 | Cloud governance | **In progress** | Azure Policy, ownership, exemptions, compliance evidence, and policy-as-code architecture |
| 03 | Zero Trust identity | Planned | **Identity & Zero Trust flagship** |
| 04 | Network modernization | Planned | Cloud security and platform networking controls |
| 05 | Security operations | Planned | Detection, telemetry, response, and operational observability |
| 06 | DevSecOps / secure delivery | Planned | **Secure Platform Engineering flagship implementation track** |
| 07 | Data protection | Planned; reduced emphasis | Required information protection and privacy baselines; no standalone flagship |
| 08 | AI security | Planned | Cross-cutting workload identity, data access, and AI safeguards |
| 09 | DLV FinTech platform | Planned | Integrated secure workload reference/capstone |

**Roadmap interpretation:** Existing folder and phase identifiers remain unchanged. Secure Platform Engineering spans Phase 01/02 foundations and Phase 06/09 engineering deliverables; it is **not** a newly claimed completed phase. The Phase 07 scope adjustment does not close or negate any previously identified data risks.

### Current focus: Phase 02 — Cloud Governance

Use the validated management-group and subscription hierarchy to design and evaluate policy scope, initiative structure, inheritance, exemptions, remediation, tagging, control ownership, compliance evidence, and progressive enforcement. Finish the current governance work before broadening deployment scope.

For detailed tasks and checkpoint status, consult [GitHub Issues](https://github.com/Bobby360720/cloud-security-architecture-portfolio/issues), [Milestones](https://github.com/Bobby360720/cloud-security-architecture-portfolio/milestones), and phase-specific evidence—not a duplicated task list here.

## 5. Implemented and Validated Foundations

### Engineering bootstrap

The existing engineering foundation includes Terraform-managed Azure infrastructure, Azure Storage remote state, GitHub version control, Azure DevOps integration, workload identity federation for Azure authentication, Terraform format/validate/plan workflows, and environment-specific configuration excluded from source control.

### Phase 00 — Brownfield enterprise assessment

The modeled enterprise assessment establishes business context, cloud inventory, current-state architecture, governance maturity, findings, enterprise risks, requirements, and transformation strategy. Representative lab reconstruction included discovering existing Azure resources, importing them to Terraform, preserving management-group identifiers, inspecting destructive changes, reconciling state, and adopting resources without a full rebuild.

[Phase 00 assessment](00-enterprise-assessment/README.md) · [Engineering foundation](00-bootstrap/README.md)

### Phase 01 — Azure Landing Zone

Validated Phase 01 implementation established the AFG governance boundary; Platform and Landing-Zones organization; Connectivity, Management, and Security platform boundaries; Corp, Online, and Legacy workload archetypes; Sandbox, Onboarding, and Decommissioned lifecycle boundaries; representative subscription placement; and Terraform remote-state ownership. Previous Production and Non-Production management groups were retired, and `Onboarding` was configured as the tenant default management group.

Representative brownfield transitions included:

```text
Connectivity  → Landing-Zones / Legacy
Identity      → Decommissioned
Security      → Decommissioned
sub-sandbox   → Sandbox
Web Apps      → Landing-Zones / Online
```

Subscription classification considered resource dependencies, RBAC, existing policy, locks, ownership, lifecycle, and workload context—not names alone. Phase 01's recorded final Terraform validation showed the desired state converged without further changes.

Formal architecture decisions include **ADR-002 — Azure Landing Zone Governance Boundary Model** and **ADR-003 — Brownfield Subscription Transition Strategy**. The underlying records, not this summary, remain authoritative for their approved rationale and boundaries.

[Phase 01 landing zone](01-azure-landing-zone/README.md) · [Phase 01 validation](01-azure-landing-zone/evidence/phase1-landing-zone-validation.md)

## 6. Secure Platform Engineering: Planned Flagship

**Objective:** Enable a workload team to use a documented, repeatable, security-validated delivery path without manually rebuilding Azure security foundations for every application.

### Proposed reference implementation

A small representative AFG application workload will exercise the existing landing-zone and governance foundations using a secure delivery workflow:

1. **Platform contract:** Define supported workload archetype, subscription placement, ownership, identity, networking, logging, recovery, tagging, and cost requirements.
2. **Reusable Infrastructure as Code:** Create appropriately scoped Terraform modules or compositions for application hosting, managed identity, secrets access, network controls, and monitoring.
3. **Secure CI:** Validate formatting, unit/tests as appropriate, static analysis, infrastructure scanning, and OPA/Rego policy checks against an actual Terraform plan.
4. **Controlled CD:** Use environment approvals, least-privilege deployment identity, separation of duties, evidence retention, and deployment guardrails where practical.
5. **Workload and API controls:** Prefer managed identities and supported PaaS patterns; assess API authentication, network exposure, secret handling, and Azure API Management based on requirements.
6. **Platform operations:** Capture diagnostic coverage, misconfiguration/drift detection, exception ownership, rollback/teardown procedures, and cost observations.
7. **Validation:** Map test results and observed Azure settings to the requirements and security controls they demonstrate.

### Proposed success criteria

| Outcome | Validation evidence to collect |
|---|---|
| Repeatable platform deployment | Documented IaC plan/apply/destroy results with reproducible configuration |
| Prevent insecure configuration | Negative policy tests and blocked pipeline checks |
| Protect deployment and workload identities | Identity assignments and permissions review; no persistent cloud secrets in the pipeline |
| Apply governance consistently | Policy assignments, compliance observations, or documented test limitations |
| Establish reliable operations | Telemetry configuration, validation of an alert or query, and recovery/teardown procedure |
| Demonstrate ownership and risk decisions | Requirement/control mappings, exception and decision records, and residual-risk notes |

These are **planned acceptance criteria**, not claims of completed enterprise implementation. Existing independent lab experiments may inform design, but are not automatically counted as integrated AFG validation.

**Scope guardrail:** Prioritize low-cost Azure PaaS and a minimal representative deployment. Avoid introducing AKS, multi-cloud, a service mesh, or a developer portal without a business requirement. Keep the core governance hierarchy persistent; deploy short-lived workloads with teardown and estimated cost checks.

## 7. Identity & Zero Trust: Planned Flagship

Phase 03 will address workforce and application federation, Conditional Access, privileged access/PIM, role design, joiner-mover-leaver processes, access reviews, managed and federated workload identity, identity threat modeling, and identity governance ownership. Microsoft Entra ID remains the primary execution platform; Okta or SailPoint evaluations require a decision case and are not assumed implemented.

The [workload identity threat model](03-zero-trust-identity/workload-identity-threat-model.md) traces the proposed GitHub Actions-to-Azure federation design to enterprise risk R-003, identifies trust boundaries, and defines the checks required before considering production use. Lab validation is pending.

## 8. Information Protection: Supporting Baseline

Phase 07 remains a repository domain because the modeled enterprise has information protection obligations. Its reduced scope emphasizes:

- Information classification and business ownership requirements.
- Encryption at rest/in transit, key and secret handling, and least-privilege data access.
- Data-sharing, retention, and privacy controls driven by AFG risk and applicable regulatory scope.
- Minimum monitoring, exception processes, residual-risk documentation, and control validation.
- Microsoft Purview or DLP design only where traceable requirements justify it; large standalone rollout or dashboard-building is not a current flagship objective.

Existing Phase 00 findings, risks, and regulatory decisions retain their references and appropriate disposition until formally reviewed.

## 9. Integrated FinTech Platform: Planned Capstone

Phase 09 is intended to demonstrate one representative business workload combining the three primary pillars: landing-zone placement and policy, human and workload identity, secure IaC delivery, application/API boundaries, logging, security operations, information protection baseline requirements, and evidence-driven acceptance. The platform remains a **planned capstone**, not a completed production environment.

## 10. Transformation Method and Evidence

```text
Discover → Assess → Design → Decide → Engineer → Validate → Operate → Improve
```

**Traceability:**

```text
Observation → Finding → Risk → Requirement → Architecture Decision
           → Control → Validation → Evidence → Residual Risk
```

Major checkpoints should explain architecture drivers, requirements, decision ownership, alternatives, implementation changes, validation, residual risks, and lessons learned. SharePoint serves as the operational findings and risk tracking system; GitHub maintains the version-controlled architecture baseline, designs, ADRs, IaC, and reproducible evidence. Sanitized references should connect the two without leaking operational information.

### Evidence classifications

| Label | Meaning |
|---|---|
| **Modeled** | Assumed or designed within the fictionalized enterprise scenario |
| **Observed** | Directly discovered in the physical Azure lab or recorded tooling output |
| **Validated** | Implemented and tested, with reproducible evidence |
| **Planned** | Proposed for later design, implementation, or validation |

The fictionalized enterprise model is broader than the cost-controlled physical lab. No modeled requirement or proposed design should be mistaken for an observed production condition or completed deployment.

## 11. Resource Organization Standards

Management groups provide durable governance boundaries—not one management group per application or team. Subscriptions reflect security isolation, workload and lifecycle, connectivity, ownership, regulation, cost, quota, and blast radius. Resource groups follow coherent deployment and operational lifecycles. Tags provide metadata, **not** security isolation or access control.

Baseline tagging targets include `Environment`, `Application`, `Owner`, `CostCenter`, `ManagedBy`, and `Criticality`. Conditional metadata may include `DataClassification`, `BusinessOwner`, `Lifecycle`, `Expiry`, `ComplianceScope`, and `RecoveryTier`. Brownfield normalization should be incremental and risk-based.

## 12. Technologies and Practices

| Domain | Primary or candidate technologies and practices |
|---|---|
| Cloud platform and governance | Azure Landing Zones, management groups, Terraform, Azure Policy, initiatives, exemptions |
| Identity and Zero Trust | Microsoft Entra ID, RBAC, PIM, federation, managed identities, Conditional Access |
| Secure platform engineering | Terraform, GitHub Actions, Azure DevOps, CI/CD, Checkov, OPA/Rego, secure pipelines, reusable patterns |
| Application and API | Azure PaaS patterns, threat modeling, Azure API Management, security testing |
| Network and workload protection | Azure Firewall, routing, private endpoints, DNS, segmentation, Key Vault |
| Security operations | Microsoft Sentinel, Defender for Cloud, Azure Monitor, diagnostic logging |
| Information protection | Classification, encryption, Microsoft Purview/DLP where requirements justify it |
| Emerging workloads | AI security architecture, identity-aware retrieval and data access controls |

Technology inclusion is **not** proof of deployment, purchasing, proficiency, or enterprise approval.

## 13. Repository Navigation

| Directory | Scope |
|---|---|
| [`00-bootstrap`](00-bootstrap/) | Engineering foundation and Terraform bootstrap |
| [`00-enterprise-assessment`](00-enterprise-assessment/) | Current state, findings, risks, requirements, and assessment baseline |
| [`01-azure-landing-zone`](01-azure-landing-zone/) | Landing Zone design, Terraform, standards, ADRs, and validation |
| [`02-cloud-governance`](02-cloud-governance/) | Azure Policy governance, compliance, ownership, and exception architecture |
| [`03-zero-trust-identity`](03-zero-trust-identity/) | Identity and Zero Trust reference architecture |
| [`04-network-modernization`](04-network-modernization/) | Network architecture and connectivity controls |
| [`05-security-operations`](05-security-operations/) | Monitoring, detection, and response |
| [`06-devsecops`](06-devsecops/) | Secure Platform Engineering delivery practices and pipeline controls |
| [`07-data-protection`](07-data-protection/) | Supporting data protection and information governance baseline |
| [`08-ai-security`](08-ai-security/) | AI security requirements and reference patterns |
| [`09-dlv-fintech-platform`](09-dlv-fintech-platform/) | Integrated representative workload capstone |

### Selected Phase 01 source artifacts

- [Landing-zone requirements](01-azure-landing-zone/architecture/landing-zone-requirements.md)
- [Management-group and subscription design](01-azure-landing-zone/architecture/management-group-subscription-design.md)
- [Resource organization standards](01-azure-landing-zone/architecture/resource-organization-standards.md)
- [ADR-002](01-azure-landing-zone/decisions/ADR-002-azure-landing-zone-governance-boundary-model.md)
- [ADR-003](01-azure-landing-zone/decisions/ADR-003-brownfield-subscription-transition-strategy.md)
- [Terraform implementation](01-azure-landing-zone/infrastructure-as-code/terraform/)
- [Phase 01 validation evidence](01-azure-landing-zone/evidence/phase1-landing-zone-validation.md)

## 14. About the Architect

**John Hilton Jr.** · [LinkedIn](https://www.linkedin.com/in/johnhilton1/)

Cloud Security Engineer advancing enterprise architecture capability across **Cloud Security, Identity & Zero Trust, and Secure Platform Engineering**. This portfolio emphasizes moving from isolated control implementation toward enterprise assessment, risk-based architecture decisions, secure platform standards, repeatable engineering, operational ownership, and measurable validation.

## Portfolio Objective

The objective is not to deploy the most tools or simulate an enterprise-sized environment in a personal lab. It is to demonstrate the ability to **assess business risk, translate requirements into defensible architecture, establish guardrails, engineer reusable secure paths, validate representative controls, and explain the resulting trade-offs and outcomes clearly.**
