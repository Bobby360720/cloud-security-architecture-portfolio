````markdown
# Cloud Security Architecture Portfolio

> **Status: Active Working Lab / In Development**

This repository is a hands-on **Cloud Security Architecture portfolio and working lab** that demonstrates the assessment, design, engineering, governance, security, and modernization of an enterprise Azure environment.

This is **not a completed reference architecture** and is not intended to represent a production-ready environment in its current state. The repository is being developed incrementally as I work through an end-to-end enterprise architecture transformation.

The objective is to demonstrate not only the final architecture, but also the **engineering and architectural process used to get there**.

---

## What I Am Building

The lab models an enterprise Azure environment and follows its transformation through multiple architecture phases.

Rather than beginning with an idealized greenfield environment, the project starts by establishing a **current-state enterprise architecture** containing realistic architectural, governance, identity, networking, operational, and security challenges.

Each subsequent phase evaluates that environment and introduces architectural changes designed to move it toward a more mature target state.

The portfolio therefore captures both:

- **Architecture decisions**
- **Hands-on implementation**
- **Current-state assessments**
- **Target-state designs**
- **Architecture Decision Records (ADRs)**
- **Infrastructure as Code**
- **Security and governance controls**
- **CI/CD workflows**
- **Validation and testing**
- **Evidence of implementation**
- **Lessons learned and design tradeoffs**

The goal is to demonstrate the complete lifecycle:

**Discover → Assess → Design → Decide → Engineer → Validate → Operate → Improve**

---

## Why I Am Building It

The purpose of this portfolio is to develop and demonstrate the skills required to operate as a **Cloud Security Architect** in a complex enterprise environment.

Cloud architecture is more than deploying technically correct Azure resources. Architects must be able to understand an existing environment, identify risk and technical debt, establish requirements, make defensible design decisions, define governance, communicate tradeoffs, and create an achievable path from the current state to the target state.

This project is therefore intentionally structured as an **architecture transformation**, rather than a collection of disconnected Azure labs.

The focus is on developing and demonstrating capabilities across:

- Enterprise architecture
- Cloud security architecture
- Azure Landing Zones
- Cloud governance
- Zero Trust
- Identity architecture
- Network architecture
- Security operations
- Infrastructure as Code
- DevSecOps
- Data protection
- AI security
- Architecture documentation and decision-making

---

## Lab Philosophy

A key principle of this project is:

> **Understand and reproduce the current state before attempting to improve it.**

The initial environment intentionally contains architectural weaknesses, inconsistent controls, operational gaps, and technical debt.

Those conditions are not necessarily implementation mistakes in the lab. Many are intentionally modeled so they can be discovered during assessment and addressed through later architecture phases.

This creates a more realistic architecture exercise:

```text
Current State
     ↓
Discovery
     ↓
Assessment
     ↓
Requirements
     ↓
Gap Analysis
     ↓
Architecture Decisions
     ↓
Target State
     ↓
Engineering
     ↓
Validation
     ↓
Operationalization
     ↓
Continuous Improvement
````

The lab may use scaled-down resource quantities where appropriate while preserving the architectural relationships and problems being studied.

---

## Current Project Status

🚧 **This repository is actively under development.**

The architecture, documentation, Terraform modules, diagrams, pipelines, controls, and implementation evidence will continue to evolve as each phase is completed.

Some directories may therefore contain:

* incomplete implementations
* design drafts
* placeholders
* planned architecture
* partially deployed infrastructure
* assessment artifacts
* experiments
* implementation evidence
* lessons learned

This is intentional.

The repository is designed to show the **evolution of the architecture**, not simply the polished final result.

---

## Engineering Approach

Infrastructure is increasingly implemented through **Terraform and Infrastructure as Code**, with GitHub serving as the source repository and Azure DevOps providing CI/CD workflow capabilities.

The Terraform engineering workflow follows:

**Write → Format → Initialize → Validate → Plan → Inspect → Apply → Verify → Document**

The emphasis is on maintaining a human architecture and security review between automated planning and infrastructure deployment.

The evolving delivery model is:

```text
Architecture / Requirements
          ↓
      Terraform
          ↓
       GitHub
          ↓
   Azure DevOps CI/CD
          ↓
 Format / Validate / Plan
          ↓
     Human Review
          ↓
        Apply
          ↓
   Azure Environment
          ↓
       Verify
          ↓
 Evidence / Documentation
```

Automation is introduced progressively as the lab matures.

---

# Architecture Transformation Roadmap

## Phase 0 — Enterprise Assessment

**Directory:** `00-enterprise-assessment`

Establish the enterprise current state before modernization begins.

Focus areas include:

* Current-state discovery
* Cloud inventory
* Architecture assessment
* Identity assessment
* Network assessment
* Security operations assessment
* Governance maturity
* Risk identification
* Requirements
* Traceability
* Architecture transformation strategy

**Primary question:**

> What exists today, how does it operate, and what problems must the architecture solve?

---

## Phase 1 — Azure Landing Zone

**Directory:** `01-azure-landing-zone`

Establish the Azure platform foundation required to support the enterprise environment.

Focus areas include:

* Management groups
* Subscription architecture
* Platform organization
* Identity foundations
* Connectivity foundations
* Logging foundations
* Platform architecture
* Resource organization

**Primary question:**

> What foundational Azure architecture should workloads inherit?

---

## Phase 2 — Cloud Governance

**Directory:** `02-cloud-governance`

Establish enterprise cloud governance and enforce architectural standards.

Focus areas include:

* Azure Policy
* Policy initiatives
* Governance baselines
* Compliance
* Naming standards
* Tagging
* Exceptions
* Resource lifecycle controls
* Policy-as-code

**Primary question:**

> How do we make the desired architecture repeatable and enforceable at scale?

---

## Phase 3 — Zero Trust Identity

**Directory:** `03-zero-trust-identity`

Develop the identity architecture around Zero Trust and least privilege.

Focus areas include:

* Microsoft Entra ID
* RBAC
* Privileged Identity Management
* Conditional Access
* Workload identities
* Entitlement architecture
* Privileged access
* Identity governance

**Primary question:**

> Who or what should have access to which resources, under what conditions, and for how long?

---

## Phase 4 — Network Modernization

**Directory:** `04-network-modernization`

Modernize enterprise cloud connectivity and segmentation.

Focus areas include:

* Network topology
* Segmentation
* Private networking
* Firewall architecture
* DNS
* Hybrid connectivity
* ExpressRoute
* Traffic inspection
* Network security controls

**Primary question:**

> How should systems communicate while minimizing unnecessary trust and exposure?

---

## Phase 5 — Security Operations

**Directory:** `05-security-operations`

Develop the monitoring, detection, and response architecture.

Focus areas include:

* Microsoft Sentinel
* Microsoft Defender
* Azure Monitor
* Log Analytics
* Detection engineering
* Security telemetry
* Incident response
* Security operations architecture

**Primary question:**

> How do we know when something is wrong, and how do we respond?

---

## Phase 6 — DevSecOps

**Directory:** `06-devsecops`

Integrate security and architecture controls into the engineering lifecycle.

Focus areas include:

* Infrastructure as Code
* Azure DevOps
* CI/CD
* Policy as Code
* Secrets management
* Pipeline security
* Software supply-chain security
* Automated validation
* Deployment controls

**Primary question:**

> How do we make secure architecture part of the delivery system rather than a manual checkpoint?

---

## Phase 7 — Data Protection

**Directory:** `07-data-protection`

Develop the architecture for protecting enterprise information throughout its lifecycle.

Focus areas include:

* Data classification
* Encryption
* Key management
* Microsoft Purview
* DLP
* Retention
* Data governance
* Data lifecycle controls

**Primary question:**

> What data are we protecting, and what controls should follow that data throughout its lifecycle?

---

## Phase 8 — AI Security

**Directory:** `08-ai-security`

Extend enterprise security architecture into AI-enabled systems.

Focus areas include:

* AI governance
* Model security
* AI identity
* Data protection
* Prompt security
* RAG security
* Monitoring
* AI threat modeling

**Primary question:**

> How should AI systems be introduced without bypassing existing security, identity, and data-governance principles?

---

## Phase 9 — DLV FinTech Platform

**Directory:** `09-dlv-fintech-platform`

Apply the architecture principles developed throughout the portfolio to the **Dynamic Liquidity & Velocity (DLV) FinTech Platform**.

This phase serves as an applied architecture exercise incorporating lessons and controls developed throughout the previous phases.

**Primary question:**

> Can the architecture principles developed throughout the portfolio be applied coherently to a complex platform?

---

# Architecture Journey

```text
Enterprise Assessment
        ↓
Azure Landing Zone
        ↓
Cloud Governance
        ↓
Zero Trust Identity
        ↓
Network Modernization
        ↓
Security Operations
        ↓
DevSecOps
        ↓
Data Protection
        ↓
AI Security
        ↓
DLV FinTech Platform
```

The objective is not simply to reach the bottom of this roadmap.

The objective is to demonstrate **why each architectural change was necessary, what evidence supported the decision, how the solution was engineered, how it was validated, and what was learned from the process.**

---

## Repository Status

**Active development — architecture and implementation are subject to change as the lab progresses.**

This repository represents a learning, engineering, and architecture environment. Content should be evaluated in the context of the phase and point in time in which it was created.

