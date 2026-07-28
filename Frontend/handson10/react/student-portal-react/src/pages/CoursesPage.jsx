import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import CourseCard from '../components/CourseCard';
import {
  fetchAllCourses,
  enroll,
  selectCourses,
  selectCoursesLoading,
  selectCoursesError
} from '../store/enrollmentSlice';

function CoursesPage() {
  const dispatch = useDispatch();

  // Step 146: components use selectors, never direct state access
  const courses = useSelector(selectCourses);
  const loading = useSelector(selectCoursesLoading);
  const error = useSelector(selectCoursesError);

  // Step 145: dispatch the thunk in useEffect — no API calls in the component
  useEffect(() => {
    dispatch(fetchAllCourses());
  }, [dispatch]);

  return (
    <section id="courses">
      <h2>Enrolled Courses</h2>

      {loading && <p className="status-msg">Loading...</p>}

      {/* Step 147: error shown in UI when thunk rejects */}
      {error && (
        <p className="status-msg error-msg">
          Failed to load courses: {error}
        </p>
      )}

      {!loading && !error && (
        <div className="course-grid">
          {courses.map((course) => (
            <div key={course.id}>
              <Link to={`/courses/${course.id}`} className="card-link">
                <CourseCard {...course} hideButton />
              </Link>
              <button
                type="button"
                className="enroll-btn-standalone"
                onClick={() => dispatch(enroll(course))}
              >
                Enroll
              </button>
            </div>
          ))}
        </div>
      )}
    </section>
  );
}

export default CoursesPage;
