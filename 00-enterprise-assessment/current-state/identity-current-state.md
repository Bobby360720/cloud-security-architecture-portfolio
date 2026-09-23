# Identity Current State

## Scope

This assessment covers human privileged access, workload identities,
application registrations, entitlement lifecycle, and emergency access.

## Current Capabilities

-   Microsoft Entra ID is the central identity provider.
-   Conditional Access is broadly deployed.
-   PIM is available and partially adopted.
-   Group-based RBAC is common.
-   Managed identities are increasingly used.
-   Break-glass accounts exist.
-   Access Reviews and entitlement management are available but
    selectively used.

## Findings


| ID | Finding | Severity |
|---|---|---|
| IAM-01 | Some privileged roles remain standing assignments | Critical |
| IAM-02 | Direct user RBAC assignments remain | High |
| IAM-03 | Workload identity ownership is incomplete | Critical |
| IAM-04 | Client-secret usage remains significant | Critical |
| IAM-05 | Access Reviews are not universal for privileged groups | High |
| IAM-06 | Entitlement lifecycle is not the default access model | Medium-High |
| IAM-07 | API permission review is inconsistent | High |


## Finding Management

IAM-01 through IAM-07 are modeled enterprise findings
documented during Phase 0.

The AFG Security Governance Portal's Active Findings
Register tracks their validation, ownership, remediation,
risk relationships, and closure evidence.

These findings are not confirmed vulnerabilities in
the physical Azure architecture lab.

Engineering validation will be documented separately
as relevant lab components are implemented.

## Target Direction

Phase 3 will establish:

-   group-based access as the default;
-   PIM/JIT for privileged roles where supported;
-   recurring access reviews;
-   managed identities or federation before client secrets;
-   application ownership and credential lifecycle standards;
-   least-privilege API permissions;
-   controlled emergency access;
-   entitlement packages for repeatable access scenarios.

## Evidence Needed Later

-   privileged-role inventory;
-   direct assignment count;
-   workload identity inventory;
-   secret/certificate expiration inventory;
-   application owner coverage;
-   access-review coverage.
