# AFG representative brownfield Terraform lab

This **temporary, representative** Azure workload lab is separate from the persistent Phase 0 bootstrap and management-group configurations. It does not deploy or claim to reproduce all 12 logical subscriptions or the modeled enterprise inventory.

## Safety and cost

- **No Terraform backend is declared here.** By default Terraform uses **local state**, which includes secrets (e.g. Function storage keys). Never commit state. Before team use or important deployments, configure a separate remote state key in your existing `tfstate` container, e.g. `brownfield.tfstate`, using your existing Azure AD CLI authentication. Do not reuse `bootstrap.tfstate` or the enterprise assessment state key.
- Default switches: no VM, no public IP, no Log Analytics workspace, no policy. Function App is deployed but **contains no application code**; a working HTTP function must be published separately.
- An empty Log Analytics workspace does not ingest logs. Add diagnostics and DCRs later, with a budget and retention plan. `daily_quota_gb` is a safeguard, not a billing cap.
- Storage and Function App use an access key for host storage in this small lab. Replacing it with identity-based host storage is a future identity modernization exercise.
- Key Vault soft deletion can retain the name after destroy; purge protection is disabled **only for this disposable lab**. Never store real secrets or sensitive data.
- Optional VM has no public IP by default. If public IP is enabled, restrict SSH to your operator /32. A private VM requires an existing private access path; this configuration does not provision a Bastion or VPN.
- Public IP, VM disks, storage, Key Vault operations, Function executions, monitoring ingestion and egress may incur charges. Azure budgets alert but do not stop charges. Use Azure Pricing Calculator and Cost Management for current regional estimates.
- Do not use `terraform destroy` against the persistent bootstrap or enterprise assessment folders.

## Deploy

```bash
cd ~/projects/cloud-security-architecture-portfolio
mkdir -p 01-brownfield-lab/terraform
# Copy the ZIP contents into 01-brownfield-lab/terraform
cd 01-brownfield-lab/terraform
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars: set subscription_id and paste `cat ~/.ssh/id_ed25519.pub`
az login
az account set --subscription YOUR_LAB_SUBSCRIPTION_ID
terraform init
terraform fmt -check
terraform validate
terraform plan -out=brownfield.tfplan
terraform apply brownfield.tfplan
```

For a short VM exercise, set `deploy_vm = true` and re-plan. Check `Standard_B1s` availability and quota in your region. If a provider requires registration, use `az provider register --namespace Microsoft.Web` etc. only in the intended lab subscription.

## Validate

```bash
terraform state list
terraform output
az resource list --resource-group "$(terraform output -raw resource_group)" --output table
```

## Tear down temporary resources

```bash
terraform plan -destroy -out=destroy.tfplan
terraform apply destroy.tfplan
```

Destroy uses the same backend and variables as apply. Confirm the selected subscription and workspace first. **Do not remove the resource group manually while it is Terraform-managed.** The existing management groups, subscriptions, and remote state storage are not in this configuration.

## Future exercises

- Phase 1: landing-zone placement and subscription vending design.
- Phase 2: tag inheritance, policy assignment and remediation.
- Phase 3: RBAC, workload identity, secret replacement.
- Phase 4: segmentation, private endpoints, DNS; do not deploy expensive Azure Firewall by default.
- Phase 5: diagnostic settings, limited Log Analytics ingestion, detection validation.
- Phase 6+: CI/CD, data protection and application-specific tests.

## Evidence

Track observed Azure outputs separately from the fictional enterprise inventory. Record plan results, control tests, cost and teardown confirmation. No lab deployment or test is claimed by these source files alone.
