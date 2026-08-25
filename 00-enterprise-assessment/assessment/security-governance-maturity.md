# Security Governance Maturity Assessment

## Maturity Scale

  ------------------------------------------------------------------------
                         Level Name                  Definition
  ---------------------------- --------------------- ---------------------
                             1 Initial               Ad hoc,
                                                     person-dependent,
                                                     primarily manual

                             2 Developing            Controls exist but
                                                     are inconsistent
                                                     across scope

                             3 Defined               Standards and
                                                     ownership are
                                                     documented

                             4 Managed               Controls are
                                                     automated, measured,
                                                     reviewed, and
                                                     governed

                             5 Optimized             Continuous,
                                                     risk-driven
                                                     improvement with high
                                                     automation
  ------------------------------------------------------------------------

## Current and Target Maturity

  Domain                                       Current   Target   Gap Primary Phase
  ------------------------------------------ --------- -------- ----- ---------------
  Enterprise cloud governance                        2        4     2 1--2
  Management-group/subscription governance           2        4     2 1
  Azure Policy governance                            2        4     2 2
  Identity governance                                2        4     2 3
  Workload identity/credentials                      2        4     2 3/6
  Network security                                   2        4     2 4
  Security operations                                3        4     1 5
  Logging/telemetry                                  3        4     1 5
  DevSecOps                                          2        4     2 6
  Policy/Infrastructure as Code                      1        4     3 6
  Data protection                                    2        4     2 7
  Resilience governance                              2        4     2 1/5
  AI security                                        1        3     2 8

## Interpretation

### Strongest Existing Capability

Security monitoring has reached **Defined** maturity in portions of the
environment. Sentinel, Defender, Log Analytics, and modern monitoring
components are present.

### Largest Engineering Gap

Policy and Infrastructure as Code have the largest maturity gap. Manual
configuration makes otherwise sound standards difficult to reproduce and
validate.

### Highest-Risk Governance Gap

Identity and workload credential governance are rated only Developing
despite their high potential impact.

## Target-State Characteristics

Level 4 does not mean every control is automated. It means the
enterprise can consistently demonstrate:

-   an accountable owner;
-   an approved standard;
-   measurable implementation;
-   evidence of compliance;
-   controlled exceptions;
-   lifecycle review;
-   automated enforcement where appropriate.

## Reassessment

Maturity should be reassessed after major transformation milestones.
Scores should only increase when evidence demonstrates the new operating
capability.
