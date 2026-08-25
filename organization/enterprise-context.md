# Enterprise Context and Security Governance Assessment

## Executive Summary

AFG Enterprises has reached the point where continued cloud growth
without a unified architecture and governance model would increase
security, compliance, operational, and financial risk.

The environment is not characterized by a complete absence of security
tooling. The larger problem is that **security capabilities, governance
controls, ownership, enforcement, and operational processes have not yet
been integrated into one consistent enterprise system**.

This distinction is important.

Deploying Microsoft Defender, Sentinel, Azure Policy, RBAC, logging, or
private networking does not by itself create security governance.
Governance requires defined standards, accountable owners, measurable
controls, enforcement, exception management, lifecycle management, and
evidence.

The transformation therefore focuses on moving from **tool-centric
security** toward **architecture-led governance**.

------------------------------------------------------------------------

# Current-State Governance Problem

The core problem can be summarized as:

> Azure has grown faster than the governance model used to control it.

This creates several interconnected risks.

## 1. Management-Group and Subscription Governance

### Current-State Concerns

The existing environment requires a deliberate enterprise
management-group hierarchy rather than allowing subscriptions to operate
as largely independent governance boundaries.

Without a standardized hierarchy:

-   policy inheritance becomes inconsistent;
-   production and non-production controls can diverge unintentionally;
-   shared platform services lack a clear governance boundary;
-   security controls may be assigned repeatedly at subscription scope;
-   ownership of enterprise controls becomes difficult to determine;
-   new subscriptions can be created without automatically inheriting
    the intended baseline.

### Target Direction

Establish a hierarchy that separates:

-   platform services;
-   landing zones;
-   production;
-   non-production;
-   sandbox;
-   decommissioned or transitional workloads.

Enterprise controls should inherit from the highest appropriate scope.

------------------------------------------------------------------------

## 2. Governance Is Too Dependent on Human Knowledge

A major governance weakness exists whenever resource purpose, owner,
environment, cost center, or criticality can only be determined by
asking someone.

This creates operational and security risk when:

-   staff change roles;
-   teams reorganize;
-   applications are retired;
-   incidents occur;
-   auditors request evidence;
-   cloud spend must be attributed.

### Target Direction

Resource metadata and platform state should make ownership and business
context discoverable without tribal knowledge.

A controlled tagging taxonomy should identify, where appropriate:

-   workload;
-   environment;
-   owner;
-   business unit;
-   cost center;
-   criticality/tier;
-   data sensitivity;
-   management responsibility.

------------------------------------------------------------------------

## 3. Security and Governance Controls Are Not Yet Fully Codified

Manual standards and portal configuration are difficult to scale and
audit.

Risks include:

-   inconsistent implementation;
-   undocumented configuration drift;
-   controls being bypassed unintentionally;
-   difficulty reproducing environments;
-   weak peer-review evidence;
-   slow recovery from configuration mistakes.

### Target Direction

Move repeatable platform controls toward:

-   Azure Policy as Code;
-   Bicep/Terraform;
-   version control;
-   pull-request review;
-   CI/CD validation;
-   controlled deployment.

------------------------------------------------------------------------

## 4. Policy Enforcement Requires a Formal Lifecycle

Immediately deploying restrictive `Deny` controls can interrupt business
workloads. Leaving everything in `Audit` indefinitely creates the
opposite problem: known noncompliance without enforcement.

### Target Direction

Use a defined policy lifecycle:

`Draft → Lab Testing → Audit → Modify/DeployIfNotExists → Deny → Operational Standard`

Every policy should have:

-   an owner;
-   defined scope;
-   expected effect;
-   testing evidence;
-   remediation guidance;
-   review cadence;
-   exception path.

------------------------------------------------------------------------

## 5. Governance and Security Ownership Can Become Blurred

Governance, security, platform engineering, networking, FinOps,
application teams, and change-management functions have overlapping
responsibilities.

Without explicit accountability:

-   findings remain unresolved;
-   policy changes stall;
-   security teams become owners of application risk they do not
    control;
-   platform teams may deploy controls without security review;
-   nobody owns exceptions after approval.

### Target Direction

Establish a RACI model for:

-   architecture;
-   policy ownership;
-   control deployment;
-   remediation;
-   exception approval;
-   privileged access;
-   logging;
-   incident response;
-   subscription onboarding;
-   decommissioning.

------------------------------------------------------------------------

# Security Governance Gap Assessment

## 6. Identity and Privileged Access

Identity is the primary security boundary in modern cloud architecture.

Potential governance weaknesses include:

-   standing privileged roles;
-   overly broad RBAC assignments;
-   direct user permissions instead of group-based access;
-   inconsistent privileged elevation;
-   unmanaged service principals;
-   long-lived application secrets;
-   weak ownership of workload identities;
-   limited access-review processes;
-   insufficient entitlement lifecycle management.

### Target Direction

Phase 3 should establish:

-   least privilege;
-   PIM;
-   Conditional Access;
-   workload identity governance;
-   managed identities;
-   access reviews;
-   entitlement management;
-   emergency-access controls;
-   separation of duties.

------------------------------------------------------------------------

## 7. Public Exposure and Network Trust

Legacy cloud designs often treat the network boundary as inherently
trusted.

Security risks arise from:

-   public PaaS endpoints;
-   inconsistent private endpoint adoption;
-   insufficient segmentation;
-   unrestricted administrative paths;
-   unclear egress controls;
-   inconsistent DNS architecture;
-   network rules managed independently by workloads.

### Target Direction

Phase 4 should move toward:

-   private connectivity by default;
-   controlled exceptions;
-   segmentation;
-   centralized inspection where appropriate;
-   standardized DNS;
-   secure ExpressRoute/hybrid connectivity;
-   explicit ingress and egress architecture.

------------------------------------------------------------------------

## 8. Logging Coverage and Telemetry Consistency

Security monitoring becomes unreliable when logging differs by
subscription, workload, resource type, or owner.

Potential gaps include:

-   resources without diagnostic settings;
-   inconsistent Log Analytics destinations;
-   incomplete Entra telemetry;
-   missing network telemetry;
-   inconsistent Azure Arc monitoring;
-   legacy monitoring agents;
-   incomplete Data Collection Rule association;
-   insufficient retention;
-   unclear log ownership.

### Target Direction

Phase 5 should define:

-   enterprise logging requirements;
-   standard diagnostic settings;
-   AMA/DCR architecture;
-   centralized security telemetry;
-   retention standards;
-   Sentinel integration;
-   Defender integration;
-   detection coverage;
-   monitoring KPIs.

------------------------------------------------------------------------

## 9. Security Operations Can Become Tool-Centric

Purchasing or enabling Sentinel and Defender does not automatically
create a mature security-operations architecture.

Governance gaps may include:

-   unclear alert ownership;
-   insufficient detection engineering;
-   inconsistent onboarding;
-   weak incident escalation paths;
-   unmanaged analytics rules;
-   no defined detection lifecycle;
-   limited measurement of coverage and effectiveness.

### Target Direction

Treat detections and security monitoring as managed engineering
artifacts with owners, versioning, testing, review, and retirement
processes.

------------------------------------------------------------------------

## 10. Secrets and Workload Credentials

Application credentials create significant risk when ownership and
lifecycle are unclear.

Potential issues include:

-   client secrets stored outside managed secret stores;
-   secrets without documented owners;
-   manual secret rotation;
-   excessive API permissions;
-   unused application registrations;
-   credentials that outlive the workload;
-   unclear separation between development and production identities.

### Target Direction

Prefer:

1.  managed identities;
2.  workload identity federation;
3.  Key Vault-backed secrets where secrets remain necessary;
4.  automated rotation;
5.  least-privilege API permissions;
6.  recurring application and credential reviews.

------------------------------------------------------------------------

## 11. Cloud Resource Configuration Drift

Security baselines can degrade when individual teams configure resources
independently.

Examples include inconsistent:

-   TLS requirements;
-   storage public access;
-   network controls;
-   diagnostic settings;
-   Key Vault protections;
-   backup;
-   managed identity usage;
-   allowed regions;
-   allowed SKUs.

### Target Direction

Use Azure Policy and IaC to detect, remediate, or deny configurations
that violate enterprise standards.

------------------------------------------------------------------------

## 12. Exception Management

A security policy without a usable exception process will eventually be
bypassed informally.

Weak exception governance includes:

-   permanent exemptions;
-   undocumented business justification;
-   missing compensating controls;
-   no expiration;
-   no re-review;
-   exemptions broader than necessary.

### Target Direction

Every exception should be:

-   formally requested;
-   scoped narrowly;
-   risk assessed;
-   approved by the correct authority;
-   time limited;
-   tracked;
-   reviewed;
-   removed when no longer required.

------------------------------------------------------------------------

## 13. Security Baselines Need Independent Ownership and Versioning

Combining every governance and security requirement into one monolithic
policy initiative makes change difficult.

Security controls and general governance controls frequently have
different:

-   owners;
-   risk tolerances;
-   deployment timelines;
-   review cycles.

### Target Direction

Separate modular baselines such as:

-   Core Governance;
-   Core Security;
-   Tagging and Resource Governance;
-   Platform Services;
-   Production;
-   Non-Production;
-   Sandbox;
-   Azure Arc.

This supports independent versioning while preserving inheritance.

------------------------------------------------------------------------

## 14. Compliance Must Be Measurable

A written standard is not sufficient evidence of compliance.

Weak governance occurs when the enterprise cannot quickly answer:

-   Which resources violate the baseline?
-   Which subscriptions have incomplete logging?
-   Which resources are publicly accessible?
-   Which privileged roles are standing?
-   Which exemptions are expired?
-   Which workloads have no owner?
-   Which controls are only auditing instead of enforcing?

### Target Direction

Define governance KPIs and dashboards that measure control effectiveness
and remediation progress.

------------------------------------------------------------------------

## 15. Azure Arc Extends the Governance Boundary

Hybrid infrastructure should not become a separate security-governance
island.

Without consistent governance, on-premises or externally hosted servers
may have different:

-   monitoring;
-   tagging;
-   policy;
-   inventory;
-   vulnerability management;
-   ownership standards.

### Target Direction

Use Azure Arc to extend appropriate Azure governance and monitoring
patterns to hybrid servers while recognizing the differences between
Azure-native and Arc-enabled resources.

------------------------------------------------------------------------

## 16. Change Management Must Support Security Engineering

Traditional change processes can conflict with cloud's faster
configuration lifecycle.

Too little governance creates uncontrolled change. Too much manual
governance pushes teams around the process.

### Target Direction

Automate low-risk validation and preserve human approval for high-risk
changes.

The desired model combines:

-   Git history;
-   peer review;
-   automated tests;
-   policy validation;
-   staged deployment;
-   approval gates;
-   rollback/remediation plans.

------------------------------------------------------------------------

## 17. Naming and Resource Standards Need Enforcement

Naming standards improve:

-   inventory;
-   automation;
-   troubleshooting;
-   incident response;
-   cost attribution.

However, naming conventions alone are not security controls.

### Target Direction

Use naming standards alongside immutable metadata, tags, resource
inventory, and policy. Avoid relying on names as the only source of
identity or ownership.

------------------------------------------------------------------------

## 18. Data Protection Requires Classification

Infrastructure security cannot determine the appropriate protection
level if the enterprise does not know what data a workload processes.

Potential risks include:

-   sensitive data stored without classification;
-   inconsistent encryption/key ownership;
-   excessive retention;
-   insufficient DLP;
-   weak data-access governance;
-   production data appearing in non-production systems.

### Target Direction

Phase 7 should establish a data-protection model based on sensitivity
and lifecycle.

------------------------------------------------------------------------

## 19. AI Adoption Creates New Governance Risks

AI workloads introduce risks that traditional Azure baselines do not
fully address.

Examples include:

-   sensitive information entering prompts;
-   prompt injection;
-   RAG authorization failures;
-   excessive agent permissions;
-   untrusted model/tool output;
-   insecure plugins/tools;
-   AI supply-chain dependencies;
-   inadequate monitoring;
-   unclear model/data ownership.

### Target Direction

Phase 8 establishes a dedicated AI security architecture rather than
assuming conventional application controls are sufficient.

------------------------------------------------------------------------

## 20. Product Security Must Integrate the Entire Architecture

The DLV FinTech platform introduces a higher-consequence environment
involving financial data, scoring logic, APIs, identity, privacy, and
potentially open-banking integrations.

It should not be designed as an isolated application.

### Target Direction

Phase 9 applies the preceding architecture capabilities to a product:

-   landing-zone controls;
-   governance;
-   Zero Trust;
-   private networking;
-   security operations;
-   DevSecOps;
-   data protection;
-   AI security where applicable;
-   product threat modeling;
-   privacy and compliance.

------------------------------------------------------------------------

# Security Governance Risk Summary

  -----------------------------------------------------------------------
  Domain                  Governance Concern      Relative Priority
  ----------------------- ----------------------- -----------------------
  Enterprise governance   Inconsistent control    Critical
                          inheritance and         
                          ownership               

  Identity                Excessive or persistent Critical
                          privilege               

  Workload credentials    Secret lifecycle and    Critical
                          application permissions 

  Network                 Public exposure and     High
                          inconsistent            
                          segmentation            

  Logging                 Incomplete or           High
                          inconsistent telemetry  

  Policy                  Controls not            High
                          consistently            
                          codified/enforced       

  Exceptions              Exemptions becoming     High
                          permanent risk          

  DevSecOps               Manual configuration    High
                          and insufficient        
                          deployment gates        

  Data                    Classification and      High
                          lifecycle controls      

  Security operations     Tool deployment without Medium-High
                          engineering lifecycle   

  Hybrid/Arc              Different governance    Medium-High
                          for non-Azure           
                          infrastructure          

  Cost/ownership          Resources without       Medium
                          reliable accountability 
                          metadata                

  AI                      New threat classes and  High as adoption grows
                          governance requirements 
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Target Security Governance Model

The desired end state is:

**Business requirements** ↓\
**Architecture principles** ↓\
**Management-group and subscription architecture** ↓\
**Security and governance standards** ↓\
**Policy / RBAC / network / data controls** ↓\
**Infrastructure and Policy as Code** ↓\
**CI/CD validation and approval** ↓\
**Deployment** ↓\
**Central monitoring and compliance** ↓\
**Risk and exception management** ↓\
**Continuous improvement**

Security governance becomes a continuous operating system for cloud
rather than a periodic review exercise.

------------------------------------------------------------------------

# Transformation Mapping

## Phase 0 --- Enterprise Assessment

Establish current state, requirements, risks, ownership, dependencies,
and transformation priorities.

## Phase 1 --- Azure Landing Zone

Create the enterprise Azure platform foundation and management
hierarchy.

## Phase 2 --- Cloud Governance

Codify governance and security baselines, policy lifecycle, exceptions,
compliance, and accountability.

## Phase 3 --- Zero Trust Identity

Modernize identity, privilege, workload access, and entitlement
governance.

## Phase 4 --- Network Modernization

Reduce implicit network trust and standardize private, segmented
connectivity.

## Phase 5 --- Security Operations

Create measurable centralized monitoring, detection, response, and
security posture management.

## Phase 6 --- DevSecOps

Move security controls into code, pipelines, and repeatable delivery
workflows.

## Phase 7 --- Data Protection

Govern data according to sensitivity, business impact, and lifecycle.

## Phase 8 --- AI Security

Extend governance to generative AI, models, RAG, agents, prompts, and AI
data flows.

## Phase 9 --- DLV FinTech Platform

Demonstrate how the entire architecture model protects a new
financial-technology platform.

------------------------------------------------------------------------

# Definition of Success

The transformation is successful when the organization can answer, using
authoritative platform data rather than tribal knowledge:

-   What do we own?
-   Who owns it?
-   Why does it exist?
-   How critical is it?
-   What data does it process?
-   Who can administer it?
-   Is it compliant?
-   Is it publicly exposed?
-   Is it monitored?
-   Is it recoverable?
-   What exceptions exist?
-   Who accepted the residual risk?
-   Can the environment be reproduced through code?
-   Can we prove the controls are working?

That is the security-governance standard the remainder of the portfolio
is designed to demonstrate.
