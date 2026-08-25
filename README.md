# Cloud Security Architecture Portfolio

A portfolio of cloud security architecture projects focused on designing secure, scalable, and governed enterprise cloud environments.

My work focuses primarily on Microsoft Azure and demonstrates how security architecture principles can be translated into practical designs, security controls, infrastructure as code, and operational guardrails.

---

## Architecture Focus

- ☁️ Cloud Security Architecture
- 🔐 Identity & Zero Trust
- 🏛️ Cloud Governance
- ⚙️ DevSecOps & Infrastructure as Code
- 🛡️ Security Operations & Monitoring
- 🤖 AI Security
- 🔄 Security Automation

---

## Featured Architecture Projects

### 01 — Azure Enterprise Security Landing Zone
**Status:** Planned

Enterprise Azure landing zone security architecture incorporating management groups, Azure Policy, identity, network security, Defender for Cloud, centralized monitoring, and governance controls.

**Architecture Areas:**  
Azure | Entra ID | Azure Policy | Defender for Cloud | Zero Trust | IaC

---

### 02 — Enterprise Identity & Zero Trust Architecture
**Status:** Planned

Identity security architecture covering privileged access, RBAC, Conditional Access, workload identities, entitlement management, and least-privilege access.

**Architecture Areas:**  
Entra ID | PIM | RBAC | Conditional Access | Managed Identity | Zero Trust

---

### 03 — Secure Azure DevSecOps Platform
**Status:** In Development

Reference architecture for securely delivering Azure infrastructure and applications through automated CI/CD pipelines.

The project explores infrastructure as code, workload identity federation, secrets management, security validation, policy enforcement, and deployment governance.

**Architecture Areas:**  
Azure DevOps | Bicep | Terraform | CI/CD | Workload Identity | Policy as Code

---

### 04 — Security Monitoring Reference Architecture
**Status:** Planned

Centralized security monitoring architecture integrating cloud and hybrid telemetry with Microsoft Sentinel and Defender.

**Architecture Areas:**  
Microsoft Sentinel | Defender XDR | AMA | DCR | KQL | Azure Monitor

---

### 05 — Secure AI Reference Architecture
**Status:** Planned

Enterprise reference architecture for securely deploying AI workloads while addressing identity, data protection, network isolation, secrets management, governance, and AI-specific threats.

**Architecture Areas:**  
Azure AI | Entra ID | Key Vault | Private Networking | Data Security | AI Security

---

## Architecture Methodology

Projects are developed as architecture case studies rather than standalone technology labs.

Where appropriate, each project documents:

1. **Business Problem**
2. **Architecture Requirements**
3. **Security Requirements**
4. **Threat Model**
5. **Reference Architecture**
6. **Security Controls**
7. **Architecture Decision Records (ADRs)**
8. **Infrastructure as Code**
9. **Security Validation**
10. **Risks & Tradeoffs**
11. **Future-State Design**

---

## Architecture Principles

The portfolio is built around several core principles:

**Secure by Design**  
Security requirements are incorporated during architecture and design rather than added after deployment.

**Zero Trust**  
Explicit verification, least-privilege access, and assumed breach guide identity and access decisions.

**Policy as Code**  
Security and governance requirements should be automated and consistently enforceable.

**Identity First**  
Human and workload identities are treated as primary security boundaries.

**Automation First**  
Repeatable security controls should be implemented through infrastructure as code and automated pipelines whenever practical.

**Defense in Depth**  
Identity, network, application, data, and monitoring controls work together rather than relying on a single security layer.

---

## Technologies

**Cloud & Identity**  
Azure • Microsoft Entra ID • Microsoft 365

**Security**  
Microsoft Defender • Microsoft Sentinel • Azure Policy • Microsoft Purview • Key Vault

**Infrastructure as Code**  
Bicep • Terraform

**DevSecOps**  
Azure DevOps • GitHub • CI/CD

**Automation & Detection**  
PowerShell • Python • KQL

---

## Repository Structure

```text
cloud-security-architecture-portfolio/
│
├── README.md
├── architecture/
├── case-studies/
├── diagrams/
├── threat-models/
├── adr/
└── standards/
