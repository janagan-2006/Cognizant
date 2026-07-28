import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hangon_6"))

from task1 import Base, Department, Student, Course, Enrollment, Professor, engine
