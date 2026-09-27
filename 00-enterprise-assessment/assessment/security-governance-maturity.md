# Security Governance Maturity Assessment

**Organization:** AFG Enterprises (modeled)  
**Phase:** 0 — Enterprise Assessment  
**Evidence classification:** Modeled assessment; selected management-group and subscription-placement patterns have been validated in the portfolio lab.

## Purpose and Scope

Assess the consistency, ownership, enforcement, measurement, and lifecycle of governance controls across AFG's fictionalized Azure-first, hybrid enterprise. This assessment establishes design inputs for subsequent phases; it does not assert that modeled enterprise controls or maturity ratings have been independently verified in production.

## Maturity Scale

| Level | Name | Definition |
|---:|---|---|
| 1 | Initial | Ad hoc, person-dependent, primarily manual |
| 2 | Developing | Controls exist but are inconsistent across scope |
| 3 | Defined | Standards and ownership are documented |
| 4 | Managed | Controls are automated, measured, reviewed, and governed |
| 5 | Optimized | Continuous, risk-driven improvement with high automation |

## Assessment Methodology

Current ratings are **modeled assessment judgments** based on the Phase 0 cloud inventory, current-state assessments, enterprise risk register, and requirements. They are not independently validated measurements of a production enterprise. Target ratings express intended future operating capability, not approved or completed implementations.

Assess each domain against six dimensions: (1) documented standards, (2) accountable ownership, (3) consistency of implementation across scopes, (4) enforcement and exception handling, (5) measurable effectiveness and retained evidence, and (6) periodic review and remediation. The rating reflects the overall modeled operating capability; the gap is the target minus current rating. Ratings must not increase solely because a product is enabled or a design has been written.

The portfolio distinguishes **modeled** enterprise inventory and findings from **validated** lab evidence. The management-group hierarchy, selected platform subscription placement, and Terraform brownfield-reconciliation patterns have been documented as lab-validated elsewhere in Phase 0. Those lab results do not validate enterprise-wide policy, RBAC, monitoring, or operational maturity.

## Current and Target Maturity

| Domain | Current | Target | Gap | Primary Phase |
|---|---:|---:|---:|---|
| Enterprise cloud governance | 2 | 4 | 2 | 1–2 |
| Management-group/subscription governance | 2 | 4 | 2 | 1 |
| Azure Policy governance | 2 | 4 | 2 | 2 |
| Identity governance | 2 | 4 | 2 | 3 |
| Workload identity/credentials | 2 | 4 | 2 | 3/6 |
| Network security | 2 | 4 | 2 | 4 |
| Security operations | 3 | 4 | 1 | 5 |
| Logging/telemetry | 3 | 4 | 1 | 5 |
| DevSecOps | 2 | 4 | 2 | 6 |
| Policy/Infrastructure as Code | 1 | 4 | 3 | 6 |
| Data protection | 2 | 4 | 2 | 7 |
| Resilience governance | 2 | 4 | 2 | 1/5 |
| AI security | 1 | 3 | 2 | 8 |

These ratings are retained from the existing Phase 0 assessment. The domain-specific observations below explain their architectural basis and do not constitute additional verified findings.

## Interpretation

### Existing Security Monitoring Capability

Security monitoring is modeled at **Defined (Level 3)** in portions of the enterprise: Sentinel, Defender for Cloud, Log Analytics, and modern monitoring components are present. Coverage, retention, detection ownership, and telemetry collection are not yet consistent across all modeled workloads.

### Policy and Infrastructure as Code Gap

Policy and Infrastructure as Code have the largest numerical gap in this assessment (Level 1 to Level 4). Manual configuration and inconsistent deployment patterns impede repeatability, review, drift detection, and auditability.

### Identity and Workload Credential Exposure

Identity governance and workload credentials are modeled at **Developing (Level 2)**. Standing privilege, inconsistent access reviews, incomplete workload ownership, and stored credentials create material risk even where core identity tooling exists.

## Management-Group and Subscription Governance

**Modeled current maturity: Level 2; target: Level 4.** The logical enterprise separates platform services from production, non-production, sandbox, and legacy landing zones. The portfolio lab has validated selected management-group and core platform subscription-placement patterns, but this does not demonstrate consistent governance across all 12 modeled subscriptions.

The modeled enterprise has inconsistent subscription ownership, incomplete secondary ownership, overlapping control scopes, and uneven inheritance between legacy and modern workloads. Subscription placement must be linked to workload purpose, business criticality, delegated administration, and applicable guardrails.

**Required future capabilities:** documented management-group responsibilities; repeatable subscription onboarding and placement; accountable primary and backup owners; inherited baseline controls at the highest appropriate scope; and periodic reviews of exceptions and subscription lifecycle. Phase 1 establishes the organizational architecture; Phase 2 establishes consistent governance enforcement.

## Azure Policy, Inheritance, and Exception Governance

**Modeled current maturity: Level 2; target: Level 4.** The cloud inventory models 74 Azure Policy assignments, including 31 management-group and 43 subscription-level assignments, 29 custom definitions, and 11 initiatives. These figures describe the fictionalized enterprise, not verified live inventory.

Policy assignments overlap across scopes; some controls remain in Audit without an established progression to enforcement; ownership and remediation are inconsistent. A higher-level assignment is not automatically appropriate for every control: applicability, workload impact, exemptions, and deployment prerequisites must be evaluated.

**Required future capabilities:** control-purpose-based initiatives; documented policy owners; an audit-to-enforcement lifecycle; scoped, approved, time-bound, reviewable exceptions; assigned remediation owners; compliance measurement; and version-controlled changes. SharePoint remains the operational exception, findings, and risk-tracking system; GitHub maintains the version-controlled architecture baseline.

## Identity, Privileged Access, and Accountability

**Modeled current maturity: Level 2; target: Level 4.** Entra ID, Conditional Access, group-based RBAC, and PIM are available in the modeled environment, but privileged access and review practices vary. Some standing roles and direct user RBAC assignments remain, and access-review coverage is selective. Workload identities also lack consistent owners and credential lifecycle controls.

**Required future capabilities:** role ownership and separation of duties; group-based least-privilege RBAC; controlled elevation through PIM where supported; recurring access reviews; emergency-access procedures; and named business and technical owners for high-privilege application permissions. Phase 3 addresses identity governance, with workload identity patterns also feeding Phase 6.

## Naming, Tagging, Ownership, and Resource Lifecycle

**Governance assessment: Level 2 within enterprise cloud governance.** The modeled inventory indicates incomplete ownership and classification metadata: `Environment` 91%, `Application` 76%, `Owner` 63%, `BusinessUnit` 69%, `CostCenter` 72%, `Criticality` 41%, and `DataClassification` 27%. These are modeled estimates, not measured compliance results.

The existing inventory does not establish a verified enterprise-wide naming-compliance percentage or a complete resource retirement process. Both are **assessment gaps**, not grounds for inventing additional findings.

**Required future capabilities:** approved naming conventions; mandatory metadata with defined owners; resource onboarding and change review; periodic orphaned-resource and ownership checks; exception handling; and documented archival, decommissioning, and disposal responsibilities. Phase 2 should define measurable coverage and compliance evidence, including the business requirement for at least 95% required ownership metadata coverage.

## Cross-Domain Governance Dependencies

Network security (Level 2) depends on consistent ownership of public exposure, private connectivity, DNS, and segmentation standards. Security operations and telemetry (Level 3) depend on approved collection patterns, DCR associations, retention, and detection ownership. DevSecOps (Level 2) and Policy/Infrastructure as Code (Level 1) depend on version control, reviewable deployment, and change auditability. Data protection (Level 2) depends on classification and ownership; resilience governance (Level 2) depends on workload criticality and approved RTO/RPO; AI security (Level 1) requires use-case, data-flow, identity, and agent governance before broader adoption.

These relationships explain why governance improvements must be sequenced with landing-zone, identity, network, security-operations, engineering, data-protection, resilience, and AI work rather than treated as an isolated policy exercise.

## Governance Risk and Requirements Traceability

The relationships below reference the established enterprise risk register and requirements; they do not introduce new risk IDs or claim that treatment is complete.

| Governance gap | Existing risk | Relevant requirements | Primary delivery |
|---|---|---|---|
| Inconsistent management-group and subscription guardrails | R-001 | BR-001, SEC-006, SEC-015, TR-001, TR-002 | 1–2 |
| Standing privilege and inconsistent access governance | R-002 | SEC-001, TR-006 | 3 |
| Workload identity ownership and credential lifecycle | R-003 | SEC-002, SEC-003, TR-007 | 3/6 |
| Policy exception and enforcement lifecycle | R-006 | BR-002, SEC-007, TR-003, TR-004 | 2 |
| Manual configuration, drift, and weak change auditability | R-007 | BR-007, SEC-008, SEC-014, TR-012, TR-013 | 6 |
| Incomplete ownership and tagging metadata | R-008 | BR-003, SEC-009, TR-005 | 2 |
| Incomplete security telemetry | R-005 | SEC-005, TR-010 | 5 |
| Unmanaged detection lifecycle | R-011 | SEC-012, TR-011 | 5/6 |
| Uneven legacy and Arc governance | R-013 | BR-006, BR-010 | 1/2/5 |

Operational findings, remediation assignments, exception approvals, and residual-risk reassessments belong in SharePoint. GitHub records the modeled architecture, baseline risk and requirements relationships, and later validation evidence. No residual risk reduction is asserted by this maturity assessment.

## Target-State Characteristics

Level 4 does not mean every control is automated. It means the enterprise can consistently demonstrate:

- an accountable owner and an approved standard;
- consistent, measurable implementation and evidence of compliance;
- scoped, approved, time-bound, reviewable exceptions;
- assigned remediation and lifecycle review;
- automated enforcement where appropriate, with documented operational safeguards.

## Reassessment and Validation

Reassess maturity after major transformation milestones, using evidence from the relevant delivery phase. Acceptable evidence may include approved standards, policy-assignment exports, exception and remediation records, access-review results, deployment pipeline results, configuration-drift checks, telemetry coverage reports, and recorded control tests. Each item must identify its scope and date; evidence from a small lab must not be generalized to the entire modeled enterprise.

Scores should increase only when implementation and operating evidence support the new level. Document remaining gaps and unresolved decisions; do not treat planned controls, modeled counts, or written requirements as proof of operational effectiveness.

## Phase 0 Assessment Conclusion

AFG's modeled governance challenge is uneven adoption and enforcement of existing capabilities, not simply the absence of tools. The Phase 0 maturity baseline provides risk-linked design inputs for subsequent phases. It does not authorize target-state decisions, verify enterprise-wide control effectiveness, or replace the operational SharePoint findings and risk registers.
