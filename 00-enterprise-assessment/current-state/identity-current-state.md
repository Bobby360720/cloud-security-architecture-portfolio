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

  -----------------------------------------------------------------------
  ID                      Finding                 Severity
  ----------------------- ----------------------- -----------------------
  IAM-01                  Some privileged roles   Critical
                          remain standing         
                          assignments             

  IAM-02                  Direct user RBAC        High
                          assignments remain      

  IAM-03                  Workload identity       Critical
                          ownership is incomplete 

  IAM-04                  Client-secret usage     Critical
                          remains significant     

  IAM-05                  Access Reviews are not  High
                          universal for           
                          privileged groups       

  IAM-06                  Entitlement lifecycle   Medium-High
                          is not the default      
                          access model            

  IAM-07                  API permission review   High
                          is inconsistent         
  -----------------------------------------------------------------------

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
