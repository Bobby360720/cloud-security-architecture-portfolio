# Phase 3 — Zero Trust Identity & Identity Governance

## Objective

Design and validate an enterprise Zero Trust identity architecture that integrates Microsoft Entra ID and SailPoint Identity Security Cloud to secure and govern workforce, privileged, application, and workload identities across AFG Enterprises.

The architecture will establish consistent authentication, authorization, identity lifecycle management, entitlement governance, access certification, and privileged access controls.

Microsoft Entra ID will remain AFG's primary Azure identity and access control plane. SailPoint Identity Security Cloud will be evaluated as the enterprise Identity Governance and Administration (IGA) platform supporting governance across Microsoft and non-Microsoft systems.

## Business Context

AFG Enterprises operates an Azure-first hybrid environment supporting digital payments, financial services, enterprise applications, and business-critical workloads.

The enterprise must address identity-related risks associated with excessive privileges, inconsistent lifecycle processes, orphaned accounts, incomplete entitlement visibility, and insufficient access governance.

AFG is also evaluating potential acquisitions as part of its long-term growth strategy.

Acquired organizations may operate independent directories, identity providers, applications, and access governance processes. Immediate consolidation may introduce operational disruption, security risks, and integration challenges.

AFG requires an identity architecture that supports multiple technology environments, establishes consistent governance, and enables controlled integration of acquired organizations.

**The acquisition scenario is a modeled business assumption, not an approved transaction. SailPoint adoption is a proposed architecture evaluation, not an approved product selection or completed implementation.**

## Architecture Goals

- Establish identity as a primary Zero Trust security control.
- Apply least-privilege access and phishing-resistant authentication.
- Standardize authentication, authorization, and privileged access.
- Establish authoritative identity sources and lifecycle ownership.
- Govern joiner, mover, and leaver processes.
- Standardize access requests, approvals, and certifications.
- Establish enterprise entitlement governance.
- Enforce segregation-of-duties requirements.
- Reduce standing administrative privileges.
- Govern workload and non-human identities.
- Support secure identity integration during acquisitions.
- Centralize identity monitoring and improve threat detection.
- Automate selected identity processes through APIs and Infrastructure as Code.
- Demonstrate measurable security improvements through validation evidence.

## Architecture Areas

### 1. Enterprise Identity Architecture

- Microsoft Entra ID.
- SailPoint Identity Security Cloud.
- Identity trust boundaries.
- Enterprise identity architecture.
- Hybrid identity integration.
- Identity source-of-authority models.
- Identity correlation and aggregation.
- Identity and entitlement data flows.
- Microsoft and non-Microsoft application integration.
- Authentication and governance control-plane responsibilities.

### 2. Authentication and Access Control

- Zero Trust authentication principles.
- Multifactor authentication (MFA).
- Phishing-resistant authentication and passkeys.
- Microsoft Entra Conditional Access.
- Role-Based Access Control (RBAC).
- Attribute-Based Access Control (ABAC).
- Single Sign-On (SSO).
- SAML 2.0, OpenID Connect (OIDC), and OAuth 2.0.
- Device and session security.
- Guest and external identity access.

### 3. Privileged Identity Security

- Microsoft Entra Privileged Identity Management (PIM).
- Just-in-time privileged access.
- Least-privilege administrative roles.
- Privileged access separation.
- Emergency-access accounts.
- Privileged entitlement governance.
- Privileged access certifications.
- Privileged activity monitoring.

### 4. Enterprise Identity Governance — SailPoint

- SailPoint Identity Security Cloud architecture.
- Identity aggregation and correlation.
- Identity lifecycle governance.
- Joiner, mover, and leaver workflows.
- Birthright access provisioning.
- Access request and approval workflows.
- Role and entitlement modeling.
- Access certifications and recertification campaigns.
- Segregation-of-duties controls.
- Orphaned and dormant account identification.
- Application onboarding and connector architecture.
- Provisioning and reconciliation.
- Governance reporting and audit evidence.

### 5. Microsoft Entra ID Governance

- Microsoft Entra entitlement management.
- Access packages.
- Lifecycle workflows.
- Access reviews.
- Group-based access governance.
- Application provisioning.
- External identity governance.
- Microsoft Entra and SailPoint integration.
- Governance responsibility boundaries.
- Prevention of conflicting provisioning workflows.

### 6. Workload and Non-Human Identity

- Azure managed identities.
- Service principals and application registrations.
- Federated workload identity.
- Credential and secret lifecycle management.
- Workload identity permissions.
- Application permission governance.
- Non-human identity ownership and accountability.
- SailPoint non-human identity governance capabilities and integration requirements.

### 7. Merger and Acquisition Identity Integration

- Acquired organization identity assessments.
- Cross-tenant and cross-organization access.
- Identity and entitlement discovery.
- Identity correlation across organizational boundaries.
- Temporary and transitional access governance.
- Identity coexistence and migration strategies.
- Access certifications during acquisition integration.
- Identity consolidation decision criteria.
- Integration risk assessment.

### 8. Identity Threat Detection and Monitoring

- Identity threat modeling.
- Authentication and authorization telemetry.
- Microsoft Entra sign-in and audit logs.
- Microsoft Sentinel integration.
- Privileged access monitoring.
- Suspicious authentication and privilege escalation.
- Provisioning and governance exception monitoring.
- Identity-related detection use cases.
- Identity incident investigation.

### 9. Identity Automation and Integration

- Terraform-managed Microsoft Entra configuration.
- Microsoft Graph API integration.
- SailPoint API architecture and integration.
- REST API authentication and authorization.
- Identity provisioning automation.
- SCIM-based provisioning patterns.
- Python-based identity automation.
- Identity reconciliation testing.
- Configuration validation and drift detection.
- Secure API credential management.
- Automated control validation and evidence collection.

## Architecture Decision Requirements

Before implementation, Phase 3 will document decisions addressing:

1. Microsoft Entra and SailPoint responsibilities.
2. Authoritative identity sources and lifecycle ownership.
3. Enterprise access request and certification ownership.
4. Role and entitlement governance standards.
5. Application provisioning and reconciliation boundaries.
6. Privileged identity governance responsibilities.
7. Non-human identity governance.
8. Acquisition identity integration patterns.
9. Licensing, operational cost, and platform ownership.

Architecture decisions will reference the enterprise risk register, findings register, security requirements, and established AFG architecture baseline.

## Validation Approach

Selected architecture patterns will be validated in a controlled, low-cost lab environment.

### Microsoft Entra Validation

- Conditional Access enforcement.
- MFA and authentication strength.
- RBAC and least-privilege enforcement.
- Privileged Identity Management, where licensed.
- Access packages and access reviews, where licensed.
- Workload identity federation.
- Microsoft Graph API automation.

### SailPoint Validation

Depending on authorized training and lab access:

- Identity aggregation and correlation.
- Access request workflows.
- Joiner, mover, and leaver processes.
- Role and entitlement management.
- Access certification campaigns.
- Application provisioning and reconciliation.
- Identity governance reporting.

Where direct SailPoint access is unavailable, equivalent IGA workflows may be demonstrated through a separately identified open-source lab or simulated integration.

Such exercises will not be represented as completed SailPoint implementations.

### Automation Validation

- Python-based identity workflow exercises.
- Microsoft Graph API integration.
- REST API request and response handling.
- SCIM provisioning patterns.
- Terraform identity configuration.
- Automated policy and access validation.

## Expected Outcomes

Phase 3 will establish:

- A documented enterprise Zero Trust identity architecture.
- Defined Microsoft Entra and SailPoint responsibility boundaries.
- An enterprise identity governance operating model.
- Standardized identity lifecycle management requirements.
- Access request, approval, and certification architecture.
- Privileged identity security standards.
- Workload and non-human identity governance standards.
- Acquisition identity integration patterns.
- Identity security monitoring requirements.
- Repeatable identity automation patterns.
- Documented validation evidence and residual risks.

Success will be assessed using measurable outcomes such as privileged-access exposure, access removal performance, entitlement ownership, certification coverage, and identity control effectiveness.

## Status

**Planned — Architecture design, SailPoint evaluation, and implementation pending.**

Phase 3 builds upon the enterprise assessment, Azure landing-zone architecture, and cloud governance requirements established in earlier phases.

SailPoint Identity Security Cloud is the proposed enterprise IGA platform for evaluation. Its implementation remains subject to architecture decisions, licensing, access availability, and cost assessment.

Modeled assumptions, proposed controls, observed configurations, and validated implementations will be documented separately.