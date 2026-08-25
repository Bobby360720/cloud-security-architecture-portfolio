# Architecture Principles

## Purpose

These principles define the decision-making guardrails for the Cloud
Security Architecture Portfolio. They are intended to keep every
phase---from enterprise assessment through the DLV FinTech
platform---consistent, secure, governable, and explainable.

## 1. Security Is an Architectural Requirement

Security is designed into platforms, workloads, identities, networks,
data flows, and delivery pipelines from the beginning. It is not a
control layer added after deployment.

**Implications** - Security requirements are documented alongside
business and technical requirements. - Architecture reviews include
threat, identity, data, network, logging, and recovery considerations. -
Controls are implemented as close to the platform and deployment process
as practical.

## 2. Zero Trust Is the Default Security Model

No identity, workload, device, network location, or service is trusted
solely because of where it resides.

**Principles** - Verify explicitly. - Use least privilege. - Assume
breach. - Prefer short-lived and managed credentials. - Continuously
evaluate access and risk.

## 3. Governance Is Platform Engineering

Governance should be built into the cloud platform rather than dependent
on tribal knowledge or recurring manual review.

**Implications** - Azure Policy is used to express enforceable
guardrails. - Policy and configuration should be version controlled. -
Management-group inheritance is used deliberately. - Exceptions are
documented, approved, time-bound, and reviewed.

## 4. Policy Follows a Safe Enforcement Lifecycle

Controls should mature through a predictable lifecycle:

`Draft → Lab Testing → Audit → Modify/DeployIfNotExists → Deny → Operational Standard`

Deny controls should not be introduced blindly. Compliance impact, false
positives, dependencies, and remediation paths must be understood first.

## 5. Architecture Must Be Modular

Large monolithic control sets create unnecessary coupling. Governance,
security, networking, identity, monitoring, resilience, cost, and
compliance controls should be modular where ownership or change cadence
differs.

This enables: - independent versioning; - clearer accountability; -
targeted assignments; - safer change management; - easier
troubleshooting.

## 6. Centralize Shared Platform Capabilities

Capabilities that benefit the entire enterprise should be designed once
and consumed consistently.

Examples include: - connectivity; - identity foundations; - security
monitoring; - policy; - DNS; - logging; - secrets and key management.

Centralization should not create unnecessary operational bottlenecks.
Platform services must expose clear ownership and consumption patterns.

## 7. Least Privilege and Separation of Duties

Human and workload access should be limited to the minimum required
scope, privilege, and duration.

Architecture should favor: - RBAC over direct individual permissions; -
privileged elevation over standing administrative access; - workload
identities over stored secrets; - separation between builders,
approvers, security reviewers, and operators where risk warrants it.

## 8. Private Access Is Preferred

Public exposure should be an explicit architectural decision rather than
the default.

Where practical: - use Private Link/private endpoints; - segment
networks; - restrict administrative paths; - control ingress and
egress; - centralize network inspection where it provides meaningful
security value.

Any required public exposure must have compensating controls and
documented justification.

## 9. Everything Important Must Be Observable

A control that cannot be measured is difficult to govern.

Critical services should produce sufficient telemetry for: - security
monitoring; - incident response; - compliance; - availability; -
configuration drift; - forensic investigation.

Logging architecture must consider retention, access, cost, data
quality, and ownership---not merely log collection.

## 10. Secure Defaults, Explicit Exceptions

The platform should make the secure path the easiest path.

Exceptions must include: - business justification; - resource/scope; -
risk; - approver; - expiration date; - compensating controls; - review
date.

Permanent undocumented exceptions are architecture debt.

## 11. Infrastructure and Policy as Code

Repeatable cloud configuration should be automated and version
controlled wherever practical.

The portfolio will demonstrate: - Bicep and/or Terraform; - Azure Policy
as Code; - CI/CD validation; - peer review; - deployment gates; -
rollback or remediation planning.

Manual portal configuration should be minimized for repeatable platform
controls.

## 12. Design for Enterprise Scale

Architectural decisions must account for growth in subscriptions,
workloads, identities, regions, teams, and regulatory requirements.

Designs should avoid assumptions that only work for a small tenant or a
single workload.

## 13. Data Protection Follows the Data Lifecycle

Data security includes discovery, classification, access, encryption,
retention, monitoring, loss prevention, privacy, and destruction.

The required protection level is driven by data sensitivity and business
impact.

## 14. Resilience Is Part of Security

Availability and recoverability are security properties.

Architectures should consider: - redundancy; - backup; - disaster
recovery; - dependency failure; - administrative recovery; - break-glass
access; - restoration testing.

## 15. Architecture Decisions Must Be Explainable

Significant decisions are documented using Architecture Decision Records
(ADRs).

Each ADR should capture: - context; - decision; - alternatives
considered; - security implications; - operational implications; -
tradeoffs; - status.

The goal is not to pretend every decision is perfect. The goal is to
make the reasoning visible.

## 16. Measure Outcomes, Not Just Deployments

Success is not measured only by the number of policies, tools, or
security products deployed.

Architecture should be evaluated through outcomes such as: - policy
compliance; - privileged-access reduction; - public-exposure
reduction; - logging coverage; - remediation time; - exception aging; -
deployment consistency; - security findings; - recovery readiness.

## 17. AI Requires Its Own Security Model

AI workloads introduce additional concerns beyond conventional
application security, including: - prompt injection; - unsafe tool
use; - sensitive-data disclosure; - model and supply-chain risk; - RAG
authorization; - output validation; - agent identity; - AI governance
and monitoring.

AI security is therefore treated as a dedicated architecture phase.

## 18. Security Must Enable the Business

Controls should reduce material risk without creating unnecessary
friction.

When a control conflicts with a legitimate business requirement, the
architecture process should evaluate alternatives, compensating
controls, and residual risk rather than defaulting to either
unrestricted access or absolute prohibition.

------------------------------------------------------------------------

## Decision Test

A proposed architecture should be challenged with five questions:

1.  **Is it secure by default?**
2.  **Can it be governed at enterprise scale?**
3.  **Can it be automated and repeated?**
4.  **Can we observe and validate it?**
5.  **Can we explain why we designed it this way?**

If the answer to one or more is no, the design requires additional
review.
