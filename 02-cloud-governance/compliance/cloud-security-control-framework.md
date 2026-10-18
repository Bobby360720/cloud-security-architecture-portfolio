# P02-02 — Cloud Security Control Framework

| Attribute | Value |
| --- | --- |
| Enterprise | AFG Enterprises (modeled) |
| Phase | 2 — Cloud Governance & Compliance |
| GitHub issue | #23 — Develop Cloud Security Control Framework |
| Status | Proposed architecture baseline — pending review |
| Evidence classification | Modeled / planned; not implemented or validated |
| Framework approach | Security-outcome-centered |

## 1. Purpose and Scope

This framework translates AFG's modeled business risks, security requirements, and potentially applicable regulatory and contractual obligations into reusable cloud security control objectives. It is the **architecture control baseline**, not a certification claim, a full regulatory control catalog, or a deployment record.

The framework reuses Phase 0 business requirements (BR-001–BR-010), enterprise risks (R-001–R-015), security requirements (SEC-001–SEC-015), and technical requirements (TR-001–TR-016). The [P02-01 regulatory applicability and PCI scope baseline](regulatory-applicability-and-pci-scope.md) establishes regulatory assumptions, including AFG's modeled payment-partner tokenization arrangement. The Phase 1 landing-zone architecture supplies the management-group and subscription design context.

A control may support several obligations, but **a thematic mapping does not establish that a specific regulatory clause is satisfied**. Legal applicability, PCI DSS system scope, precise obligation-to-control mapping, implementation, and effectiveness require further review and evidence.

## 2. Framework Design Principles and Prioritization

1. **Organize by security outcome.** Define shared control objectives once and map regulatory drivers to them rather than duplicate controls by regulation.
2. **Maintain traceability.** Preserve the chain: regulatory or business driver → control objective → existing requirement and risk → architecture decision or dependency → Azure mechanism → planned validation → evidence.
3. **Preserve the baseline.** Control IDs below are *framework identifiers*, not new Phase 0 risks or SEC/TR requirements. Do not revise authoritative risk scores or requirement IDs through this document.
4. **Separate design from operation.** A documented control, proposed owner, or planned test is not proof of deployment, compliance, or risk treatment.
5. **Apply policy by appropriate scope.** Management-group assignment inheritance creates consistent coverage, not automatic resource compliance. Effects, exclusions, resource applicability, and remediation must be assessed.
6. **Introduce enforcement responsibly.** Exception handling, ownership, impact assessment, and audit-first testing precede broad disruptive deny enforcement.
7. **Minimize overhead.** Keep detailed Azure Policy design in #24, guardrail design in #25, monitoring/evidence architecture in #26, exception procedure in #27, operating model in #28, and representative validation in #29.

### Initial priority: GOV-01 — Enterprise Guardrail Inheritance

GOV-01 is prioritized because it addresses critical risk **R-001** and supports **BR-001**. Assigning approved policies at appropriate management-group scopes can reduce repetitive subscription-level administration and make onboarding more consistent. Reduced onboarding cost is an **expected benefit to measure**, not a validated result. Its prerequisites include the Phase 1 hierarchy and subscription placement model; its safe operation depends on policy lifecycle, owner identification, exceptions, and monitoring.

## 3. Control Domains

| Domain | Intended security outcome | Controls |
| --- | --- | --- |
| GOV — Governance | Consistent guardrails, policy lifecycle, approved exceptions | GOV-01–GOV-04 |
| OWN — Ownership | Discoverable accountable resource ownership | OWN-01 |
| CFG — Secure Configuration | Repeatable, auditable changes | CFG-01 |
| IAM — Identity and Access | Restricted privilege and secure workload permissions | IAM-01–IAM-02 |
| NET — Network Security | Reduced unnecessary public exposure | NET-01 |
| MON — Monitoring | Required telemetry and managed detections | MON-01–MON-02 |
| DAT — Information Protection | Sensitivity-based production and non-production safeguards | DAT-01–DAT-02 |
| RES — Resilience | Tested recovery for critical workloads | RES-01 |
| AI — AI Security | AI-specific security and data-flow review | AI-01 |

## 4. Enterprise Control Inventory and Traceability

**Status of every control:** Proposed / not validated. The controls describe *intended* mechanisms and do not select or attest to deployed configurations. Assigned functional owners below are proposed for planning and must be confirmed under Issue #28. The indicated delivery phase refers to the existing roadmap, not completion.

| ID | Control objective | Source risk / business requirement | Existing security / technical requirements | Architecture dependency and proposed Azure mechanism | Proposed coordinating owner | Primary delivery phase |
| --- | --- | --- | --- | --- | --- | --- |
| **GOV-01** | Ensure new subscriptions inherit appropriate enterprise guardrails | R-001; BR-001 | SEC-006, SEC-015; TR-001, TR-002 | Phase 1 management-group hierarchy and subscription placement; scoped Azure Policy assignments | Cloud Platform / Governance | 1–2 |
| **GOV-02** | Maintain modular, governed policy controls | R-001; BR-001 | SEC-006; TR-003 | Policy initiatives grouped by purpose and owner; version-controlled definitions | Cloud Governance | 2 |
| **GOV-03** | Introduce enforcement with assessed business impact | R-006, R-007; BR-002 | SEC-007, SEC-014; TR-004 | Audit-first lifecycle, impact reviews, staged deny and remediation planning | Cloud Governance / Security | 2 (design); 2/6 (change dependencies) |
| **GOV-04** | Approve, scope, time-limit and review exceptions | R-006; BR-002, BR-005 | SEC-007; TR-004 (supporting) | Azure Policy exemptions paired with externally recorded approval and residual-risk decisions | Governance / Security | 2 |
| **OWN-01** | Identify accountable owners of critical resources | R-008; BR-003 | SEC-009; TR-005 | Ownership and criticality metadata standard; policy-assisted tagging and inventory | Cloud Governance | 2 |
| **CFG-01** | Make platform changes repeatable and auditable | R-007; BR-007 | SEC-008, SEC-014; TR-012, TR-013 | Reviewed Terraform/Bicep and CI checks; change history and audit records | Platform Engineering | 6 (supporting Phase 2 governance) |
| **IAM-01** | Restrict privileged administrative access | R-002 | SEC-001; TR-006 | Entra PIM where supported and Azure RBAC least privilege | Identity / Security | 3 |
| **IAM-02** | Secure workload identities and high-privilege application permissions | R-003 | SEC-002, SEC-003; TR-007 | Managed identity/federation patterns, app-permission ownership and periodic review | App / Identity Security | 3/6 |
| **NET-01** | Minimize unjustified public exposure | R-004 | SEC-004; TR-008, TR-009 | Approved ingress and private endpoint/segmentation patterns; applicable policy checks | Network / Workload Owners | 4 |
| **MON-01** | Collect required security-relevant telemetry | R-005; BR-009 (supporting) | SEC-005; TR-010 | Azure Monitor diagnostic settings and applicable AMA/DCR patterns | Security Operations | 5 |
| **MON-02** | Govern security detections through their lifecycle | R-011 | SEC-012; TR-011 | Sentinel detection ownership, testing, review, version control and retirement | Security Operations | 5/6 |
| **DAT-01** | Protect financial and other data according to documented sensitivity | R-009 | SEC-010; TR-014 | Classification-led access, encryption and Microsoft Purview patterns | Data Governance | 7 |
| **DAT-02** | Safeguard production-like data in non-production environments | R-015 | SEC-010; TR-014 (supporting) | Data minimization, masking/synthetic data and environment isolation patterns | Data / App Owners | 7 |
| **RES-01** | Establish and test Tier 1 recovery arrangements | R-010; BR-004 | SEC-011; no dedicated TR stated | Approved RTO/RPO, recovery architecture and representative recovery tests | Platform / Workload Owners | 1/5 |
| **AI-01** | Require AI-specific security and data-flow review | R-012; BR-008 | SEC-013; TR-015 | Review AI identity, model/agent tools, connected data and monitoring requirements | AI Governance / Security | 8 |

**Additional risk coverage:** R-013 (hybrid/Arc governance) is a cross-cutting applicability consideration for GOV-01 and MON-01; R-014 (Defender coverage) is a supporting posture/monitoring consideration for MON-01. Their coverage is **partial** and their Phase 0 treatment and delivery phases remain unchanged. These mappings do not replace dedicated later-phase assessments.

**Evidence publication:** TR-016 applies across all controls when publishing architecture evidence: do not expose real secrets or confidential identifiers. TR-016 is **not** a substitute for SEC-014's auditable administrative changes.

## 5. Regulatory and Business Driver Crosswalk

| Driver | Candidate framework controls | Applicability / mapping status |
| --- | --- | --- |
| PCI DSS v4.0.1 — modeled payment service-provider environment | IAM-01, IAM-02, NET-01, MON-01, CFG-01, DAT-01 | Thematic candidate relationships only. System boundaries, actual applicable PCI requirements and service-provider validation method remain to be assessed under the P02-01 assumptions. |
| PCI DSS — payment-partner assurance and boundary responsibilities | GOV-04, CFG-01, DAT-01 (supporting) | **Coverage gap:** None of these alone establishes partner assurance or scope validation. Payment-partner responsibility and cardholder-data exclusion remain payment-specific candidates identified in P02-01. |
| GLBA / FTC Safeguards Rule and banking partner requirements | IAM-01, IAM-02, DAT-01, MON-01, CFG-01 | Direct legal applicability undetermined; contractual safeguards require separate review. Do not treat these mappings as a Safeguards Rule compliance conclusion. |
| State privacy, data-security and breach-notification obligations | DAT-01, MON-01 | Jurisdiction, data, entity role and statutory applicability remain unresolved. |
| Internal enterprise governance and risk management | GOV-01–GOV-04, OWN-01, CFG-01 | Enterprise governance driver; maps to existing Phase 0 business and risk requirements. |
| NIST CSF 2.0 / CIS Controls | Applicable framework controls across domains | Voluntary organizing references; no full category or safeguard crosswalk is claimed. |

This framework does **not** register new payment requirements, establish PCI scope definitively, or substitute for the full regulatory applicability assessment. Transaction integrity, replay/duplicate prevention, payment-partner responsibility, and cardholder-data exclusion validation remain **provisional requirement gaps** in P02-01 pending appropriate requirements review.

## 6. Planned Validation and Evidence

| Controls | Planned validation approach | Expected evidence (not yet collected) |
| --- | --- | --- |
| GOV-01, GOV-02 | Inspect intended assignments and inherited scopes; inspect initiative composition | Assignment exports, scope diagram, policy definitions and compliance observations |
| GOV-03, GOV-04 | Exercise test/audit-to-enforcement workflow and exemption scoping, ownership and expiration | Test results, documented approvals, exemption records, remediation plan |
| OWN-01 | Assess required metadata coverage and owner discoverability | Resource inventory, tagging coverage report, owner review |
| CFG-01 | Check IaC change and pipeline control operation | Pull requests, CI validation, change/deployment records |
| IAM-01, IAM-02 | Inspect privileged roles, workload identities and application permission governance | Role and permission reviews, configuration exports, access review evidence |
| NET-01 | Test exposure and approved segmentation patterns | Configuration inventory, connectivity and exposure test results |
| MON-01, MON-02 | Verify logging coverage and representative detection behavior | Diagnostic configurations, collection results, alerts, detection-test records |
| DAT-01, DAT-02 | Review classification-driven controls and non-production data handling | Data classification assessment, access/encryption configurations, masking test results |
| RES-01 | Exercise representative recovery and compare with stated objectives | Recovery test report and RTO/RPO comparison |
| AI-01 | Review representative AI workload identity, data movement, agent/tool permissions | Threat review, data-flow assessment, permission and monitoring evidence |

Evidence must be labeled **modeled**, **observed**, or **validated** as appropriate; the present document is modeled. Where real evidence is eventually captured, sanitize it consistent with TR-016. Detailed monitoring architecture is #26 and representative deployment/testing is #29; later specialist phases validate their own controls.

## 7. Governance Effectiveness Measures

| Metric | Proposed measure / target | Status |
| --- | --- | --- |
| Subscription baseline assignment coverage | Target 100% of applicable production subscriptions with intended inherited assignments before production use; separately measure actual policy compliance | Target, not verified |
| Resource ownership metadata coverage | Target ≥95%, consistent with BR-003 | Target, not verified |
| Exception governance completeness | Target 100% of approved exceptions recorded with owner, rationale, scoped applicability and review/expiration date | Proposed target |
| Subscription onboarding administrative effort | Measure baseline and post-standardization hours and manual steps; quantify improvements rather than assume savings | Measurement not established |
| Policy compliance and remediation | Track applicable policy compliance rates, noncompliant resources, exceptions and remediation age by scope | Baseline/targets pending |

Coverage is not equivalent to compliance, and these targets do not establish actual risk reduction or operating-cost savings.

## 8. Delivery Boundaries, Ownership and Open Dependencies

**Proposed ownership is not formal assignment.** The operating model, approvers, escalation routes and exception decision rights will be specified in Issue #28. The enterprise risk register's accountable teams remain the Phase 0 reference; operational SharePoint tracking remains the source for risk ownership and acceptance. GitHub maintains this version-controlled architecture baseline.

| Follow-on issue | Responsibility / boundary |
| --- | --- |
| #24 — Azure Policy Governance Architecture | Policy initiatives, management-group assignment scopes, inheritance and lifecycle detail |
| #25 — Preventive, Detective and Corrective Guardrails | Specific guardrail mechanisms and control effects |
| #26 — Compliance Monitoring and Evidence Architecture | Reporting, evidence sources, retention and monitoring design |
| #27 — Governance Exception and Risk-Acceptance Process | Exception workflow, approval authority, expiry and compensating controls |
| #28 — Governance Roles and Operating Model | Confirmed RACI, owners, escalation and accountability |
| #29 — Representative Control Implementation and Validation | Low-cost Azure lab deployment, tests and evidence |
| #30 — Architecture Review | End-to-end consistency, requirements traceability and milestone exit review |

**Open dependencies:** Verify source-specific regulatory clauses and applicability; finalize payment-system PCI boundaries and partner responsibilities; confirm Phase 1 scope names before designing assignments; review provisional payment-specific requirements; confirm functional control owners; collect actual validation evidence only in appropriate workstreams.

**Architecture status:** No controls are asserted to be approved, implemented, tested, or compliant by virtue of this framework. Final Issue #23 closure requires repository review against the issue objective and a committed baseline.
