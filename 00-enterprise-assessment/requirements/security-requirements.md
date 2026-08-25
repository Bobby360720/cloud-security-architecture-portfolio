# Security Requirements

## Traceability Convention

Each security requirement maps back to one or more Phase 0 risks and
forward to the phase responsible for architecture and implementation.

  -------------------------------------------------------------------------------
  ID             Requirement         Priority       Source Risk    Delivery Phase
  -------------- ------------------- -------------- -------------- --------------
  SEC-001        Privileged roles    Critical       R-002          3
                 MUST use controlled                               
                 elevation where                                   
                 supported.                                        

  SEC-002        Workloads MUST      Critical       R-003          3/6
                 prefer managed                                    
                 identity or                                       
                 federation over                                   
                 stored secrets.                                   

  SEC-003        High-privilege      Critical       R-003          3
                 application                                       
                 permissions MUST                                  
                 have an owner and                                 
                 recurring review.                                 

  SEC-004        Public PaaS         High           R-004          4
                 exposure SHOULD be                                
                 disabled unless                                   
                 explicitly                                        
                 justified.                                        

  SEC-005        Security-relevant   High           R-005          5
                 resources MUST emit                               
                 required telemetry                                
                 to approved                                       
                 destinations.                                     

  SEC-006        Enterprise          High           R-001          1/2
                 guardrails MUST be                                
                 assigned at the                                   
                 highest appropriate                               
                 governance scope.                                 

  SEC-007        Policy exceptions   High           R-006          2
                 MUST be approved,                                 
                 scoped, time-bound,                               
                 and reviewable.                                   

  SEC-008        Repeatable platform High           R-007          6
                 configuration                                     
                 SHOULD be version                                 
                 controlled and                                    
                 delivered as code.                                

  SEC-009        Critical resources  High           R-008          2
                 MUST have                                         
                 identifiable                                      
                 technical and                                     
                 business owners.                                  

  SEC-010        Data protection     High           R-009          7
                 controls MUST be                                  
                 driven by                                         
                 documented                                        
                 sensitivity.                                      

  SEC-011        Tier 1 workloads    High           R-010          1/5
                 MUST have tested                                  
                 recovery                                          
                 arrangements.                                     

  SEC-012        Security detections Medium-High    R-011          5
                 MUST have                                         
                 ownership,                                        
                 validation, review,                               
                 and retirement                                    
                 criteria.                                         

  SEC-013        AI workloads MUST   High           R-012          8
                 undergo AI-specific                               
                 security and                                      
                 data-flow review.                                 

  SEC-014        Administrative and  High           R-007          2/6
                 security                                          
                 configuration                                     
                 changes MUST be                                   
                 auditable.                                        

  SEC-015        New subscriptions   Critical       R-001          1/2
                 MUST inherit an                                   
                 approved baseline                                 
                 before production                                 
                 use.                                              
  -------------------------------------------------------------------------------

## Validation Principle

A requirement is not complete because a product was enabled. Each
requirement requires a defined validation method and evidence in its
delivery phase.
