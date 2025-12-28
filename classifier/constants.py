# ==========================================
# 1. SOFTWARE & BIG TECH (FAANG+)
# ==========================================
# Includes Big Tech, High-Growth Unicorns, and Top-Tier Public Tech
FAANG_PLUS = {
    # The Big 5/6
    "google", "alphabet", "meta", "facebook", "amazon", "apple", "netflix", "microsoft", "nvidia",
    
    # High Prestige / High Pay (Tier 1-2)
    "uber", "lyft", "airbnb", "stripe", "coinbase", "databricks", "snowflake", "palantir",
    "openai", "anthropic", "xai", "perplexity", "mistral", "scale ai", "anduril",
    "linkedin", "snap", "tiktok", "bytedance", "pinterest", "reddit", "roblox",
    "spotify", "shopify", "dropbox", "box", "atlassian", "okta", "twilio",
    "slack", "discord", "zoom", "crowdstrike", "zscaler", "cloudflare", "datadog",
    
    # Fintech & Neo-Banks (Non-Quant)
    "block", "square", "cash app", "paypal", "venmo", "robinhood", 
    "affirm", "sofi", "chime", "plaid", "brex", "ramp", "mercury",
    "revolut", "monzo", "nubank",
    
    # Enterprise & Hardware Giants
    "oracle", "salesforce", "adobe", "intuit", "servicenow", "workday",
    "cisco", "intel", "amd", "qualcomm", "broadcom", "arm", "samsung",
    "ibm", "hp", "dell", "lenovo", "sony", "tsmc", "asml",
    
    # E-commerce / Delivery / Auto
    "tesla", "spacex", "rivian", "waymo", "cruise", "doordash", "instacart",
    "ebay", "etsy", "wayfair", "chewy", "booking", "expedia",
    
    # Other Notable
    "canva", "notion", "figma", "miro", "gitlab", "github", "grafana"
}

# ==========================================
# 2. QUANTITATIVE FINANCE (HFT / HEDGE FUNDS)
# ==========================================
# These often pay $300k+ for new grads but have obscure names.
QUANT_FIRMS = {
    # The "Big Names"
    "jane street", "hudson river trading", "hrt", "citadel", "citadel securities", 
    "two sigma", "d. e. shaw", "d.e. shaw", "deshaw", "bridgewater",
    
    # Prop Trading & Market Makers
    "five rings", "imc", "jump trading", "drw", "tower research", "tower research capital",
    "akuna capital", "optiver", "susquehanna", "sig", "wolverine trading", "belvedere trading",
    "flow traders", "virtu", "virtu financial", "xtx markets", "gsa capital",
    
    # Quant Hedge Funds & Multi-Strat
    "point72", "cubist", "millennium", "worldquant", "aqr", "bamberger",
    "balyasny", "bam", "pdt partners", "renaissance technologies", "rentech",
    "tgs management", "aqr capital", "man group", "winton", "capula",
    "bluecrest", "brevan howard", "marshall wace", "viking global"
}

# ==========================================
# 3. ROLE CLASSIFICATION
# ==========================================
# Keywords to detect specific role types from the job title
ROLE_KEYWORDS = {
    "software_engineer": [
        "software engineer", "sde", "swe", "developer", "programmer", 
        "full stack", "backend", "frontend", "web developer", "systems engineer"
    ],
    "data_science": [
        "data scientist", "data engineer", "machine learning", "ml engineer", 
        "ai engineer", "research scientist", "computer vision", "nlp", "deep learning"
    ],
    "product_manager": [
        "product manager", "pm", "apm", "technical product manager", "program manager"
    ],
    "quant": [
        "quant", "quantitative", "trader", "trading", "alpha", "hft", 
        "strategist", "researcher", "algo", "algorithmic"
    ]
}