# Phase 2 — Cloud Governance Validation Evidence

**AFG Enterprises | Issue #29 — P02-08**
**Control:** GR-02 — Azure Storage Public Network Access
**Control framework mapping:** NET-01
**Traceability:** R-004 → SEC-004 → TR-008 → NET-01 → GR-02
**Validation period:** November 5–6, 2026
**Evidence status:** Three control tests validated; final cleanup verification pending

## 1. Validation Summary

| Test ID | Validation method | Observed result | Status |
|---|---|---|---|
| P02-08-GR02-AUDIT-01 | Azure Policy compliance assessment | NonCompliant | PASS |
| P02-08-GR02-OPA-01 | OPA/Rego unit tests and Terraform plan evaluation | 7/7 tests passed; compliant plan produced no violations | PASS |
| P02-08-GR02-DENY-01 | Azure Policy preventive enforcement | RequestDisallowedByPolicy | PASS |

These tests demonstrate detection of an existing noncompliant resource, local pre-deployment policy evaluation, and Azure-enforced prevention of a noncompliant resource creation request.

The tests do not establish enterprise-wide enforcement or management-group inheritance.

---

## 2. P02-08-GR02-AUDIT-01 — Azure Policy Audit Detection

**Test date:** November 5, 2026
**Evidence classification:** Validated Azure compliance evaluation

**Configuration**

- Policy: Storage accounts should disable public network access
- Definition ID: `b2982f36-99f2-4db5-8eff-283140c09693`
- Policy version previously inspected: `1.1.0`
- Assignment: `afg-gr02-storage-audit`
- Scope: Sandbox brownfield resource group `rg-afg-bf-6nxews`
- Resource: `stafgbf6nxews`
- Policy effect: Audit

**Expected result:** NonCompliant

**Observed result:** NonCompliant

**Evaluation timestamp:** `2026-11-05T10:55:28.673585+00:00`

**Outcome: PASS**

Azure Policy identified the existing Storage account as noncompliant with the GR-02 public network access requirement.

**Limitations**

This test demonstrates audit detection only. It does not prove remediation, deny enforcement, or management-group inheritance. Preventive enforcement was evaluated separately in DENY-01.

---

## 3. P02-08-GR02-OPA-01 — OPA/Rego Pre-Deployment Validation

**Validation date:** November 6, 2026
**Evidence classification:** Validated local policy execution
**Environment:** `~/projects/opa-rego-lab`
**Terraform version in saved plan:** `1.17.1`

### Unit Test Results

| Test scenario | Observed result |
|---|---|
| Public network access enabled | PASS — violation detected |
| Private Storage configuration | PASS — allowed |
| Missing public access setting | PASS — violation detected |
| Anonymous blob access enabled | PASS — violation detected |
| Delete-only operation | PASS — allowed |
| Unknown public network access | PASS — violation detected |
| Unknown anonymous blob access | PASS — violation detected |

**Unit test outcome: 7/7 PASS**

### Terraform Plan Evaluation

**Planned resource:** `azurerm_storage_account.lab`
**Planned action:** `create`

Validated planned properties:

- `public_network_access_enabled = false`
- `allow_nested_items_to_be_public = false`
- Neither evaluated security setting was marked unknown.

**Observed OPA output:**

```json
[]
```

The Rego policy identified no violations in the inspected compliant Terraform plan.

A separate noncompliant JSON fixture generated two violation messages, demonstrating detection of public network access enabled and anonymous blob access not explicitly disabled.

**Outcome: PASS**

### Limitations

- Validation was executed locally.
- CI/CD pipeline enforcement was not demonstrated.
- No Azure resources were created or modified through these OPA evaluations.
- Results confirm behavior for the tested scenarios, not exhaustive policy correctness.
- The anonymous blob access requirement is an additional Rego guardrail; the selected Azure built-in GR-02 policy evaluates public network access.

---

## 4. P02-08-GR02-DENY-01 — Azure Policy Preventive Enforcement

**Validation date:** November 6, 2026
**Evidence classification:** Validated Azure preventive control execution
**Environment:** Sandbox subscription, isolated resource group `rg-afg-policy-deny-test`

### Test Objective

Verify that Azure Policy rejects the creation of an Azure Storage account when public network access is enabled.

### Policy Configuration

- Policy: Storage accounts should disable public network access
- Definition ID: `b2982f36-99f2-4db5-8eff-283140c09693`
- Policy version: `1.1.0`
- Assignment: `afg-gr02-storage-deny`
- Scope: `rg-afg-policy-deny-test`
- Effect: `Deny`
- Enforcement mode: `Default`

### Test Execution

**Attempted resource:** `afgdeny1793984107`

**Requested configuration:** `publicNetworkAccess = Enabled`

**Observed Azure response:**

```text
(RequestDisallowedByPolicy)
Resource 'afgdeny1793984107' was disallowed by policy.
```

Azure Policy evaluation details confirmed:

- Resource type matched `Microsoft.Storage/storageAccounts`.
- Requested public network access was `Enabled`.
- The policy required `Disabled` or `SecuredByPerimeter`.
- The assignment applied `Deny`.
- No policy exemptions were reported.

**Outcome: PASS — Noncompliant deployment rejected**

### Resource Verification and Cleanup

After the denied deployment:

- Storage account inventory returned no resources.
- Resource inventory returned no resources.
- The temporary policy assignment deletion command completed without a reported error.
- The temporary resource group deletion command completed without a reported error.

**Cleanup status:** Deletion commands executed; independent confirmation of final resource-group deletion remains pending.

### Limitations

- Deny enforcement was validated at isolated resource-group scope.
- Management-group policy inheritance was not tested.
- Enterprise-wide assignment and enforcement were not tested.
- Successful creation of a compliant Azure Storage resource was not tested.
- The result does not demonstrate remediation of an existing noncompliant resource.

---

## 5. Architectural Assessment

The validation provides representative evidence for three complementary governance capabilities:

**Detect:** Azure Policy Audit identifies an existing noncompliant configuration.

**Validate:** OPA/Rego evaluates planned infrastructure configurations against security rules before deployment.

**Prevent:** Azure Policy Deny rejects a noncompliant resource creation request at the Azure control plane.

Together, these tests support the GR-02 security architecture design and establish a traceable relationship between risk, requirements, controls, and observed results.

## 6. Remaining Validation Boundaries

The following capabilities remain outside the validated scope:

- Management-group policy inheritance
- Enterprise-wide policy enforcement
- CI/CD pipeline deployment blocking
- Automated remediation
- Exception and risk-acceptance workflow execution
- Compliant Azure deployment validation

These are not claimed as implemented or validated.

## 7. Conclusion

**GR-02 representative validation: PASS**

The available evidence demonstrates that Azure Policy detected an existing noncompliant Storage account, OPA/Rego evaluated representative Terraform configurations, and Azure Policy rejected a deliberately noncompliant Storage account creation request.

The evidence supports a limited but defensible preventive and detective governance demonstration for AFG Enterprises.

Final cleanup confirmation and repository commit remain outstanding.


### P02-08-GR02-ALLOW-01 — Compliant Azure Storage Deployment

**Validation date:** November 6, 2026  
**Control:** GR-02 / NET-01  
**Evidence classification:** Validated Azure resource deployment  
**Environment:** Sandbox subscription, isolated resource group `rg-afg-policy-allow-test`

**Objective:** Confirm that Azure Policy permits the deployment of a compliant Storage account while the GR-02 Deny assignment is active.

**Policy configuration:**
- Policy: Storage accounts should disable public network access
- Assignment: `afg-gr02-storage-allow-test`
- Effect: `Deny`
- Enforcement mode: `Default`
- Scope: Isolated resource group

**Observed resource configuration:**
- Storage account: `afgallow1793992987`
- Provisioning state: `Succeeded`
- Public network access: `Disabled`
- Anonymous blob access: `false`
- Minimum TLS version: `TLS1_2`

**Test outcome: PASS**

Azure successfully provisioned the compliant Storage account within the scope of the enforced Deny policy assignment.

**Limitations:** This test demonstrates successful resource creation under the configured policy assignment. It does not independently confirm a completed Azure Policy compliance evaluation, management-group inheritance, or CI/CD enforcement.

**Cleanup status:** Complete.
