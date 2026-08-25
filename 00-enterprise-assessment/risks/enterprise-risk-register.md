# Enterprise Risk Register

## Rating Model

Likelihood and Impact use a 1--5 scale. **Inherent Score = Likelihood ×
Impact.**

-   20--25: Critical
-   15--19: High
-   8--14: Medium
-   1--7: Low

  ------------------------------------------------------------------------------------------------------------------------
  ID      Risk                              L         I     Score Rating     Treatment   Owner                     Phase
  ------- ------------------------- --------- --------- --------- ---------- ----------- ------------------------- -------
  R-001   Fragmented                        4         5        20 Critical   Mitigate    Cloud Platform            1--2
          management-group/policy                                                                                  
          inheritance causes                                                                                       
          inconsistent enterprise                                                                                  
          controls.                                                                                                

  R-002   Standing or excessive             4         5        20 Critical   Mitigate    Identity/Security         3
          privilege enables                                                                                        
          unauthorized high-impact                                                                                 
          change.                                                                                                  

  R-003   Long-lived workload               4         5        20 Critical   Mitigate    App/Identity Security     3/6
          credentials or excessive                                                                                 
          API permissions are                                                                                      
          compromised or abused.                                                                                   

  R-004   Unnecessary public                4         4        16 High       Mitigate    Network/Workload Owners   4
          exposure increases attack                                                                                
          surface.                                                                                                 

  R-005   Incomplete telemetry              4         4        16 High       Mitigate    Security Operations       5
          prevents timely detection                                                                                
          or investigation.                                                                                        

  R-006   Weak exception lifecycle          4         4        16 High       Mitigate    Governance/Security       2
          creates permanent                                                                                        
          unmanaged security debt.                                                                                 

  R-007   Manual configuration              4         4        16 High       Mitigate    Platform Engineering      6
          causes drift,                                                                                            
          inconsistent controls,                                                                                   
          and weak auditability.                                                                                   

  R-008   Missing                           4         4        16 High       Mitigate    Cloud Governance          2
          ownership/criticality                                                                                    
          metadata delays                                                                                          
          remediation and incident                                                                                 
          response.                                                                                                

  R-009   Incomplete data                   3         5        15 High       Mitigate    Data Governance           7
          classification leads to                                                                                  
          insufficient protection                                                                                  
          of sensitive data.                                                                                       

  R-010   Inconsistent recovery             3         5        15 High       Mitigate    Platform/Workload Owners  1/5
          testing results in                                                                                       
          failure to meet business                                                                                 
          recovery needs.                                                                                          

  R-011   Unmanaged detection               3         4        12 Medium     Mitigate    Security Operations       5
          lifecycle causes alert                                                                                   
          gaps, noise, or stale                                                                                    
          controls.                                                                                                

  R-012   AI adoption exposes               3         5        15 High       Mitigate    AI Governance/Security    8
          sensitive data or                                                                                        
          introduces unsafe                                                                                        
          model/agent behavior.                                                                                    

  R-013   Legacy/Arc workloads              3         4        12 Medium     Mitigate    Infrastructure/Platform   1/2/5
          remain outside modern                                                                                    
          governance patterns.                                                                                     

  R-014   Inconsistent Defender             3         4        12 Medium     Mitigate    Security Engineering      5
          coverage leaves                                                                                          
          preventable security                                                                                     
          blind spots.                                                                                             

  R-015   Non-production                    3         5        15 High       Mitigate    Data/App Owners           7
          environments process                                                                                     
          production-like data                                                                                     
          without equivalent                                                                                       
          safeguards.                                                                                              
  ------------------------------------------------------------------------------------------------------------------------

## Residual Risk

Residual scores are not assigned in Phase 0 because treatment controls
have not yet been validated. Each delivery phase will reassess its
source risks after implementation evidence exists.
