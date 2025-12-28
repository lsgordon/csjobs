import os
import json
import dotenv
from google import genai
from google.genai import types
from constants import FAANG_PLUS, QUANT_FIRMS


def is_prestige_company(raw_company_name):
    # Normalize: "Google Inc." -> "google"
    clean_name = raw_company_name.lower().strip()
    
    # 1. Direct hit
    if clean_name in FAANG_PLUS or clean_name in QUANT_FIRMS:
        return True
        
    # 2. Partial hit (be careful with short words like "Box")
    # This catches "Amazon Web Services" if "amazon" is in the set
    for company in FAANG_PLUS | QUANT_FIRMS:
        if len(company) > 3 and company in clean_name: 
            return True
            
    return False

dotenv.load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Define the schema for structured output
# This forces the LLM to return exactly this JSON structure
JOB_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "is_active": {"type": "BOOLEAN"},
        "company_name": {"type": "STRING"},
        "job_title": {"type": "STRING"},
        "experience_level": {
            "type": "STRING", 
            "enum": ["Internship", "New Grad", "Junior (1-3y)", "Senior (3y+)", "N/A"]
        },
        "visa_sponsorship": {"type": "BOOLEAN"},
        "primary_tech_stack": {"type": "ARRAY", "items": {"type": "STRING"}},
        "role_category": {"type": "STRING", "enum": ["Frontend", "Backend", "Fullstack", "ML/AI", "Quant", "DevOps", "Other"]},
        "salary_range": {"type": "STRING"},
        "core_posting": {"type": "BOOLEAN"},
        "post_date": {"type": "STRING"}
    },
    "required": ["is_active", "company_name", "job_title", "experience_level", "role_category"]
}

def analyze_job_url(url: str) -> dict:
    model = "gemini-3-flash-preview" # Use Flash 2.0 or 1.5 Pro for better JSON adherence
    
    prompt = f"""
    Analyze the job posting at this URL: {url}
    
    Extract the following details into a valid JSON object:
    1. Is the job still active/live?
    2. The canonical Company Name (e.g. 'Google' not 'Google Inc').
    3. The Job Title.
    4. Experience Level (Internship, New Grad, etc).
    5. Does it explicitly mention visa sponsorship?
    6. Primary languages/tools mentioned (e.g. Python, React).
    7. Role Category.
    8. Salary Range if mentioned, normalized to a monthly USD figure. Use the middle of the range if given, else "N/A". Format with no currency symbols, just a single integer. e.g "7000" for $7,000/month.
    9. Core Posting, 
    is this an extremely high headcount/core role in the CS recruiting cycle that most people who 
    recruit seriously will apply to? (Y/N) For example, "Software Engineer I" at 
    Google/C1/JPMC/Walmart would be core. "Research Intern: Compilers" at Amazon or "Vibecoder @ <shitty startup>" 
    would not be. Any unspecialized role at a FAANG+ or Quant firm is automatically core.
    10. Post Date (if applicable), in YYYY-MM-DD format.  if not available, return "N/A".
    """

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=JOB_SCHEMA
            )
        )
        
        # Parse the JSON response
        data = json.loads(response.text)
        
        # --- Post-Processing Filters (The Python Layer) ---
        
        # 1. Normalize company name for matching
        company_clean = data.get("company_name", "").lower().strip()
        
        # 2. Add 'Prestige' flag
        data['is_faang_plus'] = is_prestige_company(company_clean)
        
        # 3. Add 'Quant' flag (Check list OR role category)
        data['is_quant'] = (company_clean in QUANT_FIRMS) or (data.get('role_category') == "Quant")

        
        # 4. Signal Score (Simple heuristic for sorting)
        # 2 points for FAANG/Quant, 1 for New Grad/Intern, 1 for Visa
        score = 0
        if data['is_faang_plus'] or data['is_quant']: score += 2
        if data['experience_level'] in ["Internship", "New Grad"]: score += 1
        if data.get('visa_sponsorship'): score += 1
        
        if score >= 3: data['signal_strength'] = "High"
        elif score == 2: data['signal_strength'] = "Medium"
        else: data['signal_strength'] = "Low"

        # add current date 
        from datetime import datetime
        data['analysis_date'] = datetime.now().isoformat()

        # include original URL
        data['url'] = url

        return data

    except Exception as e:
        print(f"Error processing {url}: {e}")
        return None

import pandas as pd
from pandarallel import pandarallel
import json

# Initialize with a progress bar. 
# CRITICAL: Keep nb_workers low (e.g., 4-8) to avoid Gemini 429 Rate Limits.
pandarallel.initialize(progress_bar=True, nb_workers=5)

if __name__ == "__main__":
    # 1. Load CSV from txt file using lines as URLs
    df = pd.read_csv(
    "scrapers/simplify_links_sub.txt", 
    header=None, 
    names=["url"],
    sep='\t',        # <--- Treat as "Tab Separated" so commas are ignored
    quoting=3        # <--- QUOTE_NONE: Prevents errors if URLs have quotes
)

    # 2. Define a safe wrapper function
    def process_row(url):
        try:
            return analyze_job_url(url)
        except Exception as e:
            print(f"Error on {url}: {e}")
            return None

    # 3. Run in parallel
    print("Starting parallel analysis...")
    # This creates a new column 'result' with the dict or None
    df['result'] = df['url'].parallel_apply(process_row)

    # 4. Filter failures and save
    success_df = df.dropna(subset=['result'])
    
    # Write to JSONL
    with open("job_analysis_output.jsonl", "w") as f:
        for entry in success_df['result']:
            f.write(json.dumps(entry) + "\n")
            
    print("Done!")