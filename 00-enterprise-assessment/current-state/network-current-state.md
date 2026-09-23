# Network Current State

## Overview

AFG uses hybrid connectivity and a developing hub-and-spoke Azure
network model. Newer workloads increasingly use private connectivity,
while legacy and independently deployed workloads contain inconsistent
exposure patterns.

## Current Capabilities

-   ExpressRoute connectivity;
-   hub-and-spoke VNets;
-   Azure Firewall;
-   NSGs;
-   Application Gateway/load balancing;
-   private endpoints;
-   private DNS zones;
-   centralized connectivity subscription.

## Findings

## Findings

| ID | Finding | Severity |
|---|---|---|
| NET-01 | Public exposure is not consistently governed | High |
| NET-02 | Private endpoint adoption varies by workload | High |
| NET-03 | NSG rule ownership and normalization require improvement | Medium-High |
| NET-04 | DNS governance differs between legacy and modern workloads | Medium |
| NET-05 | Egress standards are incomplete | High |
| NET-06 | Legacy network patterns do not fully align with target segmentation | High |
  -----------------------------------------------------------------------

## Target Direction

Phase 4 will establish:

-   private access by default for appropriate PaaS services;
-   documented public-access exceptions;
-   consistent segmentation;
-   standardized DNS;
-   deliberate ingress/egress paths;
-   centralized inspection where justified;
-   network controls deployed and validated through repeatable patterns.
