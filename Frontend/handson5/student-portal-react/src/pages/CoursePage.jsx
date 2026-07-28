import { useState, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { Link } from 'react-router-dom';
import CourseCard from '../components/CourseCart';
import { enroll } from '../store/enrollmentSlice';

function CoursesPage() {
  const dispatch = useDispatch();
  const [courses, setCourses] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadCourses() {
      try {
        setLoading(true);
        setError(null);

        const response = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=5');
        if (!response.ok) {
          throw new Error(`Request failed: ${response.status}`);
        }
        const posts = await response.json();

        const mappedCourses = posts.map((post, index) => ({
          id: post.id,
          name: post.title.slice(0, 30),
          code: `CS10${index + 1}`,
          credits: 3 + (index % 2),
          grade: ['A', 'B+', 'A-', 'B', 'A'][index % 5]
        }));

        setCourses(mappedCourses);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    loadCourses();
  }, []);

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <section id="courses">
      <h2>Enrolled Courses</h2>

      <input
        type="text"
        placeholder="Search courses..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        className="search-input"
      />

      {loading && <p className="status-msg">Loading...</p>}
      {error && <p className="status-msg error-msg">Couldn't load courses: {error}</p>}

      {!loading && !error && (
        <div className="course-grid">
          {filteredCourses.map((course) => (
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