# ============================================================
# HANDS-ON 6 | TASK 2: CRUD Operations via ORM
# college_db_orm — SQLAlchemy Session API
# ============================================================

from sqlalchemy.orm import sessionmaker
import datetime

from task1 import Base, Department, Student, Course, Enrollment, Professor, engine

# ------------------------------------------------------------
# STEP 80: Open a Session using sessionmaker
# ------------------------------------------------------------

# Reuse the shared engine from task1 so both scripts point at the same DB.
engine.echo = True
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def get_or_create_department(dept_name, hod_name, budget):
    department = session.query(Department).filter(Department.dept_name == dept_name).first()
    if department is None:
        department = Department(dept_name=dept_name, hod_name=hod_name, budget=budget)
        session.add(department)
        session.flush()
    return department


def get_or_create_student(first_name, last_name, email, date_of_birth, department_id, enrollment_year):
    student = session.query(Student).filter(Student.email == email).first()
    if student is None:
        student = Student(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date_of_birth=date_of_birth,
            department_id=department_id,
            enrollment_year=enrollment_year,
        )
        session.add(student)
        session.flush()
    return student


def get_or_create_course(course_name, course_code, credits, department_id):
    course = session.query(Course).filter(Course.course_code == course_code).first()
    if course is None:
        course = Course(
            course_name=course_name,
            course_code=course_code,
            credits=credits,
            department_id=department_id,
        )
        session.add(course)
        session.flush()
    return course


def get_or_create_enrollment(student_id, course_id, enrollment_date, grade):
    enrollment = (
        session.query(Enrollment)
        .filter(Enrollment.student_id == student_id, Enrollment.course_id == course_id)
        .first()
    )
    if enrollment is None:
        enrollment = Enrollment(
            student_id=student_id,
            course_id=course_id,
            enrollment_date=enrollment_date,
            grade=grade,
        )
        session.add(enrollment)
        session.flush()
    return enrollment


# ------------------------------------------------------------
# STEP 81: INSERT — 3 Departments, 5 Students
# ------------------------------------------------------------

dept_cs = get_or_create_department("Computer Science", "Dr. Ramesh Kumar", 850000.00)
dept_ec = get_or_create_department("Electronics", "Dr. Priya Nair", 620000.00)
dept_me = get_or_create_department("Mechanical", "Dr. Suresh Iyer", 540000.00)

student1 = get_or_create_student(
    "Arjun",
    "Mehta",
    "arjun.mehta@college.edu",
    datetime.date(2003, 4, 12),
    dept_cs.department_id,
    2022,
)
student2 = get_or_create_student(
    "Priya",
    "Suresh",
    "priya.suresh@college.edu",
    datetime.date(2003, 7, 25),
    dept_cs.department_id,
    2022,
)
student3 = get_or_create_student(
    "Rohan",
    "Verma",
    "rohan.verma@college.edu",
    datetime.date(2002, 11, 8),
    dept_ec.department_id,
    2021,
)
student4 = get_or_create_student(
    "Sneha",
    "Patel",
    "sneha.patel@college.edu",
    datetime.date(2004, 1, 30),
    dept_me.department_id,
    2023,
)
student5 = get_or_create_student(
    "Vikram",
    "Das",
    "vikram.das@college.edu",
    datetime.date(2003, 9, 14),
    dept_cs.department_id,
    2022,
)

session.commit()


# ------------------------------------------------------------
# STEP 82: INSERT — 3 Courses, 4 Enrollments
# ------------------------------------------------------------

course1 = get_or_create_course(
    "Data Structures & Algorithms",
    "CS101",
    4,
    dept_cs.department_id,
)
course2 = get_or_create_course(
    "Database Management Systems",
    "CS102",
    3,
    dept_cs.department_id,
)
course3 = get_or_create_course(
    "Circuit Theory",
    "EC101",
    3,
    dept_ec.department_id,
)

enrollment1 = get_or_create_enrollment(
    student1.student_id,
    course1.course_id,
    datetime.date(2022, 7, 1),
    "A",
)
enrollment2 = get_or_create_enrollment(
    student1.student_id,
    course2.course_id,
    datetime.date(2022, 7, 1),
    "B",
)
enrollment3 = get_or_create_enrollment(
    student2.student_id,
    course1.course_id,
    datetime.date(2022, 7, 1),
    "B",
)
enrollment4 = get_or_create_enrollment(
    student3.student_id,
    course3.course_id,
    datetime.date(2021, 7, 1),
    "A",
)

session.commit()


# ------------------------------------------------------------
# STEP 83: READ — all students in 'Computer Science'
# ------------------------------------------------------------

cs_students = (
    session.query(Student)
    .join(Department)
    .filter(Department.dept_name == "Computer Science")
    .all()
)

print("\n--- Computer Science students ---")
for s in cs_students:
    print(f"{s.first_name} {s.last_name}")


# ------------------------------------------------------------
# STEP 84: READ — all enrollments with student + course names
# (echo=True already enabled above — watch the console SQL log)
# ------------------------------------------------------------

print("\n--- Enrollments (watch the SQL log above this print!) ---")
all_enrollments = session.query(Enrollment).all()   # query #1

for e in all_enrollments:
    # e.student and e.course are LAZY-LOADED relationships —
    # accessing them HERE triggers a NEW query each time, per row
    print(f"{e.student.first_name} {e.student.last_name} -> {e.course.course_name}")

# WITH 4 ENROLLMENTS, EXPECTED SQL LOG SHOWS:
#   1 query to fetch all enrollments
#   + 4 queries to lazy-load e.student (one per row)
#   + 4 queries to lazy-load e.course (one per row)
#   = 9 queries total for what LOOKS like one simple loop.
# THIS IS THE N+1 PROBLEM — confirmed live via echo=True logging.


# ------------------------------------------------------------
# STEP 85: UPDATE — find student by email, update enrollment_year
# ------------------------------------------------------------

student_to_update = (
    session.query(Student)
    .filter(Student.email == "arjun.mehta@college.edu")
    .first()
)
student_to_update.enrollment_year = 2023
session.commit()

print(f"\nUpdated {student_to_update.first_name}'s enrollment_year to {student_to_update.enrollment_year}")


# ------------------------------------------------------------
# STEP 86: DELETE — remove an enrollment record
# ------------------------------------------------------------

enrollment_to_delete = (
    session.query(Enrollment)
    .filter(Enrollment.student_id == student3.student_id,
            Enrollment.course_id == course3.course_id)
    .first()
)
if enrollment_to_delete is not None:
    session.delete(enrollment_to_delete)
    session.commit()

    # Verify deletion
    remaining = session.query(Enrollment).count()
    print(f"\nRemaining enrollments after delete: {remaining}")
else:
    print("\nEnrollment already deleted; remaining enrollments unchanged.")

session.close()