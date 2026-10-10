# Phase 3 — Zero Trust Identity

## Objective

Design and validate an identity-centric Zero Trust architecture that supports secure access across AFG Enterprises, its Azure environment, enterprise applications, and potentially acquired organizations.

The architecture will establish consistent identity governance, authentication, authorization, privileged access, and workload identity controls while supporting integration between Microsoft Entra ID and Okta.

## Business Context

AFG Enterprises is evaluating potential acquisitions as part of its long-term growth strategy.

Acquired organizations may operate independent identity providers, directories, applications, and security policies. Immediate consolidation into AFG's existing Microsoft Entra ID environment may introduce operational disruption, security risks, and integration challenges.

AFG requires an identity architecture that can support multiple identity providers, establish appropriate trust boundaries, and integrate acquired organizations through a controlled transition process.

Microsoft Entra ID remains the primary identity control plane for AFG's Azure environment. Okta will be evaluated as a complementary workforce identity and federation platform to support enterprise applications and potential acquisition scenarios.

**The acquisition scenario is a modeled business assumption, not an approved transaction or implementation decision.**

## Architecture Goals

- Establish identity as a primary Zero Trust security control.
- Apply least-privilege access and continuous access evaluation where supported.
- Standardize authentication, authorization, and privileged access controls.
- Support secure identity federation across organizational boundaries.
- Integrate Microsoft Entra ID and Okta using established federation standards.
- Establish identity lifecycle governance for workforce and non-human identities.
- Reduce standing administrative privileges and credential-related risks.
- Support secure identity integration during mergers and acquisitions.
- Centralize identity security monitoring and improve threat detection.
- Implement and validate selected identity controls through Infrastructure as Code.

## Architecture Areas

### 1. Enterprise Identity Architecture
- Microsoft Entra ID
- Okta Workforce Identity
- Identity provider integration and federation
- Identity trust boundaries
- Hybrid and multi-IdP architecture
- Identity source-of-authority models

### 2. Authentication and Access Control
- Zero Trust authentication principles
- Multifactor authentication (MFA)
- Conditional Access and Okta authentication policies
- Role-Based Access Control (RBAC)
- Attribute-Based Access Control (ABAC)
- Single Sign-On (SSO)
- SAML 2.0, OpenID Connect (OIDC), and OAuth 2.0

### 3. Privileged Identity Security
- Microsoft Entra Privileged Identity Management (PIM)
- Just-in-time privileged access
- Least-privilege administrative roles
- Privileged access separation
- Emergency-access accounts
- Privileged activity monitoring

### 4. Identity Governance and Lifecycle
- Joiner, mover, and leaver processes
- Identity provisioning and deprovisioning
- System for Cross-domain Identity Management (SCIM)
- Entitlement management
- Access reviews and certifications
- Group-based access governance
- Identity ownership and accountability

### 5. Workload and Non-Human Identity
- Azure managed identities
- Service principals and application registrations
- Federated workload identity
- Credential and secret lifecycle management
- Workload identity permissions
- Non-human identity governance

### 6. Merger and Acquisition Identity Integration
- Acquired organization identity assessments
- Cross-tenant and cross-organization access
- Identity federation and trust establishment
- Identity coexistence and migration strategies
- Temporary and transitional access controls
- Identity consolidation decision criteria
- Integration risk assessment

### 7. Identity Threat Detection and Monitoring
- Identity threat modeling
- Authentication and authorization telemetry
- Microsoft Entra sign-in and audit logs
- Okta System Log
- Microsoft Sentinel integration
- Identity-related detection use cases
- Identity incident investigation

### 8. Identity Infrastructure as Code
- Terraform Microsoft Entra configuration
- Terraform Okta configuration
- Repeatable identity policy deployment
- Configuration validation
- Drift detection
- Secure management of provider credentials

## Validation Approach

Selected architecture patterns will be validated using a controlled, low-cost lab environment.

Validation scenarios may include:

- Microsoft Entra ID and Okta authentication policy enforcement.
- SAML and OIDC application federation.
- SCIM-based identity provisioning and deprovisioning.
- Privileged access and least-privilege enforcement.
- Cross-organization identity integration.
- Workload identity and credential management.
- Identity event collection and security monitoring.
- Terraform-based identity configuration.

Implementation evidence will be recorded separately from modeled enterprise assumptions and proposed architectural decisions.

## Expected Outcomes

Phase 3 will establish a documented Zero Trust identity architecture that:

- Supports secure workforce and workload access.
- Defines responsibilities and trust boundaries across identity providers.
- Enables controlled identity integration for potential acquisitions.
- Reduces risks associated with excessive privilege, inconsistent authentication, and unmanaged identities.
- Establishes repeatable identity governance and operational controls.
- Demonstrates security control effectiveness through documented validation evidence.

## Status

**Planned — Architecture design and implementation pending.**

Phase 3 will build upon the enterprise assessment, landing-zone architecture, and governance requirements established in earlier phases.