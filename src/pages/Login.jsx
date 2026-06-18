import { useState } from 'react';
import { useNavigate, Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { Lock, User, LogIn, AlertCircle } from 'lucide-react';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const { login, isAuthenticated } = useAuth();
  const navigate = useNavigate();

  if (isAuthenticated) {
    return <Navigate to="/dashboard" replace />;
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    
    if (!username || !password) {
      setError('Please fill in all fields to continue.');
      return;
    }
    
    setIsSubmitting(true);
    
    try {
      const success = await login(username, password);
      if (success) {
        navigate('/dashboard');
      } else {
        setError('Invalid username or password.');
      }
    } catch (err) {
      setError('An error occurred. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="center-content">
      <div className="glass-panel animate-fade-in-up" style={{ padding: '3.5rem', width: '100%', maxWidth: '440px' }}>
        <div style={{ textAlign: 'center', marginBottom: '2.5rem' }}>
          <div style={{ 
            width: '72px', height: '72px', 
            borderRadius: '20px', 
            background: 'linear-gradient(135deg, var(--primary-light), rgba(245, 158, 11, 0.2))',
            border: '1px solid var(--border-highlight)',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            margin: '0 auto 1.5rem auto',
            boxShadow: '0 0 20px var(--primary-light)',
            animation: 'pulse-glow 2s infinite alternate'
          }}>
            <Lock size={36} color="var(--primary)" />
          </div>
          <h2 style={{ fontSize: '2rem', margin: '0 0 0.5rem 0' }}>Welcome Back</h2>
          <p style={{ color: 'var(--text-muted)' }}>Enter your credentials to access your account</p>
          <div style={{ marginTop: '1rem', padding: '0.75rem', backgroundColor: 'var(--primary-light)', borderRadius: '8px', border: '1px solid var(--border-highlight)', display: 'inline-block' }}>
            <p style={{ margin: 0, fontSize: '0.85rem', color: 'var(--primary)' }}>Demo: <strong>xyz</strong> / <strong>xyz123</strong></p>
          </div>
        </div>
        
        {error && (
          <div className="stagger-1" style={{ 
            backgroundColor: 'rgba(244, 63, 94, 0.1)', 
            color: 'var(--danger)', 
            padding: '1rem', 
            borderRadius: '12px', 
            marginBottom: '2rem', 
            border: '1px solid rgba(244, 63, 94, 0.2)',
            display: 'flex', alignItems: 'center', gap: '0.75rem',
            fontSize: '0.9rem', fontWeight: '500'
          }}>
            <AlertCircle size={18} />
            {error}
          </div>
        )}
        
        <form onSubmit={handleSubmit}>
          <div className="input-group stagger-2">
            <label className="input-label" htmlFor="username">Username</label>
            <div className="input-wrapper">
              <User size={18} className="input-icon" />
              <input
                type="text"
                id="username"
                className="input-field"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Enter your username"
              />
            </div>
          </div>
          
          <div className="input-group stagger-3">
            <label className="input-label" htmlFor="password">Password</label>
            <div className="input-wrapper">
              <Lock size={18} className="input-icon" />
              <input
                type="password"
                id="password"
                className="input-field"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••"
              />
            </div>
          </div>
          
          <button 
            type="submit" 
            className="btn btn-primary stagger-4" 
            style={{ width: '100%', marginTop: '1.5rem', padding: '1rem' }} 
            disabled={isSubmitting}
          >
            {isSubmitting ? (
              <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <div style={{ width: '18px', height: '18px', border: '2px solid rgba(255,255,255,0.3)', borderTopColor: 'white', borderRadius: '50%', animation: 'spin 1s linear infinite' }}></div>
                Authenticating...
              </span>
            ) : (
              <>
                <LogIn size={20} />
                Sign In to Dashboard
              </>
            )}
          </button>
        </form>
      </div>
      <style dangerouslySetInnerHTML={{__html: `
        @keyframes spin { to { transform: rotate(360deg); } }
        @keyframes pulse-glow {
          from { transform: scale(1); box-shadow: 0 0 10px var(--primary-light); }
          to { transform: scale(1.05); box-shadow: 0 0 25px var(--primary); }
        }
      `}} />
    </div>
  );
};

export default Login;
