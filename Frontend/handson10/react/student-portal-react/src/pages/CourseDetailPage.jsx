import { useState, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { useParams, useNavigate } from 'react-router-dom';
import { enroll } from '../store/enrollmentSlice';
import { getCourseById } from '../api/courseApi';

function CourseDetailPage() {
  const dispatch = useDispatch();
  const { courseId } = useParams();
  const navigate = useNavigate();
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadCourse() {
      try {
        setLoading(true);
        setError(null);
        const data = await getCourseById(courseId);
        setCourse(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
    loadCourse();
  }, [courseId]);

  function handleEnroll() {
    dispatch(enroll(course));
    navigate('/profile');
  }

  if (loading) return <p className="status-msg">Loading course details...</p>;
  if (error) return <p className="status-msg error-msg">{error}</p>;
  if (!course) return <p className="status-msg error-msg">Course not found.</p>;

  return (
    <section className="course-detail">
      <h2>{course.name}</h2>
      <p className="code">{course.code}</p>
      <p>{course.description}</p>
      <p><strong>Credits:</strong> {course.credits}</p>
      <p><strong>Grade:</strong> {course.grade}</p>
      <button type="button" onClick={handleEnroll}>
        Enroll &amp; Go to Profile
      </button>
    </section>
  );
}

export default CourseDetailPage;
