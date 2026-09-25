# Enterprise Risk Register

**Organization:** AFG Enterprises (modeled)  
**Assessment:** Phase 0 — Enterprise Assessment  
**Status:** Baseline documented; modeled risks pending validation  
**Risk IDs:** R-001 through R-015

## Purpose

This register documents the consolidated enterprise architecture risks identified during Phase 0. It establishes the risk baseline used to prioritize and trace the cloud-security transformation.

Detailed assessment findings are maintained separately in the Enterprise Findings Register. Multiple findings may contribute to a single enterprise risk.

The SharePoint Enterprise Risk Register is the operational tracking system. This document is the version-controlled architecture baseline.

## Rating Model

Likelihood and Impact use a scale of 1–5.

**Inherent Risk Score = Likelihood × Impact**

| Score | Rating |
|---|---|
| 20–25 | Critical |
| 15–19 | High |
| 8–14 | Medium |
| 1–7 | Low |

The scores below represent the modeled Phase 0 assessment. They have not been independently validated against a production environment.

## Enterprise Risks

| ID | Risk Statement | L | I | Score | Rating | Treatment | Accountable Team | Phase |
|---|---|---:|---:|---:|---|---|---|---|
| R-001 | Fragmented management-group/policy inheritance causes inconsistent enterprise controls. | 4 | 5 | 20 | Critical | Mitigate | Cloud Platform | 1–2 |
| R-002 | Standing or excessive privilege enables unauthorized high-impact change. | 4 | 5 | 20 | Critical | Mitigate | Identity/Security | 3 |
| R-003 | Long-lived workload credentials or excessive API permissions are compromised or abused. | 4 | 5 | 20 | Critical | Mitigate | App/Identity Security | 3/6 |
| R-004 | Unnecessary public exposure increases attack surface. | 4 | 4 | 16 | High | Mitigate | Network/Workload Owners | 4 |
| R-005 | Incomplete telemetry prevents timely detection or investigation. | 4 | 4 | 16 | High | Mitigate | Security Operations | 5 |
| R-006 | Weak exception lifecycle creates permanent unmanaged security debt. | 4 | 4 | 16 | High | Mitigate | Governance/Security | 2 |
| R-007 | Manual configuration causes drift, inconsistent controls, and weak auditability. | 4 | 4 | 16 | High | Mitigate | Platform Engineering | 6 |
| R-008 | Missing ownership/criticality metadata delays remediation and incident response. | 4 | 4 | 16 | High | Mitigate | Cloud Governance | 2 |
| R-009 | Incomplete data classification leads to insufficient protection of sensitive data. | 3 | 5 | 15 | High | Mitigate | Data Governance | 7 |
| R-010 | Inconsistent recovery testing results in failure to meet business recovery needs. | 3 | 5 | 15 | High | Mitigate | Platform/Workload Owners | 1/5 |
| R-011 | Unmanaged detection lifecycle causes alert gaps, noise, or stale controls. | 3 | 4 | 12 | Medium | Mitigate | Security Operations | 5 |
| R-012 | AI adoption exposes sensitive data or introduces unsafe model/agent behavior. | 3 | 5 | 15 | High | Mitigate | AI Governance/Security | 8 |
| R-013 | Legacy/Arc workloads remain outside modern governance patterns. | 3 | 4 | 12 | Medium | Mitigate | Infrastructure/Platform | 1/2/5 |
| R-014 | Inconsistent Defender coverage leaves preventable security blind spots. | 3 | 4 | 12 | Medium | Mitigate | Security Engineering | 5 |
| R-015 | Non-production environments process production-like data without equivalent safeguards. | 3 | 5 | 15 | High | Mitigate | Data/App Owners | 7 |

## Risk Ownership

The Accountable Team column identifies the proposed functional owner of each risk. It does not establish individual ownership or formal risk acceptance.

Individual risk owners will be recorded in the SharePoint Enterprise Risk Register when assigned.

## Relationship to Enterprise Findings

The Enterprise Findings Register maintains detailed assessment findings, including:

- **IAM:** IAM-01 through IAM-07
- **Network:** NET-01 through NET-06
- **Security Operations:** SOC-01 through SOC-07

Each numbered finding retains its own identifier and can reference one or more enterprise risks.

The seven cross-domain architecture candidates remain subject to governance review. They are not automatically treated as additional enterprise risks.

## Residual Risk

Residual scores are not assigned in Phase 0 because treatment controls have not yet been validated.

Each delivery phase will reassess its source risks after implementation and validation evidence exists. Residual likelihood, impact, rating and any formal risk acceptance will be maintained in the operational SharePoint register.

## Architecture Traceability

Enterprise risks are linked to architecture findings, security requirements, technical requirements and delivery phases in the [Phase 0 Traceability Matrix](../assessment/traceability-matrix.md).

Risk IDs R-001 through R-015 are the canonical identifiers for this architecture baseline.
