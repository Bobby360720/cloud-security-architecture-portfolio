# P02-05 — Compliance Monitoring and Evidence Architecture

| Attribute | Value |
|---|---|
| Enterprise | AFG Enterprises (fictionalized, modeled enterprise) |
| Phase | 02 — Cloud Governance & Compliance |
| GitHub issue | #26 — P02-05: Design Compliance Monitoring and Evidence Architecture |
| Status | Proposed architecture baseline — review pending |
| Evidence classification | Modeled design; implementation and control effectiveness not validated |
| Primary risks | R-001, R-005, R-006, R-007, R-008; supporting R-014 |
| Primary controls | GOV-01 through GOV-04; OWN-01, CFG-01, MON-01; GR-01 through GR-06 |

## 1. Purpose, outcomes and boundaries

AFG needs defensible evidence that applicable cloud security controls **are assigned, evaluate the intended resources, operate as designed, and have accountable follow-up when they fail**. A configuration screenshot, a policy assignment or a dashboard score alone is insufficient to establish complete control effectiveness or regulatory compliance.

The proposed architecture connects Phase 0 enterprise risks and BR/SEC/TR requirements to Phase 2 framework controls, six selected guardrails, technical observations, operational findings, and sanitized validation artifacts.

**In scope:** evidence assertions; source systems; collection and correlation model; minimum record schema; quality, integrity, access and retention principles; reporting, metrics and failure handling; functional responsibilities; and planned validation.

**Out of scope:** deploying diagnostic settings, enabling paid services, implementing a central evidence database, building a custom dashboard, claiming regulatory certification, establishing the formal risk-acceptance process (Issue #27), assigning the final RACI (Issue #28), or executing controls and tests (Issue #29). Detailed Sentinel detection engineering remains within Phase 5.

### Authoritative architecture references

- [Enterprise risk register](../../00-enterprise-assessment/risks/enterprise-risk-register.md) and [traceability matrix](../../00-enterprise-assessment/assessment/traceability-matrix.md)
- [Business requirements](../../00-enterprise-assessment/requirements/business-requirements.md), [security requirements](../../00-enterprise-assessment/requirements/security-requirements.md), and [technical requirements](../../00-enterprise-assessment/requirements/technical-requirements.md)
- [Phase 1 management-group and subscription design](../../01-azure-landing-zone/architecture/management-group-subscription-design.md)
- [P02-01 regulatory applicability and PCI scope baseline](regulatory-applicability-and-pci-scope.md)
- [P02-02 security control framework](cloud-security-control-framework.md)
- [P02-03 Azure Policy governance architecture](../architecture/azure-policy-governance-architecture.md)
- [P02-04 security guardrail design](../architecture/security-guardrail-design.md)

## 2. Evidence principles and architecture decision

**Decision — Native-source, control-linked evidence.** AFG will use Azure Policy, Microsoft Defender for Cloud, Azure Activity Logs, Azure Monitor / Log Analytics, Microsoft Sentinel where justified, and Git/CI/IaC/OPA test results as technical evidence sources. SharePoint remains the **operational system of record for findings, risks, exception approvals and remediation follow-up**. GitHub remains the **version-controlled architecture and sanitized lab-evidence baseline**. No additional central evidence database or custom dashboard is authorized by this design.

Evidence must be:

1. **Traceable:** link an existing risk/requirement and framework or guardrail control to a specific assertion and evidence reference.
2. **Scoped:** identify the evaluated management group, subscription, resource population, exclusions, assignment or workflow version, and evaluation period.
3. **Time-bound:** record collection and observation times, including any known reporting lag or freshness limitation.
4. **Reproducible where practical:** retain a sanitized query, test definition, configuration reference or pipeline commit SHA.
5. **Integrity-aware:** protect source and exported evidence from unauthorized modification, log access and changes, and preserve provenance.
6. **Honest about confidence:** separate **modeled**, **observed** and **validated** results. A passing technical test is evidence for its tested scope, not the entire fictional enterprise.
7. **Risk-proportionate:** collect sufficient evidence without duplicating native telemetry or incurring unjustified ingestion/retention cost.

## 3. Evidence assertions: distinguish four questions

| Evidence dimension | Assertion | Example | What it does *not* establish |
|---|---|---|---|
| Coverage | The approved control reaches its **applicable** targets | Azure Policy assignment at `AFG`, inherited by an eligible subscription | That resources comply |
| Configuration compliance | Evaluated resources satisfy a specific configuration condition | Storage account reports compliant with selected public-network-access policy | That application connectivity or all security objectives are assured |
| Operating effectiveness | The tested guardrail produced the intended result | An unsafe test deployment is rejected; compliant control deployment succeeds | That every resource, time period or attack path was tested |
| Governance accountability | Gaps are assigned, remediated or risk-accepted through authorized process | SharePoint finding with owner, due date, disposition and referenced approval | That accepting the risk removes a technical vulnerability |

Evidence completeness and resource compliance are independent metrics. Report the denominator, exclusions, exemptions and unsupported resource types instead of treating missing observations as compliant.

## 4. Logical evidence flow and source responsibilities

```text
Existing enterprise risk / requirement / framework control
                         |
                   Guardrail assertion
                         |
       +-----------------+-----------------------+
       |                 |                       |
  Azure Policy      Defender for Cloud      Git / CI / IaC / OPA
  assignments,       assessments and        policies, tests,
  evaluation,        recommendations        plan and pipeline results
  exemptions              |                       |
       +-----------------+-----------------------+
                         |
        Azure Activity Logs / Azure Monitor / Log Analytics
          (relevant changes and operational verification)
                         |
              Evidence reference / review
                         |
          +--------------+------------------+
          |                                 |
  SharePoint operational             GitHub architecture and
  findings, exceptions,             sanitized representative
  ownership and risk status          lab validation evidence
          |
     Governance metrics / review and escalation

  Sentinel contributes detection/incident records only where
  relevant; it is not the mandatory compliance evidence store.
```

| Source | Evidence role | Limitations / design dependency |
|---|---|---|
| Azure Policy / Policy Insights | Definition and initiative references, assignments, effective scope, parameters, exemptions and evaluated resource compliance | Periodic evaluation may lag; `notScopes`, exemption category, eligibility and unsupported types affect interpretation. Assignment inheritance is not compliance. |
| Defender for Cloud | Applicable posture findings and regulatory-control assessments | Recommendations may overlap with Azure Policy; a regulatory dashboard or secure score is not an attestation or complete proof of a standard. Licensing/plan scope matters. |
| Azure Activity Logs | Selected Azure Resource Manager control-plane changes and policy/assignment-related activity | Not a substitute for service data-plane logging or proof that a policy blocked a specific operation. Default retention is limited; long-term export is conditional on requirements. |
| Azure Monitor / Log Analytics | Queryable logs, diagnostic output and selected operational outcomes | Only configured data is collected; cost, sampling, workspace access and retention affect evidence. A diagnostic setting alone does not prove expected events arrived. |
| Microsoft Sentinel | Security incident, analytic-rule, investigation and response records for material cases | No generated incident does not prove no exposure; do not send every compliance finding to incident response. Additional cost may apply. |
| GitHub / CI/CD / Terraform / OPA-Rego | Source versions, review approvals, static/plan checks, policy test fixtures, passing/failing job results, and deployment outcome | Pipeline pass proves only evaluated inputs at that commit/configuration; does not guarantee deployed state, complete test coverage or no bypass. |
| SharePoint | Operational risk and finding ownership, exception approvals, due dates, treatment decisions and closure verification | Not a replacement for the technical source record or a copy of all raw logs. |

### Correlation rule

Every reviewed finding or test should reference the **control ID + applicable scope + time window + source record identifier**. Where available, include policy assignment/definition version, resource ID (sanitized in public artifacts), CI run/commit, remediation task or incident reference. Use stable references rather than manually recopying source data into multiple trackers.

## 5. Minimum evidence record contract

The following is a **logical schema**, not a new database or required SharePoint list. Existing systems may supply fields through links, metadata and stored test notes.

| Field | Purpose |
|---|---|
| Evidence reference | Stable ID, path or URI to the original authoritative technical observation |
| Risk / requirement / control | Existing R-, BR-, SEC-, TR-, GOV-/other framework control and GR-xx links as applicable |
| Assertion and expected result | Precise claim being tested (coverage, compliance, effectiveness or accountability) |
| Evaluation scope and denominator | Management group, subscription(s), eligible resources, exclusions and exemptions |
| Source and collection method | Product, query/API or test/CI job identifier, configuration/definition version |
| Observation timestamp and period | UTC timestamp(s), freshness expectation and any policy-evaluation delay |
| Actual result and outcome | Pass, fail, partial, inconclusive or not evaluated; relevant observed details |
| Evidence classification | Modeled / observed / validated (for the stated test and scope only) |
| Responsible function and follow-up | Test operator/reviewer or owning team, SharePoint finding/exception reference if needed |
| Limitations and integrity | Missing telemetry, unsupported resources, sanitized fields, immutable commit or controlled storage reference |

**Example — planned, not executed:** `GR-02 / NET-01` would be linked to the Rego policy revision, Terraform plan fixture, expected decision, actual Conftest result, timestamp, reviewer, and later (separately) an Azure Policy deny-test result. Neither result can stand in for the other.

## 6. Six-guardrail evidence matrix

All entries describe **required/planned evidence**, not existing evidence. The security assertions and candidate guardrails come from P02-04.

| Guardrail / linked control | Configuration and coverage evidence | Operating-effectiveness evidence | Operational follow-up / owner |
|---|---|---|---|
| **GR-01 Ownership metadata** — OWN-01; R-008 | Eligible-resource inventory, tagging rule and scope, sampled assignment/compliance output, approved tag vocabulary | Missing-owner-tag test produces expected finding or deny where selected; verified correction reflects actual owner | Cloud Governance and workload owner; SharePoint finding for unresolved gaps |
| **GR-02 Storage public network access** — NET-01; R-004 | Azure Policy definition/version, assignments and effective parameters, Storage network configuration; Rego rule/plan fixture reference | Noncompliant Terraform plan fails and compliant fixture passes; separate representative enforced Azure deny succeeds, with legitimate compliant deployment unaffected | Cloud Security Architecture and workload/platform owner; exception or incident only if justified |
| **GR-03 Key Vault diagnostics** — MON-01; R-005 | Selected vaults and eligible resource types, diagnostic-setting policy and destination configuration, deployment permissions | Missing diagnostics detected; test operation produces the expected log event in approved destination (subject to event support and ingestion delay); correction reassessed | Security Operations and Platform; investigate data-collection gaps |
| **GR-04 Approved locations** — GOV-01/GOV-02; R-001 | Approved-region parameters, applicability, documented global-service exclusions, assignment inheritance | Representative prohibited-region deployment denied and permitted-region deployment succeeds when enforcement tested | Cloud Governance and Platform; deployment failures routed to owning team |
| **GR-05 Key Vault public network access** — NET-01; R-004 | Vault network configuration, selected policy version/effect, effective assignment and approved connectivity patterns | Noncompliant representative request detected or blocked; intended private/approved application access verified separately | Cloud Security Architecture and vault owner; avoid false assumptions about data-plane reachability |
| **GR-06 Storage secure transfer** — DAT-01 supporting; R-009 | Storage account secure-transfer-required configuration, applicable policy, scope and evaluated resources | Configuration-incompatible deployment denied where supported; compliant request passes; optional client-protocol testing if justified | Data Security and workload owner; protect application protocol compatibility |

**Evidence interpretation:** GR-02's OPA check assesses a **proposed Terraform change**, whereas Azure Policy assesses applicable Azure resource requests/states. GR-03 requires proof of **log delivery**, not merely existence of a diagnostic setting. GR-05 network compliance is not proof of a complete network threat model. GR-06 addresses transport protection, not data classification itself.

## 7. Collection, freshness and validation rules

| Evidence class | Proposed collection trigger | Review / escalation condition |
|---|---|---|
| Policy assignment, initiative, parameter and exemption inventory | After approved deployment/change; periodic reconciliation | Missing expected assignments, unexpected scope change, stale or expired exemption |
| Azure Policy configuration compliance | After relevant evaluation / on defined reporting cadence | Critical missing evaluation, recurring noncompliance, denominator unexpectedly reduced |
| Defender for Cloud posture | On standard governance review cadence and after material control changes | Relevant new high-risk finding, assessment coverage gap or disputed mapping |
| Activity Logs and service diagnostics | Collected only for agreed control assertions and operational needs | Source stops producing required events or retention falls below approved requirement |
| CI/CD, Terraform and Rego | Each relevant proposed change / policy revision | Failed check, skipped/bypassed gate, unapproved policy version or incomplete evidence |
| Remediation / exceptions / incidents | Upon action and at scheduled reviews | Overdue remediation, invalid approval, missing verification, recurring incident pattern |

Define actual cadence and thresholds by control criticality in the operating model (Issue #28). Azure Policy evaluation is not continuous for every state change, and a fresh assignment may need time or an explicitly triggered scan before results become available. Treat `not evaluated`, `not applicable`, `exempt`, `noncompliant` and `compliant` as distinct states when available.

### Verification gates

- Confirm the record represents the correct **resource cohort**, period, assignment/definition version and policy effect/enforcement mode.
- Review sample **positive and negative cases** where feasible; do not use a single compliant sample as enterprise proof.
- Verify source fidelity: links resolve, evidence was produced by the described method, and required logs actually arrived.
- Record outcomes as **inconclusive** when source coverage, freshness, permissions or data quality prevent a defensible conclusion.
- After remediation, verify both corrected source configuration and effective state; record an observed result rather than relying on task completion alone.

## 8. Evidence protection, retention and cost

1. **System of record:** keep full operational records and approvals in controlled enterprise systems; keep GitHub artifacts limited to version-controlled specifications and **sanitized** representative lab results.
2. **Confidentiality:** avoid publishing tenant IDs, subscription IDs, resource identifiers, user identities, payment data, API tokens, secrets, incident details, or customer information where unnecessary. Apply least-privilege access and appropriate redaction.
3. **Integrity:** use source-system audit trails, protected branches/reviews and immutable commit IDs; where exports require stronger integrity, consider checksums and controlled retention. A checksum alone is not an enterprise retention control.
4. **Retention:** derive schedules from applicable legal, contractual, regulatory, security and investigation requirements. **Do not invent a single retention period for GLBA or PCI DSS.** Azure Activity Logs have a default retention window; long-term preservation requires an approved export/storage configuration. Verify the current service-specific limits and costs before implementation.
5. **Data minimization:** collect only needed log categories and evidence fields. Avoid duplicating all raw event streams into GitHub, SharePoint or Sentinel merely to populate a dashboard.
6. **Lab cost:** prefer existing subscriptions and policy metadata, local Rego/CI outputs, and brief representative tests. Before enabling Key Vault diagnostic routing, Log Analytics ingestion, Defender plans or Sentinel, estimate per-test and monthly cost; clean up only temporary test resources according to the existing teardown plan.

**Storage decision deferred:** Whether AFG needs immutable storage, longer-term log archiving or regulated evidence preservation cannot be determined without approved evidence retention, authenticity and legal-hold requirements. A secure operational evidence store may be needed in a production enterprise, but is not required for the current fictional lab deliverable.

## 9. Governance reporting and effectiveness metrics

Use native Azure Policy and Defender for Cloud reporting for technical posture; use SharePoint views for open findings, ownership, waivers and follow-up. A manually reviewed cross-source summary is acceptable while scale is small. A custom dashboard is justified only after documenting consumers, decisions, expected refresh, integrations, cost and ownership.

| Metric | Proposed target or baseline method | Interpretation / caveat |
|---|---|---|
| Applicable production subscription guardrail inheritance | Target **100%** of eligible production subscriptions before production use | Inventory scope, approved exclusions and assignment inheritance; does not prove compliance |
| Resource ownership completeness | Target **>=95%** of eligible resources, aligned with BR-003 | Define eligible population and authoritative owner value; no fabricated coverage |
| Active approved exception record completeness | Target **100%** with owner, rationale, scope, approval reference, expiry/review date | Measures process record quality, not risk elimination |
| Control evaluation / evidence coverage | Baseline percentage of selected critical controls with current, applicable evidence | Flag not evaluated separately from pass/fail |
| Policy-specific compliant resource rate | Establish initial baseline; set risk-based targets after measuring | Count exemptions, unsupported types and stale evaluations separately |
| Remediation verification rate / age | Measure verified corrections and time open by severity | Closing a task/ticket is not verification |
| Pre-deployment guardrail effectiveness | Count expected unsafe plan failures and unintended bypasses | Requires tested negative cases and identified CI execution population |
| Operational impact | Track policy-induced deployment failures, outages and exception trends | Balance preventive protection against legitimate business delivery |
| Evidence freshness | Measure percentage meeting control-specific collection/review cadence | Targets require service behavior and stakeholder agreement |

Metrics are **proposed**, not collected, and must not be represented as actual AFG performance.

## 10. Functional ownership and failure handling

| Responsibility | Proposed lead | Boundary |
|---|---|---|
| Define control assertions and acceptable proof | Cloud Security Architecture / Governance | Reviews mapping to risks, requirements and control outcomes |
| Maintain Azure Policy and cloud collection configuration | Cloud Platform Engineering | Reviews permissions, deployment changes and service costs |
| Validate operational log arrival and relevant detections | Security Operations | Phase 5 owns detailed Sentinel rules and incident processes |
| Maintain workload-specific evidence and remediate gaps | Workload / application owner | Confirms service behavior and corrections |
| Track findings, remediation and exception approvals | Cloud Governance / Risk Management in SharePoint | Business risk acceptance requires separately delegated authority (#27/#28) |
| Maintain architecture baselines and sanitized lab evidence | Portfolio architecture owner / version-control reviewers | GitHub is not the operational risk register or sensitive evidence vault |
| Interpret statutory and contractual evidence obligations | Compliance / Legal | Conditional obligations established in P02-01 require formal applicability decisions |

These are **proposed functions**, not approved appointments or permissions. If evidence is missing, stale, contradictory or unusable, classify the assertion as **not demonstrated / inconclusive**, assign a source-system or workload owner, and open or update the operational finding when material. Re-test after correction. Escalate material risks through authorized governance; do not automatically turn every compliance finding into a Sentinel incident.

## 11. Representative validation plan — Issue #29

No tests below are claimed as executed. Select a small subset based on lab permissions, risk reduction and cost.

| Test ID | Planned control assertion | Minimum method | Expected sanitized evidence | Cost |
|---|---|---|---|---|
| EV-01 | Parent assignment is inherited by an eligible subscription, with correct evaluated population | Inspect hierarchy, effective assignments, and resource compliance after evaluation | Scoped assignment export, resource count, evaluation time and exclusions | Metadata/CLI first; no new workload required |
| EV-02 | GR-02 pre-deployment Rego check distinguishes safe, unsafe and unknown Terraform configurations | Test a local set of compliant and noncompliant Terraform plan JSON fixtures | Rego revision, fixture cases, pass/fail output, run timestamp | Local only |
| EV-03 | Validated Azure Policy `deny` stops a selected unsafe request but permits a compliant test request | Scoped test assignment after approved compatibility review and temporary resource operation | Assignment mode/parameters, negative and positive request results, cleanup evidence | Estimate and constrain test Storage costs |
| EV-04 | GR-03's diagnostic setting produces usable telemetry for an expected supported event | Check eligible Key Vault settings; generate approved test event; verify delivery to destination | Configuration, event/query reference, ingestion timing, reviewer | Optional; assess log/Key Vault charges before approval |
| EV-05 | Exceptions and resulting compliance/evidence treatment are traceable | Review a narrowly scoped test exemption or approved simulated record without implying risk approval | Exemption definition/state, operational reference, compliance comparison, expiry | Metadata-first; avoid real business-risk claims |

**Acceptance:** Evidence for each executed test identifies expected versus observed behavior, eligible scope, test date, policy version/mode, source record and limitations. A test is **validated only for its observed scope**. Unexecuted cases remain planned rather than passed.

## 12. Traceability, dependencies and Issue #26 closure criteria

| Design outcome | Canonical requirements and risks | Relevant controls | Future validation / owner dependency |
|---|---|---|---|
| Policy assignment coverage and inheritance | R-001; BR-001; SEC-006, SEC-015; TR-001–TR-004 | GOV-01, GOV-02; GR-04 | EV-01; Platform Engineering |
| Controlled enforcement and authorized exceptions | R-006; BR-002; SEC-007; TR-004 | GOV-03, GOV-04 | EV-03/EV-05; Issues #27–#29 |
| Security telemetry visibility | R-005; SEC-005; TR-010 | MON-01; GR-03 | EV-04; Operations/Platform |
| Resource ownership completeness | R-008; BR-003; SEC-009; TR-005 | OWN-01; GR-01 | Governance/workload ownership review |
| Repeatable, auditable changes and predeployment checks | R-007; BR-007; SEC-008, SEC-014; TR-012, TR-013 | CFG-01; GR-02 | EV-02; DevSecOps/Platform |
| Public exposure and secure data transport | R-004, R-009; SEC-004, SEC-010; TR-008, TR-014 | NET-01, DAT-01 supporting; GR-02, GR-05, GR-06 | Guardrail validation; network/data owners |
| Security posture findings coverage | R-014 (supporting); BR-009 | Relevant guardrail assessments | Defender plan applicability and evidence source confirmation |
| Sanitized validation records | TR-016; BR-005, BR-009 | Cross-cutting | GitHub review; SharePoint remains operational tracker |

**Deferred decisions:** final evidence retention/immutability requirements; precise evaluation/review cadence; telemetry destinations, data volumes and costs; compliance assessment applicability and licenses; evidence ownership and final RACI; dashboard need; proof thresholds for regulatory attestations; implementation details and representative test execution.

**Issue #26 may close after architecture review and version-controlled publication when:**

1. Each of GR-01 through GR-06 has explicit configuration/coverage and effectiveness evidence assertions.
2. Sources, scope/correlation, minimum evidence fields and interpretation limits are documented.
3. SharePoint/GitHub roles, evidence integrity, access and conditional retention requirements are clear.
4. Planned metrics and a risk-proportionate validation plan are present, with no false implementation claims.
5. Detailed workflow, operating-model and actual validation responsibilities are explicitly deferred to Issues #27, #28 and #29.

Completion of this design **does not** establish that controls have been deployed, logs are collected, policy evaluation has passed, or AFG meets PCI DSS, GLBA or FTC Safeguards requirements.
