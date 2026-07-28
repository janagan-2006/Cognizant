import { useSelector, useDispatch } from 'react-redux';
import StudentProfile from '../components/StudentProfile';
import { unenroll } from '../store/enrollmentSlice';

function ProfilePage() {
  const dispatch = useDispatch();
  const enrolledCourses = useSelector((state) => state.enrollment.enrolledCourses);

  return (
    <>
      <StudentProfile />

      <section className="enrolled-list">
        <h2>My Enrolled Courses</h2>
        {enrolledCourses.length === 0 ? (
          <p className="status-msg">No courses enrolled yet.</p>
        ) : (
          <ul>
            {enrolledCourses.map((course) => (
              <li key={course.id}>
                {course.name} — {course.credits} credits
                <button
                  type="button"
                  className="remove-btn"
                  onClick={() => dispatch(unenroll(course.id))}
                >
                  Remove
                </button>
              </li>
            ))}
          </ul>
        )}
      </section>
    </>
  );
}

export default ProfilePage;