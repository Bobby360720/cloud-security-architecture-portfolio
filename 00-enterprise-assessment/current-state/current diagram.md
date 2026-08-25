                    AFG ENTERPRISE
                         │
              ┌──────────┴──────────┐
              │                     │
         On-Premises              Azure
              │                     │
        Legacy Systems        ┌─────┴─────┐
              │               │           │
         ExpressRoute      Prod Subs   NonProd Subs
                              │           │
                          Resources    Resources
                              │           │
                              └─────┬─────┘
                                    │
                              Shared Services

CURRENT-STATE CONCERNS

⚠ Inconsistent governance
⚠ Mixed policy assignments
⚠ Public endpoints
⚠ Privileged access
⚠ Inconsistent logging
⚠ Manual configuration
⚠ Weak ownership metadata
⚠ Credential lifecycle