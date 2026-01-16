# Defect Triage Document

**Purpose:**  
This document outlines the process and details for **triaging defects** reported during testing. It ensures **consistent prioritization, assignment, and resolution tracking**.  

---

## 1. Defect Summary

| Defect ID | Summary | Reporter | Date Reported | Module/Feature | Severity | Priority | Status |
|-----------|---------|---------|---------------|----------------|---------|---------|--------|
| DEF-001   | Example defect description | Ankita bhatt | 2026-01-15 | Login Module | High | P1 | Open |

**Notes:**  
- **Severity:** Impact on application functionality (Critical, High, Medium, Low)  
- **Priority:** Order of resolution based on business needs (P1, P2, P3)  

---

## 2. Triage Team

| Role | Name | Responsibility |
|------|------|----------------|
| QA Lead | Ankita | Review and validate defects |
| Developer Lead | TBD | Provide technical insights and resolution estimates |
| Product Owner | TBD | Decide business priority and impact |
| Release Manager | TBD | Track deployment and closure status |

---

## 3. Triage Meeting Details

- **Frequency:** Daily / Weekly (adjust as per project)  
- **Mode:** In-person / Zoom / Teams  
- **Duration:** 30–45 minutes  
- **Agenda:**  
  1. Review new defects since last triage  
  2. Validate severity and priority  
  3. Assign defects to developers  
  4. Identify blockers or dependencies  
  5. Update defect statuses in tracking tool  

---

## 4. Defect Analysis

| Defect ID | Root Cause | Environment | Steps to Reproduce | Comments / Notes |
|-----------|------------|------------|------------------|----------------|
| DEF-001   | Null Pointer Exception | QA | Login >> Click Profile | Happens intermittently in Chrome |

---

## 5. Defect Status & Resolution

| Status | Description |
|--------|------------|
| Open | Defect reported and awaiting triage |
| In Progress | Assigned to developer for fixing |
| Fixed | Resolved and awaiting verification |
| Verified | QA has validated the fix |
| Deferred | Decision to fix in future release |
| Closed | Defect fixed and verified, no further action needed |

---

## 6. Priority Matrix

| Severity / Impact | Business Critical | Major Functionality | Minor / Cosmetic |
|------------------|-----------------|------------------|----------------|
| Critical | P1 | P1 | P2 |
| High | P1 | P2 | P3 |
| Medium | P2 | P3 | P3 |
| Low | P3 | P3 | P4 |

---

## 7. Tools / References

- **Defect Tracking Tool:** Jira / ALM / qTest  
- **Project Documentation:** [Link to requirements/specs]  
- **Environment Details:** QA / Staging / Production  

---

## 8. Notes / Actions

- Record any **follow-ups, blockers, or decisions made during triage**  
- Update **defect tracking tool immediately** after each meeting  
- Ensure **communication to all stakeholders**  

---

> **Tip:** Keep this document **updated and accessible** to all team members to ensure transparency and efficient defect resolution.
