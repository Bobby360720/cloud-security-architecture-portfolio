# P02-03 — Azure Policy Governance Architecture

| Attribute | Value |
|---|---|
| Enterprise | AFG Enterprises (modeled) |
| Phase | 2 — Cloud Governance & Compliance |
| Related GitHub issue | #24 — P02-03 |
| Status | Proposed architecture baseline — pending review and validation |
| Evidence classification | Modeled design; no policy deployment or control effectiveness claimed |
| Primary risks | R-001, R-006 |
| Supporting risks | R-007, R-008, R-013 |
| Primary controls | GOV-01 through GOV-04; supporting OWN-01 and CFG-01 |

## 1. Purpose and boundaries

This document defines how AFG will organize, assign, evaluate, enforce, remediate, and govern Azure Policy across the Phase 1 management-group and subscription model. It translates the Phase 0 requirements and the Phase 2 cloud security control framework into a proposed technical governance architecture.

**In scope:** policy initiative organization, assignment and inheritance boundaries, progressive rollout, enforcement and remediation patterns, policy exemptions, functional ownership, and planned validation evidence.

**Out of scope:** a catalog of individual policy definitions and detailed guardrail effects (Issue #25); full compliance reporting architecture (Issue #26); risk acceptance workflow and approval thresholds (Issue #27); approved enterprise RACI (Issue #28); policy deployment and testing (Issue #29). Detailed identity, network, telemetry, and data protection architecture remains in its respective delivery phases.

Authoritative inputs:

- [Phase 1 management-group and subscription design](../../01-azure-landing-zone/architecture/management-group-subscription-design.md)
- [Phase 2 cloud security control framework](../compliance/cloud-security-control-framework.md)
- [Phase 0 enterprise risk register](../../00-enterprise-assessment/risks/enterprise-risk-register.md)
- [Phase 0 traceability matrix](../../00-enterprise-assessment/assessment/traceability-matrix.md)
- Phase 0 business, security, and technical requirements in `../../00-enterprise-assessment/requirements/`
- [P02-01 regulatory applicability and PCI scope baseline](../compliance/regulatory-applicability-and-pci-scope.md)

## 2. Architectural decision and principles

**Decision — Progressive, risk-based enforcement (selected for the proposed Phase 2 design).** AFG will establish common policy visibility at the highest appropriate management-group scope, assess applicability and operational impact, address findings and exceptions, and enable preventive enforcement in controlled increments. New subscriptions must receive the applicable *approved and validated* baseline before production use. Brownfield and acquired subscriptions follow compatibility assessment and risk-prioritized transition.

**Rationale:** This addresses fragmented governance (R-001) while reducing the chance that new restrictive assignments disrupt business-critical or legacy workloads (R-006; BR-002). Central policy inheritance is expected to reduce repeated assignment administration, but cost savings and compliance improvements must be measured rather than presumed.

Principles:

1. **One control intent, reusable assignments.** Reuse existing enterprise control IDs and requirements; do not duplicate a policy solely to serve each regulation.
2. **Highest appropriate scope, not highest possible scope.** Assign a control where it consistently applies; specialize at children or subscriptions only when justified.
3. **Evaluation is not enforcement or compliance.** `audit` reports selected noncompliance; `deny` can prevent certain requests; an assignment with `enforcementMode: DoNotEnforce` evaluates without enforcing eligible effects. Actual results depend on policy definition, resource applicability, exclusions, and evaluation timing.
4. **Brownfield-safe rollout.** Validate impact before enabling disruptive effects; new subscriptions may enforce an already validated baseline immediately upon governed onboarding.
5. **Exception before workaround.** Do not silently remove inherited assignments to accommodate workloads; document and technically scope approved deviations.
6. **Remediate at source.** For Terraform/Bicep-managed resources, update source configuration and avoid permanent drift between declarative templates and policy remediation.
7. **Evidence integrity.** Keep modeled decisions, lab observations, and validated outcomes distinct. Do not expose secrets or sensitive identifiers in published evidence (TR-016).

## 3. Management-group inheritance and assignment model

The hierarchy below is the **Phase 1 target design**, not a claim that every node or subscription has been deployed. Production and non-production are subscription classifications, **not** additional management groups.

```text
Tenant Root Group
└── AFG
    ├── Platform
    │   ├── Identity
    │   ├── Management
    │   ├── Connectivity
    │   └── Security
    ├── Landing-Zones
    │   ├── Corp
    │   ├── Online
    │   └── Legacy
    ├── Sandbox
    ├── Decommissioned
    └── Onboarding
```

`Onboarding` is the planned restrictive holding management group for subscriptions created outside governed vending (Phase 1 ALZ-DEC-008); its deployment must be checked separately. Approved vending assigns subscriptions directly to their intended management group. `Legacy` is transitional, not a permanent reduced-security alternative. Production/non-production differences are normally expressed through subscription-scoped policy-as-code assignments within `Corp` or `Online`.

| Assignment scope | Proposed assignment intent | Notes / constraints |
|---|---|---|
| Tenant Root Group | Exceptional Azure Resource Manager controls requiring tenant-wide scope | Avoid broad workload policy here. |
| AFG | Common enterprise governance visibility and universally applicable baseline | Evaluate impact across Platform, Landing-Zones, Sandbox, Decommissioned, and Onboarding before enforcing. |
| Platform | Shared platform service baseline | Child branches inherit relevant enterprise controls. |
| Platform / Identity | Configuration controls for Azure-hosted identity infrastructure if justified | Tenant-level Entra/Okta capabilities alone do not require an identity subscription. |
| Platform / Management | Management-plane resource safeguards | Avoid policies that impede required monitoring/management services. |
| Platform / Connectivity | Network platform configuration safeguards | Permit intentionally required public/network infrastructure through policy applicability or reviewed exceptions. |
| Platform / Security | Security platform configuration safeguards | Protect security tooling without obstructing its approved functions. |
| Landing-Zones | Shared business-workload baseline | Applies to Corp, Online, and Legacy subject to policy applicability and justified exceptions. |
| Landing-Zones / Corp | Controls applicable to workloads dependent on corporate/hybrid connectivity | Connectivity patterns follow Phase 1 placement criteria. |
| Landing-Zones / Online | Controls applicable to independently connected digital services | Public-facing business requirements do not imply unrestricted backend access. |
| Landing-Zones / Legacy | Transitional audit and remediation visibility plus compatible enterprise guardrails | Time-bound exceptions and migration/retirement criteria required. |
| Sandbox | Experimentation-focused restrictions and data-handling visibility | Limit production data and unnecessary production connectivity; budgets are handled through Cost Management, not assumed to be Azure Policy effects. |
| Decommissioned | Restrict new deployment or unauthorized change while preserving retention/retirement activities | Test compatibility with legitimate decommissioning steps before enforcement. |
| Onboarding | Restrictive holding controls pending ownership, classification, and placement | Must not break necessary onboarding, investigation, or reassignment operations. |
| Selected subscriptions/resource groups | Validated environment- or workload-specific assignments | Use centrally maintained policy-as-code; do not add production/nonproduction management groups by default. |

**Inheritance rule:** A child receives applicable assignments from ancestor scopes unless the resource/assignment is excluded or appropriately exempted. Assignment inheritance is not evidence that deployed resources comply. Avoid redundant child assignments of the same control without a documented reason.

## 4. Modular policy initiative architecture

The following are **logical initiative families**, not published policy definition names or an assertion that four initiatives have already been created. Individual policy selection, parameters, effect choices, and effect compatibility are addressed in Issue #25.

| Family | Objective | Candidate placement | Primary framework references | Proposed stewardship |
|---|---|---|---|---|
| Core Governance | Common governance metadata, scope visibility, approved-location controls where universally justified | AFG | GOV-01, OWN-01 | Cloud Governance / Cloud Platform |
| Platform Security | Resource safeguards specific to shared connectivity, management, and security platforms | Platform and relevant children | GOV-02, CFG-01 | Cloud Platform with service owners |
| Workload Security | Workload exposure, configuration, and data-service control expectations | Landing-Zones; Corp/Online specializations | GOV-02, NET-01, DAT-01 | Cloud Security Architecture with workload teams |
| Lifecycle Governance | Admission, experimentation, transitional, and retirement controls | Onboarding, Sandbox, Legacy, Decommissioned | GOV-03, GOV-04, OWN-01 | Cloud Governance / Cloud Platform |

Composition rules:

- Use Microsoft built-in policy definitions where they meet the desired outcome; use custom definitions only for a documented gap.
- Version initiative definitions and assignments in Git. Record each initiative's purpose, parameters, applicable scopes, owner, and mapping to enterprise control IDs.
- Keep shared controls at parent scopes where safe; specialize through assignment parameters or child-scope assignments where required.
- Do not presume all identity, networking, payment-integrity, resilience, or contractual safeguards can be enforced by Azure Policy. Document out-of-band controls and owners in the security control framework.
- Actual Azure Policy limits, supported effects, aliases, and remediation prerequisites must be verified against selected definitions before implementation.

## 5. Progressive evaluation and enforcement lifecycle

| Stage | Required design activity | Exit gate / decision evidence |
|---|---|---|
| 1. Define | Map proposed control to source risk, requirement, initiative, effect, owner, target scope, and business impact. | Reviewed control specification and assignment proposal. |
| 2. Evaluate safely | Test policy definition/parameters on representative sandbox or nonproduction resources using audit effects or `DoNotEnforce` as appropriate. | Compatibility results and list of affected resource types; note that non-enforcing mode is not the same as changing effects to audit. |
| 3. Assess impact | Identify noncompliance, deployment conflicts, legitimate exceptions, and dependencies across platform, workload, legacy, and acquired subscriptions. | Workload-owner impact review and enforcement readiness decision. |
| 4. Remediate / authorize deviations | Assign corrective actions and approve narrowly scoped exemptions where necessary. | Remediation plan and approved, reviewable exception references. |
| 5. Enforce incrementally | Enable validated preventive effects for selected scopes/cohorts, monitor failures and apply rollback steps if needed. | Approved change, monitored rollout, and actual enforcement test results. |
| 6. Operate and improve | Reassess drift, exceptions, coverage, policy versions, and business impact. | Periodic metrics and evidence supporting ongoing governance review. |

**New versus existing subscriptions:** New subscriptions must inherit the approved applicable baseline before production onboarding (SEC-015); the baseline itself still requires prior testing. Existing subscriptions may remain in audit/non-enforcing assessment during transition, with tracked remediation, time-limited exceptions, and escalation of critical exposures. There is no universal mandatory audit waiting period, and high-severity exposures may warrant earlier mitigation.

**Rollback design:** Record the prior assignment version, enforcement mode and parameters; approve the rollback authority; monitor its business/security consequences. Reverting a policy assignment does not necessarily reverse resource changes already performed by `modify` or `deployIfNotExists`.

## 6. Remediation architecture

| Pattern | Use when | Architecture conditions | Proposed operator |
|---|---|---|---|
| Manual workload remediation | Configuration change can affect application behavior or availability | Workload owner reviews change, modifies configuration, and validates outcome. | Workload Engineering |
| Policy remediation task | Supported `modify` or `deployIfNotExists` effect is appropriate for the resource type | Managed identity has least-privilege permissions; target scope, impact, idempotence, and task output reviewed. | Cloud Platform |
| IaC source correction | Resources are managed by Terraform/Bicep | Update authoritative source and validate resulting state; prevent recurring drift. | Platform / Workload Engineering |
| Temporary exception | Remediation is currently impractical or causes disproportionate business impact | Approved scope, risk owner, compensating controls, review/expiry and remediation path. | Authorized governance process; Cloud Platform implements |

A `deny` effect may stop noncompliant requests, but does not automatically repair existing resources. `modify`/`deployIfNotExists` effects have implementation-specific remediation prerequisites; a successful remediation task does not by itself establish that the security objective is met. Retain policy reassessment results and workload test evidence after remediation.

## 7. Policy exemption design boundary

Azure Policy exemptions are technical artifacts associated with relevant assignments; they do not themselves constitute risk acceptance. The detailed request, approval authority, escalation, and review workflow belongs to Issue #27.

Proposed requirements for each exception record:

- Reference to source risk and policy assignment/definition (and affected definition references when an initiative is involved).
- Business/technical owner, business justification, workload and resource scope.
- Applicable exemption category: `Waiver` for an accepted deviation or `Mitigated` for an alternative control that meets the intent, with supporting evidence.
- Approval record held in the operational SharePoint tracking system; Git records design and non-sensitive linkage, not a duplicate risk register.
- Review or expiration date for temporary exceptions, compensating controls where appropriate, remediation milestone and follow-up owner.
- Monitoring for expiry or scope changes; uncontrolled `notScopes` exclusions are not a substitute for a reviewed exception.

Exemptions should be as narrow as practicable. Resolve incorrect policy applicability or false positives in definitions/parameters where feasible instead of accumulating permanent exemptions. Review exceptional cases where expiry enforcement could cause significant disruption.

## 8. Functional ownership and segregation of duties

These are **proposed functional responsibilities**, not appointed individuals or approved risk-acceptance authority. Issue #28 will establish the detailed RACI.

| Activity | Proposed lead | Required collaboration / independent decision |
|---|---|---|
| Define control objective, applicability and architecture standard | Cloud Security Architecture | Cloud Governance, Compliance/Legal where relevant, platform/workload owners |
| Maintain initiative and assignment code | Cloud Platform Engineering | Security Architecture review, version-control reviewers |
| Assess deployment impact and remediate workload settings | Workload owner / engineering | Platform Engineering and Cloud Security |
| Approve rollout/change | Authorized change/platform authority (TBD) | Security and affected workload owners |
| Review compliance and exemption lifecycle | Cloud Governance / Security | Workload owners and Risk Management |
| Accept residual business risk | Authorized business risk owner (TBD) | Security/Governance advise; implementer does not self-approve risk acceptance |
| Apply approved technical exemption | Cloud Platform Engineering | Requires prior approved risk/exception record |
| Monitor related security signals | Security Operations | Platform and workload incident responders |
| Interpret specific regulatory obligations | Compliance / Legal | Security Architecture and relevant business owners |

## 9. Planned validation and evidence

The following tests are **planned for representative implementation under Issue #29**, not completed in Issue #24. Evidence must identify tested resources and date, distinguish observations from modeled enterprise assumptions, and exclude secrets or confidential identifiers.

| Test ID | Design assertion to validate | Planned method | Expected evidence |
|---|---|---|---|
| PV-01 | Applicable AFG parent assignments reach intended descendant subscriptions | Inspect policy assignment scopes and a representative child subscription; check inheritance after placement | Assignment exports, management-group path, scoped evaluation results |
| PV-02 | Specialized policies apply to the intended Corp/Online/platform scope only | Review assignments, parameters, exclusions and representative evaluation | Assignment/parameter records, in-scope/out-of-scope comparisons |
| PV-03 | Non-enforcing evaluation does not deny the tested noncompliant deployment | Run approved benign test with audit or `DoNotEnforce`, record compliance results | Test plan, policy state and sanitized deployment results |
| PV-04 | An approved enforced `deny` blocks the intended noncompliant operation | Repeat a representative low-cost test after approved enforcement | Rejected request evidence and successful compliant control test |
| PV-05 | A supported remediation mechanism corrects a modeled configuration gap | Run approved remediation task or IaC correction with narrowly scoped permissions | Managed identity role scope, task results, resource reassessment and source diff |
| PV-06 | Scoped exemption changes evaluation only where authorized and expires as planned | Create/test limited-duration exemption and compare resource compliance | Exemption JSON without sensitive fields, approval linkage, evaluation before/after |
| PV-07 | Subscription onboarding applies the approved baseline | Check placement and effective assignments for a newly vended/test subscription | Subscription placement export, assignment inheritance, onboarding checklist |
| PV-08 | Brownfield policy change avoids unforeseen operational interruption | Compare compatibility assessment, trial rollout and rollback readiness | Impact analysis, approved change, monitoring and test results |

**Cost control:** Prefer management-group and policy metadata inspection plus short-lived representative resources. Estimate deployment cost in advance; retain existing core lab subscriptions and tear down new test resources after validation. Some Azure Policy capabilities are free, while supporting services/resources and data ingestion may incur charges—confirm pricing for the actual lab scenario.

## 10. Governance effectiveness measures

| Measure | Proposed target / approach | Evidence source |
|---|---|---|
| Guardrail inheritance coverage | 100% of applicable production subscriptions inherit their approved baseline before production use | Subscription inventory joined to effective assignment records |
| Ownership metadata coverage | ≥95% of applicable resources, aligned with BR-003 | Tag/ownership evaluation; define exclusions and denominator |
| Exception record completeness | 100% of approved active exceptions have owner, rationale, scope, review/expiry and approval reference | Operational exception tracking plus Azure exemption inventory |
| Policy compliance trend | Baseline first, then set policy-specific targets by resource/scope | Azure Policy compliance results, interpreted alongside exemptions and unsupported resources |
| Subscription onboarding effort | Measure median hands-on time before/after standardization; no savings claimed until compared | Subscription-vending and change records |
| Enforcement-related disruption | Track failed deployments and incidents attributable to policy rollout | Deployment failure review and incident/change records |

Metrics distinguish **assignment coverage**, **compliance state**, and **operational effectiveness**. A 100% inherited-assignment rate does not imply 100% compliant resources.

## 11. Traceability and dependencies

| Architecture element | Canonical traceability | Framework controls | Follow-on work |
|---|---|---|---|
| Enterprise assignment inheritance | R-001; BR-001; SEC-006, SEC-015; TR-001, TR-002 | GOV-01 | Issue #29 tests inheritance; Phase 1 hierarchy retained |
| Modular initiative organization | R-001; SEC-006; TR-003 | GOV-02 | Issue #25 selects concrete policy definitions/effects |
| Progressive enforcement and auditable change | R-006, R-007; BR-002; SEC-014; TR-004 | GOV-03 | Issue #25 guardrail patterns; Issue #29 enforcement test |
| Controlled exemptions | R-006; SEC-007; TR-004 | GOV-04 | Issue #27 detailed exception process |
| Ownership and tagging | R-008; BR-003; SEC-009; TR-005 | OWN-01 | Issue #28 accountability; Issue #25 technical choices |
| Policy-as-code governance | R-007; BR-007; SEC-008, SEC-014; TR-012, TR-013 | CFG-01 | Issue #29 representative implementation and validation |
| Hybrid and acquired workload alignment | R-013; BR-006, BR-010 | GOV-01/GOV-03 supporting | Maintain Phase 1 Legacy migration and Azure Arc considerations |

Additional issue relationships: Issue #26 designs the compliance monitoring/evidence architecture; Issue #30 reviews final governance architecture and validates overall traceability. Regulatory requirements remain scoped by P02-01; inheriting Azure Policy does not, on its own, prove PCI DSS, GLBA, or state-law compliance.

## 12. Open items and closure criteria

**Open design dependencies:** actual policy definitions and parameters; approved enforcement effects; selected policy initiative versioning/deployment mechanics; formal exception approval authority; detailed RACI; precise remediation identity permissions; tested hierarchy/assignment behavior; regulatory clause-level applicability if required.

**P02-03 architecture design may be considered complete when:**

1. Initiative families, assignment scopes, inheritance and subscription-specific variations are documented against the Phase 1 hierarchy.
2. Enforcement lifecycle, exemption boundary, remediation mechanisms and functional ownership are defined.
3. The design maps to the existing risk, BR/SEC/TR and control IDs without duplicating registers.
4. Validation tests and expected evidence have been identified and clearly marked **not validated**.
5. Issue #24 is linked to this reviewed, version-controlled artifact.

Completing this document does **not** demonstrate deployed Azure Policy assignments, effective preventive enforcement, remediation execution, PCI DSS compliance, or formal enterprise approval. Technical implementation and validation remain planned for Issue #29.
