# SDLC vs TDLC — V-Model Analysis

## 1. V-Model Diagram (ASCII)
Requirements              Acceptance Testing

\                         /

\                       /

System Design        System Testing

\                   /

\                 /

Architecture Design  Integration Testing

\               /

\             /

Module Design   Unit Testing

\           /

\         /

\       /

Coding

(bottom vertex)

Left side = Development phases (top to bottom). Right side = Testing phases (bottom to top). 
Each development phase has a corresponding testing phase at the same horizontal level — this 
is the "V" shape.

---

## 2. SDLC ↔ TDLC Phase Mapping & Test Artifacts

| SDLC Phase | Corresponding TDLC Phase | Test Artifact Produced |
|---|---|---|
| Requirements | Acceptance Testing | Acceptance Test Plan / User Acceptance Criteria |
| System Design | System Testing | System Test Plan, end-to-end test scenarios |
| Architecture Design | Integration Testing | Integration Test Plan, interface/contract specs |
| Module Design | Unit Testing | Unit Test Cases, test stubs/mocks design |
| Coding | — | Code + Unit Tests (developer-written) |

**Example:** During the Requirements phase, while business analysts define what the Course 
Management API should do, QA simultaneously drafts the Acceptance Test Plan based on those 
same requirements — so testing artifacts are ready before a single line of code exists.

---

## 3. Entry & Exit Criteria — All 4 Testing Levels

| Testing Level | Entry Criteria | Exit Criteria |
|---|---|---|
| **Unit Testing** | Module code is complete and compiles; unit test cases are written | All unit tests pass; code coverage meets target (e.g., 80%); no critical defects open |
| **Integration Testing** | All required modules/components are unit-tested and available; integration test environment is set up | All integration test cases executed; interfaces between components verified; no critical/high defects open |
| **System Testing** | Integration testing complete; full system build deployed to test environment; test data prepared | All planned system test cases executed; defect count below threshold; no critical/high defects open |
| **Acceptance Testing (UAT)** | System testing complete and signed off; UAT environment ready; UAT test cases reviewed by stakeholders | Business stakeholders approve the system meets requirements; no critical defects open; sign-off obtained |

---

## 4. Early QA Engagement Points in the Course Management API Project

1. **Requirements Review:** QA reviews the requirements documents (e.g., "admin can create a 
course") for ambiguity, testability, and missing edge cases (e.g., "what happens on duplicate 
course codes?") *before* any code is written. Catching this early is far cheaper than catching it 
during system testing.

2. **Architecture/API Design Review:** QA reviews the planned API contract (e.g., the OpenAPI/
Swagger spec for `/api/courses/`) to ensure response codes, error formats, and edge cases are 
clearly defined and testable — before developers start implementing endpoints.

Hands-On 2 — Task 2: Agile QA and Shift-Left Testing
markdown## 5. Problems with Waterfall Testing (Testing After Development)

For the Course Management API project, testing only after development is complete causes:

1. **Late defect discovery = expensive fixes:** A flawed requirement (e.g., ambiguous course 
code format) discovered during final system testing requires reworking the database schema, 
API logic, and frontend — far more costly than catching it at requirements stage.

2. **Compressed testing timelines:** If development overruns (common in real projects), testing 
gets squeezed at the end, leading to rushed, incomplete test coverage right before a release 
deadline.

3. **No early feedback loop:** Developers don't learn about quality issues until weeks/months 
after writing the code, making root-cause analysis harder and increasing the risk of repeating the 
same mistakes in other modules.

---

## 6. QA Role in Agile Ceremonies

| Ceremony | QA Role |
|---|---|
| **Sprint Planning** | Defines acceptance criteria for each user story (e.g., "Create Course" story) alongside the team, ensuring stories are testable before they're committed to the sprint. |
| **Daily Standup** | Reports blocking issues — e.g., "Can't test the create-course endpoint, the staging DB is down" — so the team can unblock testing quickly. |
| **Sprint Review** | Demonstrates tested functionality to stakeholders, highlighting what was verified to work and any known limitations. |
| **Retrospective** | Raises process improvements — e.g., "We had 3 regressions in course creation this sprint; we need automated regression tests for that endpoint going forward." |

---

## 7. Shift-Left Practices Applied to the Course Management API

| Practice | Application to Course Management API |
|---|---|
| (a) Reviewing requirements for testability | QA reviews the "create course" user story early and asks: "What's the expected behavior for a duplicate course code?" — forcing clarity before coding starts. |
| (b) Writing test cases before code (TDD/BDD) | Before implementing `POST /api/courses/`, the team writes a Gherkin scenario: "Given valid course data, when I POST it, then I should receive a 201" — and the implementation is built to satisfy it. |
| (c) Static code analysis | Run tools like `pylint`/`flake8` on every commit to the API codebase to catch code smells and potential bugs before they reach a test environment. |
| (d) API contract testing before integration | Validate the OpenAPI schema for `/api/courses/` against a contract-testing tool (e.g., Schemathesis) before the frontend team starts integrating, catching mismatches early. |

---

## 8. Acceptance Criteria — Gherkin Format

**User Story:** As a college admin, I want to create a new course, so that students can enroll in it.

```gherkin
Scenario: Successfully create a new course (Happy Path)
  Given I am logged in as a college admin
  And I provide valid course details (name, code, credits, semester)
  When I submit the create course request
  Then the course should be created successfully
  And I should see a 201 success response with the new course details

Scenario: Attempt to create a course with a duplicate course code
  Given I am logged in as a college admin
  And a course with the code "CS101" already exists
  When I submit a create course request using the code "CS101"
  Then the request should be rejected
  And I should see an error message stating the course code already exists

Scenario: Attempt to create a course with missing required fields
  Given I am logged in as a college admin
  And I omit the required "name" field from the course details
  When I submit the create course request
  Then the request should be rejected
  And I should see a validation error indicating "name" is required
```


## 5. Comparison of 5 Automation Framework Types

| Framework | Description | Advantage | Disadvantage | Use Case for Course Management |
|---|---|---|---|---|
| **Linear** | Tests are written as a straight sequence of steps/commands with no reusable functions — essentially "record and playback" style scripts. | Very quick to write for one-off tests. | Highly repetitive code; any UI change requires editing every script that uses that element. | A one-time smoke test verifying the API is up after a hotfix deployment. |
| **Modular** | Application is broken into independent modules, each with its own reusable test script (functions for login, course creation, etc.) that other tests call. | Reusable, easier to maintain than Linear. | Still requires programming knowledge; logic and data are mixed together. | Reusing a `login()` function across 20 different test scripts for the Course Management frontend. |
| **Data-Driven** | Test logic is separated from test data, which is stored externally (CSV/Excel/JSON) and the same test runs once per data row. | Easily test many input combinations without duplicating code. | Doesn't address reusability of UI interaction logic itself. | Testing course creation with 50 different combinations of name/code/credits to check validation. |
| **Keyword-Driven** | Test steps are defined as "keywords" (e.g., "ClickButton", "EnterText") in a spreadsheet/table, interpreted by a driver script — testers don't need to code. | Non-technical team members can write/maintain tests. | Significant upfront effort to build the keyword interpretation engine. | Allowing a non-technical QA member to define test steps for the course listing page in a spreadsheet. |
| **Hybrid** | Combines Modular (reusability) + Data-Driven (parameterization) + optionally Keyword-Driven (abstraction) into one framework. | Most flexible and powerful; scales well for large, evolving projects. | More complex to design and set up initially. | The full Course Management test suite — reusable page objects, data-driven login tests, and clear structure for the whole team. |

---

## 6. Framework Recommendation for the Given Scenario

**Scenario:** Test login with 50 different user/password combinations, reuse login steps across 20 
test cases, support both technical and non-technical team members writing tests.

**Recommendation: Hybrid Framework** (combining Data-Driven + Modular, with optional 
Keyword-Driven elements)

**Justification:**
- **Data-Driven** component handles the 50 different user/password combinations by externalizing 
them into a CSV/JSON file, looping the same login test over each row.
- **Modular** component (via Page Object Model) ensures the login interaction logic is written 
once and reused across all 20 test cases that need to log in first.
- **Keyword-Driven** elements (optional) can be layered in so non-technical team members can 
add new login data combinations or simple test flows without writing Python code directly.

This combination satisfies all three requirements simultaneously, which no single framework 
type does alone.

---

## 7. Hybrid Framework Folder Structure

```
course_management_tests/
│
├── test_data/
│   ├── login_credentials.csv          # 50 user/password combinations
│   └── course_creation_data.json      # data-driven course test inputs
│
├── pages/                              # Page Object files
│   ├── base_page.py
│   ├── login_page.py
│   ├── course_page.py
│   └── checkbox_page.py
│
├── utils/                              # Utility/helper files
│   ├── driver_factory.py               # WebDriver setup/teardown helpers
│   ├── data_reader.py                  # reads CSV/JSON test data
│   └── logger.py
│
├── tests/                              # Test files (assertions live here)
│   ├── test_login.py
│   ├── test_course_creation.py
│   └── test_checkbox.py
│
├── config/
│   ├── config.yaml                     # base_url, timeouts, environment settings
│   └── conftest.py                     # pytest fixtures (driver, base_url)
│
├── reports/
│   └── report.html                     # pytest-html generated report
│
└── requirements.txt
```