-- task 1

select s.student_id, concat(s.first_name,' ',s.last_name) as fullname, count(e.enrollment_id) as `count`,avg_data.enrollementcount  from students s
 join enrollments e on e.student_id=s.student_id
 cross join (
select avg(enrollmentcount) as enrollementcount from (
select count(*) as enrollmentcount from enrollments group by student_id
) as per_count_students) as avg_data
group by s.student_id,avg_data.enrollementcount having count(e.enrollment_id)> avg_data.enrollementcount;

SELECT c.course_id, c.course_name
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
HAVING COUNT(*) = SUM(CASE WHEN e.grade = 'A' THEN 1 ELSE 0 END);
SELECT 1 FROM enrollments e WHERE e.course_id = 1;

select *from professors p join departments d on d.department_id=p.department_id;
select prof_name from professors group by department_id having salary=Max(salary);

SELECT 
    p.professor_id,
    p.prof_name,
    p.department_id,
    p.salary
FROM professors p
WHERE p.salary = (
    -- Correlated subquery: re-runs per outer row, scoped to
    -- the SAME department as the current professor
    SELECT MAX(p2.salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
)
ORDER BY p.department_id;

SELECT 
    dept_avg.department_id,
    d.dept_name,
    dept_avg.avg_salary
FROM (
    -- Derived table: MUST have an alias (dept_avg here)
    SELECT department_id, ROUND(AVG(salary), 2) AS avg_salary
    FROM professors
    GROUP BY department_id
) AS dept_avg
JOIN departments d ON dept_avg.department_id = d.department_id
WHERE dept_avg.avg_salary > 85000
ORDER BY dept_avg.avg_salary DESC;

-- task 2

CREATE VIEW vw_student_enrollment_summary AS
SELECT 
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS full_name,
    d.dept_name,
    COUNT(e.enrollment_id) AS courses_enrolled,
    ROUND(AVG(
        CASE e.grade
            WHEN 'A' THEN 4
            WHEN 'B' THEN 3
            WHEN 'C' THEN 2
            WHEN 'D' THEN 1
            WHEN 'F' THEN 0
        END
    ), 2) AS gpa
FROM students s
JOIN departments d ON s.department_id = d.department_id
LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id;
select *from vw_student_enrollment_summary;
select *from courses;
create view vw_course_stats as
select c.course_name, c.course_code,count(e.enrollment_id) as total_enrollment,
    ROUND(AVG(
        CASE e.grade
            WHEN 'A' THEN 4
            WHEN 'B' THEN 3
            WHEN 'C' THEN 2
            WHEN 'D' THEN 1
            WHEN 'F' THEN 0
        END
    ), 2) AS avg_gpa
 from courses c
left join enrollments e on c.course_id=e.course_id group by c.course_id;

select c.course_name, c.course_code,count(e.enrollment_id) as total_enrollment,
    ROUND(AVG(
        CASE e.grade
            WHEN 'A' THEN 4
            WHEN 'B' THEN 3
            WHEN 'C' THEN 2
            WHEN 'D' THEN 1
            WHEN 'F' THEN 0
        END
    ), 2) AS avg_gpa
 from courses c
left join enrollments e on c.course_id=e.course_id group by c.course_id;

select s.student_id,  	round(avg(
        CASE e.grade
            WHEN 'A' THEN 4
            WHEN 'B' THEN 3
            WHEN 'C' THEN 2
            WHEN 'D' THEN 1
            WHEN 'F' THEN 0
        END),2) AS total_gpa
    from students s 
    left join enrollments e on s.student_id=e.student_id group by s.student_id HAVING total_gpa > 3;
    
-- update inside the view will not work when I am using group by or distinct in the view 
-- otherwise update will work and also it will change the under layer table not only in the virtual table

drop view vw_student_enrollment_summary;
drop view vw_course_stats;

CREATE VIEW vw_student_enrollment_summary AS
SELECT 
    student_id,
    first_name,
    last_name,
    email,
    department_id,
    enrollment_year
FROM students
WHERE department_id = 1   -- Computer Science only
WITH CHECK OPTION;

-- ============================================================
-- HANDS-ON 3 | TASK 3: Stored Procedures and Transactions
-- college_db — Procedures, Transactions, SAVEPOINT
-- ============================================================

-- ------------------------------------------------------------
-- STEP 44: sp_enroll_student — checks for duplicate enrollment,
-- then inserts the record
-- ------------------------------------------------------------

-- MySQL syntax:
DELIMITER $$

CREATE PROCEDURE sp_enroll_student (
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN
    DECLARE existing_count INT;

    -- Check if this student is already enrolled in this course
    SELECT COUNT(*) INTO existing_count
    FROM enrollments
    WHERE student_id = p_student_id AND course_id = p_course_id;

    IF existing_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Duplicate enrollment: student is already enrolled in this course.';
    ELSE
        INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
        VALUES (p_student_id, p_course_id, p_enrollment_date, NULL);
    END IF;
END$$

DELIMITER ;

-- Test it:
-- CALL sp_enroll_student(1, 1, '2024-01-15'); -- should FAIL (student 1 already in course 1)
-- CALL sp_enroll_student(3, 1, '2024-01-15'); -- should SUCCEED (new pairing)

-- ------------------------------------------------------------
-- PostgreSQL equivalent (function instead of procedure):
-- ------------------------------------------------------------
-- CREATE OR REPLACE FUNCTION fn_enroll_student(
--     p_student_id INT, p_course_id INT, p_enrollment_date DATE
-- ) RETURNS VOID AS $$
-- DECLARE
--     existing_count INT;
-- BEGIN
--     SELECT COUNT(*) INTO existing_count
--     FROM enrollments
--     WHERE student_id = p_student_id AND course_id = p_course_id;
--
--     IF existing_count > 0 THEN
--         RAISE EXCEPTION 'Duplicate enrollment: student is already enrolled in this course.';
--     ELSE
--         INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
--         VALUES (p_student_id, p_course_id, p_enrollment_date, NULL);
--     END IF;
-- END;
-- $$ LANGUAGE plpgsql;


-- ------------------------------------------------------------
-- STEP 45: sp_transfer_student — moves a student between
-- departments, logs the transfer, wrapped in a transaction
-- ------------------------------------------------------------

-- First, create the log table:
CREATE TABLE department_transfer_log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    old_department_id INT,
    new_department_id INT,
    transfer_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$

CREATE PROCEDURE sp_transfer_student (
    IN p_student_id INT,
    IN p_new_department_id INT
)
BEGIN
    DECLARE old_dept INT;

    -- If anything inside fails, roll back everything
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;  -- re-throw the error so the caller sees it
    END;

    START TRANSACTION;

    SELECT department_id INTO old_dept
    FROM students
    WHERE student_id = p_student_id;

    UPDATE students
    SET department_id = p_new_department_id
    WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log (student_id, old_department_id, new_department_id)
    VALUES (p_student_id, old_dept, p_new_department_id);

    COMMIT;
END$$

DELIMITER ;

-- Test it:
-- CALL sp_transfer_student(3, 1);  -- moves student 3 from dept 2 to dept 1
-- SELECT * FROM department_transfer_log;

-- ------------------------------------------------------------
-- STEP 46: Test the transaction by introducing an invalid FK
-- and verify the UPDATE also rolls back
-- ------------------------------------------------------------

-- Manual test (run these lines directly, not inside the procedure,
-- to see ROLLBACK behavior explicitly):

START TRANSACTION;

UPDATE students
SET department_id = 1
WHERE student_id = 3;

-- Intentionally invalid FK — department_id 999 does not exist
INSERT INTO department_transfer_log (student_id, old_department_id, new_department_id)
VALUES (3, 2, 999999);  -- this won't actually fail unless new_department_id has an FK constraint

-- To make this genuinely fail, try inserting into a column with
-- a real FK constraint, e.g., attempting to set students.department_id
-- to a non-existent department:
-- UPDATE students SET department_id = 999 WHERE student_id = 3;
-- ERROR: Cannot add or update a child row: a foreign key constraint fails

ROLLBACK;

-- Verify: student 3's department_id should be UNCHANGED (back to 2)
SELECT department_id FROM students WHERE student_id = 3;

-- ------------------------------------------------------------
-- STEP 47: SAVEPOINT — partial rollback test
-- ------------------------------------------------------------

START TRANSACTION;

-- First insert (we want this one to SURVIVE)
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
VALUES (3, 2, '2024-01-15', 'A');

SAVEPOINT after_first_insert;

-- Second insert — deliberately fail it with an invalid FK
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
VALUES (999, 999, '2024-01-15', 'A');  -- student_id 999 doesn't exist → FK violation

-- If the above line throws an error, run this to undo ONLY
-- the failed second insert, while keeping the first one:
ROLLBACK TO SAVEPOINT after_first_insert;

COMMIT;

-- Verify: only the FIRST insert (student 3, course 2) should exist
SELECT * FROM enrollments WHERE student_id = 3 AND course_id = 2;
