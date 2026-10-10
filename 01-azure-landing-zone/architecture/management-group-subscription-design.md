# Management Group and Subscription Design

## 1. Purpose

This document defines the target management-group and subscription architecture for AFG Enterprises.

The design establishes governance boundaries for platform services, business workloads, sandbox environments, transitional legacy workloads, and retired subscriptions. These boundaries support consistent control inheritance, clear workload placement, operational accountability, and secure growth as AFG expands its Azure environment.

This document represents the **proposed target-state architecture** unless a control, resource, or placement decision is explicitly identified as validated in the lab.

## 2. Design Inputs

The management-group and subscription architecture is derived from the Phase 1 Azure Landing Zone requirements and the risks and business requirements established during Phase 0.

### 2.1 Phase 1 Requirements

- **ALZ-001** — Management-group hierarchy
- **ALZ-002** — Subscription organization
- **ALZ-003** — Platform/workload separation
- **ALZ-004** — Production/non-production separation
- **ALZ-005** — Corp vs. Online placement
- **ALZ-006** — Legacy transition
- **ALZ-007** — Sandbox isolation
- **ALZ-008** — Subscription lifecycle
- **ALZ-009** — Shared platform services
- **ALZ-010** — Brownfield adoption

### 2.2 Phase 0 Drivers

- **R-001** — Management-group hierarchy and subscription governance
- **R-010** — Recovery architecture and resilience
- **R-013** — Legacy and hybrid governance
- **BR-001** — Scalable cloud governance
- **BR-010** — Incremental modernization

## 3. Design Principles

### 3.1 Governance Boundaries Over Organization Structure

Management groups represent governance and control boundaries rather than AFG's organizational chart. This reduces the need to restructure Azure governance when departments, teams, or reporting relationships change.

### 3.2 Architecture-Driven Subscription Boundaries

Separate subscriptions require a defined architectural justification, such as workload ownership, environment, connectivity, regulatory scope, lifecycle, cost accountability, quota requirements, or isolation needs.

Resource type alone does not justify creating a separate subscription.

### 3.3 Inheritance at the Highest Appropriate Scope

Enterprise controls should be assigned at the highest scope where they apply consistently. Specialized controls should be applied at lower shared scopes only when a distinct governance requirement exists.

Management groups should not be added solely to avoid repeatable subscription-level configuration. Where environment-specific controls are required, Phase 2 policy-as-code and assignment patterns should provide consistent deployment without creating unnecessary management-group layers.

### 3.4 Production and Non-Production Separation

Production and non-production workloads are separated primarily through subscription boundaries when differences in access, change management, data handling, resilience, or operational risk justify isolation.

Production and non-production subscriptions may remain beneath the same `Corp` or `Online` management-group archetype. The detailed method for applying environment-specific Azure Policy controls is defined in Phase 2 — Cloud Governance.

### 3.5 Platform and Workload Separation

Shared enterprise platform services remain logically separated from application and business workloads to support centralized ownership, governance, and lifecycle management.

### 3.6 Controlled Legacy Transition

Legacy workloads that cannot immediately comply with the target baseline use controlled transitional governance boundaries rather than weakening standards applied to modern workloads.

### 3.7 Incremental Brownfield Adoption

Existing subscriptions migrate toward the target architecture incrementally based on dependencies, risk, and operational impact rather than requiring an immediate greenfield rebuild.

## 4. Proposed Management Group Hierarchy

```text
Tenant Root Group
└── AFG
    ├── Platform
    │   ├── Identity
    │   ├── Management
    │   ├── Connectivity
    │   └── Security
    │
    ├── Landing-Zones
    │   ├── Corp
    │   ├── Online
    │   └── Legacy
    │
    ├── Sandbox
    └── Decommissioned
```

This hierarchy represents the proposed target-state governance model. It uses three modeled management-group levels beneath the Tenant Root Group and remains within Azure management-group hierarchy limits.

Existing subscriptions will be assessed against the placement criteria defined in this document before migration into the target hierarchy.

AFG should configure the tenant-level default management group for newly created subscriptions so that unclassified subscriptions are routed to a controlled onboarding scope rather than remaining directly beneath the Tenant Root Group. `Sandbox` may serve this purpose in the representative lab; a dedicated onboarding or quarantine scope should be introduced only if a distinct governance requirement justifies it.

## 5. Management Group Responsibilities

| Management Group | Purpose | Governance Intent |
|---|---|---|
| Tenant Root Group | Azure tenant root scope. | Keep assignments minimal and limited to controls that genuinely apply across the entire tenant. Tenant emergency-access design is handled through Microsoft Entra ID and is not represented as management-group RBAC. |
| `AFG` | Enterprise governance root beneath the Tenant Root Group. | Establish the common enterprise governance baseline inherited by AFG platform and workload subscriptions. |
| `Platform` | Parent boundary for shared enterprise platform services. | Separate centrally managed platform capabilities from business workloads. |
| `Identity` | Hosts identity-related Azure platform infrastructure where dedicated Azure resources are required. | Apply identity-specific governance and administration without mixing identity infrastructure with application workloads. |
| `Management` | Hosts centralized management and operational services. | Provide a boundary for shared management, automation, monitoring, and operational tooling. |
| `Connectivity` | Hosts shared network and connectivity services. | Centralize shared routing, DNS, firewall, hybrid connectivity, and other enterprise network platform capabilities. |
| `Security` | Hosts shared security platform capabilities. | Provide a dedicated governance boundary for centralized security services and security-operations tooling. |
| `Landing-Zones` | Parent boundary for business and application workloads. | Apply common workload governance while allowing connectivity-specific controls beneath `Corp`, `Online`, and transitional `Legacy` scopes. |
| `Corp` | Hosts workloads requiring corporate, shared-platform, or hybrid connectivity. | Apply controls appropriate for workloads integrated with enterprise routing, DNS, private connectivity, or hybrid services. |
| `Online` | Hosts workloads that operate independently of the corporate connectivity model. | Apply controls appropriate for independently connected or internet-oriented workloads without assuming corporate network dependencies. |
| `Legacy` | Transitional boundary for workloads that cannot immediately meet the target landing-zone baseline. | Isolate approved exceptions and prevent legacy constraints from weakening standard workload governance. |
| `Sandbox` | Hosts experimentation, proofs of concept, and temporary learning workloads. | Provide an isolated, cost-conscious environment with restricted production connectivity and defined lifecycle expectations. |
| `Decommissioned` | Holds subscriptions undergoing controlled retirement. | Restrict new deployment and unnecessary change while retention, evidence, and deletion requirements are completed. |

The management-group hierarchy is designed around governance requirements rather than organizational reporting structures. Child management groups should exist only when a distinct policy, access, connectivity, lifecycle, or compliance requirement justifies the boundary.

## 6. Subscription Architecture

AFG uses subscriptions as governance, ownership, lifecycle, cost-management, and isolation boundaries rather than as simple resource containers.

Subscription placement is determined by workload purpose, environment, ownership, connectivity, operational responsibility, security requirements, and lifecycle. Resource type alone does not justify creation of a separate subscription.

The following model represents the proposed Phase 1 target state.

| Subscription | Target Management Group | Primary Purpose | Status |
|---|---|---|---|
| `sub-identity-01` | Platform / Identity | Host Azure-based identity infrastructure and supporting services where dedicated identity isolation is justified. | Pending validation |
| `sub-management-01` | Platform / Management | Host centralized Azure management and operational services. | Existing |
| `sub-connectivity-01` | Platform / Connectivity | Host shared enterprise connectivity services such as hub networking, routing, private DNS, firewall services, and hybrid connectivity. | Proposed |
| `sub-security-01` | Platform / Security | Host centralized security platform capabilities and shared security services. | Proposed |
| `sub-prod-apps-01` | Landing-Zones / Corp | Host production business applications requiring corporate or hybrid connectivity. | Proposed |
| `sub-prod-data-01` | Landing-Zones / Corp | Host production data services where a separate subscription is justified by ownership, security, lifecycle, regulatory, or operational requirements. | Pending validation |
| `sub-nonprod-apps-01` | Landing-Zones / Corp | Host non-production application workloads requiring corporate or hybrid connectivity. | Proposed |
| `sub-nonprod-data-01` | Landing-Zones / Corp | Host non-production data services where a separate data boundary is justified. | Pending validation |
| `sub-prod-apps-02` | Landing-Zones / Online | Host production workloads that operate independently of the corporate connectivity model. | Pending validation |
| `sub-nonprod-apps-02` | Landing-Zones / Online | Host non-production Online workloads only if a distinct workload and environment boundary is required. | Pending validation |
| `sub-legacy-01` | Landing-Zones / Legacy | Host existing workloads that temporarily require exceptions from the target landing-zone baseline. | Transitional |
| `sub-sandbox-01` | Sandbox | Host temporary experimentation, learning, and isolated development workloads. | Proposed |

### 6.1 Platform Subscriptions

Platform subscriptions provide shared enterprise capabilities used across multiple workloads.

These subscriptions are separated from business workloads to establish clearer ownership, reduce administrative overlap, and support different governance and lifecycle requirements.

The target model includes dedicated management, connectivity, security, and, where justified, identity subscriptions.

### 6.2 Workload Subscriptions

Business workloads are placed beneath the `Landing-Zones` hierarchy.

Workload subscriptions are classified according to connectivity model, environment, ownership, security requirements, and lifecycle. Production and non-production workloads may use separate subscriptions while remaining beneath the same `Corp` or `Online` management-group archetype.

### 6.3 Application and Data Separation

The target model shows separate application and data subscriptions as candidates; this separation is not final.

A dedicated data subscription should be created only when one or more of the following provide sufficient justification:

- distinct ownership or database-administration responsibility;
- stronger access-control requirements;
- regulatory or contractual scope;
- materially different network requirements;
- independent lifecycle or deployment cadence;
- cost-accountability requirements;
- reduced operational or security blast radius;
- materially different data-sensitivity or protection requirements.

If these conditions are not present, application and data services may remain within the same workload subscription and use appropriate resource-group, RBAC, networking, and data-protection boundaries.

### 6.4 Corp and Online Placement

Workloads should be placed under `Corp` when they require integration with AFG corporate or hybrid connectivity services, such as shared enterprise routing, private DNS, on-premises connectivity, or other centrally provided network dependencies.

Workloads should be placed under `Online` when they operate independently from the corporate connectivity model and use workload-specific or internet-oriented connectivity.

Internet exposure alone does not determine placement. A public-facing workload may remain under `Corp` when it depends on corporate connectivity or shared enterprise network services.

### 6.5 Legacy Subscription

`sub-legacy-01` represents a transitional brownfield boundary for workloads that cannot immediately comply with the target landing-zone baseline.

Legacy placement must not become a permanent mechanism for avoiding enterprise controls. Exceptions associated with the legacy subscription should have documented ownership, justification, risk treatment, and modernization or retirement criteria.

### 6.6 Disaster Recovery Architectural Boundary

AFG will default secondary regional recovery resources to the workload's existing subscription unless recovery, administrative isolation, quota, regulatory, or blast-radius requirements justify a separate subscription.

A separate disaster-recovery subscription is technically possible but introduces additional RBAC, networking, policy, recovery-plan, and operational complexity. Regional separation alone is not sufficient justification for creating `sub-dr-01`.

A dedicated DR subscription should therefore be introduced only when business-continuity analysis demonstrates a meaningful requirement for independent administration, capacity, quota, security isolation, or recovery operations. This remains an open architecture decision under **ALZ-DEC-003**.

### 6.7 Brownfield Subscription Migration

Existing subscriptions will be assessed before movement into the target hierarchy.

Each subscription should be evaluated for:

- current workload purpose;
- ownership;
- environment;
- connectivity dependencies;
- policy compatibility;
- access-control dependencies;
- custom RBAC role-definition dependencies;
- legacy exceptions;
- operational dependencies;
- recovery requirements;
- target management-group placement.

Subscription migration should occur incrementally and should not require workload rebuild solely to achieve alignment with the target hierarchy.

## 7. Subscription Placement Criteria

AFG shall use consistent placement criteria when assigning subscriptions to the target management-group hierarchy.

Placement decisions should be based on governance, connectivity, ownership, lifecycle, operational, security, and compliance requirements rather than individual preference or organizational reporting lines.

### 7.1 Platform vs. Workload

A subscription should be placed beneath `Platform` when its primary purpose is to deliver shared enterprise capabilities used by multiple workloads or teams.

Typical examples include:

- identity infrastructure;
- centralized management services;
- shared connectivity services;
- centralized security services.

A subscription should be placed beneath `Landing-Zones` when its primary purpose is to host business applications, data platforms, APIs, or other workload-specific resources.

### 7.2 Corp vs. Online

A workload should be placed beneath `Corp` when it requires integration with AFG corporate or hybrid connectivity services.

Indicators include:

- dependency on centralized enterprise routing;
- connectivity to on-premises or hybrid services;
- reliance on shared private DNS or firewall services;
- private connectivity to other corporate workloads;
- integration with enterprise network-security controls.

A workload should be placed beneath `Online` when it operates independently of the corporate connectivity model and primarily uses workload-specific or internet-oriented connectivity.

Internet exposure alone does not determine placement.

### 7.3 Production vs. Non-Production

Production and non-production workloads should use separate subscriptions when differences in operational risk, access, change management, data handling, resilience, or lifecycle justify isolation.

A separate production boundary is appropriate when it supports:

- stronger access restrictions;
- stricter change control;
- production-specific monitoring or recovery requirements;
- reduced risk of non-production activity affecting production systems;
- separation of production data from lower environments.

Production and non-production subscriptions may remain beneath the same `Corp` or `Online` management group. Detailed environment-specific policy assignments are defined in Phase 2.

Non-production environments must not be assumed to have lower security requirements when they contain sensitive or production-like data.

### 7.4 Legacy Placement

A subscription should be placed beneath `Legacy` only when existing workload dependencies prevent immediate compliance with the target landing-zone baseline.

Legacy placement requires:

- documented business or technical justification;
- identified control gaps or exceptions;
- assigned ownership;
- documented risk treatment;
- modernization, migration, or retirement criteria;
- periodic review.

The `Legacy` management group is a transitional governance boundary and must not become a permanent alternative to standard landing-zone controls.

### 7.5 Sandbox Placement

A subscription should be placed beneath `Sandbox` when its purpose is temporary experimentation, learning, proof-of-concept activity, or other non-production work that does not require normal enterprise workload connectivity.

Sandbox subscriptions should have:

- limited connectivity to production environments;
- defined cost controls;
- restricted data use;
- defined ownership;
- short or reviewable lifecycles.

Sensitive production data should not be placed in sandbox subscriptions unless explicitly approved through a documented exception process.

### 7.6 Decommissioned Placement

A subscription should be moved beneath `Decommissioned` when its workloads are no longer intended for normal production or development use and the subscription is being retained temporarily before cancellation or deletion.

Subscriptions placed beneath `Decommissioned` should:

- prohibit or tightly restrict new workload deployment;
- restrict unnecessary administrative changes;
- retain only resources required for approved transition, evidence, recovery, or retention purposes;
- have a documented retirement owner and deletion or review date.

### 7.7 Placement Decision Sequence

Subscription placement should follow the sequence below:

1. Determine whether the capability is a shared platform service or a business workload.
2. Identify the workload owner and operational owner.
3. Determine the environment classification.
4. Determine required connectivity and hybrid dependencies.
5. Identify security, compliance, and data requirements.
6. Identify lifecycle and resilience requirements.
7. Determine whether an existing subscription can satisfy the requirements.
8. Create a new subscription only when a justified architectural boundary exists.
9. Assign the subscription to the appropriate management group.
10. Record any exceptions or transitional dependencies.

### 7.8 Placement Examples

| Workload Scenario | Recommended Placement | Rationale |
|---|---|---|
| Centralized Azure Firewall and enterprise DNS | Platform / Connectivity | Shared enterprise network capability |
| Centralized security tooling | Platform / Security | Shared security platform capability |
| Corporate production application requiring hybrid connectivity | Landing-Zones / Corp | Depends on corporate connectivity; production isolation is provided through its subscription boundary |
| Corporate staging environment | Landing-Zones / Corp | Non-production workload requiring corporate connectivity; separated from production by subscription |
| Internet-oriented application with no corporate network dependency | Landing-Zones / Online | Independently connected workload |
| Existing application unable to meet the target baseline | Landing-Zones / Legacy | Transitional exception boundary |
| Temporary developer proof of concept | Sandbox | Short-lived experimentation |
| Retired subscription awaiting final cancellation | Decommissioned | Controlled retirement state |

## 8. Subscription Boundary Criteria

AFG shall create separate Azure subscriptions only when a distinct governance, security, operational, financial, or lifecycle boundary is required.

Subscriptions should not be created solely because workloads use different Azure services or resource types. Each subscription boundary should have a documented architectural reason and an assigned owner.

### 8.1 Ownership and Administrative Boundary

A separate subscription may be justified when a workload or platform capability has a distinct owner, administrative team, or operational responsibility.

This boundary is appropriate when separation improves accountability, simplifies access management, or reduces unnecessary administrative privileges across unrelated workloads.

### 8.2 Environment Boundary

Production and non-production workloads may require separate subscriptions when differences in access, change control, monitoring, recovery, data handling, or operational risk justify stronger isolation.

Environment separation should reduce the likelihood that development, testing, or administrative activity affects production services.

### 8.3 Security and Blast-Radius Boundary

A separate subscription may be used to reduce the impact of subscription-scoped privilege, misconfiguration, quota exhaustion, deployment errors, or operational failures.

Subscription isolation does not protect against compromise of tenant-wide identities or controls. Tenant-level identity and privileged-access risks are addressed separately in Phase 3.

Security-driven separation may be appropriate where workloads have:

- materially different security requirements;
- distinct privileged-administration models;
- sensitive assets;
- high business criticality;
- independent security ownership.

### 8.4 Regulatory and Compliance Boundary

A separate subscription may be justified when a workload is subject to distinct regulatory, contractual, or compliance requirements.

Examples may include workloads requiring:

- specialized access restrictions;
- dedicated evidence collection;
- distinct policy enforcement;
- separate compliance reporting;
- restricted administrative populations.

Subscription separation should support the compliance objective and must not be treated as sufficient evidence of compliance by itself.

### 8.5 Data Sensitivity Boundary

Workloads that process or store materially different classes of data may require separate subscriptions where isolation improves access control, governance, monitoring, or accountability.

Data sensitivity alone does not automatically require a dedicated subscription. The architecture should consider ownership, access, networking, lifecycle, encryption, and regulatory requirements together.

### 8.6 Connectivity Boundary

A separate subscription may be justified when workloads require materially different connectivity architectures or administrative ownership.

Examples include:

- centralized enterprise connectivity services;
- independently connected Online workloads;
- isolated environments;
- specialized hybrid connectivity;
- network services managed by a dedicated platform team.

Connectivity differences should first be evaluated through management-group placement and network architecture before additional subscriptions are created.

### 8.7 Lifecycle Boundary

Workloads with independent provisioning, operation, modernization, or retirement lifecycles may justify separate subscriptions.

This is particularly relevant where one workload must be migrated, transferred, suspended, or decommissioned without affecting unrelated workloads.

### 8.8 Financial and Cost-Accountability Boundary

A separate subscription may be appropriate where products, projects, or platform teams require clear cost ownership, budgets, showback, or chargeback accountability.

Subscription boundaries should not be the only cost-management mechanism. Tags, cost-management scopes, budgets, and financial-governance processes should also be used where appropriate.

### 8.9 Azure Quota and Service-Limit Boundary

A separate subscription may be justified when validated Azure quotas, service limits, capacity constraints, or deployment scale create a legitimate technical requirement.

Quota limitations should be confirmed before a new subscription is created, because quota increases or alternative resource organization may provide a simpler solution.

### 8.10 Resilience and Recovery Boundary

A separate subscription may be justified when recovery architecture requires independent administration, reduced subscription-level blast radius, separate capacity, distinct quotas, or independent recovery operations.

Regional deployment alone does not require a separate subscription.

### 8.11 Boundary Decision Checklist

Before creating a new subscription, architecture review should answer:

1. Is there a distinct workload or platform owner?
2. Are different administrative privileges required?
3. Does the workload require stronger production or security isolation?
4. Are there distinct compliance or contractual obligations?
5. Are data-sensitivity requirements materially different?
6. Does the workload require a different connectivity model?
7. Does it have an independent lifecycle?
8. Is separate financial accountability required?
9. Are validated Azure quotas or technical limits driving the boundary?
10. Does resilience architecture require independent recovery operations?
11. Can the requirement be satisfied through management groups, resource groups, RBAC, policy, networking, or tagging without creating another subscription?

A new subscription should be created only when the benefits of the additional boundary outweigh the operational and governance complexity it introduces.

### 8.12 Boundary Examples

| Scenario | Separate Subscription? | Rationale |
|---|---|---|
| Production and development workloads with different administrators and change controls | Likely | Environment and administrative isolation |
| Application and database owned by the same team with the same lifecycle and controls | Usually no | Resource type alone does not justify separation |
| Centralized network platform serving multiple workloads | Yes | Shared platform capability with dedicated ownership |
| Regulated workload with distinct access and evidence requirements | Possibly | Depends on whether subscription isolation materially supports the compliance objective |
| Same application deployed to a second Azure region | Usually no | Region alone is insufficient justification |
| Disaster-recovery environment requiring independent administration and recovery capacity | Possibly | Depends on resilience requirements |
| Temporary proof-of-concept workload | Usually no dedicated workload subscription | Prefer approved Sandbox placement |

## 9. Policy, Security, and RBAC Inheritance Model

Azure Resource Manager governance can be inherited from management groups to child management groups, subscriptions, resource groups, and resources. AFG will use this hierarchy to apply controls at the highest appropriate scope while keeping inheritance understandable and avoiding unnecessary management-group complexity.

```text
Tenant Root Group
└── AFG                         Enterprise baseline intent
    ├── Platform               Shared platform governance
    │   ├── Identity
    │   ├── Management
    │   ├── Connectivity
    │   └── Security
    │
    ├── Landing-Zones          Common workload baseline
    │   ├── Corp               Corporate/hybrid connectivity requirements
    │   │   ├── Production subscriptions
    │   │   └── Non-production subscriptions
    │   ├── Online             Independent connectivity requirements
    │   │   ├── Production subscriptions
    │   │   └── Non-production subscriptions
    │   └── Legacy             Transitional exceptions
    │
    ├── Sandbox                Experimentation controls
    └── Decommissioned         Retirement controls
```

Production and non-production in this diagram are **subscription classifications**, not additional management groups.

### 9.1 Inheritance Principles

AFG will use the following principles:

- Enterprise-wide controls should be assigned at the highest scope where they apply consistently.
- Specialized controls should be assigned at the lowest shared scope that satisfies the requirement.
- Subscription-level assignments are appropriate when a control applies to an environment or workload but not to every subscription beneath its parent management group.
- Policy-as-code should be used in Phase 2 to deploy repeatable subscription-level assignments where environment-specific controls are required across multiple subscriptions.
- Exceptions should be documented rather than implemented through uncontrolled removal or duplication of inherited controls.
- Human RBAC should prefer Microsoft Entra security groups and least-privilege roles rather than broad direct-user assignments.
- Workload identities and managed identities may receive direct resource or scope assignments where technically appropriate.

### 9.2 Tenant Root Group

The Tenant Root Group should contain only controls and access assignments that genuinely need tenant-wide Azure Resource Manager scope.

AFG should avoid placing business- or workload-specific controls at Tenant Root when the same governance outcome can be achieved beneath the `AFG` intermediate root.

Emergency-access and Microsoft Entra directory-role design are tenant identity concerns and are addressed separately from Azure management-group RBAC.

### 9.3 AFG Enterprise Root

The `AFG` management group establishes the common enterprise governance baseline for the modeled AFG Azure estate.

Potential control categories include:

- resource ownership and metadata expectations;
- approved location constraints where universally applicable;
- baseline audit requirements;
- enterprise security expectations;
- governance metadata and cost-accountability requirements.

Detailed policy definitions, enforcement modes, and initiatives are addressed in Phase 2. Detailed telemetry and security-operations configuration are addressed in Phase 5.

### 9.4 Platform Branch

The `Platform` hierarchy inherits the enterprise baseline and applies additional governance appropriate for shared platform services.

Child management groups may apply specialized controls for:

- Identity;
- Management;
- Connectivity;
- Security.

Controls should reflect the responsibilities of each platform capability rather than duplicate controls already inherited from higher scopes.

### 9.5 Landing-Zones Branch

The `Landing-Zones` hierarchy inherits the enterprise baseline and applies common workload governance.

`Corp` and `Online` provide connectivity-based governance archetypes:

- `Corp` supports workloads dependent on shared corporate or hybrid connectivity.
- `Online` supports workloads operating independently from the corporate connectivity model.

Production and non-production separation occurs through subscriptions. If they require different controls, Phase 2 should apply those controls through repeatable subscription-scoped policy assignments or equivalent policy-as-code patterns rather than introducing environment management groups by default.

### 9.6 Legacy Branch

The `Legacy` hierarchy should inherit as much of the enterprise workload baseline as practical.

Exceptions should apply only to controls that a legacy workload cannot currently meet. Each exception should have an owner, rationale, risk treatment, and review or expiration criteria.

### 9.7 Sandbox Branch

The `Sandbox` management group should inherit appropriate enterprise security requirements while allowing controlled experimentation.

Sandbox-specific governance may include:

- spending limits or budgets;
- deployment restrictions;
- shorter lifecycle expectations;
- restricted production connectivity;
- prohibited or tightly controlled use of sensitive data;
- service or SKU restrictions where justified by cost or risk.

### 9.8 Decommissioned Branch

The `Decommissioned` management group should apply restrictive governance intended to prevent new workload deployment and minimize configuration change while approved retention and retirement activities are completed.

The exact technical enforcement mechanism is defined during Phase 2 and should be validated before production use.

### 9.9 RBAC Delegation Model

Microsoft Entra directory roles and Azure RBAC roles serve different control planes and should not be treated as interchangeable.

AFG should use the following RBAC principles:

- prefer Microsoft Entra security groups for recurring human access assignments;
- use least-privilege built-in or approved custom roles rather than defaulting to `Owner` or `Contributor` broadly;
- scope platform-team permissions to the platform capabilities they operate;
- scope workload-team write permissions to their workload subscriptions or resource groups unless a broader scope is justified;
- minimize direct-user Azure RBAC assignments and review unavoidable exceptions;
- use managed identities or workload identities for non-human access where supported;
- account for custom role-definition scope before moving subscriptions between management groups.

Privileged Identity Management, access reviews, privileged-access workflows, and broader identity governance are addressed in Phase 3 — Zero Trust Identity.

### 9.10 Phase Boundary

Phase 1 defines the intended governance and access inheritance architecture.

It does not define:

- complete Azure Policy initiatives;
- final enforcement modes;
- detailed policy-as-code implementation;
- every RBAC role definition;
- privileged identity workflows;
- access-review processes;
- complete networking or telemetry enforcement.

Those controls are addressed in their respective later architecture phases.

## 10. Legacy and Brownfield Transition

AFG will transition existing subscriptions and workloads toward the target landing-zone architecture incrementally.

The migration approach accounts for existing dependencies, operational risk, policy compatibility, ownership, connectivity, and business continuity. Existing workloads should not be rebuilt or moved solely to make the environment visually match the target hierarchy.

### 10.1 Transition Principles

The brownfield transition follows these principles:

- assess before moving;
- prioritize risk reduction over cosmetic alignment;
- preserve business continuity;
- identify dependencies before applying inherited controls;
- use transitional governance where immediate compliance is not feasible;
- avoid weakening the target baseline to accommodate legacy workloads;
- remove temporary exceptions when the underlying constraint is resolved;
- document the difference between target-state design and validated implementation evidence.

### 10.2 Existing Subscription Assessment

Before an existing subscription is moved into the target hierarchy, AFG should assess:

- current business purpose and workload inventory;
- workload and operational owners;
- production or non-production classification;
- connectivity dependencies;
- identity and access dependencies;
- custom RBAC role definitions and their assignable scopes;
- policy compatibility;
- logging and monitoring dependencies;
- recovery requirements and backup dependencies;
- regulatory or data-handling requirements;
- resource locks, deployment scripts, and automation dependencies;
- target management-group placement.

Custom RBAC role definitions require particular attention because a subscription move can break the hierarchy path between a role definition scoped at a previous parent management group and assignments within the subscription.

### 10.3 Direct Migration

A subscription may move directly into the target hierarchy when:

- its purpose and ownership are understood;
- target placement is clear;
- inherited controls have been assessed for compatibility;
- required connectivity will remain available;
- custom role-definition dependencies have been addressed;
- no critical operational dependency is expected to break;
- rollback or recovery actions are understood.

### 10.4 Transitional Legacy Placement

Subscriptions that cannot immediately meet target landing-zone requirements should be placed beneath `Landing-Zones / Legacy` when a controlled transitional boundary is required.

Legacy placement should identify:

- the specific control or dependency preventing standard placement;
- the business and technical owner;
- the associated risk;
- temporary compensating controls where appropriate;
- the intended target-state destination;
- modernization, migration, or retirement criteria;
- the required review cadence.

The `Legacy` management group is not a permanent destination.

### 10.5 Policy Compatibility During Migration

Before enforcing inherited controls on a brownfield subscription, AFG should:

1. evaluate target policy requirements against the subscription;
2. identify non-compliant resources and potential operational impact;
3. remediate blockers where practical;
4. document required temporary exceptions;
5. move the subscription only after the impact is understood;
6. validate policy evaluation after movement;
7. enable stronger enforcement only when the workload is ready and the applicable Phase 2 policy design has been approved.

Audit-first evaluation should be preferred where a deny or modify effect could disrupt an existing workload.

### 10.6 Connectivity and Dependency Validation

Subscription movement must not assume that management-group placement is operationally neutral.

AFG should validate dependencies including:

- virtual network peering and hub connectivity;
- hybrid routing;
- private DNS zone links and name resolution;
- user-defined routes and firewall dependencies;
- private endpoints and service dependencies;
- managed identities and service principals;
- Key Vault access and RBAC dependencies;
- custom RBAC role definitions;
- monitoring and diagnostic integrations;
- deployment automation;
- recovery dependencies.

Network modernization and detailed connectivity design remain within Phase 4, but Phase 1 must ensure that subscription placement does not unintentionally break required dependencies.

### 10.7 Migration Prioritization

Brownfield migration should follow a staged sequence:

1. establish and validate the target management-group hierarchy;
2. place or validate shared platform subscriptions;
3. migrate low-risk subscriptions with clear ownership and few dependencies;
4. migrate standard non-production workloads that are compatible with the target baseline;
5. migrate production workloads after dependency and policy-impact validation;
6. place complex or non-compliant workloads under `Legacy` for controlled remediation;
7. move retired subscriptions into `Decommissioned` when retirement criteria are met.

Critical exposures or risks may require treatment outside this sequence and should not be delayed solely because their broader transformation phase occurs later.

### 10.8 Transition Evidence

Transition evidence must include the following artifacts where applicable:

- documented target management-group placement;
- pre-migration resource inventory;
- policy compatibility or compliance assessment;
- documented dependency review;
- architecture or workload-owner decision record;
- post-migration validation of network, identity, and application availability;
- documented exceptions and remediation dates;
- Azure CLI, Resource Graph, Terraform, or portal evidence for actions actually validated in the lab.

Evidence must distinguish modeled enterprise decisions from actions actually performed in the AFG lab.

### 10.9 Transition Success Criteria

The brownfield transition is successful when:

- every active subscription has a defined owner and purpose;
- each subscription has a documented target management-group placement;
- unclassified subscriptions are reduced and no longer intentionally remain beneath Tenant Root Group;
- incompatible legacy dependencies are identified and tracked;
- temporary exceptions are documented and reviewable;
- subscription moves do not introduce unacceptable service disruption;
- transitional legacy placement trends toward remediation, migration, or retirement.

## 11. Subscription Lifecycle

AFG manages subscriptions through a defined lifecycle from initial request through retirement and deletion.

The lifecycle is intended to ensure that subscriptions have a clear business purpose, accountable ownership, appropriate governance placement, and a controlled exit path when they are no longer required.

### 11.1 Lifecycle Stages

```text
Request
  ↓
Review
  ↓
Approve
  ↓
Vending / Provision
  ↓
Place
  ↓
Operate
  ↓
Review / Change
  ↓
Transition or Retire
  ↓
Decommission
  ↓
Delete
```

### 11.2 Request

A subscription request should identify:

- business or platform purpose;
- workload owner;
- operational owner;
- environment classification;
- expected connectivity model;
- data sensitivity;
- regulatory or contractual requirements;
- estimated lifecycle;
- cost center or financial owner;
- recovery requirements;
- requested target management-group placement.

A subscription should not be created without a defined owner and purpose.

### 11.3 Architecture Review

The request should be evaluated against the subscription placement and boundary criteria defined in this document.

The review should determine:

- whether a new subscription is actually required;
- whether an existing subscription can satisfy the requirement;
- whether the capability belongs under Platform or Landing-Zones;
- whether the workload belongs under Corp, Online, Legacy, or Sandbox;
- whether production and non-production separation is required;
- whether special security, compliance, connectivity, data, or resilience requirements exist.

### 11.4 Approval

Subscription creation should require the appropriate governance, workload, and financial approvals for the modeled enterprise process.

Approval should confirm that:

- the business need is valid;
- the subscription boundary is justified;
- ownership is assigned;
- target placement is defined;
- funding or cost accountability exists;
- known exceptions or risks are documented.

This document defines the target operating intent and does not claim that an enterprise approval workflow has already been implemented in the lab.

### 11.5 Vending and Provisioning

Approved subscriptions should be provisioned through a standardized subscription-vending process as the platform matures.

#### Core Phase 1 Vending Baseline

The Phase 1 vending model should establish:

- standardized subscription naming;
- assignment to the approved target management group;
- ownership and lifecycle metadata;
- baseline RBAC group assignments;
- budget and cost-management configuration;
- required repository or Infrastructure-as-Code records.

#### Integration Hooks for Later Phases

Subscription vending should expose integration points for capabilities that are designed in later phases, including:

- IPAM address allocation;
- virtual network creation and hub or Virtual WAN connectivity;
- private DNS integration;
- centralized diagnostic-log routing;
- Azure Monitor Baseline Alerts or equivalent monitoring enrollment;
- security-platform enrollment;
- policy-as-code assignment;
- workload identity bootstrap where required.

These integrations are architectural targets, not claims that every capability has been implemented during Phase 1.

### 11.6 Placement

Each vended subscription should be assigned to its approved management group before normal workload deployment.

Subscriptions should not remain indefinitely in an unclassified Tenant Root location.

### 11.7 Operation

During normal operation, subscription ownership and placement should remain reviewable.

Operational governance should verify that:

- ownership remains current;
- the subscription still serves its intended purpose;
- inherited controls remain appropriate;
- exceptions remain justified;
- cost and utilization remain understood;
- the workload remains in the correct management group.

### 11.8 Change and Reclassification

A subscription may require reclassification when its purpose, ownership, connectivity, environment, risk profile, or lifecycle changes.

Examples include:

- a proof of concept becoming a production workload;
- an Online workload gaining corporate or hybrid dependencies;
- a legacy workload completing modernization;
- a workload changing business ownership;
- a production service entering retirement.

Changes in classification should trigger architecture review before management-group placement is modified.

### 11.9 Retirement

A subscription should enter retirement when its workloads are no longer required or are being replaced, migrated, or consolidated.

Retirement activities should include:

- confirmation from the workload owner;
- dependency review;
- data-retention review;
- backup or evidence-retention requirements;
- removal of unnecessary access;
- disconnection of unneeded network and DNS dependencies;
- validation that remaining resources are understood;
- definition of the final deletion or review date.

### 11.10 Decommissioned State

Subscriptions awaiting final cancellation or deletion should be moved beneath `Decommissioned` where appropriate.

The decommissioned state should:

- prevent or tightly restrict new workload deployment;
- minimize administrative changes;
- restrict unnecessary access;
- preserve required data or evidence;
- maintain a documented owner;
- include a deletion or formal review date.

Retention duration should be based on business, recovery, legal, contractual, and data-retention requirements rather than a fixed universal window.

### 11.11 Deletion

Final subscription cancellation or deletion should occur only after AFG confirms that:

- required workloads have been migrated or removed;
- retention requirements have been satisfied;
- required evidence has been preserved;
- billing, reservation, or financial dependencies have been resolved;
- no required recovery dependency remains;
- the responsible owner has approved final removal under the applicable operating process.

### 11.12 Lifecycle Governance Outcomes

The subscription lifecycle should enable AFG to answer the following questions for every subscription:

1. Why does this subscription exist?
2. Who owns it?
3. What environment and data-sensitivity classification does it support?
4. Why is it in its current management group?
5. What controls should it inherit?
6. What active exceptions exist?
7. What cost center or financial owner is accountable for it?
8. What is its expected lifecycle?
9. How will it eventually be retired?

A subscription that cannot answer these questions should be treated as a governance gap requiring review.

## 12. Open Architecture Decisions

The following decisions remain unresolved and require evidence or analysis before the Phase 1 target state is considered final.

| Decision ID | Decision | Current Status | Evidence / Analysis Required |
|---|---|---|---|
| `ALZ-DEC-001` | Determine whether the existing shared-services subscription should become `sub-identity-01` or remain a transitional shared-services subscription. | Open | Inventory current resources, confirm ownership, identify non-identity dependencies, and assess whether identity isolation provides sufficient governance value. |
| `ALZ-DEC-002` | Determine whether `sub-prod-apps-02` belongs beneath `Corp` or `Online`. | Open | Validate routing, hybrid connectivity, DNS, firewall, private connectivity, and dependencies on shared enterprise services. |
| `ALZ-DEC-003` | Determine whether disaster-recovery workloads require a dedicated `sub-dr-01`. | Open | Validate recovery operating model, administrative isolation, quota/capacity requirements, security isolation, ownership, and whether same-subscription multi-region recovery is sufficient. |
| `ALZ-DEC-004` | Determine whether application and data workloads require separate subscriptions. | Open | Evaluate ownership, data sensitivity, lifecycle, RBAC, regulatory scope, cost accountability, networking, and operational isolation. |
| `ALZ-DEC-005` | Confirm whether legacy workloads should use a dedicated `Legacy` management group. | Proposed | Identify workloads requiring exceptions, assess whether exceptions would otherwise weaken the standard Corp or Online baseline, and define exit criteria. |
| `ALZ-DEC-006` | Determine the migration sequence for existing subscriptions. | Open | Assess current placement, dependencies, policy compatibility, custom RBAC dependencies, operational risk, and business criticality. |
| `ALZ-DEC-007` | Determine which Phase 1 decisions require formal Architecture Decision Records. | Open | Identify decisions that are significant, difficult to reverse, cross-domain, or likely to require future reconsideration. |
| `ALZ-DEC-008` | Determine the default management group for newly created or unclassified subscriptions. | Open | Decide whether `Sandbox` is sufficient for the representative model or whether a dedicated onboarding/quarantine boundary has distinct governance requirements. |

### 12.1 Decision Governance

An open architecture decision should not be treated as approved until the required evidence has been reviewed and the decision rationale is documented.

Significant decisions should record:

- the problem being solved;
- options considered;
- decision drivers;
- selected option;
- risks and tradeoffs;
- dependencies;
- implementation impact;
- conditions that would require reconsideration.

### 12.2 ADR Criteria

A formal Architecture Decision Record should be created when a decision:

- materially affects multiple architecture domains;
- establishes a long-lived enterprise standard;
- creates significant operational, security, or financial impact;
- is difficult or expensive to reverse;
- resolves competing architecture options;
- accepts a meaningful tradeoff or risk;
- is likely to be questioned or revisited later.

Routine implementation details do not require individual ADRs.

### 12.3 Current ADR Candidates

Based on the current Phase 1 design, likely ADR candidates include:

- adoption of the `AFG` intermediate-root management-group model;
- separation of Platform and Landing-Zones;
- use of Corp, Online, Legacy, Sandbox, and Decommissioned governance boundaries;
- production/non-production separation through subscription boundaries rather than environment management groups;
- legacy workload transition strategy;
- disaster-recovery subscription strategy if ALZ-DEC-003 results in a long-lived enterprise standard.

These remain candidates until the underlying decisions are validated and formally recorded.

## 13. Requirement Traceability

This section maps the Phase 1 Azure Landing Zone requirements to the design responses documented in this architecture.

| Requirement | Design Response | Primary Section |
|---|---|---|
| ALZ-001 | Establishes a standardized management-group hierarchy for enterprise, platform, workload, sandbox, legacy, and retired environments. | Sections 4, 5 |
| ALZ-002 | Defines subscription placement based on workload purpose, ownership, connectivity, environment, governance, and lifecycle. | Sections 6, 7 |
| ALZ-003 | Separates shared platform services from business and application workloads. | Sections 4, 5, 6 |
| ALZ-004 | Separates production and non-production workloads through subscription boundaries where required while retaining the Corp/Online management-group archetypes. | Sections 3, 6, 7, 8, 9 |
| ALZ-005 | Establishes placement criteria for Corp and Online landing zones based primarily on connectivity and routing requirements. | Sections 5, 6, 7 |
| ALZ-006 | Provides a transitional Legacy boundary for workloads that cannot immediately meet the target baseline. | Sections 5, 7, 10 |
| ALZ-007 | Defines Sandbox as a separate governance and lifecycle boundary for temporary experimentation and learning workloads. | Sections 5, 7 |
| ALZ-008 | Defines the subscription lifecycle from request and provisioning through operation, decommissioning, and deletion. | Section 11 |
| ALZ-009 | Establishes dedicated governance boundaries for identity, management, connectivity, and security platform services where justified. | Sections 4, 5, 6 |
| ALZ-010 | Defines an incremental brownfield transition model that avoids unnecessary greenfield rebuilds. | Sections 6, 10 |

### 13.1 Traceability Outcome

The management-group and subscription design provides a direct response to each Phase 1 architecture requirement.

Open architecture decisions identified in Section 12 remain subject to validation and should not be treated as final implementation decisions until the required evidence and analysis are complete.

Where later phases define detailed identity, governance, networking, security operations, DevSecOps, data protection, or AI controls, those artifacts should reference the relevant Phase 1 platform boundaries rather than redefining them.

## 14. Validation Criteria

The Phase 1 management-group and subscription design is architecturally ready for closeout when the target hierarchy, subscription placement model, transition approach, traceability, and required decisions are documented and supported by representative validation evidence.

Implementation validation must distinguish between the proposed enterprise target state and controls or resources actually deployed in the lab.

### 14.1 Architecture Validation

| Validation Criterion | Expected Evidence |
|---|---|
| Every management group has a documented governance purpose. | Management-group responsibility table in Section 5 |
| Every modeled subscription has a defined target placement or an explicit pending decision. | Subscription architecture table in Section 6 |
| Subscription placement follows documented criteria rather than individual preference. | Section 7 placement criteria |
| Separate subscriptions have an architectural justification. | Section 8 boundary criteria |
| Platform services are separated from business workloads. | Target hierarchy and responsibility model in Sections 4 and 5 |
| Corp and Online placement is based on connectivity requirements. | Placement analysis in Sections 6 and 7 |
| Production and non-production separation is represented through justified subscription boundaries. | Sections 6, 7, 8, and 9 |
| Legacy workloads have a controlled transitional path. | Sections 7 and 10 |
| Sandbox workloads are isolated from normal enterprise workloads. | Sections 5 and 7 |
| Retired subscriptions have a defined decommissioning path. | Section 11 |
| Policy and RBAC inheritance intent follows the management-group hierarchy. | Section 9 |
| Brownfield workloads can transition incrementally. | Section 10 |
| All ALZ requirements have a documented design response. | Section 13 traceability table |

### 14.2 Lab Validation

Where practical within the AFG Azure lab, validation should demonstrate that:

- the `AFG` management group exists beneath the Tenant Root Group;
- the proposed Platform and Landing-Zones hierarchy can be represented in Azure;
- representative subscriptions can be assigned to their intended management groups;
- management-group policy inheritance behaves as expected for tested controls;
- moving a representative subscription does not create unexpected RBAC or governance issues after dependency review;
- custom role-definition dependencies are identified before subscription movement;
- the hierarchy can be deployed or maintained through the selected Infrastructure-as-Code approach where included in Phase 1 scope;
- the configured default management group for new subscriptions matches the documented onboarding decision where that setting is tested;
- the deployed lab hierarchy matches the documented design for the elements actually implemented.

Lab validation does not require every modeled enterprise subscription to exist. Representative implementation is sufficient where the architecture intent can be demonstrated without unnecessary Azure cost or operational complexity.

### 14.3 Evidence Requirements

Evidence should be retained only for controls and architecture elements that were actually validated.

Acceptable evidence may include:

- Infrastructure-as-Code configuration and plan/apply output;
- Azure CLI output;
- Azure Resource Graph query output;
- management-group hierarchy screenshots;
- subscription placement output;
- policy evaluation or compliance results;
- RBAC inventories showing the tested delegation model and identifying direct-user exceptions;
- repository configuration;
- architecture diagrams;
- documented test results.

Evidence must not imply that modeled enterprise capabilities have been implemented when they have not been validated in the lab.

### 14.4 Open Decision Validation

Open architecture decisions from Section 12 may be closed when:

- relevant dependencies have been identified;
- reasonable alternatives have been considered;
- the selected option has documented rationale;
- major risks and tradeoffs are understood;
- an accountable decision owner is identified;
- an ADR is created where the decision meets the ADR criteria.

### 14.5 Phase 1 Design Completion Criteria

The Phase 1 design is ready for final review when:

1. the target management-group hierarchy is documented;
2. management-group responsibilities are defined;
3. subscription placement and boundary criteria are documented;
4. modeled subscriptions have target placements, statuses, or explicit open decisions;
5. policy and RBAC inheritance intent is defined without duplicating later-phase control design;
6. brownfield transition and subscription lifecycle are documented;
7. all Phase 1 requirements are traceable to design responses;
8. unresolved decisions are explicitly tracked and either resolved or formally deferred with rationale;
9. representative lab validation has been completed where practical;
10. validated evidence is stored separately from modeled architecture assumptions.

Completion of this design document does not indicate that all target-state Azure resources or controls have been deployed.
