create database college_db;
use college_db;
create table students(
student_id int AUTO_INCREMENT PRIMARY KEY ,
first_name varchar(50)  NOT NULL,
last_name  VARCHAR(50)  NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
date_of_birth DATE,
department_id INT,
enrollment_year INT,
FOREIGN KEY (department_id) references departments(department_id));

create table departments(
department_id INT AUTO_INCREMENT PRIMARY KEY,
dept_name VARCHAR(100) NOT NULL,
hod_name VARCHAR(100),
budget DECIMAL(12,2));

create table courses(
course_id INT AUTO_INCREMENT PRIMARY KEY,
course_name VARCHAR(100) NOT NULL,
course_code VARCHAR(100) UNIQUE,
credits INT,
department_id INT,

 FOREIGN KEY (department_id) references departments(department_id));
create table enrollments(
enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
student_id int	,
course_id int ,
enrollment_date DATE,
grade CHAR(2)
,
 FOREIGN KEY (student_id) references students(student_id),
 FOREIGN KEY (course_id) references courses(course_id));
 
 create table professors(
professor_id INT AUTO_INCREMENT PRIMARY KEY,
prof_name  VARCHAR(100) NOT NULL	,
email VARCHAR(100)  UNIQUE ,
department_id INT ,
salary DECIMAL(10,2)
,

 FOREIGN KEY (department_id) references departments(department_id));
 
 
INSERT INTO departments (dept_name, hod_name, budget) VALUES
  ('Computer Science', 'Dr. Ramesh Kumar', 850000.00),
  ('Electronics', 'Dr. Priya Nair', 620000.00),
  ('Mechanical', 'Dr. Suresh Iyer', 540000.00),
  ('Civil', 'Dr. Ananya Sharma', 430000.00);
  -- students
INSERT INTO students (first_name, last_name, email, date_of_birth, department_id, 
enrollment_year) VALUES
  ('Arjun',  'Mehta',    'arjun.mehta@college.edu',    '2003-04-12', 1, 2022),
  ('Priya',  'Suresh',   'priya.suresh@college.edu',   '2003-07-25', 1, 2022),
  ('Rohan',  'Verma',    'rohan.verma@college.edu',    '2002-11-08', 2, 2021),
  ('Sneha',  'Patel',    'sneha.patel@college.edu',    '2004-01-30', 3, 2023),
  ('Vikram', 'Das',      'vikram.das@college.edu',     '2003-09-14', 1, 2022),
  ('Kavya',  'Menon',    'kavya.menon@college.edu',    '2002-05-17', 2, 2021),
  ('Aditya', 'Singh',    'aditya.singh@college.edu',   '2004-03-22', 4, 2023),
  ('Deepika','Rao',      'deepika.rao@college.edu',    '2003-08-09', 1, 2022);-- courses
INSERT INTO courses (course_name, course_code, credits, department_id) VALUES
  ('Data Structures & Algorithms', 'CS101', 4, 1),
  ('Database Management Systems',  'CS102', 3, 1),
  ('Object Oriented Programming',  'CS103', 4, 1),
  ('Circuit Theory',               'EC101', 3, 2),
  ('Thermodynamics',               'ME101', 3, 3);-- enrollments
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES
  (1, 1, '2022-07-01', 'A'), (1, 2, '2022-07-01', 'B'),
  (2, 1, '2022-07-01', 'B'), (2, 3, '2022-07-01', 'A'),
  (3, 4, '2021-07-01', 'A'), (4, 5, '2023-07-01', NULL),
  (5, 1, '2022-07-01', 'C'), (5, 2, '2022-07-01', 'A'),
  (6, 4, '2021-07-01', 'B'), (7, 5, '2023-07-01', NULL),
  (8, 1, '2022-07-01', 'A'), (8, 3, '2022-07-01', 'B');

-- professors
INSERT INTO professors (prof_name, email, department_id, salary) VALUES
  ('Dr. Anand Krishnan',  'anand.k@college.edu',   1, 95000.00),
  ('Dr. Meena Pillai',    'meena.p@college.edu',   1, 88000.00),
  ('Dr. Sunil Rajan',     'sunil.r@college.edu',   2, 82000.00),
  ('Dr. Latha Gopal',     'latha.g@college.edu',   3, 79000.00),
  ('Dr. Kartik Bose',     'kartik.b@college.edu',  4, 76000.00);

-- ------------------------------------------------------------
-- 1NF (First Normal Form)
-- Rule: Every column must hold atomic (indivisible) values.
--       No repeating groups or multi-valued fields.
-- ------------------------------------------------------------

-- COMPLIANT: All columns in every table hold exactly one value.
--   Example: students.first_name and students.last_name are
--   stored separately (not as 'Arjun Mehta' in one column).
--
-- HYPOTHETICAL VIOLATION: If we had stored multiple phone
--   numbers as 'phone_numbers VARCHAR(200)' with values like
--   '9876543210, 9123456789', that would break 1NF because
--   the column is no longer atomic — it holds a list.
--   Fix: create a separate student_phones table.
--
-- CONCLUSION: All 5 tables satisfy 1NF. ✓

-- ------------------------------------------------------------
-- 2NF (Second Normal Form)
-- Rule: Must be in 1NF. Every non-key column must be FULLY
--       dependent on the ENTIRE primary key (no partial deps).
--       Relevant only when a table has a composite primary key.
-- ------------------------------------------------------------
select *from enrollments;
-- FOCUS TABLE: enrollments
--   Candidate composite key: (student_id, course_id)
--   Columns: enrollment_id, enrollment_date, grade
--
--   - enrollment_date depends on BOTH student_id + course_id
--     (it's the date a specific student enrolled in a specific
--     course) → FULL DEPENDENCY ✓
--   - grade depends on BOTH student_id + course_id
--     (a student's grade is per course) → FULL DEPENDENCY ✓
--
-- HYPOTHETICAL VIOLATION: If we stored course_name inside the
--   enrollments table, it would only depend on course_id
--   (not on student_id) — a PARTIAL dependency, violating 2NF.
--   Fix: course_name stays in the courses table (already done).
--
-- CONCLUSION: enrollments satisfies 2NF. All other tables have
--   a single-column PK, so partial dependency is impossible. ✓


-- ------------------------------------------------------------
-- 3NF (Third Normal Form)
-- Rule: Must be in 2NF. No transitive dependencies.
--       Non-key column C must NOT depend on another
--       non-key column B which depends on the primary key A.
--       (A → B → C is a violation; A → C directly is fine.)
-- ------------------------------------------------------------

-- FOCUS: students table
--   students.department_id (FK) → departments.dept_name
--   If we stored dept_name directly in students:
--     student_id → department_id → dept_name  (transitive!)
--   This would be a 3NF violation.
--   Fix: dept_name lives in departments, referenced via FK. ✓
--
-- FOCUS: enrollments table
--   enrollment_id → student_id → first_name (transitive!)
--   enrollment_id → course_id  → course_name (transitive!)
--   Neither student names nor course names are stored in
--   enrollments — they are referenced via FK. ✓
--
-- FOCUS: professors table
--   professor_id → department_id → dept_name (would be transitive)
--   dept_name is NOT stored in professors — only the FK. ✓
--
-- CONCLUSION: No transitive dependencies exist in any table.
--   All 5 tables satisfy 3NF. ✓

-- ------------------------------------------------------------
-- OVERALL NORMALISATION SUMMARY
-- ------------------------------------------------------------
-- Table              1NF   2NF   3NF
-- departments         ✓     ✓     ✓
-- students            ✓     ✓     ✓   (dept stored via FK)
-- courses             ✓     ✓     ✓   (dept stored via FK)
-- enrollments         ✓     ✓     ✓   (no partial/transitive deps)
-- professors          ✓     ✓     ✓   (dept stored via FK)

-- Task 3

Alter table students add column phone_number VARCHAR(15);

select *from students;