#!/usr/bin/env python3
"""Generate deterministic, entirely fictional AFG IGA lab data (CSV only).

No Azure / Microsoft Graph / SailPoint API calls are made.  All UPNs use
example.test, a reserved testing domain that must not be used in production.
"""
import argparse
import csv
import random
import re
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

DEPARTMENTS = [
    ("D001", "Executive Office", "Corporate", "Atlanta", 4),
    ("D002", "Finance & Accounting", "Corporate", "Atlanta", 12),
    ("D003", "People & Culture", "Corporate", "Atlanta", 8),
    ("D004", "Legal & Compliance", "Corporate", "Atlanta", 10),
    ("D005", "Risk Management", "Risk", "Atlanta", 10),
    ("D006", "Information Security", "Technology", "Atlanta", 14),
    ("D007", "Cloud Platform Engineering", "Technology", "Atlanta", 14),
    ("D008", "Software Engineering", "Technology", "Dallas", 20),
    ("D009", "Digital Banking", "Banking", "Atlanta", 16),
    ("D010", "Consumer Lending", "Lending", "Dallas", 14),
    ("D011", "Payments Operations", "Payments", "Atlanta", 14),
    ("D012", "Wealth Management", "Wealth", "Charlotte", 10),
    ("D013", "Customer Experience", "Operations", "Dallas", 10),
    ("D014", "Data & Analytics", "Technology", "Atlanta", 12),
    ("D015", "Identity & Access Management", "Technology", "Atlanta", 8),
]
FIRST_NAMES = ["Alex", "Morgan", "Jordan", "Taylor", "Casey", "Riley", "Avery", "Quinn", "Drew", "Reese", "Jamie", "Cameron", "Parker", "Sydney", "Sage", "Harper", "Ellis", "Rowan", "Emerson", "Blair", "Skyler", "Kendall", "Finley", "Dakota", "Micah", "Robin", "Marley", "Adrian", "Terry", "Devon"]
LAST_NAMES = ["Brooks", "Carter", "Hayes", "Morgan", "Patel", "Reed", "Chen", "Bennett", "Jackson", "Kim", "Williams", "Rivera", "Thomas", "Nguyen", "Davis", "Harris", "Martin", "Price", "Collins", "Shaw", "Bell", "Ross", "Howard", "Perry", "Young", "Turner", "Ward", "Cooper", "Gray", "Flores"]
ROLES = {
    "Executive Office": ["Executive Analyst", "Executive Operations Specialist"],
    "Finance & Accounting": ["Financial Analyst", "Accountant", "Finance Specialist"],
    "People & Culture": ["HR Generalist", "Talent Operations Specialist"],
    "Legal & Compliance": ["Compliance Analyst", "Legal Operations Analyst"],
    "Risk Management": ["Risk Analyst", "Enterprise Risk Specialist"],
    "Information Security": ["Security Analyst", "Cloud Security Engineer"],
    "Cloud Platform Engineering": ["Cloud Platform Engineer", "Site Reliability Engineer"],
    "Software Engineering": ["Software Engineer", "Application Developer"],
    "Digital Banking": ["Banking Operations Analyst", "Digital Banking Specialist"],
    "Consumer Lending": ["Lending Analyst", "Loan Operations Specialist"],
    "Payments Operations": ["Payments Analyst", "Transaction Operations Specialist"],
    "Wealth Management": ["Wealth Operations Analyst", "Client Services Associate"],
    "Customer Experience": ["Customer Experience Specialist", "Support Analyst"],
    "Data & Analytics": ["Data Analyst", "Analytics Engineer"],
    "Identity & Access Management": ["IAM Analyst", "Identity Engineer"],
}

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def write_csv(path, columns, rows):
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

def generate(count, seed, outdir):
    if count < len(DEPARTMENTS) * 2:
        raise ValueError(f"--users must be at least {len(DEPARTMENTS) * 2} (manager + employee per department)")
    rng = random.Random(seed)
    outdir.mkdir(parents=True, exist_ok=True)
    total_weight = sum(d[4] for d in DEPARTMENTS)
    # One manager and one employee in each department, extras apportioned by weight.
    weights = [d[4] / total_weight for d in DEPARTMENTS]
    extras = count - len(DEPARTMENTS) * 2
    raw = [extras * w for w in weights]
    allocations = [2 + int(x) for x in raw]
    remainder = count - sum(allocations)
    for i in sorted(range(len(raw)), key=lambda i: (raw[i] - int(raw[i]), -i), reverse=True)[:remainder]:
        allocations[i] += 1

    users, groups, memberships, departments = [], [], [], []
    group_ids = set()
    def add_group(gid, name, category, description, dept_id="", privileged="false"):
        if gid not in group_ids:
            group_ids.add(gid)
            groups.append({"groupId": gid, "displayName": name, "groupType": "Security", "category": category,
                           "departmentId": dept_id, "privileged": privileged, "description": description})
    add_group("G-ALL", "AFG-All-Employees", "birthright", "Standard employee access")
    add_group("G-MANAGERS", "AFG-All-Managers", "job-function", "Department management access")
    add_group("G-SEC-READ", "AFG-Security-Readers", "job-function", "Read-only security operations")
    add_group("G-PLATFORM-READ", "AFG-Platform-Readers", "job-function", "Read-only Azure platform access")
    add_group("G-PAYMENTS-OPS", "AFG-Payments-Operators", "job-function", "Payment operations access")
    add_group("G-FINANCE-AP", "AFG-Finance-AP", "job-function", "Accounts payable request processing")
    add_group("G-FINANCE-APPROVE", "AFG-Finance-Approvers", "sensitive", "Payment approval; mutually exclusive with Finance AP")
    add_group("G-IAM-REVIEW", "AFG-IAM-Access-Reviewers", "governance", "IGA access reviewers")
    add_group("G-AZURE-PRIV-ELIGIBLE", "AFG-Azure-Privileged-Eligible", "privileged", "Modeled eligible Azure role access; not an actual role assignment", privileged="true")

    identifier = 10000
    for dept_idx, (dept_id, dept, business, location, _) in enumerate(DEPARTMENTS):
        manager_id = f"AFG-{identifier:05d}"
        dept_group = f"G-DEPT-{dept_id}"
        add_group(dept_group, f"AFG-Dept-{slug(dept)}", "department", f"Birthright access for {dept}", dept_id)
        departments.append({"departmentId": dept_id, "departmentName": dept, "businessUnit": business,
                            "location": location, "managerEmployeeId": manager_id, "costCenter": f"CC-{dept_id[1:]}"})
        for n in range(allocations[dept_idx]):
            eid = f"AFG-{identifier:05d}"
            first = rng.choice(FIRST_NAMES)
            last = rng.choice(LAST_NAMES)
            # Include ID in UPN to guarantee uniqueness even when names repeat.
            upn = f"{slug(first)}.{slug(last)}.{identifier}@afg.example.test"
            manager = n == 0
            title = f"Director, {dept}" if manager else rng.choice(ROLES[dept])
            # Static, seeded snapshot for reproducibility; not a representation of current employment.
            start = date(2020, 1, 1) + timedelta(days=rng.randint(0, 2100))
            status = "Active"
            if not manager and n >= 3 and rng.random() < 0.07:
                status = "Terminated"
            elif not manager and n >= 3 and rng.random() < 0.05:
                status = "Leave"
            users.append({"employeeId": eid, "userPrincipalName": upn, "givenName": first, "surname": last,
                          "displayName": f"{first} {last}", "departmentId": dept_id,
                          "department": dept, "businessUnit": business, "jobTitle": title,
                          "managerEmployeeId": "" if manager else manager_id, "location": location,
                          "employeeType": "Employee", "employmentStatus": status,
                          "hireDate": start.isoformat(), "costCenter": f"CC-{dept_id[1:]}"})
            def member(gid, kind):
                memberships.append({"employeeId": eid, "groupId": gid, "assignmentType": kind})
            if status == "Active":
                member("G-ALL", "birthright")
                member(dept_group, "birthright")
                if manager:
                    member("G-MANAGERS", "job-function")
                if dept in ("Information Security", "Identity & Access Management"):
                    member("G-SEC-READ", "job-function")
                if dept == "Cloud Platform Engineering":
                    member("G-PLATFORM-READ", "job-function")
                if dept == "Payments Operations":
                    member("G-PAYMENTS-OPS", "job-function")
                if dept == "Finance & Accounting":
                    member("G-FINANCE-APPROVE" if manager else "G-FINANCE-AP", "sensitive")
                if dept == "Identity & Access Management":
                    member("G-IAM-REVIEW", "governance")
                # One deliberately modeled privileged *eligibility* for testing an approval workflow.
                if manager and dept == "Cloud Platform Engineering":
                    member("G-AZURE-PRIV-ELIGIBLE", "privileged-eligible")
            identifier += 1
    # Write output; all records are synthetic and non-provisioning.
    write_csv(outdir / "departments.csv", ["departmentId", "departmentName", "businessUnit", "location", "managerEmployeeId", "costCenter"], departments)
    write_csv(outdir / "users.csv", ["employeeId", "userPrincipalName", "givenName", "surname", "displayName", "departmentId", "department", "businessUnit", "jobTitle", "managerEmployeeId", "location", "employeeType", "employmentStatus", "hireDate", "costCenter"], users)
    write_csv(outdir / "groups.csv", ["groupId", "displayName", "groupType", "category", "departmentId", "privileged", "description"], groups)
    write_csv(outdir / "group_memberships.csv", ["employeeId", "groupId", "assignmentType"], memberships)
    print(f"Created {len(users)} synthetic identities across {len(departments)} departments, {len(groups)} groups and {len(memberships)} memberships in {outdir}")
    print("No accounts or groups were created in Microsoft Entra ID or SailPoint.")
    print("Employment statuses:", dict(Counter(u["employmentStatus"] for u in users)))

def main():
    p = argparse.ArgumentParser(description="Generate fictional AFG workforce/IGA test CSV data")
    p.add_argument("--users", type=int, default=150, help="Number of employee identities (minimum 30; default 150)")
    p.add_argument("--seed", type=int, default=42, help="Reproducible random seed")
    p.add_argument("--output", type=Path, default=Path("03-zero-trust-identity/labs/seed-data"), help="Output directory")
    args = p.parse_args()
    generate(args.users, args.seed, args.output)

if __name__ == "__main__":
    main()
