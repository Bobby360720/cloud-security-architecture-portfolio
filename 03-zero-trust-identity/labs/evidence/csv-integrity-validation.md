# AFG Phase 3 — Synthetic Identity Data Validation

**Lab:** Phase 3 — Identity Data Integrity  
**Validation type:** Referential integrity and structural validation  
**Environment:** Local Python / Linux  
**Evidence classification:** Validated — Synthetic Dataset  
**Status:** Passed

## Objective

Verify that AFG's synthetic identity dataset contains valid references between employees, departments, managers, groups, and group memberships before using the data in identity lifecycle governance exercises.

## Dataset

| Component | Records |
|---|---:|
| Synthetic users | 150 |
| Departments | 15 |
| Security groups | 24 |
| Group memberships | 349 |

## Validation Results

All 11 defined integrity checks passed.

The validation checked:

- Duplicate employee, department, and group identifiers.
- Valid employee-to-department references.
- Valid employee-to-manager references.
- Valid department manager references.
- Valid group-to-department references.
- Valid group membership references.
- Duplicate group memberships.
- Group memberships associated with terminated employees.

**Result:** No exceptions were reported by the defined checks.

## Security Architecture Relevance

The successful validation establishes a consistent synthetic identity baseline for planned joiner, mover, and leaver exercises, access governance testing, and entitlement reconciliation.

This supports the design and validation of representative controls associated with enterprise risks R-002 and R-003.

## Limitations

- The validation covers synthetic CSV data only.
- No Microsoft Entra ID or SailPoint identities were created.
- No production identities or enterprise access permissions were assessed.
- Least-privilege access, segregation of duties, and lifecycle automation have not yet been validated.
- This result does not demonstrate a reduction in R-002 or R-003 residual risk.

## Related GitHub Issues

- #36 — Define JML, entitlement, certification, and SoD operating model.
- #40 — Validate IGA JML and entitlement reconciliation scenario.

## Conclusion

The synthetic identity dataset passed the defined structural and referential integrity checks and is suitable as a baseline for subsequent identity governance simulations.
