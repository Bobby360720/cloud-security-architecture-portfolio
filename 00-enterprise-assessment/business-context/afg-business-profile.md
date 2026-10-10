# AFG Enterprises — Business and Customer Profile

## 1. Company Overview

**AFG Enterprises** is a fictional U.S.-based financial technology company that provides digital payment, treasury, financial-data, and embedded-finance services to businesses and financial institutions.

AFG operates primarily as a **business-to-business (B2B) and business-to-business-to-consumer (B2B2C) fintech provider**.

The company does not operate as a traditional retail bank. Instead, AFG provides technology platforms and financial services that allow other organizations to process transactions, integrate financial capabilities into their applications, manage business payments, and consume financial data.

AFG follows an **Azure-first cloud strategy** while maintaining selected legacy systems, SaaS platforms, acquired technologies, and hybrid infrastructure.

The company is also pursuing growth through **strategic acquisitions**, creating an ongoing requirement to integrate new companies, applications, identities, networks, APIs, and data environments into the AFG enterprise architecture.

---

# 2. Primary Business

AFG operates in the:

> **Financial Technology, Payments, and Digital Financial Services industry**

Its core business is providing secure technology platforms that connect:

- businesses;
- banks and financial institutions;
- payment networks;
- consumers;
- financial-data providers;
- software platforms; and
- third-party financial service providers.

AFG generates revenue through transaction fees, platform subscriptions, API usage, managed services, and enterprise contracts.

---

# 3. Core Services

## 3.1 Digital Payments

AFG provides payment-processing services that allow businesses and software platforms to accept and manage electronic payments.

Services include:

- ACH payment processing;
- electronic funds transfers;
- account-to-account payments;
- payment initiation;
- recurring payments;
- payment status tracking;
- payment reconciliation;
- merchant payment integrations; and
- payment APIs.

AFG may rely on banking and payment-network partners for portions of transaction settlement while providing the technology and orchestration layer.

---

## 3.2 Business Payments and Treasury Services

AFG provides treasury and payment-management capabilities for commercial customers.

Services include:

- accounts payable automation;
- vendor payment management;
- cash-position reporting;
- transaction reconciliation;
- payment approval workflows;
- financial reporting;
- treasury dashboards; and
- ERP/accounting integrations.

Typical customers include mid-market and enterprise organizations managing large volumes of financial transactions.

---

## 3.3 Embedded Finance and Financial APIs

AFG provides APIs that allow software companies and enterprise customers to incorporate financial capabilities directly into their applications.

Example APIs include:

- payment initiation;
- transaction status;
- account verification;
- account information;
- financial-data retrieval;
- customer verification;
- payment history; and
- reporting.

AFG maintains an enterprise API platform to control:

- API authentication;
- authorization;
- rate limiting;
- API lifecycle management;
- application onboarding;
- threat protection;
- observability; and
- partner integrations.

This capability provides the business justification for the portfolio's **Kong API Gateway / API management architecture**.

---

## 3.4 Financial Data and Analytics

AFG provides financial-data services that help customers analyze transactions and financial activity.

Capabilities include:

- transaction analytics;
- financial dashboards;
- payment reporting;
- fraud indicators;
- reconciliation analytics;
- operational reporting;
- customer financial insights; and
- API-based data delivery.

AFG processes data from internal applications, customers, banking partners, payment processors, and external financial-data providers.

---

## 3.5 Risk and Fraud Services

AFG provides technology that assists customers with identifying suspicious financial activity and managing transaction risk.

Capabilities may include:

- transaction monitoring;
- fraud scoring;
- behavioral analytics;
- payment-risk indicators;
- suspicious-activity alerts;
- account-risk analysis; and
- machine-learning-assisted fraud detection.

These capabilities create legitimate architecture requirements around:

- machine learning;
- AI security;
- data governance;
- model access;
- sensitive financial data;
- privileged identities; and
- security monitoring.

---

## 3.6 Enterprise Integration Services

Large customers can integrate AFG services with:

- ERP systems;
- accounting platforms;
- banking systems;
- SaaS applications;
- payment processors;
- internal applications; and
- third-party financial platforms.

Integration methods include:

- REST APIs;
- event-driven messaging;
- managed file transfers;
- webhooks;
- application connectors; and
- batch processing.

This creates realistic security requirements for:

- API security;
- workload identities;
- certificates and secrets;
- service principals;
- managed identities;
- network segmentation;
- private connectivity; and
- third-party risk management.

---

# 4. Customer Base

AFG primarily serves organizations rather than individual retail consumers.

## Primary Customer Segments

### Mid-Market Businesses

Organizations that need payment automation, financial integrations, and treasury capabilities but do not want to develop their own financial infrastructure.

Examples include:

- professional-services firms;
- healthcare organizations;
- logistics companies;
- retailers;
- property-management companies;
- manufacturers; and
- technology companies.

---

### Large Enterprises

Enterprise customers use AFG to integrate payment and financial capabilities into complex corporate environments.

Requirements from these customers frequently include:

- SSO;
- enterprise APIs;
- audit logging;
- contractual security requirements;
- data residency;
- regulatory reporting;
- business continuity;
- SLA commitments; and
- advanced identity federation.

---

### Banks and Credit Unions

Regional banks, community banks, credit unions, and other financial institutions may consume AFG technology rather than building equivalent platforms internally.

AFG may provide these organizations with:

- payment APIs;
- data services;
- financial integrations;
- fraud capabilities;
- customer-facing financial technology; and
- white-label services.

---

### Fintech and Software Companies

Software companies use AFG APIs to embed financial functionality into their own products.

Examples include:

- accounting software;
- property-management platforms;
- vertical SaaS providers;
- payroll applications;
- financial-management platforms; and
- industry-specific business applications.

These customers represent an important **B2B2C** segment because consumers may ultimately interact with AFG services through another company's application.

---

### Strategic Partners

AFG also integrates with organizations that are not necessarily direct customers, including:

- banks;
- card networks;
- payment processors;
- identity-verification providers;
- credit bureaus;
- financial-data providers;
- cloud providers;
- SaaS vendors; and
- regulatory/compliance service providers.

These relationships introduce significant third-party and supply-chain security requirements.

---

# 5. End Consumers

AFG does not primarily market directly to consumers.

However, consumers may indirectly interact with AFG technology when they:

- make payments;
- receive payments;
- connect bank accounts;
- authorize transactions;
- use applications powered by AFG APIs; or
- interact with a financial institution using AFG technology.

AFG therefore processes potentially sensitive consumer information even when the consumer is not an AFG customer.

---

# 6. Revenue Model

AFG earns revenue through a combination of:

| Revenue Source | Description |
|---|---|
| Transaction Fees | Fee charged for processing financial transactions |
| SaaS Subscriptions | Monthly or annual access to AFG platforms |
| API Consumption | Usage-based pricing for financial APIs |
| Enterprise Contracts | Negotiated agreements with large customers |
| Platform Licensing | Financial capabilities licensed to partners |
| Implementation Services | Integration and onboarding services |
| Managed Services | Operational support and managed financial technology |

This creates both **high-volume transactional workloads** and **recurring SaaS revenue**, making service availability and cybersecurity directly connected to business performance.

---

# 7. Geographic Scope

AFG is headquartered in the United States and initially operates primarily within the U.S. market.

The company supports customers across multiple U.S. regions and is evaluating selective international expansion.

This allows the architecture to initially focus on U.S. requirements while leaving room for future requirements involving:

- GDPR;
- international data residency;
- cross-border data transfers; and
- multinational identity architecture.

---

# 8. Growth Strategy

AFG uses three primary growth strategies:

### Organic Product Growth

Expand the capabilities of the existing financial platform.

### Strategic Partnerships

Integrate AFG platforms with banks, fintech companies, software vendors, and financial-data providers.

### Mergers and Acquisitions

Acquire smaller fintech and financial-technology companies.

Acquisitions may initially retain their existing technologies, including:

- AWS;
- Azure;
- SaaS platforms;
- Okta;
- Microsoft Entra ID;
- independent Active Directory environments;
- legacy applications; and
- separate security tooling.

This creates an intentional **multi-identity and limited multi-cloud architecture challenge**.

AFG's long-term strategy is not necessarily to immediately eliminate acquired technology. Instead, the company establishes enterprise security standards and determines whether each acquired capability should be:

1. integrated;
2. migrated;
3. modernized;
4. retained temporarily; or
5. retired.

---

# 9. Enterprise Technology Profile

AFG should be modeled as approximately:

- **3,500–5,000 employees**;
- primarily U.S.-based;
- multiple offices;
- hybrid workforce;
- several acquired business units;
- Azure as the strategic cloud platform;
- Microsoft 365 as the primary productivity platform;
- Microsoft Entra ID as the primary enterprise identity platform;
- Okta retained or introduced where appropriate for acquired companies and customer/partner identity scenarios;
- legacy on-premises infrastructure;
- SaaS-heavy business operations;
- customer-facing APIs;
- highly sensitive financial and identity data; and
- a growing DevSecOps and platform-engineering capability.

---

# 10. Business-Critical Assets

AFG's most important technology assets include:

### Tier 0 — Enterprise Control Plane

- Microsoft Entra ID;
- privileged identities;
- Azure management groups and subscriptions;
- CI/CD platforms;
- secrets and key-management systems;
- enterprise networking;
- security monitoring infrastructure.

### Tier 1 — Revenue-Critical Platforms

- payment-processing platforms;
- customer-facing APIs;
- transaction systems;
- banking integrations;
- financial-data platforms;
- authentication services.

### Tier 2 — Business Operations

- ERP;
- CRM;
- collaboration platforms;
- HR systems;
- internal applications;
- analytics platforms.

---

# 11. Primary Business Risks

Because AFG is a financial technology company, its major enterprise risks include:

1. unauthorized financial transactions;
2. compromise of privileged identities;
3. customer financial-data exposure;
4. API compromise;
5. payment-service outages;
6. ransomware;
7. fraud;
8. third-party compromise;
9. cloud misconfiguration;
10. regulatory noncompliance;
11. acquisition-related security gaps;
12. compromised workload identities;
13. supply-chain attacks;
14. insider threats; and
15. misuse of AI or sensitive information by AI systems.

These risks drive the security architecture developed throughout the AFG portfolio.

---

# 12. Business Architecture Statement

> **AFG Enterprises is an acquisition-oriented financial technology company providing digital payments, treasury services, financial-data platforms, risk services, and embedded-finance APIs to businesses, financial institutions, and software companies. AFG operates an Azure-first hybrid enterprise environment while integrating acquired technologies and supporting highly regulated, availability-sensitive financial workloads.**

---

# 13. Architecture Implications

The AFG business model requires the enterprise architecture to support:

- Zero Trust;
- strong identity governance;
- customer and partner federation;
- privileged access management;
- multi-IdP integration;
- API security;
- workload identity security;
- secure cloud landing zones;
- network segmentation;
- sensitive-data protection;
- cryptographic key management;
- security monitoring and incident response;
- DevSecOps;
- software supply-chain security;
- AI governance;
- third-party risk management;
- resilient financial workloads;
- disaster recovery;
- merger and acquisition integration; and
- regulatory compliance.

These requirements should drive architecture decisions rather than technology being introduced solely for demonstration purposes.