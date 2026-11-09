#!/usr/bin/env python3
"""Idempotent Phase 3 milestone and issue creation using authenticated GitHub CLI."""
import json, subprocess, sys
REPO='Bobby360720/cloud-security-architecture-portfolio'
MILESTONE='Phase 3 — Zero Trust Identity & Identity Governance'
DESCRIPTION=('Design risk-based Zero Trust identity architecture; evaluate Microsoft Entra ID and SailPoint Identity Security Cloud responsibilities; complete targeted SailPoint learning; validate low-cost identity and IGA patterns. No production implementation or SailPoint tenant access is assumed.')

def gh(*args, input_text=None):
    p=subprocess.run(['gh',*args],input=input_text,text=True,capture_output=True)
    if p.returncode: raise RuntimeError(f"gh {' '.join(args)} failed:\n{p.stderr}")
    return p.stdout

def api(method,path,data=None):
    args=['api','-X',method,path,'-H','Accept: application/vnd.github+json']
    if data is not None:
        args += ['--input','-']
    return json.loads(gh(*args,input_text=json.dumps(data) if data is not None else None))

issues=[
('P03-01 — Map identity risks and requirements to the Phase 3 scope', '''## Objective
Establish the authoritative architecture basis before designing solutions.

## Tasks
- Review Phase 0 findings, enterprise risks, business/security/technical requirements, and relevant Phase 1–2 decisions.
- Map existing IDs to workforce, privileged, governance, and workload identity use cases.
- Identify missing requirements without inventing observed findings.
- Confirm modeled acquisition context and AFG business-service dependencies.

## Acceptance criteria
- [ ] Traceability links actual existing register IDs to proposed Phase 3 controls.
- [ ] Unresolved requirements and assumptions are clearly labeled.
- [ ] No changes are made to the authoritative risk register without appropriate review.

**Evidence:** Updated traceability matrix or documented links to authoritative records.'''),
('P03-02 — SailPoint Identity Security Leader training and IGA fundamentals', '''## Objective
Complete the SailPoint **Identity Security Leader** training path as the foundation for architectural decisions.

## Tasks
- Complete the eight-course Identity Security Leader learning path, subject to access.
- Prioritize identity security strategy, team/ownership, implementation planning, and IAM vs IGA concepts.
- Summarize JML, entitlement models, certifications, segregation of duties, and governance accountabilities in an AFG-specific learning note.
- Attempt the Leader credential only if available and appropriate.

## Acceptance criteria
- [ ] Learning modules are tracked as completed (or blocked with access reason).
- [ ] AFG-specific reflection ties the concepts to at least three enterprise identity risks.
- [ ] Credential status is accurately documented; do not claim completion without evidence.

**Dependency:** Can proceed alongside P03-01; finish fundamentals before identity governance labs.'''),
('P03-03 — SailPoint Identity Security Cloud fundamentals and platform comparison', '''## Objective
Gain working conceptual knowledge of Identity Security Cloud and evaluate overlap with Microsoft Entra ID Governance.

## Tasks
- Complete introductory Identity Security Cloud materials and selected administration fundamentals.
- Study identity profiles, sources, aggregation, correlation, lifecycle states, roles, access requests, and certifications.
- Compare SailPoint with Microsoft Entra ID Governance by control ownership, integration, licensing, and operational burden.
- Note required product or training tenant access; record access and licensing blockers.

## Acceptance criteria
- [ ] Training notes distinguish observed product exercise from documentation-based knowledge.
- [ ] Capability/responsibility comparison completed.
- [ ] Any proposed SailPoint selection remains conditional on assessment and ADR.

**Dependency:** P03-02 recommended.'''),
('P03-04 — Design enterprise identity reference architecture and trust boundaries', '''## Objective
Design Entra-centric authentication with evaluated SailPoint governance responsibilities.

## Tasks
- Identify authoritative HR/identity sources and targets; define identity correlation and provisioning flows.
- Distinguish authentication, authorization, governance, provisioning, and audit boundaries.
- Model workforce, guest, privileged, workload, and acquired-company scenarios.
- Document dependencies, failure modes, operational ownership, and security assumptions.

## Acceptance criteria
- [ ] Logical data-flow and trust-boundary diagram reviewed.
- [ ] Ownership and provisioning conflict controls documented.
- [ ] M&A is clearly marked as a modeled design scenario.

**Dependency:** P03-01, P03-03.'''),
('P03-05 — Record Entra ID Governance vs SailPoint architecture decision', '''## Objective
Select a defensible *proposed* IGA responsibility model, not a predetermined vendor purchase.

## Tasks
- Evaluate Entra-only, Entra + SailPoint, and alternative limited-governance options.
- Compare role ownership, access requests/certifications, licensing, administration, connector availability, and resilience.
- Define authoritative systems and avoid dual ownership of entitlement writes.
- Record ADR including alternatives, trade-offs, decision authority, risks, and conditions for revisiting.

## Acceptance criteria
- [ ] ADR references actual requirements and risks.
- [ ] Selected lab design is distinct from unapproved enterprise product adoption.
- [ ] Cost and licensing assumptions are explicit.

**Dependency:** P03-03, P03-04.'''),
('P03-06 — Define JML, entitlement, certification, and SoD operating model', '''## Objective
Turn IGA capabilities into business-owned processes and measurable controls.

## Tasks
- Define joiner/mover/leaver triggers, data ownership, exception paths, deprovisioning targets.
- Specify access request and approval matrix, birthright access, role model, and certifications.
- Define SoD conflicts relevant to a modeled fintech business service.
- Define operating roles, escalation, reconciliation, and evidence retention.

## Acceptance criteria
- [ ] JML flows and RACI/ownership matrix documented.
- [ ] One representative entitlement model and SoD conflict defined.
- [ ] Acceptance criteria include timing and ownership rather than only product setup.

**Dependency:** P03-04, P03-05.'''),
('P03-07 — Define workforce, privileged, and workload identity security standards', '''## Objective
Extend existing Azure governance with coherent identity standards.

## Tasks
- Specify phishing-resistant authentication and Conditional Access policies, exclusions, and emergency access.
- Define Entra roles vs Azure RBAC, PIM eligibility and approvals where licensed.
- Specify managed identities, workload federation, credentials, and application permission governance.
- Connect workload identity design to Secure Platform Engineering without duplicating that phase.

## Acceptance criteria
- [ ] Standards identify supported vs unsupported features and licensing dependencies.
- [ ] Privileged and workload controls map to actual risks/requirements.
- [ ] Test criteria and rollback considerations documented.

**Dependency:** P03-01, P03-04.'''),
('P03-08 — Complete SailPoint engineering learning: connectors, access model, workflows and APIs', '''## Objective
Prepare for engineering validation with targeted SailPoint Identity Security Cloud coursework.

## Training scope
- **Build an Access Model in Identity Security Cloud**.
- **Configure and Extend Identity Security Cloud Connectors** (including SCIM, Web Services, JDBC, delimited file).
- **Design and Build Identity Security Cloud Workflows**.
- **Extend Identity Security Cloud** (APIs, workflow/configuration and troubleshooting).
- Progress through **Identity Security Engineer** path as access permits; advanced certification is optional, not a phase gate.

## Acceptance criteria
- [ ] Record courses completed, notes, and restricted-access gaps.
- [ ] Define source/target mapping and connector/error-handling specifications for a single AFG integration.
- [ ] Distinguish documentation-based exercises from verified SailPoint tenant work.

**Dependency:** P03-03; run concurrently with P03-09–P03-11.'''),
('P03-09 — Validate Entra access and privileged identity baseline', '''## Objective
Validate a low-cost representative Entra security control set.

## Tasks
- Inventory existing lab licensing, state, and test identities; estimate lab cost before changing resources.
- Create a controlled test case for authentication policy and least privilege.
- Where supported/licensed, test Conditional Access, eligible roles/PIM, and emergency-access exclusion behavior safely.
- Capture expected vs observed outcome, logs, rollback, and cleanup.

## Acceptance criteria
- [ ] Tests use isolated/safe accounts; no tenant lockout risk introduced.
- [ ] Evidence includes configuration and observed access decision.
- [ ] Unlicensed features are documented as planned, not validated.

**Dependency:** P03-07.'''),
('P03-10 — Validate IGA JML and entitlement reconciliation scenario', '''## Objective
Demonstrate a representative identity lifecycle without requiring an expensive production-style SailPoint tenant.

## Tasks
- Create fictional HR joiner/mover/leaver events and a test entitlement model.
- Use authorized SailPoint lab access if available; otherwise run a clearly labeled simulation or open-source implementation.
- Test account creation, role change/removal, disablement, mismatched entitlement reconciliation, and exception flow.
- Compare expected control behavior to actual result and capture evidence.

## Acceptance criteria
- [ ] Three JML scenarios have reproducible steps and outcomes.
- [ ] An orphaned or inconsistent entitlement test is included.
- [ ] No simulated output is represented as verified SailPoint functionality.
- [ ] Access and financial constraints recorded.

**Dependency:** P03-06, P03-08.'''),
('P03-11 — Validate Python/API and workload federation integration', '''## Objective
Demonstrate cross-platform integration mechanics tied to identity governance requirements.

## Tasks
- Build small Python exercises for HR source events, REST requests, and/or SCIM mock endpoint.
- Use Microsoft Graph in controlled scope and test provisioning/reconciliation error handling.
- Reuse existing GitHub-to-Azure federated workload identity controls rather than duplicate earlier engineering.
- Add validation tests, secure credential handling, and reviewable evidence.

## Acceptance criteria
- [ ] Python/API test suite passes with non-sensitive sample data.
- [ ] No static production credentials committed.
- [ ] Real API integration vs mock behavior explicitly distinguished.

**Dependency:** P03-07, P03-08.'''),
('P03-12 — Threat model, monitor identity controls, and close Phase 3 review', '''## Objective
Finish Phase 3 with measurable security results and architecture-to-evidence traceability.

## Tasks
- Threat-model source-of-authority compromise, privilege escalation, provisioning errors, and M&A trust boundary failures.
- Identify Entra/SailPoint relevant log sources and at least one realistic identity detection test where available.
- Record findings, test failures, residual risks, operational ownership, and recommended follow-on work.
- Update Phase 3 README, ADR references and evidence index; do not overstate deployment status.

## Acceptance criteria
- [ ] Every implemented test links to requirement/control and observed result.
- [ ] Proposed vs validated vs simulated outcomes are clearly separated.
- [ ] Phase 3 closure includes explicit open risks and downstream dependencies.

**Dependency:** P03-09–P03-11.''')]

def main():
    try:
        gh('auth','status')
        repo=api('GET',f'repos/{REPO}')
        if not repo.get('permissions',{}).get('push'):
            print('WARNING: Repository push permission is not confirmed; issue creation may fail.',file=sys.stderr)
        milestones=api('GET',f'repos/{REPO}/milestones?state=all&per_page=100')
        milestone=next((m for m in milestones if m['title']==MILESTONE),None)
        if milestone is None:
            milestone=api('POST',f'repos/{REPO}/milestones',{'title':MILESTONE,'description':DESCRIPTION,'state':'open'})
            print('Created milestone:',milestone['html_url'])
        else:
            print('Reusing milestone:',milestone['html_url'])
        existing=[]
        page=1
        while True:
            chunk=api('GET',f'repos/{REPO}/issues?state=all&per_page=100&page={page}')
            existing += [x for x in chunk if 'pull_request' not in x]
            if len(chunk)<100:break
            page+=1
        for title,body in issues:
            match=next((i for i in existing if i['title']==title),None)
            if match:
                print('Existing issue (skipped):',match['html_url'])
                continue
            result=api('POST',f'repos/{REPO}/issues',{'title':title,'body':body,'milestone':milestone['number']})
            print('Created issue:',result['html_url'])
    except (RuntimeError, ValueError, KeyError) as e:
        print('ERROR:',e,file=sys.stderr)
        sys.exit(1)
if __name__=='__main__': main()
