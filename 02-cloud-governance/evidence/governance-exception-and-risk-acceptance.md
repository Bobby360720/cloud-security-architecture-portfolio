# P02-06 — Governance Exception and Risk-Acceptance Process

| Attribute | Value |
|---|---|
| Enterprise | AFG Enterprises (fictional, modeled) |
| Phase | 02 — Cloud Governance & Compliance |
| GitHub issue | #27 — P02-06 |
| Status | Proposed architecture and operating process; not formally approved or implemented |
| Evidence classification | Modeled design; no actual risk acceptance, exception, or Azure deployment claimed |
| Primary risk and control | R-006 — Weak exception lifecycle; GOV-04 |
| Primary requirements | BR-002, BR-005; SEC-007; TR-004 |

## 1. Purpose and scope

Define how AFG identifies a security control deviation, assesses business and technical risk, authorizes residual-risk acceptance, applies narrowly scoped technical exceptions, and returns to compliance. The objective is to preserve business continuity without creating unaccountable or permanent control bypasses.

This process covers Azure Policy exceptions and, at the governance-process level, other security standard deviations. It does **not** confer authority to waive legal, regulatory, or contractual obligations. Technical exemption implementation is a separate act from business risk acceptance.

**Architectural inputs** (existing repository):

- [Enterprise risk register](../../00-enterprise-assessment/risks/enterprise-risk-register.md)
- [Phase 0 traceability matrix](../../00-enterprise-assessment/assessment/traceability-matrix.md)
- [Regulatory applicability and PCI scope](../compliance/regulatory-applicability-and-pci-scope.md)
- [Cloud security control framework](../compliance/cloud-security-control-framework.md)
- [Azure Policy governance architecture](../architecture/azure-policy-governance-architecture.md)
- [Security guardrail design](../architecture/security-guardrail-design.md)
- [Compliance monitoring and evidence architecture](../compliance/compliance-monitoring-and-evidence-architecture.md)

**Boundary:** Issue #27 defines the exception decision process. Issue #28 establishes the enterprise-wide operating model and formal RACI. Issue #29 performs representative technical validation. This document adds no new enterprise risk, requirement ID, repository, database, or workflow platform.

## 2. Selected design decisions

**EXC-DEC-01 — Tiered, business-owned acceptance (Option A).** An authorized business risk owner decides whether to accept residual risk within delegated limits. Cloud Security Architecture and Governance/Risk provide independent assessment and advice; they do not implicitly accept business risk. Technical implementers cannot authorize their own exceptions.

**EXC-DEC-02 — Risk-severity-based initial limits.** The initial exception term is capped at **180 / 90 / 30 / 7 calendar days** for Low / Medium / High / Critical risk respectively, subject to shorter terms where required. These are *AFG proposed internal thresholds*, not external regulatory or Microsoft requirements. Formal delegation and thresholds remain subject to enterprise approval under Issue #28.

**EXC-DEC-03 — SharePoint is the operational system of record.** SharePoint tracks assessments, decisions, owners, deadlines, renewal, and remediation. GitHub holds approved process and architecture versions plus sanitized evidence references. Azure holds the technical exemption where applicable. Do not create competing risk registers.

**EXC-DEC-04 — No standing bypass.** Exceptions must be justified, narrowly scoped, documented, monitored, and reviewed. Where technically supported, temporary Azure Policy exemptions carry an explicit expiration date. Uncontrolled assignment deletion or blanket `notScopes` exclusion is not a substitute for risk acceptance.

## 3. Exception lifecycle

```text
Policy violation / justified control conflict
    ↓
Exception request
    ↓
Risk assessment and regulatory screening
    ↓
Compensating controls / remediation options
    ↓
Approval or rejection by authorized risk owner
    ↓
Time-bound technical exemption (if approved)
    ↓
Monitoring, reviews, and remediation progress
    ↓
Expiration → remove / remediate / formally renew or escalate
```

| Stage | Required action | Record / exit condition |
|---|---|---|
| 1. Identify | Detect policy failure, unsupported workload dependency, or documented business need | Affected control and scope identified; urgent exposure triaged separately |
| 2. Request | Workload/business owner states purpose, duration, affected assets, and alternatives | SharePoint request with accountable requester |
| 3. Assess | Security evaluates likelihood, impact, data sensitivity, criticality, exposure, regulatory/contractual implications, and existing risk reference | Inherent and residual risk rationale; assessment date and assessor |
| 4. Mitigate | Identify compensating control, permanent fix, owner, cost/impact, and milestones | Feasible treatment documented, or reason unavailable |
| 5. Decide | Authorized risk owner approves/rejects within delegation; independent review recorded | Decision, authority, rationale, conditions and approval timestamp |
| 6. Implement | Authorized platform operator applies narrowly scoped technical exemption only after approval | Azure exemption ID, assignment/reference IDs, scope, category and expiration; change record |
| 7. Monitor | Review exposure, compensating-control operation, incidents, changes, approaching expiry, and remediation progress | Review history and escalation record |
| 8. Close/renew | Validate remediation and remove exception; or reassess and obtain fresh approval *before* expiration | Closure evidence or newly approved exception term |

**Default:** A rejected request receives no technical exemption; the owner must remediate, choose another compliant design, or escalate through an authorized governance channel. An exception request is not permission to deploy noncompliant infrastructure.

## 4. Risk acceptance authority and duration

| Residual-risk severity | Proposed accepting authority | Maximum initial period | Review expectations |
|---|---|---:|---|
| Low | Delegated business or workload risk owner | 180 calendar days | At least before expiry; monitor changes in exposure |
| Medium | Designated business risk owner | 90 calendar days | At least monthly and before expiry |
| High | Senior business executive within delegated authority, with independent Security/Risk review | 30 calendar days | At least weekly and before expiry |
| Critical | Executive risk committee or explicitly delegated enterprise authority; exceptional use only | 7 calendar days | Active oversight and daily review during the exception |

**Governance safeguards:**

- Severity is determined by the documented *residual* risk assessment and validated compensating controls, not merely requester preference. Record both inherent and residual risk. Do not downgrade a risk solely to obtain a longer term or lower approval authority.
- All approvers must have **formally delegated authority**; a job title alone does not establish approval rights. When authority is unknown, escalate rather than presume approval.
- The requested exemption term must be the **shortest feasible**, not automatically the maximum.
- An unresolved Critical risk is presumptively unsuitable for routine acceptance. Emergency executive escalation does not override mandatory legal or contractual safeguards.
- Where a control is legally mandatory, consult Compliance/Legal and relevant contractual stakeholders; risk acceptance alone cannot override the requirement.
- A material scope increase, new sensitive data type, incident, change in exposure, failed compensating control, or new regulatory obligation triggers immediate reassessment, even before the scheduled review date.

## 5. Azure Policy technical-exemption rules

Azure Policy exemptions apply to an existing policy or initiative assignment. They are technical records and **not** approval records. AFG will use:

- `Waiver` where a policy deviation is temporarily accepted.
- `Mitigated` where an alternative, evidenced measure satisfies the policy intent.
- The narrowest practicable resource, resource-group, subscription, or management-group scope, consistent with the approval and risk assessment. Broad exemptions require proportionately stronger review.
- `policyDefinitionReferenceIds` when only selected definitions in an assigned initiative require exemption, where supported.
- `expiresOn` in UTC for temporary waivers, matching or preceding the approved expiration. The process requires tracking expiration even where an Azure technical exemption is unavailable.
- Non-sensitive metadata referencing the SharePoint record ID, owner function, approval timestamp, and review date. Do not publish internal personal data or sensitive case details in GitHub.

**Design checks before deployment:** Confirm the assignment scope, the affected resources, who has rights to create exemptions, the prior policy state, and whether the proposed exception actually changes the desired compliance behavior. Azure exemption creation requires appropriate Azure permissions, including exemption write on the target scope and the relevant action permission on the assignment. Azure `notScopes` exclusions can suppress evaluation without the same exemption tracking semantics and must not be used as an informal substitute.

An exemption reaching `expiresOn` stops being honored, but its Azure object may remain for audit; governance must reconcile expired objects, current policy evaluation, and SharePoint status. An exemption also does **not** automatically revert configuration changes or resolve the underlying risk.

**Technical references:**

- [Microsoft Learn — Azure Policy scope, exclusions and exemptions](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/scope)
- [Microsoft Learn — Azure Policy exemption structure](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/exemption-structure)
- [Microsoft Learn — Azure Policy exemptions REST model](https://learn.microsoft.com/en-us/rest/api/policy-authorization/policy-exemptions/create-or-update?view=rest-policy-authorization-2023-04-01)

## 6. Emergency exception path

**Trigger:** An active incident or urgent operational event threatens availability, safety, or an essential business service, and an approved control demonstrably prevents necessary recovery or action. Convenience or scheduling pressure alone does not qualify.

1. **Declare and document:** Link the request to an active incident/change record and identify the precise blocker, scope, service impact and requested period.
2. **Rapid independent assessment:** On-call Security evaluates material cyber/regulatory exposure and proposes minimal safeguards; relevant platform/workload owners evaluate operational impact.
3. **Approve before implementation:** An explicitly delegated emergency business risk authority approves the bounded deviation. Critical/enterprise risk escalates to executive authority. If no authorized approver is reachable, use a compliant workaround and escalate; do not invent standing engineer approval. Any separately authorized break-glass procedure must already exist and be recorded.
4. **Constrain the change:** Apply the smallest technically feasible exemption, with explicit UTC expiry, change record, and enhanced monitoring. Do not globally disable enterprise assignments without independent, authorized emergency change approval.
5. **Reassess promptly:** Security/Governance and the business owner perform a retrospective within **one business day** of stabilization (proposed AFG operating target); record any incident/security impact, whether exposure remained, and the permanent fix.
6. **Restore:** Remove the deviation as soon as safely practicable; verify policy compliance and service health. If further exception time is necessary, obtain standard tiered approval, rather than silently extending emergency authority.

The emergency target does not extend the severity-based maximum duration and does not constitute permission to bypass applicable law, contract, or external regulatory control requirements.

## 7. Renewal, expiration, and closure

**Renewal is a new risk decision, not automatic extension.** The requester must show why remediation was not completed, update the risk assessment and compensating controls, state measurable progress, identify a new deadline, and obtain approval at the current severity tier. Repeated renewals or missed milestones trigger senior escalation; do not lower severity or fragment scope to avoid escalation.

**Proposed operational notification cadence:** Notify owners **14 days before expiry** for Low/Medium, **7 days** for High, and **daily until resolution** for Critical, starting upon approval for shorter windows. These are internal design targets pending operating-model approval, not claims of implemented automation.

At expiration, Security Governance reconciles the SharePoint decision, Azure exemption status, current compliance state, and workload health. If the resource becomes subject to `deny` again, new changes may fail; expiry and withdrawal must therefore be planned with the workload owner. Unsupported or failed renewal must be escalated, not reclassified as approved by default.

Close only after confirming the condition was resolved or the underlying control/requirement was legitimately changed, removing or otherwise terminating the technical exception, and retaining appropriate sanitized evidence. If the resource was retired, capture decommissioning confirmation instead of a remediation screenshot.

## 8. SharePoint operational record — minimum fields

Use the **existing** AFG SharePoint findings/risk tracking model. The following is a *logical field contract* to configure or map to current lists; it is not a request for a second register.

| Field | Purpose |
|---|---|
| Exception ID / linked risk ID | Unique identifier and traceability to R-### or other applicable risk |
| Requester, workload, business owner, risk owner | Accountability and contact point |
| Related control / requirements / policy assignment | GOV/SEC/TR and applicable GR-ID or policy definition reference |
| Resource scope and environment | Resource IDs or secure references; affected MG/subscription/RG/resource classification |
| Business justification and alternatives | Why a compliant solution is presently infeasible |
| Data classification and regulatory screening | PCI/GLBA/contractual considerations and consulted reviewers where applicable |
| Inherent/residual risk and assessment date | Severity, impact, likelihood, and explicit rationale |
| Compensating controls and test status | Control measures, owner, verification and limitations |
| Decision / approver / delegated authority | Approve, reject, escalate; decision timestamp and conditions |
| Technical exemption reference | Azure exemption ID/category, policy assignment, scoped definition refs, expiry |
| Start, review, expiration and renewal history | Time-bounded control and reviewer evidence |
| Remediation owner, milestone and target fix | Accountable path back to standard |
| Monitoring / incident / change references | Relevant evidence without duplicating source logs |
| Status, closure reason and closure evidence | Requested, assessed, rejected, active, expiring, expired, remediated, closed |

**Integrity and access:** Restrict sensitive exception details to authorized stakeholders, use SharePoint version/history and appropriate permissions, and reference source evidence instead of copying secrets or sensitive configuration payloads. GitHub may store sanitized exception *templates or technical test evidence* but not the operational register or personally identifying approval records.

## 9. Proposed functional separation and escalation

| Function | Proposed role in exception lifecycle |
|---|---|
| Requesting workload/business owner | Explains need and impact; owns remediation milestones |
| Cloud Security Architecture | Assesses control intent, security consequences and compensating options |
| Governance / Risk Management | Checks assessment quality, recording, delegated authority, review and escalation |
| Compliance / Legal | Determines when a request implicates mandatory obligations or customer commitments |
| Authorized business risk owner | Approves/rejects residual risk within delegation; escalation sponsor |
| Cloud Platform Engineering | Applies/reverts approved Azure technical exemptions and verifies actual scope |
| Security Operations | Monitors relevant signals and coordinates incident escalation when needed |

No individual should both approve risk acceptance and unilaterally implement/verify the exception without independent oversight. Issue #28 will determine formal RACI, named delegated roles, committee composition, backup approvers and cadence.

## 10. Measurement, oversight, and planned validation

| Measure | Proposed target or method |
|---|---|
| Active exception completeness | 100% contain risk owner, justification, authority, scope, expiry/review and remediation path |
| Expired-but-still-active deviations | Target zero; reconcile Azure exemptions against SharePoint status |
| Overdue remediation | Count by risk tier, days overdue and responsible business owner |
| Repeated renewals | Flag successive renewals for senior review; do not treat as routine |
| Scope appropriateness | Sample approved exceptions for least scope and correct policy-definition references |
| Compensating control reliability | Verify agreed control operates; log failures as findings and reassess risk |
| Time to close | Measure median exception duration and aging trend after establishing baseline |

**Representative tests deferred to Issue #29:**

| ID | Planned validation | Expected evidence |
|---|---|---|
| EX-01 | Test one approved, narrowly scoped `Waiver` against a benign Azure Policy assignment | Sanitized assignment/exemption IDs, status before/after, expiration |
| EX-02 | Demonstrate that an exemption affects only its intended scope or initiative definition | In-scope and out-of-scope compliance comparisons |
| EX-03 | Demonstrate expiration behavior without implying Azure deletes the exemption object | Expiry metadata and post-expiry evaluation; monitoring reconciliation |
| EX-04 | Review a fictional SharePoint exception record against the required field contract | Sanitized mock record/checklist; labeled **modeled**, not real approval |
| EX-05 | Show the process for withdrawing an exemption and verifying the resource returns to intended control behavior | Change record, policy reassessment, rollback/workload validation |

**Lab cost:** Favor existing policy assignments and short-lived test resources; estimate any resource/logging costs before deployment and tear down representative workloads. These tests are *not completed* by publication of this design.

## 11. Traceability and issue boundaries

| Design element | Existing authority | Relationship |
|---|---|---|
| Governed policy exception lifecycle | R-006; BR-002; SEC-007; TR-004 | GOV-04; P02-03 Azure exemption architecture |
| Maintain decision auditability | BR-005; SEC-014 | SharePoint decision history, Azure Activity Log/change evidence; P02-05 monitoring architecture |
| Control inheritance and scoped deviation | R-001; SEC-006, SEC-015; TR-001, TR-003 | GOV-01/GOV-02; Phase 1 hierarchy and Issue #24 |
| Configuration correction and source-of-truth discipline | R-007; SEC-008; TR-012, TR-013 | CFG-01; P02-04 guardrail remediation |
| Resource and remediation ownership | R-008; BR-003; SEC-009; TR-005 | OWN-01; operating ownership formalized in Issue #28 |
| Regulatory applicability and mandatory obligations | P02-01 regulatory baseline | Legal/compliance screening; no automatic waiver of GLBA/FTC/PCI obligations |
| Validated technical behavior | P02-08 / Issue #29 | Technical Azure exemption and compliance tests planned, not performed |

## 12. Open dependencies and closure criteria

**Pending enterprise decisions (Issue #28 or later):** Formal risk-acceptance delegations, emergency-authority roster, committee escalation charter, separation-of-duties exception process, review cadences, and SharePoint list configuration. These do not prevent an architecture-design closeout, but must be approved before an enterprise operational rollout.

**Issue #27 design closeout criteria:**

1. Tiered business-owned decision authority and 180/90/30/7-day proposed initial limits are documented.
2. Every Issue #27 workflow stage has a required action and exit record.
3. Emergency approval, renewal, expiration, monitoring and escalation behavior are explicit.
4. SharePoint and GitHub responsibilities remain distinct; Azure technical exemption mechanics are documented.
5. Existing enterprise risk, requirements and GOV controls are traceable; validations are classified as planned.
6. Document undergoes review, is committed/pushed, and is linked from Issue #27.

**Status declaration:** This is a modeled architecture and process standard. No business executive has been appointed, no risk has been accepted, no exception has been issued, and no Azure Policy exemption has been deployed or validated by this document.
