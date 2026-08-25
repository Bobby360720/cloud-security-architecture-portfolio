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

  -----------------------------------------------------------------------
  ID                      Finding                 Severity
  ----------------------- ----------------------- -----------------------
  NET-01                  Public exposure is not  High
                          consistently governed   

  NET-02                  Private endpoint        High
                          adoption varies by      
                          workload                

  NET-03                  NSG rule ownership and  Medium-High
                          normalization require   
                          improvement             

  NET-04                  DNS governance differs  Medium
                          between legacy and      
                          modern workloads        

  NET-05                  Egress standards are    High
                          incomplete              

  NET-06                  Legacy network patterns High
                          do not fully align with 
                          target segmentation     
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
