import requests
import re

def get_links(url=None):
    if url is None:
        url = "https://raw.githubusercontent.com/SimplifyJobs/Summer2026-Internships/refs/heads/dev/README.md"
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.text
        # Regex to find standard URLs
        pattern = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"[^>]*>\s*<img\s+[^>]*?alt="Apply"[^>]*?>\s*</a>'

        links = re.findall(pattern, content, re.IGNORECASE)
        # filter out links that contain simplify.jobs or imgur.com or github.com
        excluded_domains = ["simplify.jobs", "imgur.com", "github.com","swelist.com","pittcsc.org","githubusercontent.com","archive.org"]
        links = [link for link in links if not any(domain in link for domain in excluded_domains)]
        return links
    else:
        return []
if __name__ == "__main__":
    url_list = [
        "https://raw.githubusercontent.com/SimplifyJobs/Summer2026-Internships/refs/heads/dev/README.md",
        "https://raw.githubusercontent.com/SimplifyJobs/Summer2026-Internships/refs/heads/dev/README-Off-Season.md",
        "https://raw.githubusercontent.com/SimplifyJobs/New-Grad-Positions/refs/heads/dev/README.md",
        # "https://raw.githubusercontent.com/vanshb03/Summer2026-Internships/refs/heads/dev/README.md"
        # "https://raw.githubusercontent.com/vanshb03/Summer2026-Internships/refs/heads/dev/OFFSEASON_README.md"

    ]
    links = []
    for url in url_list:
        links.extend(get_links(url))
    # save links to a csv file
    with open("simplify_links.csv", "w+") as f:
        for link in links:
            f.write(link + "\n")
    print(f"Saved {len(links)} links to simplify_links.csv")