# P02-04 — Security Guardrail Design

| Attribute | Value |
|---|---|
| Enterprise | AFG Enterprises (fictionalized, modeled enterprise) |
| Phase | 02 — Cloud Governance & Compliance |
| GitHub issue | #25 — P02-04: Design Preventive, Detective and Corrective Guardrails |
| Status | Proposed design shortlist — architecture review pending |
| Evidence classification | Modeled design; no implementation, approval, enforcement or control effectiveness asserted |
| Primary dependencies | Phase 0 requirements and risks; P02-02 Control Framework; P02-03 Azure Policy Governance Architecture |

## 1. Purpose and boundaries

This document translates existing AFG control objectives into **six candidate Azure governance guardrails** with explicit preventive, detective, corrective and operational-response roles. The design preserves the **progressive, risk-based enforcement** selected in P02-03 and the Phase 1 management-group hierarchy. It is a design shortlist, **not** a final catalog of deployed Azure Policy definitions.

**In scope:** risk and requirement traceability; proposed mechanisms/effects; intended scopes; operational impact; correction and exception handling; functional ownership; a single OPA/Rego pre-deployment design; and representative validation plans.

**Out of scope:** deploying assignments, writing Rego code, changing CI pipelines, executing remediation, configuring Sentinel detections, establishing approval thresholds or asserting compliance. Representative tests belong to Issue #29; broader DevSecOps workflow design belongs to Phase 6; evidence architecture to #26; risk approval workflow to #27; RACI to #28.

Authoritative repository references:

- [Enterprise risk register](../../00-enterprise-assessment/risks/enterprise-risk-register.md)
- [Business requirements](../../00-enterprise-assessment/requirements/business-requirements.md), [security requirements](../../00-enterprise-assessment/requirements/security-requirements.md), [technical requirements](../../00-enterprise-assessment/requirements/technical-requirements.md)
- [Traceability matrix](../../00-enterprise-assessment/assessment/traceability-matrix.md)
- [Phase 1 management-group and subscription design](../../01-azure-landing-zone/architecture/management-group-subscription-design.md)
- [P02-02 security control framework](../compliance/cloud-security-control-framework.md)
- [P02-03 Azure Policy governance architecture](azure-policy-governance-architecture.md)
- [P02-01 regulatory applicability and PCI scope](../compliance/regulatory-applicability-and-pci-scope.md)

## 2. Operating model: prevent, detect, correct, respond

| Layer | Intended role | Candidate technology | Guardrail design boundary |
|---|---|---|---|
| Prevent: before deployment | Reject proposed noncompliant IaC changes | OPA/Rego evaluating Terraform plan JSON, optionally through Conftest | Initially **GR-02 only**; controlled CI integration deferred |
| Prevent: Azure control plane | Reject selected noncompliant create/update requests | Azure Policy `deny` (after validation) | Not an automatic repair tool; policy effect and assignment enforcement mode are distinct |
| Detect | Identify configuration gaps and security posture risks | Azure Policy `audit`/`auditIfNotExists`, Defender for Cloud where applicable | Assignment coverage is different from compliance; recommendations may overlap with Azure Policy |
| Correct | Restore approved configuration | Workload/IaC changes; Azure Policy `modify` or `deployIfNotExists` plus remediation tasks where supported | Correct source-of-truth Terraform; authorize identities and limit rollout blast radius |
| Respond | Triage material security consequences or repeated violations | Existing operational process, Sentinel where justified | A compliance finding is not automatically a security incident; Phase 5 defines detections |

The four stages need not be implemented through four products for every guardrail. AFG should choose the minimum effective combination for each risk.

## 3. Six-guardrail design shortlist

The `GR-xx` labels are **local design identifiers** for Issue #25, not new Phase 0 risks/requirements or replacements for the existing security control framework.

| ID | Proposed security outcome | Primary traceability | Azure-side candidate | Progressive rollout | Proposed assignment placement | Coordinating owner |
|---|---|---|---|---|---|---|
| **GR-01** | Identify accountable ownership for applicable Azure resources | R-008; BR-003; SEC-009; TR-005; **OWN-01** | Tag audit; selected tag inheritance via `modify` if authoritative source exists | Audit completeness first; enforce only required tags where tested | AFG; refine applicability by resource type and lifecycle | Cloud Governance + Platform |
| **GR-02** | Prevent unintended **Storage public network access** | R-004; SEC-004; TR-008; **NET-01** | Built-in Storage public-network-access policy, `audit` then `deny`; one complementary OPA/Rego check | Validate permitted network patterns and exceptions before enforcing | Landing-Zones; specialize where platform/legacy dependencies require | Cloud Security Architecture + Workload/Platform |
| **GR-03** | Ensure approved diagnostics for a selected PaaS service | R-005; SEC-005; TR-010; **MON-01** | Key Vault logs: `auditIfNotExists` and supported `deployIfNotExists` policy | Audit before automatic deployment; test managed-identity permissions and ingestion cost | Applicable Platform and Landing-Zones scopes | Security Operations + Platform |
| **GR-04** | Restrict new deployments to approved Azure regions | R-001; SEC-006; TR-003; **GOV-01/GOV-02** | Built-in allowed-locations policy, `audit` then `deny` where applicable | Assess DR, global services, region-specific services and migration | AFG only if common location set truly applies; otherwise narrower scope | Cloud Governance + Platform |
| **GR-05** | Detect and selectively prevent unintended **Key Vault public network access** | R-004; SEC-004; TR-008; **NET-01** | Key Vault public-network-access `audit` then possible `deny` | Validate private access, firewall/approved access paths and platform dependencies | Relevant Platform and Landing-Zones scopes | Cloud Security Architecture + Service owners |
| **GR-06** | Require secure transfer for Azure Storage | R-009; SEC-010; TR-014; **DAT-01** (supporting) | Storage secure-transfer/HTTPS-only built-in policy: `audit` then `deny` when supported | Validate all client/application protocol dependencies before enforcing | Applicable Landing-Zones and Platform storage services | Data Security + Workload/Platform |

**Traceability note for GR-06:** Secure transfer primarily protects data **in transit**, not public exposure. Its link to the broad data protection objective (DAT-01 / SEC-010) is *supporting*, not a claim that classification by itself enforces transport encryption. Confirm the exact built-in policy and Phase 0 requirement relationship during implementation; do not fabricate a new requirement.

### 3.1 Assignment principles

- Inherit common assignments from the highest **appropriate** management-group scope, not automatically the Tenant Root Group.
- Retain Phase 1 `AFG / Platform / {Identity, Management, Connectivity, Security}`, `AFG / Landing-Zones / {Corp, Online, Legacy}`, `AFG / Sandbox`, `AFG / Decommissioned`, and proposed `AFG / Onboarding` placement; do not create production/nonproduction management groups.
- Classify production and nonproduction at subscription level and apply repeatable subscription-scoped assignments only where necessary.
- Do not apply broad `deny` to Legacy, Onboarding, or Decommissioned without impact tests; restrictive intent must allow required transition operations.
- A policy exemption requires a separately authorized business-risk decision in operational SharePoint tracking. Issue #27 owns the approval workflow.
- Microsoft built-in policy names and supported effects must be checked at implementation time; **no assignment IDs, deployed initiative IDs or verified compliance values are claimed here**.

## 4. Guardrail behavior and operational design

### GR-01 — Ownership tags

- **Detect:** report resources missing the approved accountable-owner metadata, filtering resource types for which tags are unavailable/inappropriate.
- **Prevent:** after examining deployment patterns, optionally deny new relevant resources lacking required tags; avoid mass deny before onboarding and tagging conventions are established.
- **Correct:** populate missing tags via owners/IaC; `modify` may inherit from parent scope **only when parent metadata is accurate and the semantics match**. Never synthesize an owner value.
- **Respond:** route persistent ownership gaps through governance work management, not default Sentinel incidents.
- **Measure:** eligible resources with approved owner metadata / all eligible resources; proposed enterprise target >=95% per BR-003.

### GR-02 — Storage public network access (OPA flagship)

- **Prevent (IaC):** evaluate `azurerm_storage_account` create/update changes in Terraform plan JSON. Deny proposed values permitting public network access; **missing, null or unknown values must not silently pass**. The Rego policy needs tests for provider-version differences, `after_unknown`, update actions and exclusions.
- **Prevent (Azure):** use Microsoft's built-in **Storage accounts should disable public network access** where suitable. Begin with non-enforcing assessment/audit; enable `deny` only after compatibility review. Verify effect/parameter support on the chosen definition version.
- **Detect:** review relevant Azure Policy compliance, resource network configuration, and Defender for Cloud findings where available.
- **Correct:** update authoritative Terraform configuration and validate approved private connectivity, DNS and legitimate application access; do not automatically disable access for a business-critical account before dependency review.
- **Respond:** escalate credible exposure with sensitive financial information through the normal incident triage process.
- **Critical distinction:** `public_network_access_enabled`/`publicNetworkAccess` governs network endpoint exposure; disabling anonymous blob access is a **different** control. Neither alone proves complete data-exfiltration prevention.

### GR-03 — Key Vault diagnostic settings

- **Detect:** evaluate whether selected vaults have approved log categories routed to an authorized destination; confirm coverage, not simply the presence of *some* diagnostic setting.
- **Correct:** use a supported built-in `deployIfNotExists` assignment or approved IaC correction after destination design, permissions, managed identity, regional constraints and retention/cost are reviewed. Existing noncompliant vaults may require a remediation task.
- **Prevent:** diagnostics are typically an audit/remediation objective rather than a blanket `deny` rule; prefer enforcing through the approved provisioning standard where applicable.
- **Respond:** missing logs are a monitoring-coverage gap for governance review; investigate incidents separately if suspicious activity is indicated.
- **Cost:** estimate Log Analytics ingestion and retention before enabling test logging.

### GR-04 — Allowed regions

- **Detect:** report deployment location differences against approved geography and service-specific exceptions.
- **Prevent:** use a supported location restriction with `deny` only for validated deployment scopes; distinguish resource locations from resource-group locations and services without ordinary location behavior.
- **Correct:** moving or redeploying resources may be disruptive; do not suggest a generic automated `modify` relocation.
- **Respond:** route exceptions to governance/change review; investigate suspected unauthorized changes when warranted.

### GR-05 — Key Vault public network access

- **Detect:** audit vaults with unapproved public-network-access configuration.
- **Prevent:** consider a built-in Key Vault policy supporting `audit`/`deny` after testing approved private endpoints, trusted-service requirements, DNS, access patterns and platform-service impacts.
- **Correct:** coordinate network configuration changes through IaC and test dependent applications and break-glass procedures before restricting public access.
- **Respond:** prioritize investigation where an exposed vault also has risky identity permissions or indicators of misuse.

### GR-06 — Storage secure transfer

- **Detect:** identify storage accounts not requiring HTTPS-only/secure transfer.
- **Prevent:** choose a supported built-in secure-transfer policy and progress toward `deny` only after reviewing application compatibility.
- **Correct:** change the underlying storage setting via managed IaC and test each relevant client/protocol before enforcement.
- **Respond:** treat exceptions as data-protection risk decisions; escalate security incidents only when warranted by exposure or observed activity.

## 5. OPA/Rego integration — deliberately narrow

**Decision:** AFG will design **one pre-deployment guardrail**, GR-02, with OPA/Rego. This does **not** replace Azure Policy or create a parallel runtime policy platform.

```text
Proposed Terraform change
       |
       v
Terraform plan JSON (sensitive values sanitized; never committed)
       |
       v
OPA/Rego policy check (Conftest or OPA CLI)
       |---- fail ----> block proposed CI change / request correction
       |
      pass
       v
Approved deployment workflow
       |
       v
Azure Policy assignment/evaluation (and deny when enabled)
       |
       v
Azure resources + posture/compliance review
```

**Input contract for future implementation:** Examine `resource_changes[]` for resource type, action and `change.after` / `change.after_unknown`; ignore no-op/read/delete cases only when justified by the test specification. Fail closed for indeterminate public-network-access states unless an explicitly reviewed path applies. Ensure the check applies to *all* relevant storage-account changes and cannot be bypassed through unreviewed pipeline changes.

**Minimum planned fixtures:** (1) compliant private-only create passes; (2) public-enabled create fails; (3) public-enabled update fails; (4) missing or unknown setting fails or is held for explicit review; (5) unrelated resource does not falsely fail; (6) documented approved exception behavior is tested without embedding arbitrary bypasses. A local fixture proves the Rego evaluation logic **only**; a separate test must demonstrate the CI gate and Azure Policy behavior.

**Division of responsibility:** Phase 2 documents the guardrail specification; Issue #29 may validate one local Rego check and one low-cost Azure Policy enforcement example; Phase 6 owns generalized pipeline security, policy packaging, versioning, integrity and broad CI integration.

## 6. Progressive enforcement and exceptions

1. **Specify:** associate risk, requirement, framework control, candidate definition, owner, eligible resource types, scope and intended effect.
2. **Evaluate:** assess existing resources and benign test plans using `audit` or a suitable `DoNotEnforce` assignment. These are not interchangeable mechanisms.
3. **Review impact:** identify false positives, unsupported API/resource types, production dependencies, recovery requirements and business-critical exceptions.
4. **Correct:** prefer source IaC changes; test `modify` / `deployIfNotExists` only where supported and appropriately permissioned.
5. **Authorize:** document unavoidable residual risk and a narrow, reviewable waiver/mitigation; implement a technical Azure Policy exemption only after approved authorization.
6. **Enforce and monitor:** promote selected preventive assignments at validated scopes; monitor failed deployments, compliance changes and rollback readiness.

Do not equate an inherited assignment with a compliant resource; do not assume a successful remediation task proves the control objective. Rollback of assignment enforcement does not automatically revert all changes made by remediation.

## 7. Ownership and operating boundaries

| Activity | Proposed leading function | Approval / dependency |
|---|---|---|
| Guardrail risk and control objective | Cloud Security Architecture | Governance and business/workload review |
| Azure Policy definition/initiative/assignment source | Cloud Platform Engineering | Architecture review and authorized change |
| OPA/Rego guardrail specification | Cloud Security Architecture + Platform/DevSecOps | Phase 6 CI design; PR review |
| Application impact and source-IaC correction | Workload Engineering | Workload owner validates business continuity |
| Compliance review and exception inventory | Cloud Governance / Security | SharePoint operational record |
| Acceptance of residual business risk | Delegated business risk authority (TBD) | Cannot be presumed from technical exemption permission |
| Technical deployment of an approved exemption | Cloud Platform Engineering | Documented prior authorization |
| Incident triage and response | Security Operations | Phase 5 operating processes |

These are **proposed roles**, not assigned named employees or authorized enterprise approvals. Detailed RACI belongs to Issue #28.

## 8. Representative validation and evidence plan

The following cases are **planned** for Issue #29, not completed.

| Test | Guardrail | Planned observation | Expected sanitized evidence | Cost approach |
|---|---|---|---|---|
| GV-01 | GR-01 | Verify inherited tag audit and correct eligible-resource denominator | Assignment scope, sample compliance states, tag inventory | Reuse existing lab resources |
| GV-02 | GR-02 | Rego accepts compliant and rejects unsafe Terraform plan fixtures, including unknown values | Versioned Rego policy/fixtures, CLI test output, PR decision if integrated | Local only; no Azure cost |
| GV-03 | GR-02 | Azure Policy non-enforcing evaluation and then approved deny reject a test public-access configuration while compliant config proceeds | Assignment/effect details, compliance evaluation, sanitized deployment response | One short-lived test storage account; estimate costs first |
| GV-04 | GR-03 | Key Vault log setting is detectable and a supported correction is effective | Evaluation state, identity scope, remediation output, destination check | Optional; estimate vault/log ingestion and retention |
| GV-05 | GR-04–GR-06 | Review applicability/effect support and document test readiness without deploying all candidate controls | Versioned definition references, test matrix and decisions | Metadata/research first |

Tests are independent: success in OPA does not prove Azure assignment behavior, and Azure Policy compliance does not demonstrate operational application availability. Capture negative as well as positive tests. Maintain existing persistent management groups/subscriptions and tear down only newly created temporary resources as approved.

## 9. Control acceptance criteria and KPIs

- **Design coverage:** 6/6 candidate guardrails map to an existing enterprise risk, requirement, framework control, responsible function, proposed scope and validation method.
- **Deployment coverage (future):** all targeted test scopes have the expected **applicable** assignments and correct effect/parameters; report denominator and exclusions.
- **Enforcement effectiveness (future):** validated unsafe test operations are rejected in enforcement mode while intended compliant operations succeed.
- **Detection quality (future):** policy finds true configuration gaps without excessive false positives; track time from evaluation to triage.
- **Remediation quality (future):** source configuration corrected where applicable, resource reevaluated and application operation verified.
- **Risk governance (future):** 100% of active approved exceptions carry owner, rationale, precise scope, approval reference and review/expiry date.
- **Operating impact (future):** policy-induced failed deployments and associated incidents tracked; no assertion of cost/time savings without baseline and measurement.

The eventual governance dashboard should distinguish **assignment coverage**, **actual compliance**, **exceptions**, and **business-impact measures**. Not every candidate needs an enforcement phase: detective controls may be the correct long-term choice.

## 10. Candidate Azure policy references and design verification

Names below are **selection references**, not deployed policies. Verify the actual policy ID, version, effect parameter, alias/resource applicability and assignment compatibility before building Azure Policy as Code.

| Guardrail | Microsoft documentation reference | Verification to perform |
|---|---|---|
| GR-01 | [Azure Policy: inherit tag from resource group](https://learn.microsoft.com/en-us/azure/governance/policy/tutorials/create-and-manage) | Decide whether to audit required tags, inherit only accurate metadata, or deny new missing-tag deployments. |
| GR-02 | [Built-in policy definitions for Azure Storage](https://learn.microsoft.com/en-us/azure/storage/common/policy-reference) | Select **Storage accounts should disable public network access**; distinguish from anonymous blob-access policy. |
| GR-03 | [Built-in Key Vault policy definitions](https://learn.microsoft.com/en-us/azure/key-vault/policy-reference) | Select suitable Key Vault diagnostics audit/deployment definitions and destination configuration. |
| GR-04 | [Azure Policy built-in definitions](https://learn.microsoft.com/en-us/azure/governance/policy/samples/built-in-policies) | Verify allowed-locations built-in and exemptions for global/nonstandard service behavior. |
| GR-05 | [Key Vault Azure Policy integration](https://learn.microsoft.com/en-us/azure/key-vault/general/azure-policy) | Confirm public-network-access built-in effect and service exceptions. |
| GR-06 | [Azure Storage built-in definitions](https://learn.microsoft.com/en-us/azure/storage/common/policy-reference) | Select secure-transfer-required built-in; confirm supported effects and resource types. |

Additional technical references: [Azure Policy remediation](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources), [Azure Policy `modify` effect](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effect-modify), [OPA Terraform plan evaluation](https://www.openpolicyagent.org/docs/terraform).

## 11. Dependencies, open decisions and closure criteria

**Open technical decisions, not blockers to documenting the shortlist:** exact built-in IDs/versions and supported effects; candidate-to-initiative composition; approved region list; canonical ownership tag vocabulary; Key Vault diagnostics destination, retention and permissions; compatibility constraints for storage/Key Vault services; final exception authority; detailed CI implementation and accepted unknown-value handling; representative lab budget.

**Issue boundaries:**

- **#25 (this issue):** Document six candidate guardrails, scope, effects, control mapping, OPA design and validation plan.
- **#26:** Compliance monitoring, metrics and evidence architecture.
- **#27:** Exception request and risk-acceptance workflow.
- **#28:** Approved governance roles and RACI.
- **#29:** Implement and validate representative guardrails; retain only observed evidence.
- **#30:** Final Phase 2 architecture review.

**Issue #25 may close following review and version-controlled publication of this document** if the six entries have credible owner/scope/effect choices and traceability; deployment and measured effectiveness remain future work. Do not equate issue closure with implementation, risk acceptance or regulatory attestation.
