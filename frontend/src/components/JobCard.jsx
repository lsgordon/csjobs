const JobCard = ({ job }) => {
  const getBadgeStyle = (category) => {
    const lowerCat = category.toLowerCase();
    if (lowerCat.includes('intern')) return 'badge internship';
    return 'badge new-grad';
  };

  return (
    <div className="card">
      <div className="card-header">
        <div>
          <h3 className="job-title">{job.title}</h3>
          <div className="company-name">
            <span>🏢</span> {job.company}
          </div>
        </div>
        <span className={getBadgeStyle(job.category)}>
          {job.category}
        </span>
      </div>
      
      <div className="signal-row">
        <div style={{ display: 'flex', alignItems: 'center' }}>
          <span 
            className="signal-dot" 
            style={{ backgroundColor: job.signal === 'High' ? 'var(--signal-high)' : 'var(--signal-med)' }}
          />
          Signal: {job.signal}
        </div>
        <span>NYC / Remote</span>
      </div>
    </div>
  );
};

export default JobCard;