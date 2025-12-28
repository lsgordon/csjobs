import { Link, useLocation } from 'react-router-dom';

const NavBar = () => {
  const location = useLocation();
  const isActive = (path) => location.pathname === path ? 'nav-link active' : 'nav-link';

  return (
    <nav className="navbar">
      <Link to="/" className="nav-brand">csjobs</Link>
      <div className="nav-links">
        <Link to="/" className={isActive('/')}>Home</Link>
        <Link to="/new-grad" className={isActive('/new-grad')}>New Grad</Link>
        <Link to="/internships" className={isActive('/internships')}>Internships</Link>
        <Link to="/about" className={isActive('/about')}>About</Link>
        <Link to="/login" className={isActive('/login')}>Login</Link>
        <Link to="/search" className={isActive('/search')}>Search</Link>
      </div>
    </nav>
  );
};

export default NavBar;