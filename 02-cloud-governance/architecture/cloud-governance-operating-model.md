# P02-07 — Cloud Governance Roles, Accountability and Operating Model

| Attribute | Value |
|---|---|
| Enterprise | AFG Enterprises (fictional, modeled) |
| Phase | 02 — Cloud Governance & Compliance |
| GitHub issue | #28 — P02-07 |
| Design decision | Federated governance: centralized standards, distributed implementation and accountability |
| Status | Proposed architecture baseline — pending repository review and organizational approval |
| Evidence classification | Modeled operating model; no formal delegation or operating cadence validated |
| Principal risk and control references | R-001, R-006, R-007, R-008; GOV-01–GOV-04, OWN-01, CFG-01 |

## 1. Purpose and scope

Define the organizational responsibilities, decision rights, RACI, review cadence, escalation, and measures required to operate AFG's cloud governance controls at enterprise scale. This model applies to Azure management-group and subscription governance, Azure Policy, selected policy-as-code checks, compliance evidence, and workload remediation.

This document **does not** create a new committee, reassign real personnel, or grant approval authority. It is a proposed enterprise design. Azure Policy architecture is defined in P02-03 (#24), guardrail design in P02-04 (#25), monitoring/evidence in P02-05 (#26), and the detailed exception lifecycle and duration limits in P02-06 (#27). Representative implementation and validation belong to #29.

Authoritative design dependencies:

- [Phase 0 enterprise risks](../../00-enterprise-assessment/risks/enterprise-risk-register.md) and [traceability matrix](../../00-enterprise-assessment/assessment/traceability-matrix.md)
- [Phase 0 business, security and technical requirements](../../00-enterprise-assessment/requirements/)
- [Phase 1 management-group and subscription design](../../01-azure-landing-zone/architecture/management-group-subscription-design.md)
- [Cloud security control framework](../compliance/cloud-security-control-framework.md)
- [Azure Policy governance architecture](azure-policy-governance-architecture.md)
- [Security guardrail design](security-guardrail-design.md)
- [Compliance monitoring and evidence architecture](../compliance/compliance-monitoring-and-evidence-architecture.md)
- [Governance exception and risk acceptance](../exceptions/governance-exception-and-risk-acceptance.md)

## 2. Selected governance model

**Decision — Federated cloud governance.** Enterprise Architecture and Cloud Security set reusable architecture and security standards. Cloud Platform Engineering maintains shared governance tooling and policy deployment. Workload owners are accountable for workload configuration and remediation. Security Operations owns incident-response coordination. Compliance/Risk oversees risk and compliance process integrity and reporting. Authorized Business Risk Owners accept residual business risk under documented delegations.

Design principles:

1. **One enterprise standard, many accountable implementers.** Inherit applicable guardrails from the highest appropriate Azure management-group scope; avoid per-team divergence without review.
2. **Separate advisory, technical, and business decision rights.** Security assessment is not equivalent to residual-risk acceptance; technical implementation is not approval.
3. **Maintain least privilege and change control.** Policy definition changes, assignments, exemptions and automated remediation require scoped access and review.
4. **Use existing systems.** SharePoint is the operational findings, exception and risk system of record; GitHub is the version-controlled architecture and policy-as-code baseline.
5. **Govern by measured outcomes.** Assignment coverage, evaluated compliance, validated effectiveness and business disruption are different measures.
6. **Keep evidence honest.** Do not equate proposed standards, successful pipelines, or compliance scores with tested protection or regulatory certification.

## 3. Functional roles and accountability boundaries

| Function | Primary responsibility | Explicit boundary |
|---|---|---|
| Enterprise / Security Architecture (ARCH) | Defines architecture principles, cross-domain design decisions, approved target patterns and architecture review criteria | Does not independently authorize business risk acceptance |
| Cloud Security (CSEC) | Defines security control objectives, applicability, rollout safeguards, technical risk assessments and security review | Does not independently implement all workload fixes or accept business risk |
| Cloud Platform Engineering (PLAT) | Maintains shared management-group policy deployment, initiative assignments, policy-as-code integration, technical exemptions and approved remediation tooling | Cannot self-authorize exemptions or residual-risk acceptance |
| Workload / Application Owner (WORK) | Owns business service configuration, impact assessment, remediation, IaC changes and service reliability | Cannot silently bypass inherited controls |
| Security Operations (SOC) | Owns security detection/incident triage, incident coordination, response evidence and operational security escalations | Is not default owner of routine Azure Policy configuration |
| Compliance / Risk (RISK) | Maintains risk and exception process integrity, regulatory interpretation coordination, evidence governance, review schedules and risk reporting | Does not substitute for accountable business risk owner |
| Business Risk Owner (BIZ) | Owns residual business risk, approves/rejects acceptance within delegated authority and funds remediation tradeoffs | Authority must be formally delegated and escalated by severity |

The seven functions are roles in a modeled operating structure, not necessarily seven organizational departments. One person may support multiple functions where staffing requires it, but incompatible approval and implementation duties must remain separated through independent review.

## 4. Decision-rights model

| Decision | Proposed accountable authority | Technical execution / advice | Gate |
|---|---|---|---|
| Establish enterprise architecture standards | ARCH | CSEC, PLAT, WORK, RISK consulted | Reviewed decision recorded in Git |
| Define security objectives and guardrail applicability | CSEC | ARCH, PLAT, WORK, RISK consulted | Risk and requirement traceability |
| Approve deployment of a reviewed policy change | Delegated platform/change authority, defined during operating-model adoption | PLAT deploys; CSEC reviews security impact; WORK reviews business impact | Peer review, compatibility evidence, rollback plan |
| Change management-group assignment or subscription placement | Delegated cloud governance/change authority | PLAT executes; ARCH reviews boundary changes; WORK consulted | Phase 1 placement rules and impact assessment |
| Approve business risk acceptance | BIZ or designated executive risk authority per severity | CSEC assesses; RISK confirms governance requirements; PLAT implements authorized exemption | Signed/recorded approval before routine implementation |
| Execute approved technical exemption | PLAT | RISK verifies approval; CSEC checks technical scope | Scope/expiry match approved record |
| Remediate workload misconfiguration | WORK | PLAT assists with shared controls; CSEC advises | Source IaC updated and control re-evaluated |
| Coordinate security incident response | SOC | PLAT and WORK act as technical responders; CSEC advises | Established incident severity and response process |
| Approve regulatory interpretation and required control evidence | Authorized Compliance/Legal authority (to be named) | RISK coordinates; CSEC/ARCH map controls | Cannot waive applicable law by internal exception |

**Delegation gap:** AFG must identify actual named decision authorities, substitutes, role-based permissions and quorum/escalation rules before describing these decisions as operationally approved. No policy deployer receives implied risk acceptance authority through this table.

## 5. Proposed RACI

R = Responsible for execution; A = Accountable for outcome/decision; C = Consulted; I = Informed; — = not routinely involved. Each row has one primary A. The approval of risk acceptance is distinct from the technical exemption operation.

| Governance activity | ARCH | CSEC | PLAT | WORK | SOC | RISK | BIZ |
|---|---|---|---|---|---|---|---|
| Enterprise cloud architecture baseline | A/R | C | C | C | I | C | I |
| Security guardrail standard and applicability | C | A/R | C | C | C | C | I |
| Deploy versioned Azure Policy initiatives/assignments | C | C | A/R | I | I | I | I |
| Maintain centrally governed OPA/Rego policy definitions and tests | C | A | R | C | I | I | I |
| Consume approved OPA/Rego policies in workload CI | I | C | C | A/R | I | I | I |
| Correct workload configuration and IaC drift | I | C | C | A/R | I | I | I |
| Correct shared platform guardrail infrastructure | I | C | A/R | C | I | I | I |
| Assess security exposure and compensating safeguards | C | A/R | C | C | C | C | I |
| Accept or reject residual business risk | C | C | I | C | I | R | A |
| Implement approved Azure Policy technical exemption | I | C | A/R | C | I | C | I |
| Track exception lifecycle, approvals and expiration | I | C | C | C | I | A/R | C |
| Collect and publish technical governance evidence | I | C | R | C | C | A | I |
| Detect and coordinate security incidents | I | C | R | R | A | I | I |
| Quarterly enterprise risk reporting | C | C | C | C | C | A/R | I |

**RACI nuance:** The accountable authority for *deploying* policy changes is the delegated platform/change authority, not permission to alter policy intent unilaterally. The RACI assigns PLAT operational accountability for the technical deployment task; the prior decision gate remains mandatory. The risk owner recorded as `BIZ` must be the properly authorized individual or body, not simply any application stakeholder.

## 6. Policy-as-code ownership and distribution

- **AFG target enterprise architecture:** Centrally governed versioned OPA/Rego policy repository with review, tests, pinned releases and controlled distribution to consuming CI workflows. Cloud Security is accountable for security policy intent and content; Platform Engineering maintains distribution/engineering integration; workload teams consume approved versions and remediate violations.
- **Current low-cost portfolio implementation boundary:** GR-02 storage public network access policy may remain alongside existing Terraform lab code. A separate repository is **not required** for the Phase 2 demonstration.
- **Separation trigger:** Revisit a distinct policy repository when two or more independent workload repositories require reusable policies, security release permissions need a separate lifecycle, or central distribution becomes an operating requirement.
- **Change governance:** Require test fixtures with expected pass/fail outcomes, peer review, approved versions, recorded exceptions for authorized bypasses, and rollback to a known policy release. Do not distribute mutable unpinned policy references to production pipelines.
- **Control scope:** OPA/Rego provides pre-deployment policy evaluation; Azure Policy provides supported Azure control-plane enforcement and compliance assessment. Their results are complementary, not interchangeable.

Broad CI/CD security architecture and additional application-security gates remain in Phase 6. Issue #29 implements only representative GR-02 validation when approved.

## 7. Exception and risk acceptance handoff

The authoritative eight-stage lifecycle and initial maximum exception durations remain defined in [P02-06](../exceptions/governance-exception-and-risk-acceptance.md). This operating model only assigns ownership at the handoff points:

1. WORK/BIZ requests a deviation and supplies business impact and remediation intent.
2. CSEC evaluates technical exposure and recommended compensating controls; RISK checks completeness and regulatory implications.
3. A properly delegated BIZ/executive authority accepts or rejects residual risk using the P02-06 severity model.
4. PLAT implements **only** the approved, narrowly scoped Azure Policy exemption; RISK links it to the SharePoint decision record.
5. RISK monitors expiry/review and escalation; WORK owns correction; CSEC verifies control outcome where applicable.
6. Expiry, renewal or closure follows P02-06; no automatic renewal or implementer self-approval.

The modeled P02-06 initial limits—Low 180 days; Medium 90; High 30; Critical 7—are not a blanket authorization to tolerate prohibited exposure. Legal or contractual noncompliance cannot be waived by an internal business owner.

## 8. Operating cadence and escalation

| Cadence | Proposed forum/process | Steward | Decisions / outputs |
|---|---|---|---|
| Weekly | Operational control and remediation review | PLAT + CSEC; WORK participates | New policy failures, overdue remediation, rollout impacts, approaching expiries; update SharePoint actions |
| Monthly | Cloud security governance review | CSEC + RISK | Control coverage, compliance trends, exception aging, policy-change backlog, evidence quality |
| Quarterly | Enterprise architecture and risk review | ARCH + RISK with BIZ decision authorities | Material residual risks, policy standard changes, risk trends, investment priorities and unresolved escalations |
| Event-driven | Critical security incident | SOC | Activate incident process; capture containment, technical actions and executive notification as required |
| Event-driven | Emergency security exception / urgent production outage | Authorized emergency change/risk authority | Constrained action and follow-up review per P02-06; record scope, approval, and expiry |
| Event-driven | New acquisition, regulated workload or subscription reclassification | ARCH + CSEC + PLAT + WORK | Reassess inherited policies and business/technical boundary before transition |

Escalate outside the routine cadence for: critical exposures; policy rollouts causing production disruption; exceptions approaching expiry without a treatment plan; statutory/contractual conflicts; repeated unauthorized policy bypass; a material gap in evidence collection; or disagreement between the business risk owner and security recommendation. Escalation must identify the accountable decision authority and interim protective measures, rather than assuming Security can unilaterally accept the risk.

## 9. Monitoring and governance measures

| Measure | Proposed target / interpretation | Proposed reviewer |
|---|---|---|
| Production subscription baseline inheritance | 100% of applicable production subscriptions before production use; coverage does not imply compliance | PLAT / CSEC weekly or monthly |
| Critical resource ownership metadata | ≥95% of applicable resources (BR-003); denominator and exceptions documented | WORK / RISK monthly |
| Exception record completeness | 100% of active approved exceptions with approval, owner, control, scope, rationale and review/expiry date | RISK weekly |
| Exception aging and overdue remediation | Report by severity, owner and age; set service-level targets after baseline | RISK + BIZ monthly |
| Azure Policy evaluated compliance | Baseline by scope, policy and applicability; track trend not score alone | CSEC / PLAT monthly |
| Governance-related deployment disruption | Count, investigate and reduce inappropriate denials, false positives and outages | PLAT / WORK weekly |
| Evidence completeness/freshness | Track missing/expired proof for selected critical control assertions | RISK monthly |
| Policy-as-code adoption and release drift | Track versions consumed by intended pipelines and approved exceptions | PLAT / CSEC monthly |

Measurement definitions and detailed evidence specifications reside in P02-05 (#26). No observed AFG results or operational savings are claimed here.

## 10. Escalation and separation-of-duties checks

At implementation time, review at least these failure modes:

- A platform engineer can both create and approve a policy exemption: **not permitted** without independent business authorization.
- A workload owner changes the assigned risk rating to gain longer approval duration: **RISK/CSEC must review classification independently**.
- A policy release breaks a production deployment: follow approved rollback/change procedures, investigate impact and track residual exposure.
- A compliance dashboard shows green but test telemetry is absent: classify evidence as **insufficient**, not effective.
- A critical risk exception is requested during an incident: use the designated emergency authority and post-incident review, not the routine low-risk process.
- A new acquired subscription is moved into `Legacy`: ownership, risk treatment, placement rationale and exit criteria remain mandatory.

## 11. Traceability

| Architecture outcome | Enterprise sources | Existing control | Evidence / follow-on work |
|---|---|---|---|
| Inherited, accountable enterprise guardrails | R-001; BR-001; SEC-006, SEC-015; TR-001–TR-003 | GOV-01, GOV-02 | #29 assignment inheritance and coverage validation |
| Governed enforcement and changes | R-006, R-007; BR-002, BR-007; SEC-007, SEC-008, SEC-014; TR-004, TR-012, TR-013 | GOV-03, CFG-01 | #29 representative policy and CI controls |
| Approved and monitored exceptions | R-006; SEC-007 | GOV-04 | P02-06 SharePoint workflow specification; #29 technical test |
| Named workload and remediation accountability | R-008; BR-003; SEC-009; TR-005 | OWN-01 | GR-01 ownership test; P02-05 evidence mapping |
| Security telemetry and incident coordination | R-005, R-011; SEC-005, SEC-012; TR-010, TR-011 | MON-01, MON-02 | Phases 5 and #26 evidence definition |
| Brownfield/acquired service onboarding | R-013; BR-006, BR-010; SEC-015 | GOV-01, GOV-03 | Phase 1 hierarchy and transition validation |

## 12. Completion, validation and unresolved adoption decisions

**P02-07 design can close when:** the seven functions, decision boundaries, RACI, policy-as-code stewardship, operational cadence, escalation triggers, metrics and dependency links are reviewed and committed. This establishes a **modeled architecture design**, not a formally operating governance organization.

**Operational adoption decisions still required:** named authorities and alternates; security/architecture approval delegation; change authority and emergency delegation; segregation-of-duties implementation; reporting access; cadence approval; policy release controls; SharePoint workflow configuration; service levels and agreed response targets.

**Representative validation planned under #29:** inspect actual policy assignment ownership and permissions; test an authorized technical exemption with an independently represented approval record; verify that policy and IaC evidence identify their source and scope. No completed tests or organizational approvals are asserted in this document.

**Phase 2 closeout (#30):** verify that the governance operating model aligns with the Phase 0 requirements and other Phase 2 architecture artifacts and that any tested controls have separate dated, sanitized evidence.
