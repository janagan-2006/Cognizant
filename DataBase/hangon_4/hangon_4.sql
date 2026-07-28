-- ============================================================
-- HANDS-ON 4 | TASK 1: Baseline Performance — No Indexes
-- college_db — EXPLAIN, Query Plans, Seq Scan Detection
-- ============================================================

-- ------------------------------------------------------------
-- STEP 48: Run EXPLAIN on the join query
-- ------------------------------------------------------------

-- MySQL:
EXPLAIN FORMAT=JSON
SELECT s.first_name, s.last_name, c.course_name 
FROM enrollments e 
JOIN students s ON s.student_id = e.student_id 
JOIN courses c ON c.course_id = e.course_id 
WHERE s.enrollment_year = 2022;

-- PostgreSQL:
-- EXPLAIN
-- SELECT s.first_name, s.last_name, c.course_name 
-- FROM enrollments e 
-- JOIN students s ON s.student_id = e.student_id 
-- JOIN courses c ON c.course_id = e.course_id 
-- WHERE s.enrollment_year = 2022;

-- ------------------------------------------------------------
-- SAMPLE OUTPUT (MySQL EXPLAIN, simplified — yours may vary
-- slightly depending on MySQL version and table size):
-- ------------------------------------------------------------
--
-- +----+-------------+-------+------+---------------+------+---------+------+------+-------------+
-- | id | select_type | table | type | possible_keys | key  | key_len | ref  | rows | Extra       |
-- +----+-------------+-------+------+---------------+------+---------+------+------+-------------+
-- |  1 | SIMPLE      | s     | ALL  | NULL          | NULL | NULL    | NULL |   10 | Using where |
-- |  1 | SIMPLE      | e     | ALL  | NULL          | NULL | NULL    | NULL |   10 | Using join  |
-- |  1 | SIMPLE      | c     | ALL  | NULL          | NULL | NULL    | NULL |    5 | Using join  |
-- +----+-------------+-------+------+---------------+------+---------+------+------+-------------+
--
-- Sample PostgreSQL EXPLAIN output:
--
-- Hash Join  (cost=1.11..1.45 rows=6 width=72)
--   Hash Cond: (e.course_id = c.course_id)
--   ->  Hash Join  (cost=1.07..1.39 rows=6 width=60)
--         Hash Cond: (e.student_id = s.student_id)
--         ->  Seq Scan on enrollments e  (cost=0.00..1.10 rows=10 width=12)
--         ->  Hash  (cost=1.06..1.06 rows=5 width=52)
--               ->  Seq Scan on students s  (cost=0.00..1.06 rows=5 width=52)
--                     Filter: (enrollment_year = 2022)
--   ->  Hash  (cost=1.03..1.03 rows=3 width=20)
--         ->  Seq Scan on courses c  (cost=0.00..1.03 rows=3 width=72)

-- ------------------------------------------------------------
-- STEP 49: Identify Sequential Scan / Full Table Scan
-- ------------------------------------------------------------

-- IDENTIFIED: In MySQL, "type: ALL" on each table means a FULL
-- TABLE SCAN — MySQL reads every row of students, enrollments,
-- and courses with no index lookup.
--
-- In PostgreSQL, the plan explicitly shows "Seq Scan on students s"
-- with "Filter: (enrollment_year = 2022)" — this means PostgreSQL
-- scans every row in the students table and checks the
-- enrollment_year filter row-by-row, since there's no index on
-- that column yet.
--
-- All three tables (students, enrollments, courses) currently
-- undergo a full scan, because no indexes exist beyond the
-- automatic ones on PRIMARY KEY columns.

-- ------------------------------------------------------------
-- STEP 50: Note estimated cost / rows examined
-- ------------------------------------------------------------

-- MySQL: 'rows' column shows estimated rows examined per table:
--   students: 10 rows examined (type=ALL — full scan)
--   enrollments: 10 rows examined (type=ALL — full scan)
--   courses: 5 rows examined (type=ALL — full scan)
--
-- PostgreSQL: 'cost=0.00..1.10' format means:
--   startup_cost..total_cost (arbitrary cost units, not seconds)
--   - Seq Scan on enrollments: cost 0.00 to 1.10
--   - Seq Scan on students: cost 0.00 to 1.06 (with filter applied)
--   - Seq Scan on courses: cost 0.00 to 1.03
--   - Final Hash Join total cost: ~1.45
--
-- NOTE: With this tiny sample dataset (only 8-10 rows per table),
-- the optimizer may actually CHOOSE a Seq Scan even after you add
-- an index in Task 2 — sequential scans are often cheaper than
-- index lookups when a table is small enough to fit in one or
-- two disk/memory pages. This is expected and not a bug; the real
-- difference becomes visible only with thousands+ of rows.
-- ============================================================
-- HANDS-ON 4 | TASK 2: Add Indexes and Compare Plans
-- college_db — B-Tree, Composite, Partial Indexes
-- ============================================================

-- ------------------------------------------------------------
-- STEP 51: B-Tree index on students.enrollment_year
-- ------------------------------------------------------------

CREATE INDEX idx_students_enrollment_year
ON students (enrollment_year);

-- B-Tree is the DEFAULT index type in both MySQL and PostgreSQL,
-- so no special syntax is needed — this is already a B-Tree.

-- ------------------------------------------------------------
-- STEP 52: Composite UNIQUE index on
-- enrollments(student_id, course_id)
-- (also prevents duplicate enrollments)
-- ------------------------------------------------------------

CREATE UNIQUE INDEX idx_enrollments_student_course
ON enrollments (student_id, course_id);

-- NOTE: This will FAIL if duplicate (student_id, course_id) pairs
-- already exist in your data. Check first:
-- SELECT student_id, course_id, COUNT(*) 
-- FROM enrollments 
-- GROUP BY student_id, course_id 
-- HAVING COUNT(*) > 1;
-- (Should return 0 rows if your data is clean.)

-- Test that duplicates are now blocked:
-- INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
-- VALUES (1, 1, '2024-01-01', 'A');
-- ERROR: Duplicate entry '1-1' for key 'idx_enrollments_student_course'
-- (since student 1 is already enrolled in course 1)

-- ------------------------------------------------------------
-- STEP 53: Index on courses.course_code
-- ------------------------------------------------------------

CREATE INDEX idx_courses_course_code
ON courses (course_code);

-- This speeds up lookups like:
-- SELECT * FROM courses WHERE course_code = 'CS101';

-- ------------------------------------------------------------
-- STEP 54: Re-run EXPLAIN from Task 1 and compare
-- ------------------------------------------------------------

-- MySQL:
EXPLAIN FORMAT=JSON
SELECT s.first_name, s.last_name, c.course_name 
FROM enrollments e 
JOIN students s ON s.student_id = e.student_id 
JOIN courses c ON c.course_id = e.course_id 
WHERE s.enrollment_year = 2022;

-- PostgreSQL:
-- EXPLAIN
-- SELECT s.first_name, s.last_name, c.course_name 
-- FROM enrollments e 
-- JOIN students s ON s.student_id = e.student_id 
-- JOIN courses c ON c.course_id = e.course_id 
-- WHERE s.enrollment_year = 2022;

-- ------------------------------------------------------------
-- COMPARISON COMMENT (document your observation here):
-- ------------------------------------------------------------
--
-- BEFORE (Task 1): type=ALL on students (full scan), 10 rows examined
-- AFTER (Task 2):  type=ref, possible_keys=idx_students_enrollment_year,
--                   key=idx_students_enrollment_year — MySQL now uses
--                   the index to jump directly to enrollment_year=2022
--                   rows, instead of scanning the whole table.
--
-- IMPORTANT CAVEAT: With this small sample dataset (8-10 rows), the
-- query optimizer may STILL choose a Seq Scan / type=ALL even with
-- the index present, because reading ~10 rows sequentially can be
-- cheaper than an index lookup + row fetch. This is NOT a bug — it's
-- the optimizer correctly judging that the index isn't worth using
-- yet at this tiny scale. The plan change becomes obvious and
-- consistent once the table has thousands of rows.
--
-- To FORCE the index and observe the Index Scan behavior for this
-- exercise (PostgreSQL):
--   SET enable_seqscan = OFF;
--   EXPLAIN SELECT ... -- (same query as above)
--   SET enable_seqscan = ON;  -- reset back to normal afterward
--
-- In MySQL, you can hint the optimizer directly:
--   EXPLAIN SELECT s.first_name, s.last_name, c.course_name
--   FROM enrollments e
--   JOIN students s FORCE INDEX (idx_students_enrollment_year)
--     ON s.student_id = e.student_id
--   JOIN courses c ON c.course_id = e.course_id
--   WHERE s.enrollment_year = 2022;

-- ------------------------------------------------------------
-- STEP 55: Partial index on enrollments(student_id)
-- WHERE grade IS NULL
-- ------------------------------------------------------------

-- PostgreSQL syntax (partial indexes are a PostgreSQL-specific feature):
CREATE INDEX idx_enrollments_null_grade
ON enrollments (student_id)
WHERE grade IS NULL;

-- NOTE: MySQL does NOT support partial/filtered indexes natively
-- (as of MySQL 8.x). The closest MySQL equivalent is a regular
-- index on (grade, student_id), or using a generated/virtual
-- column with a WHERE-like condition baked in, but it's not the
-- same mechanism. If you're on MySQL, document this limitation:
--
-- -- MySQL has no native partial index support. Closest alternative:
-- CREATE INDEX idx_enrollments_grade_student
-- ON enrollments (grade, student_id);

-- Test the partial index helps this specific query pattern:
-- SELECT * FROM enrollments WHERE student_id = 4 AND grade IS NULL;
-- EXPLAIN should show the partial index being used (PostgreSQL only).

-- NOTE: After Hands-On 2's DELETE step (removing all NULL-grade
-- rows), this partial index will currently index ZERO rows — that's
-- fine; it's still valid and will activate the moment any future
-- enrollment is inserted with a NULL grade.

-- ------------------------------------------------------------
-- STEP 59: Document the N+1 cost at scale (write as a comment
-- in your script or .sql file)
-- ------------------------------------------------------------

-- With 12 enrollments (current sample data after Hands-On 2's
-- NULL-grade deletes), the N+1 version issues:
--   1 (fetch all enrollments) + 12 (one per enrollment) = 13 queries
-- The JOIN version issues: 1 query total.
--
-- AT SCALE — with 10,000 enrollments:
--   N+1 version: 1 + 10,000 = 10,001 queries
--   JOIN version: still just 1 query
--   Extra queries issued by N+1: 10,000 (literally one wasted
--   round-trip to the database PER ROW)
--
-- Each round-trip carries network latency overhead (even on
-- localhost, there's connection/protocol overhead per query).
-- At 10,000 extra queries, even 1ms of overhead per query adds
-- up to 10 seconds of pure overhead — on top of the actual query
-- execution time itself. This is why N+1 is considered one of the
-- most damaging and common performance bugs in real applications.