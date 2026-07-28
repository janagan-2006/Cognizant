# ============================================================
# HANDS-ON 6 | TASK 3: Eager Loading to Fix N+1
# college_db_orm — joinedload
# ============================================================

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from sqlalchemy.orm import joinedload, sessionmaker, subqueryload

from task1 import Base, Enrollment, engine


engine.echo = True
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# ------------------------------------------------------------
# STEP 87: Identify the N+1 query from Task 2 Step 5
# (already observed via echo=True logging in Task 2)
# ------------------------------------------------------------

# From Task 2, Step 84, the lazy-loading loop:
#
#   all_enrollments = session.query(Enrollment).all()       # 1 query
#   for e in all_enrollments:
#       print(e.student.first_name, e.course.course_name)    # 2 MORE queries PER ROW
#
# With 4 enrollment rows, the SQL log showed:
#   1 (fetch enrollments) + 4 (lazy-load student) + 4 (lazy-load course) = 9 queries
#
# This confirms an N+1 problem (technically "N+2N+1" here, since
# there are TWO relationships being lazy-loaded per row, not one).


# ------------------------------------------------------------
# STEP 88: Rewrite using joinedload to eliminate N+1
# ------------------------------------------------------------

print("\n--- Enrollments with joinedload (watch SQL log!) ---")

enrollments_eager = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for e in enrollments_eager:
    # e.student and e.course are ALREADY loaded — no new query fires here
    print(f"{e.student.first_name} {e.student.last_name} -> {e.course.course_name}")


# ------------------------------------------------------------
# STEP 89: Count SQL queries again — should now be 1
# ------------------------------------------------------------

# Check your console SQL log (echo=True) for this block — you
# should see exactly ONE SELECT statement, containing JOINs to
# both students and courses, regardless of how many enrollment
# rows exist.
#
# Example of the SINGLE generated SQL (simplified):
#
#   SELECT enrollments.*, students.*, courses.*
#   FROM enrollments
#   LEFT OUTER JOIN students ON students.student_id = enrollments.student_id
#   LEFT OUTER JOIN courses ON courses.course_id = enrollments.course_id;
#
enrollments_subquery = (
    session.query(Enrollment)
    .options(
        subqueryload(Enrollment.student),
        subqueryload(Enrollment.course)
    )
    .all()
)
# subqueryload issues 3 TOTAL queries (not 1):
#   1) SELECT * FROM enrollments
#   2) SELECT * FROM students WHERE student_id IN (...)   <- one IN-query for ALL rows
#   3) SELECT * FROM courses  WHERE course_id  IN (...)   <- one IN-query for ALL rows
# Both joinedload (1 query) and subqueryload (3 queries) ELIMINATE
# the N+1 pattern — they just do it via different strategies.


# ------------------------------------------------------------
# STEP 90: Document the comparison (top-of-file comment block)
# ------------------------------------------------------------

"""
=================================================================
QUERY COUNT COMPARISON — N+1 vs joinedload (Hands-On 6)
=================================================================

LAZY LOADING (Task 2, Step 84):
  for e in session.query(Enrollment).all():
      print(e.student.first_name, e.course.course_name)

  -> 1 query to fetch enrollments
  -> 4 queries to lazy-load .student (one per enrollment row)
  -> 4 queries to lazy-load .course (one per enrollment row)
  TOTAL: 9 queries for 4 enrollment rows

EAGER LOADING WITH joinedload (Task 3, Step 88):
  session.query(Enrollment)
      .options(joinedload(Enrollment.student), joinedload(Enrollment.course))
      .all()

  -> 1 SINGLE query using SQL JOINs to fetch enrollments + students
     + courses together
  TOTAL: 1 query, regardless of row count

CONCLUSION: query count went from 9 to 1 (consistent with the
13 -> 1 reduction observed in Hands-On 4 Task 3's raw-SQL version
of the same problem — same root cause, same fix, different layer
of the stack).
=================================================================
"""


# ------------------------------------------------------------
# STEP 91 (BONUS): Django ORM equivalent using select_related
# ------------------------------------------------------------

# If using Django instead of SQLAlchemy, models.py would define
# Enrollment with ForeignKey fields to Student and Course, and
# the eager-loading equivalent is:
#
#   from myapp.models import Enrollment
#
#   # LAZY (N+1) version:
#   for e in Enrollment.objects.all():
#       print(e.student.first_name, e.course.course_name)
#   # Each e.student / e.course access triggers a new query.
#
#   # EAGER (fixed) version:
#   enrollments = Enrollment.objects.select_related('student', 'course').all()
#   for e in enrollments:
#       print(e.student.first_name, e.course.course_name)
#   # select_related uses SQL JOINs, just like joinedload —
#   # same fix, same SQL-level mechanism, different ORM's API name.

session.close()