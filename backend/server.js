import express from 'express';
import cors from 'cors';

const app = express();

// 1. Configure CORS properly
// Using app.use(cors()) with no arguments allows all origins (good for local dev)
app.use(cors());
app.use(express.json());

// 2. Define the Health Check
// Make sure you are hitting http://localhost:5000/health
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Mock data: In production, this comes from your database
const mockJobs = [
  { id: 1, title: "Software Engineer", company: "GitHub", category: "New Grad", signal: "High" },
  { id: 2, title: "Frontend Developer", company: "Vercel", category: "Internship", signal: "Medium" }
];

app.get('/api/jobs', (req, res) => {
  res.json(mockJobs);
});

app.get("/health", (req, res) => {
    res.send("Server is healthy");
    });

const PORT = 5001;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));