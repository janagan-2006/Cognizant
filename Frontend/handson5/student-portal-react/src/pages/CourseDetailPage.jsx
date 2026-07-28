import { useState, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { useParams, useNavigate } from 'react-router-dom';
import { enroll } from '../store/enrollmentSlice';

function CourseDetailPage() {
  const dispatch = useDispatch();
  const { courseId } = useParams();
  const navigate = useNavigate();
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadCourse() {
      setLoading(true);
      const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${courseId}`);
      const post = await response.json();

      setCourse({
        id: post.id,
        name: post.title,
        code: `CS10${post.id}`,
        credits: 3 + (post.id % 2),
        grade: 'A',
        description: post.body
      });
      setLoading(false);
    }

    loadCourse();
  }, [courseId]);

  function handleEnroll() {
    dispatch(enroll(course));
    navigate('/profile');
  }

  if (loading) return <p className="status-msg">Loading course details...</p>;
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