# Aurelius Financial Group (AFG) — Company Profile

> **Fictional organization.** Aurelius Financial Group, its people, subsidiaries, systems, and
> data are entirely fabricated for use as a consistent portfolio environment. Any resemblance
> to a real company is coincidental. This document is the canonical reference for every
> case study, architecture, and artifact built under the AFG name — later projects should
> align with what's defined here rather than introducing conflicting details.

---

## 1. Company Overview

| Attribute | Detail |
|---|---|
| **Legal name** | Aurelius Financial Group, Inc. |
| **Short name** | AFG |
| **Industry** | Financial Services / FinTech |
| **Headquarters** | Charlotte, North Carolina, USA |
| **Founded** | 2011 |
| **Ownership** | Privately held, investor-backed |
| **Employees** | ~4,500 |
| **Corporate users (identities)** | ~4,000 |
| **Customers** | ~2.1 million retail and small-business customers |
| **Annual revenue** | ~$680M (fictional) |
| **Primary markets** | United States (regulated in all 50 states) |
| **Business lines** | Digital banking, consumer lending, payments processing, wealth management |

### Company narrative

AFG began as a digital-only consumer lending startup and has grown through organic
expansion and two acquisitions into a diversified financial services company. It now
operates a retail digital bank, a payments processing arm, a lending platform, and a
wealth-management advisory service. Rapid growth left the company with fragmented
cloud environments, inconsistent governance, and inherited technical debt from
acquired subsidiaries — the ongoing problem this portfolio's case studies exist to solve.

---

## 2. Business Capabilities

| Capability | Description |
|---|---|
| Digital Banking | Checking/savings accounts, mobile & web banking, bill pay |
| Consumer Lending | Personal loans, auto refinancing, buy-now-pay-later |
| Payments Processing | Merchant payment acceptance, ACH/wire transfer, card issuing |
| Wealth Management | Robo-advisory and human-advisor hybrid investment platform |
| Risk & Compliance | Credit risk modeling, fraud detection, regulatory reporting |
| Corporate Functions | HR, Finance, Legal, Marketing, Corporate IT |

---

## 3. Technology Landscape

| Attribute | Environment |
|---|---|
| **Cloud strategy** | Azure-first |
| **Hybrid footprint** | Azure + on-premises data centers (2 regional DCs, being decommissioned) |
| **Identity provider** | Microsoft Entra ID (hybrid-joined, Entra Connect sync from on-prem AD) |
| **Endpoint security** | Microsoft Defender for Endpoint |
| **SIEM / SOC** | Microsoft Sentinel |
| **Cloud governance** | Azure Policy + Management Groups (Azure Landing Zone aligned) |
| **Infrastructure as Code** | Bicep (primary), Terraform (legacy / multi-cloud pockets) |
| **CI/CD** | Azure DevOps |
| **Data platform** | Azure SQL Database, Azure Storage, Azure Synapse, Key Vault |
| **Application hosting** | App Service, AKS, Azure Container Apps |
| **Networking** | Hub-and-spoke, Azure Firewall, ExpressRoute to primary DC |
| **Architecture pattern** | Enterprise-scale Landing Zones (Microsoft CAF) |
| **Security model** | Zero Trust |

---

## 4. Regulatory & Compliance Requirements

As a U.S. financial services company handling consumer payments, deposits, and credit,
AFG operates under:

- **PCI DSS** — card payment processing (merchant + issuing operations)
- **SOC 2 Type II** — annual audit for corporate and cloud environments
- **GLBA (Gramm-Leach-Bliley Act)** — safeguarding nonpublic personal financial information
- **FFIEC guidance** — as a digital bank, aligns to FFIEC IT examination handbooks
- **State money transmitter licensing** — payments business, multi-state
- **CCPA / state privacy laws** — customer data handling and consumer rights
- **NIST 800-53 / NIST CSF** — internal control baseline mapped to Azure Policy initiatives

These drive the compliance guardrails referenced throughout the governance and security
case studies (data residency, encryption at rest/in transit, audit logging retention,
access reviews, etc.).

---

## 5. Architecture Principles

Every project in this portfolio must be consistent with these eight principles:

1. **Zero Trust by default** — never trust, always verify; no implicit trust based on network location.
2. **Identity is the primary security perimeter** — Entra ID, Conditional Access, and PIM anchor every access decision.
3. **Private connectivity preferred** — private endpoints and hub-and-spoke networking over public exposure.
4. **Infrastructure must be defined as code** — no manual "ClickOps" changes to production.
5. **Policy as Code governs cloud resources** — guardrails enforced via Azure Policy at management group scope, not tribal knowledge.
6. **Centralized security telemetry is mandatory** — all logs flow to Sentinel; no orphaned data sources.
7. **Least privilege and just-in-time privileged access** — PIM-gated, time-boxed, and audited.
8. **Security controls must be measurable** — every control maps to a metric, dashboard, or compliance score.

---

## 6. Organizational Model (Stakeholders)

```
Board / Executive Committee
           │
           ▼
          CIO
     ┌─────┴─────┐
    CISO         CTO
     │            │
Security       Platform
Architecture   Engineering
     │            │
     └─────┬──────┘
           │
     Cloud Platform Team
           │
    ┌──────┼───────┐
 Security Network  DevOps
```

Standard ownership roles used across ADRs and case studies:

| Role | Responsibility |
|---|---|
| **Business Owner** | Accountable business unit (e.g., Digital Banking, Payments) |
| **Architecture Owner** | Cloud Architecture team — designs and approves target state |
| **Control Owner** | Information Security — defines and owns required controls |
| **Implementation Owner** | Platform Engineering — builds and operates the solution |
| **Risk Owner** | CISO organization — accepts residual risk, approves exceptions |

---

## 7. Current State (Starting Problems)

The portfolio begins with AFG's technical debt as the baseline problem set:

- Inconsistent management group structure; workloads scattered across a flat subscription model
- Policy sprawl — overlapping, conflicting, or unenforced Azure Policy assignments
- Weak and inconsistent resource tagging (no reliable cost attribution)
- Fragmented logging — some subscriptions not onboarded to Sentinel/Log Analytics
- Legacy, over-permissioned RBAC assignments inherited from acquisitions
- Manual, ClickOps-style deployments in several business units
- No consistent security baseline across production vs. non-production
- Unclear ownership for shared platform services

---

## 8. Architecture Roadmap

```
PHASE 0   Enterprise Assessment
PHASE 1   Azure Landing Zone
PHASE 2   Cloud Governance
PHASE 3   Zero Trust Identity
PHASE 4   Network Modernization
PHASE 5   Security Operations
PHASE 6   DevSecOps
PHASE 7   Data Protection
PHASE 8   AI Security
PHASE 9   Digital Lending Platform (DLV)
```

Each phase produces the same artifact chain:

```
Problem → Current State → Requirements → Threat Model → Risk Assessment
   → Architecture Options → ADR → Target Architecture → Implementation
   → IaC → Security Validation → Future State → Business/Security Outcomes
```

---

## 9. Suggested Repository Structure

```
cloud-security-architecture-portfolio/
│
├── README.md
│
├── organization/
│   ├── company-profile.md          ← this document
│   ├── business-capabilities.md
│   ├── technology-landscape.md
│   ├── regulatory-requirements.md
│   ├── security-principles.md
│   └── architecture-principles.md
│
├── 01-enterprise-landing-zone/
├── 02-cloud-governance/
├── 03-zero-trust-identity/
├── 04-network-security/
├── 05-security-operations/
├── 06-devsecops/
├── 07-data-security/
├── 08-ai-security/
├── 09-business-continuity/
└── 10-dlv-platform/
```

---

*This profile is the canonical Step 0 reference. Every future AFG case study — including
the Azure Management Group & Subscription Transformation Plan already built — should be
treated as chapters of this same organization's ongoing transformation.*
