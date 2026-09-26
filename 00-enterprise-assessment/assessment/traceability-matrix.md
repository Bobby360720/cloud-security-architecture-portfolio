# Phase 0 Traceability Matrix

**Organization:** AFG Enterprises (modeled)  
**Status:** Phase 0 architecture baseline — pending validation

## Purpose

This matrix connects architecture findings, enterprise risks, requirements,
detailed assessment findings and delivery phases.

The Enterprise Risk Register defines the canonical risk IDs R-001 through
R-015. Detailed IAM, NET and SOC findings are tracked separately in the
Enterprise Findings Register.

## Architecture Traceability

| Architecture Finding | Enterprise Risk | Requirements | Primary Phase |
|---|---|---|---|
| F-001 — Governance hierarchy | R-001 | SEC-006, SEC-015, TR-001, TR-002 | 1–2 |
| F-002 — Ownership metadata | R-008 | SEC-009, TR-005 | 2 |
| F-003 — Privileged access | R-002 | SEC-001, TR-006 | 3 |
| F-004 — Workload credentials | R-003 | SEC-002, SEC-003, TR-007 | 3/6 |
| F-005 — Public exposure | R-004 | SEC-004, TR-008, TR-009 | 4 |
| F-006 — Telemetry | R-005 | SEC-005, TR-010 | 5 |
| F-007 — Policy lifecycle | R-006 | SEC-006, SEC-007, TR-003, TR-004 | 2 |
| F-008 — Manual configuration | R-007 | SEC-008, SEC-014, TR-012, TR-013 | 6 |
| F-009 — Data sensitivity | R-009 | SEC-010, TR-014 | 7 |
| F-010 — Recovery assurance | R-010 | SEC-011 | 1/5 |
| F-011 — SecOps lifecycle | R-011 | SEC-012, TR-011 | 5/6 |
| F-012 — AI governance | R-012 | SEC-013, TR-015 | 8 |



## Business Requirements Traceability

The following mappings connect AFG Enterprises' business
requirements to the enterprise risk baseline and planned
transformation phases.

These are proposed architecture relationships and remain
subject to Phase 0 review.

| Business Requirement | Business Objective | Enterprise Risks | Primary Phase |
|---|---|---|---|
| BR-001 | Scalable cloud governance | R-001, R-006 | 1–2 |
| BR-002 | Risk reduction without unnecessarily blocking delivery | R-006, R-007 | 2, 6 |
| BR-003 | Resource ownership and cost accountability | R-008 | 2 |
| BR-004 | Critical workload resilience | R-010 | 1, 5 |
| BR-005 | Auditable and explainable architecture decisions | R-001, R-006 | 0–2 |
| BR-006 | Hybrid workload support during modernization | R-013 | 1, 2, 5 |
| BR-007 | Repeatable secure deployment patterns | R-007 | 6 |
| BR-008 | Security readiness for future AI adoption | R-012 | 8 |
| BR-009 | Measurable governance effectiveness | R-005, R-006 | 2, 5 |
| BR-010 | Incremental modernization without a greenfield rebuild | R-001, R-013 | 1–8 |

### Cross-Cutting Business Requirements

BR-005 requires significant architecture decisions to be
documented through Architecture Decision Records (ADRs).

BR-010 establishes incremental modernization as a
program-wide constraint. It is addressed by ADR-001
and applies across the transformation phases.

Risk relationships identify where a requirement influences
risk treatment. They do not imply that the requirement
has been implemented or validated.


## Additional Enterprise Risk Coverage

The following risks are included in the Enterprise Risk Register but do not
yet have dedicated F-series architecture finding identifiers.

| Enterprise Risk | Risk Theme | Related Assessment Finding | Primary Phase |
|---|---|---|---|
| R-013 | Legacy/Arc governance | NET-06, NET-06 | 1/2/5 |
| R-014 | Defender coverage | SOC-06 | 5 |
| R-015 | Non-production data protection | No numbered finding assigned | 7 |

R-013 covers broader legacy and Azure Arc governance than NET-06 alone.
R-015 requires a documented assessment source before a numbered finding
can be assigned.


## Detailed Findings Crosswalk

These mappings are proposed architecture relationships. They do not
indicate that the modeled findings have been independently validated.

| Enterprise Risk | Supporting Detailed Findings |
|---|---|
| R-002 | IAM-01, IAM-02, IAM-05, IAM-06 |
| R-003 | IAM-03, IAM-04, IAM-07 |
| R-004 | NET-01, NET-02, NET-03, NET-05, NET-06 |
| R-005 | SOC-01, SOC-02, SOC-03 |
| R-008 | SOC-07; IAM-03 (secondary relationship) |
| R-011 | SOC-04, SOC-05 |
| R-013 | NET-04; NET-06 (secondary relationship) |
| R-014 | SOC-06 |

All 20 numbered IAM, NET and SOC findings have a proposed primary
enterprise-risk mapping.

## Outstanding Evidence Gaps

- R-001, R-006, R-007, R-009 and R-010 are supported by
  cross-domain architecture candidates rather than dedicated
  numbered findings.
- R-012 has no corresponding numbered AI security finding.
- R-013 includes broader Azure Arc governance that is not fully
  represented by NET-04 and NET-06.
- R-015 requires a documented assessment source for
  non-production data protection.

Do not create findings solely to fill gaps in the matrix.

## Cross-Domain Architecture Candidates

The seven architecture candidates remain subject to governance review.

| Architecture Candidate | Related Enterprise Risk |
|---|---|
| Management-group and subscription governance | R-001 |
| Azure Policy fragmentation | R-001, R-006 |
| Resource ownership metadata | R-008 |
| Security exception lifecycle | R-006 |
| Manual configuration and IaC adoption | R-007 |
| Data classification and ownership | R-009 |
| Workload resilience | R-010 |

These are proposed relationships, not additional approved findings.

## Requirements Coverage


Business requirements BR-001 through BR-010 are mapped
in the Business Requirements Traceability section above.

The authoritative requirement statements, priorities
and success measures remain in
`requirements/business-requirements.md`.


## Use

Each delivery phase should trace its implemented controls and validation
evidence back to the relevant enterprise risk and architecture
requirements.

The traceability chain is:

Assessment Finding → Enterprise Risk → Requirement → Architecture
Decision → Implemented Control → Validation → Evidence

A documented relationship does not establish that a modeled finding
has been verified or that its associated risk has been remediated.
