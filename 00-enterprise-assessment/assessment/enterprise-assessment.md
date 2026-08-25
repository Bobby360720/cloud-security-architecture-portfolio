# Enterprise Assessment

## Executive Assessment

AFG Enterprises is a hybrid, Azure-first organization whose cloud
adoption has outpaced the formalization of its enterprise cloud
operating model. The organization already uses strong Microsoft security
capabilities, but those capabilities are not consistently governed,
inherited, automated, measured, or assigned to accountable owners.

The primary architectural problem is therefore **not the absence of
security tooling**. It is the lack of a sufficiently integrated
security-governance system.

## Scope

The assessment covers:

-   Azure tenant and management groups;
-   subscriptions and workload placement;
-   Microsoft Entra ID and privileged access;
-   workload identities and application credentials;
-   hybrid connectivity and Azure networking;
-   Azure Policy and governance;
-   Microsoft Defender and Sentinel;
-   Azure Monitor, AMA, DCRs, and diagnostic settings;
-   secrets and key management;
-   infrastructure delivery and DevSecOps;
-   data protection and classification;
-   resilience and recovery;
-   emerging AI workloads.

## Assessment Boundaries

This Phase 0 assessment does not attempt to:

-   reproduce production configuration;
-   disclose confidential tenant or workload identifiers;
-   perform penetration testing;
-   replace a formal regulatory audit;
-   prescribe every Phase 1--8 implementation detail.

## Key Findings

### F-001 --- Governance hierarchy is not yet the authoritative control plane

**Severity:** High\
Policy assignments exist across multiple scopes and legacy placement
patterns remain. This increases duplication, inconsistency, and
troubleshooting complexity.

### F-002 --- Resource ownership and criticality are incomplete

**Severity:** High\
Ownership, criticality, and data-classification metadata are not
consistently available from authoritative cloud metadata.

### F-003 --- Privileged access is not uniformly just-in-time

**Severity:** Critical\
PIM is available but some privileged access remains standing or directly
assigned.

### F-004 --- Workload credential governance is inconsistent

**Severity:** Critical\
Managed identities are increasing, but client secrets and application
credentials remain in use with inconsistent ownership and review.

### F-005 --- Public exposure is not consistently governed

**Severity:** High\
Some PaaS services and legacy workloads remain publicly reachable where
private connectivity may be feasible.

### F-006 --- Telemetry coverage is uneven

**Severity:** High\
Diagnostic settings, DCR associations, retention, and security
data-source onboarding are not fully standardized.

### F-007 --- Policy enforcement lacks a uniform lifecycle

**Severity:** High\
Some controls remain in Audit indefinitely while others are assigned at
overlapping scopes.

### F-008 --- Infrastructure configuration remains partially manual

**Severity:** High\
Portal-driven and team-specific configuration creates drift and weakens
reproducibility.

### F-009 --- Data sensitivity is not consistently tied to cloud controls

**Severity:** High\
Data-classification maturity is insufficient to drive consistent
risk-based technical controls.

### F-010 --- Recovery assurance is inconsistent

**Severity:** Medium-High\
Backup is broadly available, but documented RTO/RPO and restoration
testing are not uniform.

### F-011 --- Security operations requires stronger engineering lifecycle

**Severity:** Medium-High\
Sentinel and Defender are deployed, but detection ownership, tuning,
validation, and retirement require formalization.

### F-012 --- AI governance is emerging

**Severity:** High as adoption grows\
AI proofs of concept introduce prompt, data, authorization, agent,
model, and monitoring risks that are not fully addressed by traditional
cloud baselines.

## Root Causes

The findings cluster around four root causes:

1.  **Organic growth:** cloud services expanded faster than enterprise
    architecture standards.
2.  **Distributed ownership:** teams adopted controls at different times
    and with different priorities.
3.  **Manual operations:** important configuration remains dependent on
    individual knowledge and portal changes.
4.  **Control fragmentation:** identity, network, policy, logging, data,
    and engineering controls evolved as separate capabilities.

## Strategic Conclusion

AFG should not attempt a single large remediation project. The
recommended strategy is a phased transformation in which foundational
platform decisions precede downstream enforcement.

The approved sequence is:

0.  Enterprise Assessment
1.  Azure Landing Zone
2.  Cloud Governance
3.  Zero Trust Identity
4.  Network Modernization
5.  Security Operations
6.  DevSecOps
7.  Data Protection
8.  AI Security
9.  DLV FinTech Platform capstone

This sequence creates traceability between observed risk and
architecture investment.
