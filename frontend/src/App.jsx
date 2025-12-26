import { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Import our modular components
import NavBar from './components/NavBar';
import HomePage from './pages/HomePage';
import FeedPage from './pages/FeedPage';

const App = () => {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:5001/api/jobs') 
      .then(res => res.json())
      .then(data => {
        setJobs(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Failed to fetch jobs:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container"><p style={{color: 'var(--text-secondary)'}}>Loading intelligence feed...</p></div>;

  return (
    <Router>
      <div className="container">
        <NavBar />
        
        <Routes>
          <Route path="/" element={<HomePage jobs={jobs} />} />
          
          <Route 
            path="/new-grad" 
            element={<FeedPage title="👨‍💻 New Grad Roles" jobs={jobs} filterType="New Grad" />} 
          />
          
          <Route 
            path="/internships" 
            element={<FeedPage title="🎓 Internships" jobs={jobs} filterType="Internship" />} 
          />
        </Routes>
      </div>
    </Router>
  );
};

export default App;