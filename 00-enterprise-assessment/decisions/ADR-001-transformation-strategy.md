# ADR-001 --- Adopt a Phased Enterprise Cloud-Security Transformation

**Status:** Accepted\
**Decision Type:** Enterprise Architecture\
**Phase:** 0 --- Enterprise Assessment

## Context

AFG has existing Azure, hybrid infrastructure, identity, networking,
security operations, and application workloads. Security capabilities
exist, but maturity is inconsistent. A greenfield rebuild would be
operationally disruptive and unnecessary.

The assessment found that many risks are interdependent. For example,
policy enforcement depends on governance scope; private networking
depends on platform design; security monitoring depends on standardized
telemetry; and DevSecOps depends on stable control requirements.

## Decision

AFG will use a phased transformation:

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

Each phase must trace its work to Phase 0 findings, risks, and
requirements.

## Alternatives Considered

### Big-bang redesign

Rejected because of high operational risk and weak migration
practicality.

### Tool-by-tool remediation

Rejected because it would preserve fragmented governance and obscure
architectural dependencies.

### Compliance-only program

Rejected because compliance evidence alone would not address platform
design, automation, resilience, or engineering maturity.

## Consequences

### Positive

-   clear sequencing;
-   risk traceability;
-   reusable architecture patterns;
-   measurable maturity improvement;
-   reduced change blast radius.

### Negative

-   transformation takes longer than a single remediation sprint;
-   temporary coexistence of legacy and target patterns;
-   requires disciplined documentation and ownership.

## Security Implications

The phased approach reduces the likelihood that enforcement controls are
deployed without understanding dependencies or business impact.

## Validation

The decision remains valid if later phases can demonstrate traceability
from Phase 0 risks to implemented and validated controls.
