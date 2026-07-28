-- task1
-- 18
update enrollments set grade='B' where student_id=5 and course_id=1;
SET SQL_SAFE_UPDATES = 1;
delete from enrollments where grade is null;
select *from enrollments;
select count(*) from enrollments;

-- task2
select *from students s inner join enrollments e on e.student_id=s.student_id 
where e.enrollment_date>='2022-01-01' and e.enrollment_date<='2022-12-31' 
order by last_name ;

select *from courses where credits>3;

select *from professors where salary between 80000 and 95000;
select *from students where email like '%@college.edu';
select count(student_id), year(enrollment_date) from enrollments group by year(enrollment_date);
-- nice
-- task 3
select *from students;
SELECT 
    CONCAT(s.first_name, ' ', s.last_name) AS full_name,
    d.dept_name
FROM students s
INNER JOIN departments d ON s.department_id = d.department_id
ORDER BY full_name;

SELECT 
    e.enrollment_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    c.course_name,
    e.enrollment_date,
    e.grade
FROM enrollments e
INNER JOIN students s ON e.student_id = s.student_id
INNER JOIN courses c ON e.course_id = c.course_id
ORDER BY e.enrollment_id;

SELECT 
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS full_name
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE e.enrollment_id IS NULL;

SELECT 
    c.course_id,
    c.course_name,
    COUNT(e.enrollment_id) AS student_count
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
ORDER BY c.course_id;

select count(student_id) from enrollments group by course_id having count(student_id)>=0;

SELECT 
*FROM departments d
LEFT JOIN professors p ON d.department_id = p.department_id
ORDER BY d.dept_name, p.prof_name;

-- task 4

SELECT 
    c.course_name,
    COUNT(e.enrollment_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
ORDER BY enrollment_count DESC;

SELECT 
    d.dept_name,
    ROUND(AVG(p.salary), 2) AS avg_salary
FROM departments d
JOIN professors p ON d.department_id = p.department_id
GROUP BY d.department_id, d.dept_name
ORDER BY avg_salary DESC;


SELECT 
    dept_name,
    budget
FROM departments
WHERE budget > 600000
ORDER BY budget DESC;

SELECT 
    e.grade,
    COUNT(*) AS grade_count
FROM enrollments e
JOIN courses c ON e.course_id = c.course_id
WHERE c.course_code = 'CS101'
GROUP BY e.grade
ORDER BY e.grade;SELECT 
    d.dept_name,
    COUNT(DISTINCT e.student_id) AS student_count
FROM departments d
JOIN courses c ON d.department_id = c.department_id
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY d.department_id, d.dept_name
HAVING COUNT(DISTINCT e.student_id) > 2
ORDER BY student_count DESC;