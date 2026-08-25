# Phase 0 Evidence

## Purpose

This directory is reserved for **sanitized evidence** supporting Phase 0
findings.

## Acceptable Evidence

Examples include:

-   redacted inventory exports;
-   sanitized Azure Resource Graph query output;
-   fictionalized screenshots recreated for the portfolio;
-   policy coverage summaries;
-   anonymized maturity calculations;
-   diagrams containing no production identifiers;
-   scripts used to collect inventory;
-   validation output with tenant/subscription identifiers removed.

## Never Publish

Do not commit:

-   tenant IDs;
-   subscription IDs;
-   client IDs tied to real applications;
-   secrets, certificates, tokens, keys, passwords, or connection
    strings;
-   real public/private IP addressing if sensitive;
-   employee names or email addresses;
-   internal hostnames;
-   confidential application names;
-   customer/client data;
-   proprietary internal diagrams;
-   incident data;
-   unrestricted raw exports.

## Evidence Naming

Use:

`EVID-###-short-description.ext`

Example:

`EVID-001-sanitized-resource-inventory.csv`

## Evidence Traceability

Evidence should be referenced from the finding, risk, requirement, or
validation artifact it supports.
