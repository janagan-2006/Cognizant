import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import { selectEnrolledCount } from '../store/enrollmentSlice';

function Header({ siteName }) {
  const enrolledCount = useSelector(selectEnrolledCount);

  return (
    <header className="header">
      <div className="site-name">{siteName}</div>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/courses">Courses</Link></li>
          <li><Link to="/profile">Profile</Link></li>
        </ul>
      </nav>
      <div className="enrolled-count">Enrolled: {enrolledCount}</div>
    </header>
  );
}

export default Header;
