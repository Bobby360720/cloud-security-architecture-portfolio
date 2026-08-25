# Security Operations Current State

## Overview

AFG has a meaningful Microsoft security-operations foundation. The
maturity challenge is consistency and engineering lifecycle rather than
initial tool deployment.

## Current Capabilities

-   Microsoft Sentinel;
-   Microsoft Defender for Cloud;
-   Log Analytics;
-   Azure Monitor;
-   Azure Monitor Agent;
-   Data Collection Rules;
-   analytics and automation rules;
-   security workbooks and watchlists.

## Findings

  -----------------------------------------------------------------------
  ID                      Finding                 Severity
  ----------------------- ----------------------- -----------------------
  SOC-01                  Diagnostic coverage is  High
                          not universal           

  SOC-02                  DCR association is      High
                          inconsistent            

  SOC-03                  Log retention differs   Medium
                          by workspace/use case   

  SOC-04                  Detection ownership is  Medium-High
                          not consistently        
                          documented              

  SOC-05                  Analytics-rule          Medium-High
                          testing/tuning          
                          lifecycle needs         
                          formalization           

  SOC-06                  Defender plan coverage  High
                          varies by               
                          subscription/resource   
                          type                    

  SOC-07                  Findings are not always High
                          mapped to accountable   
                          remediation owners      
  -----------------------------------------------------------------------

## Target Direction

Phase 5 will define:

-   required enterprise telemetry;
-   standard diagnostic settings;
-   AMA/DCR architecture;
-   Sentinel data-source onboarding standards;
-   detection-as-code lifecycle;
-   ownership and escalation;
-   retention requirements;
-   measurable detection and monitoring coverage.
