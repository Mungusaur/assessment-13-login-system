import { useAuth } from '../context/AuthContext';
import { Link } from 'react-router-dom';
import { Activity, Bell, CreditCard, Users, ArrowRight, User } from 'lucide-react';

const StatCard = ({ icon: Icon, label, value, color, delay }) => (
  <div className={`glass-card stagger-${delay}`} style={{ padding: '1.5rem', display: 'flex', alignItems: 'center', gap: '1.5rem' }}>
    <div style={{ 
      width: '54px', height: '54px', 
      borderRadius: '16px', 
      background: `rgba(${color}, 0.15)`,
      border: `1px solid rgba(${color}, 0.3)`,
      display: 'flex', alignItems: 'center', justifyContent: 'center'
    }}>
      <Icon size={28} style={{ color: `rgb(${color})` }} />
    </div>
    <div>
      <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', marginBottom: '0.25rem', fontWeight: '500' }}>{label}</p>
      <h3 style={{ fontSize: '1.75rem', margin: 0 }}>{value}</h3>
    </div>
  </div>
);

const Dashboard = () => {
  const { user } = useAuth();

  return (
    <div className="container animate-fade-in-up" style={{ paddingTop: '3rem', paddingBottom: '3rem' }}>
      <div style={{ marginBottom: '3rem' }}>
        <h1 style={{ fontSize: '2.5rem', marginBottom: '0.5rem' }}>Overview</h1>
        <p style={{ fontSize: '1.1rem', color: 'var(--text-muted)' }}>
          Welcome back, <span style={{ color: 'var(--text-main)', fontWeight: '600' }}>{user?.name}</span>. Here's what's happening today.
        </p>
      </div>
      
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '1.5rem', marginBottom: '3rem' }}>
        <StatCard icon={Activity} label="Total Sessions" value="2,405" color="99, 102, 241" delay="1" />
        <StatCard icon={Users} label="New Users" value="842" color="20, 184, 166" delay="2" />
        <StatCard icon={CreditCard} label="Revenue" value="$12,400" color="139, 92, 246" delay="3" />
        <StatCard icon={Bell} label="Notifications" value="14" color="244, 63, 94" delay="4" />
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(400px, 1fr))', gap: '2rem' }}>
        <div className="glass-panel" style={{ padding: '2rem', borderRadius: '20px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
            <h3 style={{ margin: 0, fontSize: '1.25rem' }}>Recent Activity</h3>
            <button className="btn btn-outline" style={{ padding: '0.5rem 1rem', fontSize: '0.875rem' }}>View All</button>
          </div>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
            {[1, 2, 3].map((i) => (
              <div key={i} style={{ display: 'flex', alignItems: 'center', gap: '1rem', paddingBottom: '1.25rem', borderBottom: i !== 3 ? '1px solid var(--border-color)' : 'none' }}>
                <div style={{ width: '40px', height: '40px', borderRadius: '50%', background: 'var(--surface-hover)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                  <User size={18} color="var(--primary)" />
                </div>
                <div style={{ flex: 1 }}>
                  <p style={{ margin: 0, fontWeight: '500' }}>New user registered</p>
                  <p style={{ margin: 0, fontSize: '0.85rem', color: 'var(--text-muted)' }}>{i * 2} hours ago</p>
                </div>
              </div>
            ))}
          </div>
        </div>
        
        <div className="glass-panel" style={{ padding: '2rem', borderRadius: '20px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
          <div>
            <h3 style={{ margin: '0 0 1rem 0', fontSize: '1.25rem' }}>Quick Actions</h3>
            <p style={{ color: 'var(--text-muted)', marginBottom: '2rem' }}>Manage your account settings and profile details from here.</p>
          </div>
          
          <Link to="/profile" className="btn btn-primary" style={{ width: '100%', justifyContent: 'space-between', padding: '1.25rem' }}>
            <span style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
              <User size={20} />
              Go to Profile Settings
            </span>
            <ArrowRight size={20} />
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
