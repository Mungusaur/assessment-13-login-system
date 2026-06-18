import { useAuth } from '../context/AuthContext';
import { Mail, Briefcase, Calendar, Shield, Edit2, LogOut } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

const InfoItem = ({ icon: Icon, label, value }) => (
  <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', padding: '1.25rem 0', borderBottom: '1px solid var(--border-color)' }}>
    <div style={{ width: '40px', height: '40px', borderRadius: '10px', background: 'var(--surface-hover)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <Icon size={18} color="var(--text-muted)" />
    </div>
    <div>
      <p style={{ margin: 0, fontSize: '0.85rem', color: 'var(--text-muted)', marginBottom: '0.2rem' }}>{label}</p>
      <p style={{ margin: 0, fontWeight: '500', color: 'var(--text-main)', textTransform: label === 'Role' ? 'capitalize' : 'none' }}>{value}</p>
    </div>
  </div>
);

const Profile = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="container animate-fade-in-up" style={{ paddingTop: '3rem', paddingBottom: '3rem' }}>
      <div style={{ maxWidth: '800px', margin: '0 auto' }}>
        <h1 style={{ fontSize: '2.5rem', marginBottom: '2rem' }}>Account Profile</h1>
        
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: '2rem' }}>
          {/* Left Column - Avatar & Quick Info */}
          <div className="glass-panel" style={{ padding: '2.5rem', borderRadius: '20px', textAlign: 'center', height: 'fit-content' }}>
            <div className="avatar-lg" style={{ margin: '0 auto 1.5rem auto' }}>
              {user?.name?.charAt(0) || 'U'}
            </div>
            
            <h2 style={{ fontSize: '1.5rem', margin: '0 0 0.5rem 0' }}>{user?.name}</h2>
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', padding: '0.4rem 1rem', background: 'rgba(20, 184, 166, 0.15)', color: 'var(--secondary)', borderRadius: '20px', fontSize: '0.85rem', fontWeight: '600', marginBottom: '2rem' }}>
              <Shield size={14} />
              Active Account
            </div>
            
            <button className="btn btn-primary" style={{ width: '100%', marginBottom: '1rem' }}>
              <Edit2 size={16} />
              Edit Profile
            </button>
            <button onClick={handleLogout} className="btn btn-outline" style={{ width: '100%', borderColor: 'rgba(244, 63, 94, 0.3)', color: 'var(--danger)' }}>
              <LogOut size={16} />
              Sign Out
            </button>
          </div>
          
          {/* Right Column - Detailed Info */}
          <div className="glass-panel" style={{ padding: '2.5rem', borderRadius: '20px' }}>
            <h3 style={{ fontSize: '1.25rem', margin: '0 0 1.5rem 0', borderBottom: '1px solid var(--border-color)', paddingBottom: '1rem' }}>
              Personal Information
            </h3>
            
            <div style={{ display: 'flex', flexDirection: 'column' }}>
              <InfoItem icon={Briefcase} label="Username" value={`@${user?.username}`} />
              <InfoItem icon={Mail} label="Email Address" value={user?.email || `${user?.username}@example.com`} />
              <InfoItem icon={Shield} label="Role" value={user?.role || 'User'} />
              <InfoItem icon={Calendar} label="Member Since" value="November 2025" />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;
