# ADR-003 — Brownfield Subscription Transition Strategy

## Status

Accepted

## Date

2026-10-15

## Context

AFG's Azure Landing Zone is modeled and implemented as a brownfield
transformation rather than a greenfield deployment.

Phase 0 reconstructed existing management groups and representative
subscriptions before Phase 1 introduced the target-state architecture.

During Phase 1, differences were identified between deployed Azure state,
Terraform configuration, and Terraform state. Existing subscriptions also
contained different combinations of active workloads, legacy resources,
policies, RBAC assignments, resource locks, and lifecycle states.

A transition strategy was required that could modernize the hierarchy without
unnecessarily rebuilding working resources or treating all existing
subscriptions as equivalent.

## Decision Drivers

The transition strategy was driven by:

- preservation of working Azure resources;
- reduction of destructive brownfield changes;
- accurate reconciliation of deployed state before modification;
- business criticality and workload dependency analysis;
- subscription ownership and lifecycle;
- Azure Policy and RBAC dependencies;
- custom-role assignable scopes;
- resource locks;
- migration readiness;
- rollback and validation requirements.

## Options Considered

### Option 1 — Rebuild the Environment as a Greenfield Landing Zone

Create new management groups and subscriptions and rebuild existing workloads
into the target structure.

This option was rejected because it would introduce unnecessary cost,
migration risk, and implementation effort solely to conform to the target
architecture.

### Option 2 — Move Existing Subscriptions Immediately Based on Their Names

Place existing subscriptions according to names such as `Connectivity`,
`Security`, or `Web Apps`.

This option was rejected because subscription names did not reliably describe
their actual workloads or lifecycle state.

For example, the brownfield `Connectivity` subscription contained Resource
Mover, Azure Site Recovery, compute, networking, application-hosting,
monitoring, and EDM development resources and therefore did not represent the
target shared Connectivity platform boundary.

### Option 3 — Reconcile, Classify, and Transition Incrementally

Reconcile Azure state, Terraform configuration, and Terraform state first,
then classify subscriptions by actual use case and move them through controlled
migration waves.

This option was selected.

## Decision

AFG will use an incremental brownfield transition strategy.

Before modifying a Terraform-managed Azure resource:

1. inspect the deployed Azure state;
2. compare deployed state with Terraform configuration;
3. compare Terraform configuration with Terraform state;
4. reconcile state differences before introducing architecture changes;
5. identify policy, RBAC, custom-role, networking, recovery, and lock dependencies;
6. determine target placement based on actual workload purpose and lifecycle;
7. review the Terraform plan for unexpected destruction or replacement;
8. apply only reviewed changes;
9. independently validate the resulting Azure state;
10. retain evidence distinguishing modeled architecture from validated implementation.

Existing management-group identifiers and working resources should be
preserved where practical.

Subscription migrations will use a risk- and dependency-based sequence rather
than an arbitrary fixed order.

The general migration sequence is:

```text
Architecture preparation
        ↓
Core platform validation
        ↓
Low-risk / representative workloads
        ↓
Standard production workloads
        ↓
Legacy and exception-heavy workloads
        ↓
Controlled retirement