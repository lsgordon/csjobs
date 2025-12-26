import JobCard from '../components/JobCard';

const FeedPage = ({ title, jobs, filterType }) => {
  // Filter jobs based on the prop passed
  const filteredJobs = jobs.filter(job => 
    job.category.toLowerCase().includes(filterType.toLowerCase())
  );

  return (
    <section>
      <div className="section-header">
        <h2 className="section-title">{title}</h2>
        <span style={{color: 'var(--text-muted)'}}>{filteredJobs.length} active roles</span>
      </div>
      <div className="job-grid">
        {filteredJobs.length > 0 ? (
          filteredJobs.map(job => <JobCard key={job.id} job={job} />)
        ) : (
          <p style={{color: 'var(--text-muted)'}}>No active roles found for this category.</p>
        )}
      </div>
    </section>
  );
};

export default FeedPage;