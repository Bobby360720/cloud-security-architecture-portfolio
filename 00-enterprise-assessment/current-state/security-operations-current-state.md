# Security Operations Current State

**Organization:** AFG Enterprises (modeled)  
**Phase:** 0 — Enterprise Assessment  
**Evidence status:** Modeled enterprise assessment; not a verified inventory of deployed security resources.

## 1. Purpose and Scope

Assess the modeled current-state monitoring, detection, and response architecture across Azure and hybrid workloads. This assessment uses the existing cloud inventory and enterprise risk and findings baselines. It identifies dependencies and gaps for Phase 5 rather than claiming that target-state controls have been implemented.

## 2. Current Monitoring and Security Operations Architecture

AFG has an established Microsoft security-operations foundation: Azure Monitor, Log Analytics, Microsoft Sentinel, Microsoft Defender for Cloud, Azure Monitor Agent (AMA), Data Collection Rules (DCRs), analytics and automation rules, workbooks, and watchlists. The primary architectural issue is inconsistent coverage, ownership, and lifecycle management across subscriptions, resource types, and legacy/hybrid workloads.

**Modeled logical flow:**

```text
Azure resources ── diagnostic settings / platform logs ──┐
Azure VMs and Arc-enabled servers ── AMA + DCRs ──────────┤
Entra ID logs / subscription activity logs ───────────────┤
                                                         ▼
                                            Log Analytics workspaces
                                                         │
                                         Sentinel-enabled workspaces
                                                         │
                                     Analytics rules / automation rules
                                                         │
                                          Security Operations response

Defender for Cloud ── posture findings / workload protection ──►
                      security review and remediation ownership
```

This is a conceptual dependency diagram, not a verified end-to-end data-flow configuration. In particular, the exact destinations, connector settings, and Defender-to-Sentinel integrations have not been established by the Phase 0 source inventory.

## 3. Modeled Workspace and Security Tooling Inventory

| Component | Modeled baseline | Current-state observation |
|---|---:|---|
| Log Analytics workspaces | 8 | Retention differs by workspace/use case. |
| Sentinel-enabled workspaces | 2 | Data-source coverage and detection ownership are inconsistent. |
| Sentinel analytics rules | 96 | Testing and tuning lifecycle needs formalization. |
| Sentinel automation rules | 18 | Rule-level ownership and incident workflow dependencies require validation. |
| Sentinel workbooks | 12 | Existing reporting capability; coverage effectiveness not validated. |
| Sentinel watchlists | 9 | Existing supporting capability; update and ownership processes not validated. |
| Data Collection Rules | 23 | DCR association is inconsistent. |
| Azure Monitor Agent | Broad deployment | Coverage and association need normalization, especially for hybrid workloads. |

**Inventory limitation:** The source inventory supplies enterprise totals, not individual workspace names, regions, subscription placement, retention settings, Sentinel connectors, ingestion volumes, or assigned owners. Those details remain evidence gaps; they must not be presented as observed or validated lab facts.

## 4. Azure and Hybrid Log Collection

The modeled estate includes 38 Azure VMs and 214 Azure Arc-enabled servers. AMA is broadly deployed, but DCR association is inconsistent. Diagnostic settings are not standardized across Azure resources, and some legacy resources lack complete telemetry.

| Collection area | Modeled current state | Assessment implication |
|---|---|---|
| Azure VM / Arc telemetry | Broad AMA deployment; inconsistent DCR associations | Agent installation alone does not demonstrate collection of required events. |
| Azure resource diagnostics | Inconsistent | Required resource logs may be missing or sent to different destinations. |
| Azure subscription Activity Logs | Forwarded for the majority of subscriptions | Remaining coverage and destinations need verification. |
| Entra logs | Forwarded | Exact log categories, destination, and retention need verification. |
| NSG flow telemetry | Partial | Network investigation visibility varies. |
| Key Vault auditing | Majority coverage | Remaining audit gaps require identification. |
| PaaS diagnostics | Partial | Workload investigations may lack service-specific events. |
| Workspace retention | Varies by workspace/use case | Retention requirements and actual configurations need reconciliation. |

The inventory does not establish resource-by-resource collection success, ingestion health, event completeness, or actual detection latency. These remain validation tasks for Phase 5.

## 5. Detection, Alerting, and Incident-Response Dependencies

The modeled Sentinel estate includes 96 analytics rules and 18 automation rules. Existing workbooks and watchlists support investigation and reporting. Detection ownership is not consistently documented, and analytics-rule testing and tuning require a formal lifecycle.

The current architecture depends on the following sequence:

1. Required Azure, identity, and hybrid events must be collected and retained.
2. Log Analytics and Sentinel data-source onboarding must make the relevant events available to analytics rules.
3. Detection rules must have owners, validation and tuning processes, and retirement criteria.
4. Alerts and incidents must have documented triage, escalation, and remediation ownership.
5. Defender for Cloud findings must be routed to accountable remediation owners.

**Unverified operational details:** The Phase 0 materials do not identify specific analytics rules, incident severity routing, playbook integrations, escalation SLAs, on-call arrangements, or tested response workflows. These dependencies are assessment and design inputs, not claims of implemented processes.

## 6. Defender for Cloud Coverage

| Capability | Modeled status |
|---|---|
| Cloud Security Posture Management (CSPM) | Enabled |
| Defender for Servers | Broad coverage |
| Defender for Storage | Partial |
| Defender for SQL | Critical workloads |
| Defender for Key Vault | Partial |
| Defender for Containers | Limited |
| Regulatory compliance dashboard | Enabled |

Coverage varies by subscription and eligible resource type. Subscription-level plan settings, protected-resource eligibility, exceptions, and actual coverage need validation. The modeled inventory does not establish that all eligible workloads are protected.

## 7. Findings and Risk Traceability

These are **modeled assessment findings**, not independently validated production findings. The existing enterprise findings register remains the operational source for detailed tracking.

| Finding | Current-state gap | Severity | Enterprise risk | Related requirement / design input |
|---|---|---|---|---|
| SOC-01 | Diagnostic coverage is not universal | High | R-005 | SEC-005; TR-010 |
| SOC-02 | DCR association is inconsistent | High | R-005 | SEC-005; TR-010 |
| SOC-03 | Log retention differs by workspace/use case | Medium | R-005 | SEC-005; retention standard to define in Phase 5 |
| SOC-04 | Detection ownership is not consistently documented | Medium-High | R-011 | SEC-012; TR-011 |
| SOC-05 | Analytics-rule testing/tuning lifecycle needs formalization | Medium-High | R-011 | SEC-012; TR-011 |
| SOC-06 | Defender plan coverage varies by subscription/resource type | High | R-014 | Approved Defender coverage baseline and exception process |
| SOC-07 | Findings are not always mapped to accountable remediation owners | High | R-008 | SEC-009; ownership metadata and remediation accountability |

**Existing risk ratings:** R-005 is High (16); R-011 is Medium (12); R-014 is Medium (12). SOC-07 relates to the existing ownership risk R-008, not a newly created security-operations risk. Detailed mapping is maintained in `../assessment/traceability-matrix.md`; the enterprise risk register is maintained in `../risks/enterprise-risk-register.md`.

## 8. Architectural Risks and Dependencies

- **Telemetry completeness:** Detection and investigation depend on consistent diagnostic settings, AMA/DCR associations, and data-source onboarding (R-005).
- **Detection lifecycle:** Rule effectiveness depends on named ownership, testing, tuning, change control, and retirement criteria (R-011).
- **Defender coverage:** Protection depends on subscription-level plans, resource eligibility, onboarding, and documented exceptions (R-014).
- **Remediation accountability:** Security findings depend on resource ownership and a defined remediation handoff (R-008).
- **Hybrid governance:** Arc-connected and legacy workloads introduce monitoring and ownership dependencies that intersect with R-013; the broader Arc governance gap is not resolved by this assessment.

## 9. Evidence Gaps and Phase 5 Validation Inputs

| Evidence needed | Validation approach for later phase |
|---|---|
| Workspace-level inventory and ownership | Export workspace and Sentinel configuration from authorized lab or enterprise sources. |
| Data-source coverage | Compare required log categories and connector configuration against onboarded subscriptions and workloads. |
| AMA/DCR association coverage | Compare eligible Azure VMs and Arc servers against installed agents and effective DCR associations. |
| Diagnostic and retention compliance | Review diagnostic destinations, collection status, and retention against approved standards. |
| Detection lifecycle | Inspect rule ownership, testing evidence, tuning history, and retirement criteria. |
| Incident-response dependencies | Review alert routing, automation rules, escalation ownership, and test evidence. |
| Defender coverage | Compare enabled plans and protected eligible resources by subscription and workload type. |
| Finding remediation | Verify accountable owners, tracked remediation, exceptions, and closure evidence in SharePoint. |

No residual risk scores are assigned in Phase 0. Risk treatment and evidence of implemented controls will be reviewed during the relevant delivery phases.

## 10. Target Direction

Phase 5 will define:

- required enterprise telemetry and standard diagnostic settings;
- AMA/DCR architecture and hybrid onboarding standards;
- Sentinel data-source onboarding and workspace governance;
- detection-as-code lifecycle, ownership, testing, tuning, and retirement;
- alert triage, incident escalation, and remediation accountability;
- retention requirements and measurable monitoring coverage;
- Defender coverage baseline, exceptions, and verification.

The assessment establishes the modeled baseline and future validation requirements; it does not assert that these target-state controls are deployed.
