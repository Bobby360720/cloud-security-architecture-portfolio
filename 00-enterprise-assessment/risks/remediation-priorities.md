# Remediation Priorities

## Prioritization Method

Priorities consider:

-   inherent risk;
-   blast radius;
-   dependency on foundational architecture;
-   implementation sequencing;
-   opportunity to create reusable controls;
-   operational disruption.

## Priority 1 --- Establish the Control Plane

**Phases 1--2**

Address: - management-group hierarchy; - subscription placement; -
governance ownership; - policy inheritance; - tagging; - exception
lifecycle.

Why first: identity, networking, logging, and workload controls are
easier to scale after the governance hierarchy is predictable.

## Priority 2 --- Reduce Identity Blast Radius

**Phase 3**

Address: - standing privilege; - direct RBAC; - workload credentials; -
application permissions; - access reviews; - entitlement lifecycle.

Why: identity compromise can bypass otherwise strong network and
workload controls.

## Priority 3 --- Reduce Exposure

**Phase 4**

Address: - public endpoints; - segmentation; - ingress/egress; - private
endpoints; - DNS governance.

## Priority 4 --- Make Control Effectiveness Observable

**Phase 5**

Address: - diagnostic settings; - AMA/DCR consistency; - Defender
coverage; - Sentinel onboarding; - detection lifecycle.

## Priority 5 --- Make the Secure State Repeatable

**Phase 6**

Address: - IaC; - policy as code; - pipeline validation; - secrets
management; - software supply-chain controls.

## Priority 6 --- Protect Data by Sensitivity

**Phase 7**

Address: - classification; - encryption/key requirements; - DLP; -
retention; - non-production data.

## Priority 7 --- Govern Emerging AI Risk

**Phase 8**

Address: - AI data flows; - prompt injection; - RAG authorization; -
agent/tool permissions; - model and supply-chain risk; - monitoring.

## Sequencing Principle

The program deliberately avoids attempting to remediate every finding
simultaneously. Foundational controls are built first so later phases
inherit a more stable platform.
