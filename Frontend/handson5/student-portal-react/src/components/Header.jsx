import { Link } from 'react-router-dom';

function Header({ siteName, enrolledCount = 0 }) {
  return (
    <header className="header">
      <div className="header-brand">
        <Link to="/" className="brand-link">
          {siteName}
        </Link>
      </div>

      <nav className="header-nav">
        <Link to="/">Home</Link>
        <Link to="/courses">Courses</Link>
        <Link to="/profile">Profile</Link>
      </nav>

      <p className="enrolled-count">Enrolled: {enrolledCount}</p>
    </header>
  );
}

export default Header;