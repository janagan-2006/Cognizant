import os

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Numeric, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


# ------------------------------------------------------------
# STEP 76: Define an engine connecting to college_db
# ------------------------------------------------------------

# Use DATABASE_URL when available; otherwise fall back to a local SQLite file
# so the script can run without a separate database server.
database_url = os.getenv("DATABASE_URL", "sqlite:///college_db_orm.db")
engine_kwargs = {"echo": False}

if database_url.startswith("sqlite"):
    engine_kwargs["connect_args"] = {"check_same_thread": False}

engine = create_engine(database_url, **engine_kwargs)

# MySQL alternative (commented):
# engine = create_engine(
#     "mysql+mysqlconnector://username:password@localhost:3306/college_db_orm",
#     echo=False
# )


# ------------------------------------------------------------
# STEP 77 & 78: Define 5 ORM model classes with relationships
# ------------------------------------------------------------

class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, autoincrement=True)
    dept_name = Column(String(100), nullable=False)
    hod_name = Column(String(100))
    budget = Column(Numeric(12, 2))

    # One department has MANY students/courses/professors
    students = relationship("Student", back_populates="department")
    courses = relationship("Course", back_populates="department")
    professors = relationship("Professor", back_populates="department")


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    date_of_birth = Column(Date)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    enrollment_year = Column(Integer)

    # STEP 78: many-to-one — many students belong to ONE department
    department = relationship("Department", back_populates="students")

    # One student has MANY enrollments
    enrollments = relationship("Enrollment", back_populates="student")


class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(150), nullable=False)
    course_code = Column(String(20), unique=True)
    credits = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.department_id"))

    department = relationship("Department", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")


class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    enrollment_date = Column(Date)
    grade = Column(String(2))

    # STEP 78: many-to-one — many enrollments belong to ONE student/course
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True, autoincrement=True)
    prof_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    salary = Column(Numeric(10, 2))

    department = relationship("Department", back_populates="professors")


# ------------------------------------------------------------
# STEP 79: Auto-create tables in a fresh database
# ------------------------------------------------------------

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print(f"All 5 tables created successfully using {database_url}.")