# Phase 00 — Terraform & CI/CD Bootstrap

## Status

**Implemented — Bootstrap v1**

This phase establishes the foundational Terraform state management and CI/CD capabilities used by the Cloud Security Architecture Portfolio.

The bootstrap exists before the broader Azure architecture because the environment needs a secure and repeatable deployment foundation before management groups, governance controls, networking, identity, security operations, and workloads are introduced.

---

## Purpose

The bootstrap answers a foundational architecture question:

> **How will infrastructure be securely deployed, tracked, and validated before the rest of the cloud platform exists?**

Terraform requires persistent state to understand the relationship between infrastructure defined in code and resources deployed in Azure.

Using only local Terraform state would create several problems:

- State would depend on a single engineering workstation.
- CI/CD systems would not have access to the authoritative state.
- Collaboration would become difficult.
- State could be lost or accidentally overwritten.
- Automated infrastructure validation would be limited.
- Local credentials could become part of the deployment dependency.

The bootstrap therefore establishes remote Terraform state in Azure and allows Azure DevOps to access Azure through workload identity federation.

---

## Architecture

The bootstrap architecture consists of four primary components:

```text
GitHub
   |
   | Source Control
   v
Azure DevOps
   |
   | Workload Identity Federation
   v
Microsoft Entra ID
   |
   | Azure RBAC
   v
Azure Subscription
sub-management-01
   |
   +-- rg-tfstate-01
          |
          +-- Azure Storage Account
                  |
                  +-- Blob Container: tfstate
                          |
                          +-- bootstrap.tfstate
```

### GitHub

GitHub is the source-control system for the portfolio.

The repository contains:

- Terraform configuration
- Architecture documentation
- CI/CD pipeline definitions
- Architectural decisions
- Assessment artifacts
- Engineering evidence

Environment-specific backend configuration and Terraform state are excluded from source control.

### Azure DevOps

Azure DevOps provides the CI/CD execution environment.

The current pipeline performs:

1. Repository checkout
2. Terraform installation
3. Terraform formatting validation
4. Azure authentication
5. Remote backend initialization
6. Terraform configuration validation
7. Terraform plan generation

The current CI pipeline does **not automatically apply infrastructure changes**.

This intentionally separates infrastructure validation from deployment.

### Microsoft Entra ID

Azure DevOps authenticates to Azure using **Workload Identity Federation (WIF)**.

The Azure DevOps service connection is:

`sc-azure-sub-management-01-wif`

Workload identity federation was selected instead of a client secret so the pipeline does not depend on a long-lived application credential.

The trust relationship is:

```text
Azure DevOps Pipeline
        |
        | OIDC Token
        v
Microsoft Entra ID
        |
        | Federated Trust
        v
Service Principal
        |
        | Azure RBAC
        v
Azure Resources
```

### Azure Storage

Terraform state is stored remotely in Azure Storage.

Bootstrap state architecture:

```text
Subscription:
sub-management-01

Resource Group:
rg-tfstate-01

Storage Account:
Environment-specific name

Blob Container:
tfstate

State Object:
bootstrap.tfstate
```

The storage account name is intentionally treated as environment-specific configuration rather than being published in the repository.

---

## Terraform Bootstrap Resources

The bootstrap Terraform configuration creates and manages:

```text
random_string.storage_suffix

azurerm_resource_group.terraform_state

azurerm_storage_account.terraform_state

azurerm_storage_container.terraform_state
```

The random suffix allows the Azure Storage account to satisfy Azure's globally unique storage-account naming requirement.

The Terraform outputs expose:

```text
resource_group_name
storage_account_name
container_name
```

---

## Remote State

Terraform initially used local state because the Azure Storage backend did not yet exist.

This creates a bootstrap dependency:

```text
Terraform needs remote state
        |
        v
Remote state requires Azure Storage
        |
        v
Azure Storage must first be created by Terraform
```

The dependency was resolved using a two-stage bootstrap process.

### Stage 1 — Local Bootstrap

Terraform initially created the state infrastructure while using local state.

```text
Beehive
   |
   | Terraform + Local State
   v
Azure
   |
   +-- rg-tfstate-01
          |
          +-- Storage Account
                  |
                  +-- tfstate
```

### Stage 2 — State Migration

After the Azure Storage backend existed, Terraform state was migrated from the local backend to Azure Storage.

```text
Local terraform.tfstate
        |
        | terraform init -migrate-state
        v
Azure Storage
        |
        +-- tfstate
              |
              +-- bootstrap.tfstate
```

After migration, Azure Storage became the authoritative location for the bootstrap Terraform state.

---

## State Access Control

Remote Terraform state is protected using Microsoft Entra authentication and Azure RBAC.

Two identities currently require state access.

### Engineering Identity

The engineering identity used from the Beehive development environment requires Blob data-plane access to perform Terraform operations against the remote backend.

### Azure DevOps Identity

The Azure DevOps workload identity also requires Blob data-plane access to the Terraform state container.

The service principal is assigned:

**Storage Blob Data Contributor**

at the appropriate state storage scope.

This allows Terraform to access the Blob state while avoiding the use of storage account access keys in the CI/CD workflow.

---

## Backend Configuration

Environment-specific backend configuration is intentionally excluded from the public repository.

The repository `.gitignore` includes:

```gitignore
**/backend.tf
```

Terraform state and plan files are also excluded from source control.

Examples include:

```gitignore
*.tfstate
*.tfstate.*
*.tfplan
tfplan
```

This separates:

```text
Reusable Terraform Configuration
            |
            +---- GitHub

Environment-Specific Backend Configuration
            |
            +---- Local / CI Environment

Terraform State
            |
            +---- Azure Storage
```

A later iteration may move toward partial backend configuration where the repository defines the AzureRM backend type while environment-specific backend values are injected during CI/CD initialization.

---

## Engineering Workflow

Infrastructure changes follow the workflow:

```text
Write
  |
  v
Format
  |
  v
Initialize
  |
  v
Validate
  |
  v
Plan
  |
  v
Inspect
  |
  v
Apply
  |
  v
Verify
  |
  v
Document
```

Each step serves a different purpose.

| Stage | Purpose |
|---|---|
| Write | Define the desired infrastructure |
| Format | Maintain consistent Terraform formatting |
| Initialize | Load providers and configure the backend |
| Validate | Confirm Terraform configuration validity |
| Plan | Calculate proposed infrastructure changes |
| Inspect | Human review of proposed changes |
| Apply | Execute approved infrastructure changes |
| Verify | Confirm deployed state matches intent |
| Document | Capture architecture, decisions, and evidence |

A successful Terraform plan does not by itself prove that the proposed architecture is correct.

The **Inspect** stage remains a deliberate human architecture and change-review gate.

---

## CI Validation

The Azure DevOps pipeline validates the Terraform configuration using an ephemeral Microsoft-hosted build agent.

The pipeline authenticates to Azure through WIF and initializes the same Azure Storage backend used by the engineering environment.

This validates the complete trust path:

```text
GitHub
   |
   v
Azure DevOps
   |
   v
Workload Identity Federation
   |
   v
Microsoft Entra ID
   |
   v
Azure RBAC
   |
   v
Terraform Remote State
   |
   v
Azure Infrastructure
```

Following state migration, the pipeline can independently read the remote state and compare the Terraform configuration against the deployed Azure environment.

A successful no-change plan demonstrates that:

- The CI runner can authenticate to Azure.
- WIF is functioning.
- The service principal can access Terraform state.
- Terraform can initialize the remote backend.
- The migrated state is readable outside the original engineering host.
- Terraform configuration, state, and deployed bootstrap resources are synchronized.

---

## Security Decisions

### Workload Identity Federation Over Client Secrets

**Decision:** Use Azure DevOps workload identity federation.

**Reasoning:** Long-lived client secrets introduce credential lifecycle, storage, rotation, and leakage risks.

WIF allows Azure DevOps to obtain short-lived federated credentials through an established trust relationship.

---

### Remote State Over Local State

**Decision:** Store authoritative Terraform state in Azure Storage.

**Reasoning:** Local state creates workstation dependency and makes CI/CD and collaboration difficult.

Remote state establishes a centralized state location that can be accessed by authorized engineering and automation identities.

---

### RBAC Over Storage Account Keys

**Decision:** Use Microsoft Entra authentication and Azure RBAC for state access.

**Reasoning:** Storage account keys are broad, long-lived credentials. Identity-based authorization provides stronger control over which principals can access Terraform state.

---

### Plan Before Apply

**Decision:** CI currently performs planning without automatic deployment.

**Reasoning:** Infrastructure changes should be inspectable before execution.

Future iterations will introduce a controlled deployment workflow where the exact reviewed Terraform plan can be promoted through an approval gate before Apply.

---

## Current Limitations

Bootstrap v1 intentionally does not solve every CI/CD requirement.

Current limitations include:

- Terraform Apply is not yet performed through Azure DevOps.
- Terraform plan artifacts are not yet promoted between Plan and Apply stages.
- Deployment approval gates have not yet been implemented.
- Backend configuration is currently environment-specific.
- The current pipeline uses a Microsoft-hosted agent.
- Broader landing-zone resources have not yet been introduced.

These are deliberate maturity steps rather than hidden implementation gaps.

---

## Planned Evolution

The CI/CD architecture will evolve toward:

```text
Pull Request
     |
     v
Format / Validate
     |
     v
Terraform Plan
     |
     v
Publish Exact Plan Artifact
     |
     v
Human Approval
     |
     v
Apply Approved Plan
     |
     v
Post-Deployment Verification
```

The important design requirement is that the plan being applied should be the **same plan that was reviewed and approved**, rather than generating an unrelated plan after approval.

---

## Bootstrap v1 Completion Criteria

Bootstrap v1 is complete.

- [x] Azure management subscription established
- [x] Terraform bootstrap resources deployed
- [x] Azure Storage remote state backend established
- [x] Local Terraform state migrated to Azure Storage
- [x] Engineering identity authorized for remote state
- [x] Azure DevOps workload identity authorized for remote state
- [x] Azure DevOps authentication implemented using WIF
- [x] Terraform formatting validation implemented
- [x] Terraform validation implemented
- [x] Azure remote backend initialization validated through CI
- [x] Terraform Plan executed against remote state
- [x] Terraform configuration, state, and deployed infrastructure verified as synchronized
- [x] Terraform state and environment-specific backend configuration excluded from source control

### Future CI/CD Maturity

The following capabilities are intentionally deferred:

- Publish the exact Terraform plan as a pipeline artifact
- Introduce approval-controlled deployment stages
- Apply the exact reviewed and approved Terraform plan
- Add post-deployment verification
- Expand reusable CI/CD patterns for subsequent architecture phases

These capabilities will be introduced when the portfolio requires them rather than expanding the bootstrap beyond its architectural purpose.
---

## Next Phase

With the engineering foundation established, the portfolio can proceed into the Azure architecture itself.

The next major architecture phase focuses on:

**Azure Landing Zone and enterprise hierarchy**

including:

- Management group architecture
- Subscription organization
- Platform boundaries
- Workload placement
- Governance inheritance
- Current-state architecture reproduction
- Identification of architectural debt

The goal is not to immediately create an idealized Azure environment.

The portfolio first reproduces and documents the intended enterprise current state so that later architectural changes can be tied to identified problems, explicit decisions, and measurable improvements.