import { Link } from 'react-router-dom';
import JobCard from '../components/JobCard';

const HomePage = ({ jobs }) => {
  // Take only the first 3 jobs for the "Recent Drops" section
  const recentJobs = jobs.slice(0, 3);

  return (
    <>
      <section className="hero">
        <h1>Building the future of <br /> computer science recruiting.</h1>
        <p className="subtitle">
          An intelligence feed of the best roles for students, curated from top tech companies and hidden gems.
        </p>
      </section>

      <section>
        <div className="section-header">
          <h2 className="section-title">🔥 Recent Drops</h2>
          <Link to="/new-grad" className="view-all-link">View all &rarr;</Link>
        </div>
        <div className="job-grid">
          {recentJobs.map(job => <JobCard key={job.id} job={job} />)}
        </div>
      </section>
    </>
  );
};

export default HomePage;