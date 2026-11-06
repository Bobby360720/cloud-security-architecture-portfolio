# Phase 2 — Cloud Governance

## Objective

Establish enterprise Azure governance, security guardrails,
policy enforcement, compliance, and exception management.

## Areas

- Azure Policy
- Policy initiatives
- Governance baselines
- Security baselines
- Tagging
- Compliance
- Policy exceptions
- Policy as Code

## Phase 2 — Representative End-to-End Traceability

The following example demonstrates how AFG connects an enterprise assessment finding to a security control and validated implementation. It represents one tested governance scenario, not enterprise-wide control coverage.

| Stage | Reference | Description |
|---|---|---|
| Finding | F-005 | Public exposure is not consistently governed |
| Enterprise risk | R-004 | Unnecessary public exposure increases attack surface |
| Business requirement | BR-002 (supporting) | Reduce risk without unnecessarily blocking delivery |
| Security requirement | SEC-004 | Restrict public PaaS exposure unless explicitly justified |
| Technical requirement | TR-008 | Establish private endpoint and public-exposure standards |
| Control objective | NET-01 | Network exposure protection |
| Architecture decision | GR-02 guardrail design | Progressive Audit-to-Deny enforcement with pre-deployment checks |
| Control | GR-02 | Azure Storage public network access guardrail |
| Implementation | Azure Policy and OPA/Rego | Resource-group-scoped Azure Policy assignments and local policy evaluation |
| Validation | P02-08 | Audit detection, seven passing Rego tests, Deny rejection, compliant deployment |
| Evidence | [Phase 2 Governance Validation](evidence/phase2-governance-validation.md) | Dated and observed test results |
| Residual risk | R-004 | Enterprise residual risk remains subject to reassessment |

### Residual Risk Disposition — R-004

**Current disposition:** Mitigation planned and partially validated through representative GR-02 testing.

The GR-02 lab demonstrated Azure Policy Audit detection, preventive Deny enforcement, compliant Storage deployment, and local OPA/Rego policy validation.

These results support the technical feasibility and effectiveness of the tested guardrail. They do not establish enterprise-wide implementation or a reduction in R-004's residual-risk rating.

**Remaining exposure:** Other publicly accessible PaaS services, approved external-facing workloads, network segmentation gaps, inconsistent private endpoint adoption, and incomplete enforcement coverage.

**Treatment ownership:** Network and Workload Owners, consistent with the Phase 0 enterprise risk register.

**Required follow-up:** Assess enterprise control coverage, validate implementation across applicable workloads, evaluate outstanding exceptions, and obtain an authorized residual-risk decision.

**System of record:** SharePoint for operational risk treatment and acceptance; GitHub for architecture and validation evidence.

**Risk status:** No change to the existing modeled High risk rating (16/25) is justified by the isolated lab results.

### Architecture and Evidence Boundaries

The representative GR-02 lab demonstrates control behavior within isolated Azure resource-group scopes and a local OPA/Rego environment.

It does not establish enterprise-wide policy deployment, management-group inheritance, automated remediation, or formal risk acceptance.

The Phase 0 risk register remains the architectural risk baseline. SharePoint remains the operational system of record for findings, risk treatment, exceptions, and residual-risk decisions.
