# Phase 0 --- Enterprise Assessment

> **Portfolio note:** AFG Enterprises is a fictionalized, sanitized
> enterprise used to demonstrate an enterprise cloud-security
> architecture methodology. All names, quantities, findings, and
> technical details are representative.

## Mission

Phase 0 establishes the evidence base for the AFG cloud-security
transformation. No major target-state technology is selected merely
because it is available. The phase first determines what exists, what
matters to the business, where material risk exists, what constraints
apply, and what the future architecture must accomplish.

## Phase 0 Questions

Phase 0 must answer:

1.  What cloud and hybrid assets exist?
2.  Who owns them and what business capabilities do they support?
3.  Which workloads and data are most critical?
4.  Where are the largest security-governance gaps?
5.  What risks arise from those gaps?
6.  What business, security, and technical requirements follow from the
    risks?
7.  Which risks should be accepted, mitigated, transferred, or avoided?
8.  What sequence of architecture work provides the greatest risk
    reduction?

## Deliverables

  ------------------------------------------------------------------------------------------
  Deliverable                                            Purpose
  ------------------------------------------------------ -----------------------------------
  `assessment/enterprise-assessment.md`                  Consolidated enterprise findings

  `assessment/security-governance-maturity.md`           Current vs. target maturity

  `current-state/cloud-inventory.md`                     Representative Azure/hybrid
                                                         inventory

  `current-state/current-state-architecture.md`          Architectural description of the
                                                         existing estate

  `current-state/identity-current-state.md`              Identity and privileged-access
                                                         baseline

  `current-state/network-current-state.md`               Connectivity and exposure baseline

  `current-state/security-operations-current-state.md`   Monitoring/detection baseline

  `requirements/business-requirements.md`                Business outcomes and constraints

  `requirements/security-requirements.md`                Traceable security requirements

  `requirements/technical-requirements.md`               Platform and engineering
                                                         requirements

  `risks/enterprise-risk-register.md`                    Prioritized risk register

  `risks/remediation-priorities.md`                      Risk-driven transformation sequence

  `diagrams/current-state-architecture.md`               Portable Mermaid current-state
                                                         diagram

  `decisions/ADR-001-transformation-strategy.md`         Architecture decision establishing
                                                         the phased program

  `templates/enterprise-assessment-template.md`          Reusable assessment template

  `templates/risk-register-template.md`                  Reusable risk template

  `evidence/README.md`                                   Rules for sanitized portfolio
                                                         evidence
  ------------------------------------------------------------------------------------------

## Assessment Method

The assessment uses a traceability chain:

`Observation → Finding → Risk → Requirement → Architecture Phase → Control → Validation → Evidence`

This prevents the portfolio from becoming a collection of disconnected
technology demonstrations.

## Executive Findings

The representative assessment identifies five dominant themes:

-   **Governance fragmentation:** control inheritance, ownership, policy
    lifecycle, and exception handling are inconsistent.
-   **Identity risk:** privileged and workload access requires stronger
    lifecycle governance.
-   **Exposure and telemetry gaps:** private connectivity and logging
    are not uniformly applied.
-   **Manual configuration:** repeatable platform controls are not
    consistently delivered as code.
-   **Data and emerging-technology governance:** classification and
    AI-specific controls are immature.

## Phase Gate

Phase 0 is complete when:

-   the current state is documented at an architecture level;
-   critical assets and owners are identifiable;
-   major security-governance gaps have been assessed;
-   risks have owners, ratings, and treatments;
-   requirements are traceable to risks;
-   transformation priorities are approved;
-   Phase 1 has sufficient requirements to begin target-state
    landing-zone design.

## Next Phase

**Phase 1 --- Azure Landing Zone** establishes the target Azure platform
foundation, management-group model, subscription organization, shared
services, and foundational platform architecture.
