# QA Concepts — Course Management API

## 1. Testing Types Mapped to the Course Management API

### Unit Testing
**Test Case:** Test the `calculate_course_duration()` function in isolation — given a start_date 
and end_date, verify it returns the correct number of weeks.
- **Type:** Functional

### Integration Testing
**Test Case:** Test the `POST /api/courses/` endpoint together with the database layer — verify 
that when a valid course payload is sent, a new row is correctly inserted into the `courses` table 
and the returned response matches the stored record.
- **Type:** Functional

### System Testing
**Test Case:** Test the complete end-to-end flow: a client sends `POST /api/courses/` with valid 
data → API validates input → API writes to the database → API returns 201 with the created 
course → a subsequent `GET /api/courses/{id}` retrieves the same data correctly.
- **Type:** Functional

### User Acceptance Testing (UAT)
**Test Case:** A college admin logs into the system, creates a new course called "Data 
Structures", assigns it to a semester, and confirms it appears correctly in the course listing page 
exactly as they expect for their daily workflow.
- **Type:** Functional

### Non-Functional Test Example
**Test Case:** Performance test — verify that `GET /api/courses/` responds within 200ms when 
the `courses` table contains 10,000 records.
- **Type:** Non-Functional (Performance)

---

## 2. Black-Box vs White-Box Testing

| Aspect | Black-Box Testing | White-Box Testing |
|---|---|---|
| Definition | Testing without knowledge of internal code/logic | Testing with full knowledge of internal code structure |
| Focus | Inputs and outputs only | Code paths, branches, logic |
| Example | Sending a request to `POST /api/courses/` and checking the response, without looking at the implementation | Writing a unit test that checks every if/else branch inside the course validation function |
| Typically performed by | QA Tester | Developer |

**Conclusion:** QA testers typically perform Black-Box testing (they validate behavior from the 
outside), while Developers typically perform White-Box testing (they validate internal logic and 
code paths, often through unit tests).

---

## 3. Formal Test Cases — POST /api/courses/

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|---|
| TC_COURSE_001 | Create a course with valid data | API server running; DB accessible; admin auth token available | 1. Send POST to `/api/courses/` with valid JSON body (name, code, credits, semester) 2. Capture response | API returns `201 Created` with the new course object including a generated `id` | | |
| TC_COURSE_002 | Create a course with a duplicate course code | A course with code "CS101" already exists in DB | 1. Send POST to `/api/courses/` with `code: "CS101"` (already existing) 2. Capture response | API returns `400 Bad Request` with an error message indicating the course code already exists | | |
| TC_COURSE_003 | Create a course with missing required field (name) | API server running; DB accessible | 1. Send POST to `/api/courses/` with JSON body missing the `name` field 2. Capture response | API returns `422 Unprocessable Entity` (or `400`) with a validation error specifying `name` is required | | |

## 4. Defect Lifecycle

**Standard Flow:**
New → Assigned → Open → Fixed → Retest → Verified → Closed

| State | Meaning |
|---|---|
| New | Defect logged by QA, not yet reviewed |
| Assigned | Defect reviewed and assigned to a developer |
| Open | Developer has acknowledged and is working on it |
| Fixed | Developer has fixed the code and checked it in |
| Retest | QA re-tests the fix in the build where it was applied |
| Verified | QA confirms the fix works correctly, no regression |
| Closed | Defect lifecycle complete — no further action needed |

**Alternate Paths:**
- **Rejected:** Developer/lead reviews the defect and determines it's not a valid bug (e.g., 
working as intended, duplicate, or not reproducible). Path: New → Rejected.
- **Deferred:** Defect is valid but the team decides to fix it in a later release/sprint due to low 
priority or time constraints. Path: Open → Deferred (and re-opened in a future cycle).

---

## 5. Severity & Priority Classification

| Bug | Severity | Priority | Justification |
|---|---|---|---|
| (a) POST /api/courses/ returns 500 for all requests | **Critical** | **P1** | Core functionality is completely broken — no course can be created. Blocks all downstream workflows. |
| (b) Course names >150 chars silently truncated, no error | **Medium** | **P3** | Functionality still partially works, but data integrity is silently compromised — not visible to the user, so not urgent but still needs fixing. |
| (c) Typo in Swagger /docs description | **Low** | **P4** | Purely cosmetic, no functional impact. Lowest urgency. |
| (d) Intermittent 401 on correct-credential login | **High** | **P1** | Severity is high because it blocks legitimate users from logging in; priority is also high because intermittent auth bugs indicate deeper system instability and are hard to diagnose — they tend to get worse if ignored. |

---

## 6. Defect Report — Bug (a)

| Field | Value |
|---|---|
| **Defect ID** | DEF-2026-001 |
| **Title** | POST /api/courses/ returns 500 Internal Server Error for all requests |
| **Environment** | Staging — Ubuntu 22.04, Python 3.11, PostgreSQL 15 |
| **Build Version** | v1.4.2 |
| **Severity** | Critical |
| **Priority** | P1 |
| **Steps to Reproduce** | 1. Authenticate as admin and obtain a valid token. 2. Send a `POST` request to `/api/courses/` with a valid JSON payload (name, code, credits, semester). 3. Observe the response. |
| **Expected Result** | API returns `201 Created` with the newly created course object. |
| **Actual Result** | API returns `500 Internal Server Error` for every request, regardless of payload validity. |
| **Attachments** | screenshot of 500 error |

---

## 7. Severity vs Priority

- **Severity** measures the technical impact of the defect on the system — how badly it breaks 
functionality.
- **Priority** measures the business urgency of fixing it — how soon it needs to be addressed, 
based on visibility, deadlines, or stakeholder impact.

**Real-world example where High Severity ≠ High Priority:**
A reporting module that generates end-of-semester transcripts crashes (High Severity — a core 
feature is completely broken), but the next semester-end run isn't due for 3 months. The team 
may mark this **P3** because there's no immediate business pressure, even though the severity 
is high — they have time to fix it before it's actually needed.

Conversely, a cosmetic typo on the CEO's dashboard ("Welcom" instead of "Welcome") is **Low 
Severity** but might be marked **High Priority** if leadership wants it fixed immediately before a 
demo.