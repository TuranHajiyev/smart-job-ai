import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
CHECK_INTERVAL_MINUTES = int(os.getenv("CHECK_INTERVAL_MINUTES", 30))

# RSS Feed sources - all open, no login required
RSS_FEEDS = [
    {
        "name": "Jobicy Remote",
        "url": "https://jobicy.com/?feed=job_feed&job_types=remote&num_listings=20",
    },
    {
        "name": "WeWorkRemotely Finance",
        "url": "https://weworkremotely.com/categories/remote-finance-legal-jobs.rss",
    },
    {
        "name": "RemoteOK Accounting",
        "url": "https://remoteok.com/remote-accounting-jobs.rss",
    },
    {
        "name": "Indeed Remote Bookkeeper",
        "url": "https://www.indeed.com/rss?q=bookkeeper+remote&sort=date",
    },
    {
        "name": "Jobspresso",
        "url": "https://jobspresso.co/feed/",
    },
]

# Keywords to PRIORITIZE
PRIORITY_KEYWORDS = [
    "bookkeeper", "bookkeeping", "quickbooks", "accounting assistant",
    "accounts payable", "accounts receivable", "reconciliation",
    "virtual bookkeeper", "remote accountant", "excel", "financial assistant",
    "finance assistant", "odoo", "google sheets"
]

# Keywords to REJECT
REJECT_KEYWORDS = [
    "senior accountant", "cpa required", "us cpa", "tax expert",
    "audit senior", "5+ years", "native english only", "onsite only",
    "must be located in us", "us citizen required"
]

CANDIDATE_PROFILE = """
Candidate Profile:
- QuickBooks Online Level 1 Certified
- Excel & Google Sheets (intermediate)
- Learning accounting (entry to intermediate level)
- Odoo accounting exposure
- Skills: bookkeeping, reconciliation, financial reporting, accounts payable/receivable
- Looking for: remote, entry-level to intermediate bookkeeping/accounting roles
- Location: Azerbaijan (worldwide remote preferred)
"""
