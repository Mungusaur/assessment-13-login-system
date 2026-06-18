import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { LayoutDashboard, User, LogOut, ShieldCheck } from 'lucide-react';

const Navbar = () => {
  const { isAuthenticated, user, logout } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const isActive = (path) => location.pathname === path ? 'active' : '';

  return (
    <nav className="navbar">
      <div className="container navbar-content">
        <Link to="/" className="navbar-brand">
          <ShieldCheck size={28} color="var(--primary)" />
          AuthPro
        </Link>
        <div className="navbar-nav">
          {isAuthenticated ? (
            <>
              <Link to="/dashboard" className={`nav-link ${isActive('/dashboard')}`}>
                <LayoutDashboard size={18} />
                Dashboard
              </Link>
              <Link to="/profile" className={`nav-link ${isActive('/profile')}`}>
                <User size={18} />
                Profile
              </Link>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginLeft: '1rem', borderLeft: '1px solid var(--border-color)', paddingLeft: '1.5rem' }}>
                <div className="avatar" style={{ width: '32px', height: '32px', fontSize: '0.9rem' }}>
                  {user?.name?.charAt(0) || 'U'}
                </div>
                <div style={{ display: 'flex', flexDirection: 'column' }}>
                  <span style={{ fontSize: '0.85rem', fontWeight: '600', color: 'var(--text-main)' }}>{user?.name}</span>
                  <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>{user?.role}</span>
                </div>
                <button onClick={handleLogout} className="btn btn-outline" style={{ padding: '0.4rem 0.75rem', marginLeft: '1rem', fontSize: '0.85rem', borderRadius: '8px' }}>
                  <LogOut size={14} />
                  Logout
                </button>
              </div>
            </>
          ) : (
            <Link to="/login" className="btn btn-primary" style={{ padding: '0.5rem 1.25rem', fontSize: '0.9rem' }}>
              Sign In
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
