# Enterprise Assessment

## Executive Assessment

AFG Enterprises is a modeled hybrid, Azure-first organization whose cloud adoption has outpaced the formalization of its enterprise cloud operating model. The modeled environment uses Microsoft security capabilities, but those capabilities are not consistently governed, inherited, automated, measured, or assigned to accountable owners.

The primary architectural concern is not the absence of security tooling. It is the lack of a sufficiently integrated security-governance system.

This Phase 0 assessment establishes an architectural baseline. Its findings and severities are provisional and require validation against authorized environment evidence.

## Scope

The assessment covers:

- Azure tenant, management groups, subscriptions and workload placement
- Microsoft Entra ID, privileged access and Azure RBAC
- Workload identities, application credentials and API permissions
- Hybrid connectivity, Azure networking and DNS
- Azure Policy, governance and exception management
- Microsoft Defender for Cloud and Microsoft Sentinel
- Azure Monitor, AMA, DCRs and diagnostic settings
- Secrets and key management
- Infrastructure delivery and DevSecOps
- Data protection and classification
- Resilience and recovery
- Emerging AI workloads

## Assessment Boundaries

This Phase 0 assessment does not:

- Reproduce or independently verify production configuration
- Disclose confidential tenant or workload identifiers
- Perform penetration testing
- Replace a formal regulatory audit
- Prescribe every Phase 1–8 implementation detail

## Findings Structure and Source of Truth

The assessment uses two complementary levels of findings:

1. **Executive findings (F-001–F-012):** Cross-domain architecture themes maintained in this document.
2. **Detailed findings (IAM-01–IAM-07, NET-01–NET-06 and SOC-01–SOC-07):** Individual modeled assessment findings maintained in the SharePoint Enterprise Findings Register and the relevant current-state assessment documents.

Executive findings summarize architecture concerns. Detailed findings provide narrower observations, proposed remediation and validation status. An executive finding may reference several detailed findings, and some executive findings currently have no numbered detailed finding.

The SharePoint Enterprise Findings Register is the operational record for detailed finding status and proposed risk mappings. The GitHub Enterprise Risk Register maintains the 15 consolidated enterprise risks.

## Executive Findings

### F-001 — Governance hierarchy is not yet the authoritative control plane

**Provisional severity:** High  
**Enterprise risk:** R-001  
**Supporting detailed findings:** No directly corresponding numbered IAM, NET or SOC finding. Supported by the cross-domain governance assessment; detailed evidence remains to be validated.

Policy assignments exist across multiple modeled scopes, and legacy placement patterns remain. This creates potential duplication, inconsistent inheritance and troubleshooting complexity.

**Proposed response:** Establish an approved management-group hierarchy, subscription placement standards and a consistent policy assignment model.

### F-002 — Resource ownership and criticality are incomplete

**Provisional severity:** High  
**Enterprise risk:** R-008  
**Supporting detailed findings:** IAM-03 (workload identity ownership, partial relationship) and SOC-07 (remediation ownership, related accountability concern).

Ownership, criticality and data-classification metadata are not consistently available from authoritative modeled cloud metadata. This may delay incident response, remediation and business impact assessment.

**Proposed response:** Define authoritative ownership and criticality standards, enforce applicable metadata and establish accountable remediation ownership.

### F-003 — Privileged access is not uniformly just-in-time

**Provisional severity:** Critical  
**Enterprise risk:** R-002  
**Supporting detailed findings:** IAM-01, IAM-02, IAM-05 and IAM-06.

Privileged access is not consistently time-bound. Some modeled access remains standing or directly assigned, while privileged access reviews and entitlement lifecycle controls are not universal.

**Proposed response:** Inventory privileged assignments, apply PIM and just-in-time access where supported, standardize governed access groups and establish recurring access reviews.

### F-004 — Workload credential governance is inconsistent

**Provisional severity:** Critical  
**Enterprise risk:** R-003  
**Supporting detailed findings:** IAM-03, IAM-04 and IAM-07.

Workload identity ownership and lifecycle controls are incomplete. Persistent client secrets and inconsistent API permission reviews create opportunities for excessive access and credential misuse.

**Proposed response:** Inventory workload identities, assign owners, prioritize managed identity or federation, manage remaining secrets and establish recurring API permission reviews.

### F-005 — Public exposure is not consistently governed

**Provisional severity:** High  
**Enterprise risk:** R-004  
**Supporting detailed findings:** NET-01, NET-02, NET-03, NET-05 and NET-06. NET-04 is related through DNS architecture but primarily maps to R-013.

Public exposure, private connectivity, network security rules, outbound traffic and legacy segmentation are not governed through a uniform modeled architecture.

**Proposed response:** Establish approved ingress, egress, segmentation and private connectivity patterns; inventory exceptions and define a phased remediation plan.

### F-006 — Telemetry coverage is uneven

**Provisional severity:** High  
**Enterprise risk:** R-005  
**Supporting detailed findings:** SOC-01, SOC-02 and SOC-03.

Diagnostic settings, DCR associations and log retention are not fully standardized. Inconsistent telemetry may limit threat detection, investigation and security reporting.

**Proposed response:** Establish diagnostic and retention baselines, standardize AMA and DCR deployment, and measure telemetry coverage.

### F-007 — Policy enforcement lacks a uniform lifecycle

**Provisional severity:** High  
**Enterprise risk:** R-006; related governance dependency R-001  
**Supporting detailed findings:** Cross-domain Azure Policy and exception-lifecycle assessment; no directly corresponding numbered detailed finding.

Some modeled controls remain in Audit without an approved enforcement transition, while others operate at overlapping scopes. Exception ownership, review and expiration are not uniformly established.

**Proposed response:** Define a policy lifecycle covering assessment, testing, enforcement, exceptions, remediation and periodic review.

### F-008 — Infrastructure configuration remains partially manual

**Provisional severity:** High  
**Enterprise risk:** R-007  
**Supporting detailed findings:** Cross-domain infrastructure delivery assessment. NET-03 is related where inconsistent network rule management contributes to configuration drift.

Portal-driven and team-specific configuration creates drift and weakens reproducibility, change control and auditability.

**Proposed response:** Adopt approved infrastructure-as-code patterns, version control, automated validation, deployment governance and drift detection.

### F-009 — Data sensitivity is not consistently tied to cloud controls

**Provisional severity:** High  
**Enterprise risk:** R-009; related risk R-015  
**Supporting detailed findings:** Cross-domain data protection assessment; no numbered data protection finding in the current 20-record SharePoint register.

Incomplete classification and ownership standards make it difficult to apply consistent protection based on data sensitivity. Non-production handling of production-like data requires separate validation.

**Proposed response:** Establish classification and ownership standards, map classifications to technical controls, and define non-production data-handling requirements.

### F-010 — Recovery assurance is inconsistent

**Provisional severity:** Medium-High (executive assessment; pending validation)  
**Enterprise risk:** R-010  
**Supporting detailed findings:** Cross-domain resilience assessment; no directly corresponding numbered IAM, NET or SOC finding.

Backup capabilities may exist without consistent documented recovery objectives, dependency mapping or restoration testing.

**Proposed response:** Define workload criticality, approved RTO/RPO, recovery runbooks and scheduled recovery validation.

### F-011 — Security operations requires a stronger engineering lifecycle

**Provisional severity:** Medium-High (executive assessment; pending validation)  
**Enterprise risks:** R-011 and R-014  
**Supporting detailed findings:** SOC-04, SOC-05 and SOC-06.

Detection ownership, analytics-rule testing, tuning and lifecycle management require formalization. Defender coverage also varies across modeled subscriptions and resource types.

**Proposed response:** Establish detection ownership and detection-as-code practices, formalize testing and tuning, and define required Defender coverage.

### F-012 — AI governance is emerging

**Provisional severity:** High (executive assessment; pending validation)  
**Enterprise risk:** R-012  
**Supporting detailed findings:** No numbered AI finding in the current SharePoint register.

Emerging AI use cases introduce potential risks involving prompts, sensitive data, authorization, connected agents, models and monitoring that may not be fully addressed by traditional cloud baselines.

**Proposed response:** Establish an AI use-case inventory, approved data and identity boundaries, model and agent review requirements, and monitoring standards.

## Detailed Finding Traceability

The following mappings connect the executive architecture themes to the current SharePoint Enterprise Findings Register. A secondary relationship does not replace the finding's primary enterprise risk.

| SharePoint Finding | Detailed Finding | Executive Finding | Primary Enterprise Risk |
|---|---|---|---|
| IAM-01 | Standing privileged assignments | F-003 | R-002 |
| IAM-02 | Direct user RBAC assignments | F-003 | R-002 |
| IAM-03 | Incomplete workload identity ownership | F-004; F-002 secondary | R-003 |
| IAM-04 | Significant client-secret usage | F-004 | R-003 |
| IAM-05 | Incomplete privileged access reviews | F-003 | R-002 |
| IAM-06 | Inconsistent entitlement lifecycle | F-003 | R-002 |
| IAM-07 | Inconsistent API permission reviews | F-004 | R-003 |
| NET-01 | Inconsistent public exposure governance | F-005 | R-004 |
| NET-02 | Variable private endpoint adoption | F-005 | R-004 |
| NET-03 | NSG ownership and standardization | F-005; F-008 related | R-004 |
| NET-04 | Legacy and modern DNS governance | F-005 related | R-013 |
| NET-05 | Incomplete egress standards | F-005 | R-004 |
| NET-06 | Legacy segmentation gaps | F-005 | R-004 |
| SOC-01 | Incomplete diagnostic coverage | F-006 | R-005 |
| SOC-02 | Inconsistent DCR associations | F-006 | R-005 |
| SOC-03 | Inconsistent log retention | F-006 | R-005 |
| SOC-04 | Inconsistent detection ownership | F-011 | R-011 |
| SOC-05 | Detection testing and tuning gaps | F-011 | R-011 |
| SOC-06 | Variable Defender plan coverage | F-011 | R-014 |
| SOC-07 | Missing accountable remediation owners | F-002 related | R-008 |

**Mapping note:** NET-06 also supports R-013 as a secondary risk. IAM-03 also supports R-008 as a secondary risk. These relationships should remain visible in SharePoint where secondary risk fields are available.

## Architecture Evidence Gaps

The detailed SharePoint register currently covers identity, network and security operations. The following enterprise risks require additional cross-domain assessment evidence:

| Risk | Evidence to Validate | Relevant Assessment |
|---|---|---|
| R-001 | Management-group hierarchy, subscription placement and policy inheritance | Enterprise governance |
| R-006 | Policy enforcement and exception lifecycle | Cloud governance |
| R-007 | Manual deployment practices and configuration drift | Infrastructure delivery |
| R-009 | Data classification, ownership and protection standards | Data protection |
| R-010 | Recovery objectives, dependencies and restoration testing | Resilience |
| R-012 | AI use cases, data flows, permissions and agent governance | AI security |
| R-013 | Arc inventory, legacy governance coverage and hybrid DNS dependencies | Hybrid architecture |
| R-015 | Production-like data handling in non-production environments | Data protection |

These are evidence requirements, not confirmed additional findings. Create new numbered findings only when an assessment supports a distinct observation.

## Root Causes

The modeled findings cluster around four architectural root causes:

1. **Organic growth:** Cloud services expanded faster than enterprise architecture standards.
2. **Distributed ownership:** Teams adopted controls at different times and with different priorities.
3. **Manual operations:** Important configuration remains dependent on individual knowledge and portal changes.
4. **Control fragmentation:** Identity, network, policy, logging, data and engineering controls evolved as separate capabilities.

## Strategic Conclusion

AFG's proposed approach is a phased transformation in which foundational platform decisions precede downstream enforcement. This sequence is an architecture planning decision, not a substitute for urgent interim treatment of critical exposures.

The approved portfolio sequence is:

0. Enterprise Assessment
1. Azure Landing Zone
2. Cloud Governance
3. Zero Trust Identity
4. Network Modernization
5. Security Operations
6. DevSecOps
7. Data Protection
8. AI Security
9. DLV FinTech Platform Capstone

The enterprise risk register establishes risk ownership and treatment planning. The traceability matrix connects executive findings, detailed findings, enterprise risks, requirements and delivery phases.

## Related Documents

- [Enterprise Risk Register](../risks/enterprise-risk-register.md)
- [Traceability Matrix](traceability-matrix.md)
- [Identity Current State](../current-state/identity-current-state.md)
- [Network Current State](../current-state/network-current-state.md)
- [Security Operations Current State](../current-state/security-operations-current-state.md)
- [ADR-001 — Transformation Strategy](../decisions/ADR-001-transformation-strategy.md)
