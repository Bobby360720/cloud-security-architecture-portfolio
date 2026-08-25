# Current-State Architecture Diagram

This Mermaid diagram is intentionally conceptual and sanitized.

``` mermaid
flowchart TB
    Users[Enterprise Users & Administrators]
    Entra[Microsoft Entra ID]
    OnPrem[On-Premises / Hybrid Estate]
    ER[ExpressRoute]
    Root[Tenant / Management Groups]
    Platform[Platform Subscriptions]
    Prod[Production Subscriptions]
    NonProd[Non-Production Subscriptions]
    Legacy[Legacy / Transitional]
    Sandbox[Sandbox]
    SecOps[Sentinel / Defender / Log Analytics]
    DevOps[Azure DevOps / Git / IaC]
    Data[Data & PaaS Services]

    Users --> Entra
    Entra --> Root
    OnPrem --> ER
    ER --> Platform
    Root --> Platform
    Root --> Prod
    Root --> NonProd
    Root --> Legacy
    Root --> Sandbox
    Platform --> Prod
    Platform --> NonProd
    Prod --> Data
    NonProd --> Data
    Legacy --> Data
    Prod --> SecOps
    NonProd --> SecOps
    Legacy -. inconsistent coverage .-> SecOps
    DevOps -. partial automation .-> Prod
    DevOps -. partial automation .-> NonProd
```

## Current-State Callouts

-   Policy inheritance is fragmented across scopes.
-   Legacy governance differs from newer landing-zone patterns.
-   Private connectivity is not universal.
-   Telemetry coverage is inconsistent.
-   Identity governance maturity varies by human vs. workload identity.
-   Infrastructure delivery is only partially automated.
-   Ownership and data sensitivity are not consistently represented in
    metadata.

## Diagram Intent

This diagram establishes the problem context. Phase 1 should replace it
with a target-state Azure Landing Zone diagram rather than editing this
artifact into the future state.
