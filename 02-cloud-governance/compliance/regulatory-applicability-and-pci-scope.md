# P02-01 — Regulatory Applicability and PCI Scope Baseline

| Attribute | Value |
| --- | --- |
| Enterprise | AFG Enterprises (fictional, modeled) |
| Phase | 2 — Cloud Governance and Security Baseline |
| Related issue | [#22](https://github.com/Bobby360720/cloud-security-architecture-portfolio/issues/22) |
| Status | Proposed architecture baseline; applicability and scope pending validation |
| Evidence classification | Modeled / Not validated |

## 1. Purpose and business scope

This document establishes a **preliminary regulatory applicability and payment-card security scope** for AFG's proposed Azure-first architecture. It identifies modeled business activities, assumptions, candidate PCI DSS system boundaries, existing enterprise requirements, prospective validation evidence, and decisions requiring further review. It is **not** a legal determination, approved architecture decision, PCI DSS assessment, or implementation record.

AFG is modeled as a U.S.-based **B2B/B2B2C financial technology service provider** delivering payment-processing technology, treasury services, financial-data capabilities, and embedded-finance APIs to businesses and regulated financial institutions. AFG is not modeled as a traditional retail bank or direct consumer lender. It maintains an Azure-first hybrid environment, integrates acquired technologies, and depends on banking and payment partners.

**Business drivers:** secure payment processing, transaction integrity, customer trust, reliable partner integrations, and incremental modernization without unnecessary internal cardholder-data handling.

## 2. Modeled payment-processing and data-flow design

### 2.1 Payment-partner tokenization model

AFG proposes an external payment partner that provides hosted card-entry fields or a partner-hosted payment component, receives cardholder data directly, tokenizes card-account references, and protects any PAN it is authorized to retain. **Sensitive authentication data (SAD), including card verification codes, must not be retained after authorization**, subject to the limited issuer/issuing-support exceptions defined by PCI DSS; AFG is not modeled as such an issuer.

AFG's principal Azure payment services are **intended** to receive only partner-issued token references, payment instructions, transaction identifiers, and the minimum necessary financial/customer metadata—not raw PAN or SAD. This exclusion is a **design objective to validate**, not an observed property.

Token design matters: whether a token can be reversed, used to retrieve PAN, or exploited to initiate payments influences risk and scope. Tokenized payment records may still contain protected personal or financial information.

### 2.2 Conceptual payment flow

```text
Customer browser / client application
   |
   | (1) Load partner-hosted capture component
   | (2) Submit PAN / required authentication data DIRECTLY to partner
   v
External payment partner — card capture / tokenization / token vault
   |
   | (3) Return partner-issued payment token to client
   v
Customer browser / client application
   |
   | (4) Submit token + authorized payment instructions (no PAN/SAD)
   v
AFG Azure API Management (APIM)
   | (5) Authenticate, authorize/rate-limit as appropriate, validate request shape
   v
AFG payment orchestration application (compute choice deferred)
   | (6) Validate payer authorization, amount/payee, replay/idempotency and state
   |---------------> Partner processing API: execute authorized payment
   |<--------------- Partner processing API: authorization/status response
   v
AFG tokenized transaction store (data service choice deferred)
   | (7) Retain permitted transaction records and sanitized audit events
   v
Reconciliation / security monitoring (logical functions; deployment deferred)
```

This is a **logical sequence**, not a validated network diagram or selection of App Service, AKS, Azure SQL, Cosmos DB, or a payment vendor. The client-side integration and page/script ownership need review: using hosted fields does **not** by itself prove that merchant/customer pages or connected systems are outside PCI DSS scope.

### 2.3 Architecture assumptions and trust boundaries

- The **external partner** owns and operates its card capture/token vault and controls PAN/SAD handling within its contracted environment; AFG must verify the partner's relevant PCI DSS standing and assigned responsibilities.
- AFG's primary Azure API, backend, database, messaging, telemetry, cache and support workflows are designed **not to receive or retain PAN/SAD**. Sanitized logging, schema validation and data-flow testing are required to verify this assumption; routing and schema checks alone cannot guarantee exclusion.
- APIM, payment orchestration, workload identities, administrative paths, deployment systems, and monitoring may **affect payment account security** and therefore require PCI scoping review despite not intentionally handling PAN.
- Token-use authorization, payment instruction integrity and replay resistance remain AFG responsibilities within the modeled division of duties; the partner's responsibilities must be specified contractually.
- Segmentation claims require validation of actual connectivity and security impact. Separate subscriptions, VNets, NSGs, or private endpoints alone do not establish an out-of-scope determination.
- AFG and the partner have not been selected, deployed, tested, assessed, or formally approved in this fictional portfolio model.

## 3. Preliminary PCI DSS boundaries — v4.0.1 planning reference

The PCI DSS v4.0.1 reference is the portfolio's **planning baseline**, pending confirmation of the applicable version and assessment expectations at the time of formal validation. Classifications below are **candidates**, not determinations by a qualified assessor or payment-program authority.

| System / function | Proposed classification | Scope rationale or question |
| --- | --- | --- |
| Partner-hosted card capture and token vault | External partner CDE | Partner receives PAN/SAD; confirm actual services, evidence and responsibility allocation. |
| Customer-facing payment page / capture integration | Scope assessment required | Ownership of page, scripts, redirects/hosted fields and ability to affect capture security must be evaluated. |
| AFG APIM | Candidate security-impacting / connected system | Routes payment operations, enforces gateway policies; examine actual interfaces and ability to affect account-data security. |
| AFG payment orchestration | Candidate security-impacting / connected system | Sends payment instructions and controls partner integrations; assess exposure and security impact. |
| AFG tokenized transaction storage | Scope assessment required; potential reduction | Determine token reversibility, PAN access, connected systems, and any security impact; tokens are not automatically out of scope. |
| AFG Entra ID, privileged administration and deployment pipelines | Candidate security-impacting systems | Review which identities and tooling administer or alter systems affecting payment account security. |
| Logging, monitoring and reconciliation services | Scope assessment required | Inspect data content, access, connections and security responsibilities. |
| Unrelated corporate workloads | Candidate out of scope | Requires demonstrated isolation and no ability to compromise in-scope security. |

**Validation track:** AFG's service-provider obligations, applicable PCI DSS requirements, evidence method (for example, a service-provider SAQ or QSA-led Report on Compliance where permitted/required), and assessment frequency must be confirmed with the relevant compliance-accepting entity and assessor. Do not assume merchant SAQ A eligibility simply because card capture is outsourced.

## 4. Preliminary regulatory applicability

| Obligation / framework | Preliminary classification | Basis and unresolved determination |
| --- | --- | --- |
| **PCI DSS** | **Modeled applicable — precise scope pending** | AFG provides payment technology potentially affecting account-data security; confirm covered services, systems, responsibilities, requirements and validation route. |
| **GLBA / FTC Safeguards Rule** | **Direct applicability not established** | Determine AFG's actual covered financial activities and regulator; separately capture bank/customer security obligations imposed by contract. Being called a fintech or vendor is not dispositive. |
| **State privacy, data-security and breach-notification laws** | **Potentially applicable; jurisdiction-specific** | Determine applicable states, consumer/resident records, covered information, entity role, statutory thresholds and incident notification duties. Do not presume CCPA/CPRA or NY SHIELD applicability solely from tokenization. |
| **NYDFS 23 NYCRR 500** | Conditional | Determine covered-entity status and contractual flow-downs from regulated customers. |
| **SOX** | Conditional | Determine reporting-entity status and financial-reporting control dependencies. |
| **SEC Regulation S-P** | Conditional | Determine whether AFG is a covered financial institution; distinguish client obligations from AFG obligations. |
| **FCRA** | Conditional | Review activities involving consumer reports and regulated consumer-reporting uses. |
| **EFTA / Regulation E** | Conditional | Review AFG's roles in covered consumer electronic fund transfers. |
| **ECOA / Regulation B** | Conditional | Review whether AFG participates in covered credit activities. |
| **NIST CSF 2.0 / CIS Controls** | Voluntary control-organizing references | They can support control rationales but are **not regulatory obligations**. |

**Applicability rule:** A legal or compliance owner must assess AFG's modeled legal entity, services, data, transaction types, jurisdictions, relevant agreements and regulator before treating a conditional obligation as directly applicable or excluded. A banking partner's obligations are not automatically AFG's statutory obligations, though contracts can impose safeguards.

## 5. Proposed architecture control outcomes

These are **design requirements for assessment**, not new canonical Phase 0 requirement IDs and not proof of PCI DSS compliance.

1. **Card-data minimization:** Design client capture so raw PAN/SAD is supplied to the partner rather than AFG; verify no unintended data ingress or retention in AFG applications, diagnostics or support tooling.
2. **Authentication and authorization:** Enforce least privilege for payment APIs, partner integrations, workload identities and administrative functions. Transaction authorization must be enforced in the application or another authoritative processing component, not merely inferred from an API gateway token.
3. **Transaction integrity:** Validate amounts, beneficiaries, customer authorization, state transitions and partner responses. Use cryptographic request integrity where the threat model or partner protocol warrants it.
4. **Replay and duplicate prevention:** Require idempotent processing and replay controls at an authoritative transaction execution boundary, using the gateway as an additional safeguard where appropriate.
5. **Information protection:** Classify tokens and associated financial/personal metadata, minimize retention, enforce approved encryption in transit/at rest, and use risk-appropriate key management. TLS 1.3 and customer-managed keys are options, **not universal mandates** absent a specific requirement.
6. **Third-party accountability:** Maintain a documented PCI responsibility allocation, contractual security obligations, partner assurance evidence and a periodic review process. Confirm evidence and review cadence with the relevant PCI and contractual expectations.
7. **Auditability and monitoring:** Create appropriately protected payment, access, administration and reconciliation records without exposing PAN/SAD in logs; define retention and investigation responsibilities.
8. **Scope and segmentation assurance:** Review data paths, security-impacting systems, administrative access, network connectivity and segmentation controls. Determine PCI-required testing frequency once scope and applicable service-provider requirements are established. Where PCI DSS Requirement 11.4.6 applies to service-provider segmentation, testing is at least every **six months** and after relevant changes—not just annually.

## 6. Enterprise architecture traceability

The **Phase 0 Enterprise Risk Register**, **Business Requirements**, **Security Requirements**, **Technical Requirements**, and **Traceability Matrix** remain authoritative. The references below show proposed relationships, not new approved requirements or validated risk treatment. SharePoint remains the operational findings/risk tracking system; GitHub remains the architecture baseline.

### 6.1 Business requirements

| ID | Baseline objective | P02-01 relationship |
| --- | --- | --- |
| BR-001 | Scalable cloud governance | Consistent governance expectations for payment-related workloads. |
| BR-002 | Risk reduction without unnecessarily blocking delivery | Outsourced tokenization and risk-based, documented scope decisions. |
| BR-005 | Auditable and explainable architecture decisions | Traceable scope assumptions, deferred decisions and review evidence. |
| BR-009 | Measurable governance effectiveness | Explicit scope/validation evidence and governance measures. |
| BR-010 | Incremental modernization | Payment-partner integration without requiring AFG to build a new internal CDE. |

BR-003 (ownership) and BR-007 (repeatable secure deployment) support later operational implementation; they need not be duplicated in this document.

### 6.2 Enterprise risks and existing security / technical requirements

| Risk | Existing requirement references | P02-01 relevance |
| --- | --- | --- |
| R-001 | SEC-006, SEC-015; TR-001, TR-002 | Governance hierarchy and inherited payment-environment controls. |
| R-002 | SEC-001; TR-006 | Privileged access to payment-related control planes. |
| R-003 | SEC-002, SEC-003; TR-007 | Workload identity and excessive partner/API permissions. |
| R-004 | SEC-004; TR-008, TR-009 | Public exposure and payment-system connectivity/segmentation. |
| R-005 | SEC-005; TR-010 | Security telemetry and investigation capability. |
| R-006 | SEC-006, SEC-007; TR-003, TR-004 | Exception approval, expiry and policy lifecycle. |
| R-007 | SEC-008, SEC-014; TR-012, TR-013 | Auditable configuration changes and secure deployment. |
| R-009 | SEC-010; TR-014 | Data sensitivity and protection controls. |
| R-015 | Existing Phase 0 risk; requirements mapping to confirm | Protection of production-derived payment data in non-production. |

**TR-016** requires safe architecture evidence production without exposing secrets or confidential identifiers. It supports portfolio publication practices; **SEC-014**, not TR-016, is the direct administrative change-auditability requirement. No Phase 0 risk score, finding, requirement ID or assigned delivery phase is changed here.

### 6.3 Payment-specific coverage candidates (not registered requirements)

| Candidate | Control need | Suggested review owner / future phase |
| --- | --- | --- |
| Payment instruction integrity | Authoritative validation of payer, amount, beneficiary and permitted state changes | Payments Engineering / Application Security; application delivery phase to confirm |
| Replay / duplicate execution prevention | Idempotent execution, replay detection and safe retries | Payments Engineering; application delivery phase to confirm |
| Partner responsibility boundaries | AFG/partner responsibility matrix, applicable contractual clauses and assurance evidence | Compliance / Third-Party Risk; governance assessment |
| Card-data exclusion and PCI scope validation | Inspect browser capture, backend/log/queue/cache paths, token characteristics and segmentation | Compliance / Security Architecture; before applicable production approval |

These are **candidate control needs**, not automatically approved `REQ-PAY-*` identifiers. Review against existing SEC/TR statements and apply the established change process before adding canonical IDs. Transaction integrity is a payment-specific scenario partially related to **R-003**, but need not create **R-016** without enterprise risk review.

## 7. Planned validation evidence and ownership

| Planned evidence | Purpose | Provisional functional owner |
| --- | --- | --- |
| Payment data-flow and system inventory | Demonstrate all card-data, token, instruction and administrative paths | Payments Engineering / Security Architecture |
| PCI scoping assessment and component inventory | Determine in-scope, connected/security-impacting, and out-of-scope systems | Compliance / Security Architecture |
| Partner assurance and responsibility matrix | Establish contracted services, controls, gaps and accountable parties | Vendor Risk / Compliance |
| Card-data exclusion tests, including sanitized logs/caches/queues | Detect unintended PAN/SAD ingestion without exposing real payment details | App Security / Payments Engineering |
| Payment API authorization and integrity test results | Verify authorization, data validation, idempotency and replay safeguards | Payments Engineering / App Security |
| Connectivity review and segmentation testing | Validate actual boundary effectiveness where relied upon | Network Security / Compliance |
| Access, configuration and monitoring evidence | Verify least privilege, logging and administrative review | Identity / Security Operations |
| Architecture review and change history | Demonstrate governance decisions and baseline revision history | Security Architecture |

Evidence artifacts are **planned only**. Use synthetic test data and approved redaction to comply with **TR-016**. No partner AoC, test report, signed matrix, or validated deployment is asserted to exist.

## 8. Deferred decisions and completion criteria

| Open decision | Closure input |
| --- | --- |
| Payment partner and integration model | Partner selection, contract, capture/script design and technical interface review |
| PCI DSS boundary and validation method | Actual data flows, service-provider obligations, assessor/compliance-program input |
| PCI requirement-level applicability | Formal mapping to the PCI DSS version and requirements applicable at assessment |
| Direct GLBA / FTC Safeguards Rule coverage | Legal/activity/regulator applicability assessment |
| State and other conditional financial regulations | Jurisdiction, entity-role, data and business-activity analysis |
| Technical implementation choices | Approved payment application, API, storage, identity and network designs in their relevant phases |
| Payment-specific requirements registration | Review of existing enterprise requirements and formal change decision |

**P02-01 can be considered a documented preliminary baseline when** business assumptions, the proposed PCI boundary, regulatory classification, Phase 0 traceability and open decisions are recorded and reviewed against Issue #22's actual acceptance criteria. Formal compliance status, final scoping and implementation validation are **not** claimed as Phase 2 outcomes.

## 9. References (guidance, not validation evidence)

- [PCI SSC — Sensitive authentication data must not be stored after authorization](https://www.pcisecuritystandards.org/faqs/1533/)
- [PCI SSC — PCI DSS scope includes entities that can impact CDE security; assessment requirements determined by compliance programs](https://www.pcisecuritystandards.org/faqs/1574/)
- [FTC — Safeguards Rule applicability depends on financial activities](https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know)
- PCI DSS v4.0.1: detailed requirement applicability and validation requirements to be reviewed with the relevant compliance authority and current official standard.

---

**Evidence statement:** This document is a fictional, modeled enterprise architecture artifact. No implementation, partner selection, approval, legal determination, PCI DSS compliance validation, certification, or measured reduction in residual risk is represented as completed.
