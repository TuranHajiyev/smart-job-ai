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
    "finance assistant", "odoo", "google sheets", "financial reporting",
    "ifrs", "financial analyst", "financial controller", "finance manager",
    "cfo", "chief financial", "financial director", "management accounting"
]

# Keywords to REJECT
REJECT_KEYWORDS = [
    "us cpa required", "cpa license required",
    "must be located in us", "us citizen required",
    "onsite only", "in-office only",
]

CANDIDATE_PROFILE = """
CANDIDATE: Turan Hajiyev
Location: Baku, Azerbaijan (available for worldwide remote)
Email: turan.tga@gmail.com

EXPERIENCE: 17+ years in finance and accounting

CURRENT ROLE: Founder & CEO, Digitalium Agency LLC (Jan 2023 – Present)
- Financial consulting and outsourced accounting for SMEs
- Financial reporting frameworks and business performance dashboards
- Budgeting, cost optimization, financial planning
- Implementing financial management systems

PREVIOUS ROLES:
- Freelance Accountant / Financial Consultant (2018–2023)
- Financial Director, ALLES Construction 77 LLC (2016–2018)
- Head of Accounting Sector, Labor & Social Protection Center (2013–2016)
- Financial Director, Fahrali LLC (2011–2013)
- Accountant / Assistant Chief Accountant, Kapital Bank (2008–2011)

KEY SKILLS:
- Financial Analysis & Forecasting
- IFRS Financial Reporting (DiplIFR ACCA in progress)
- Budgeting & Cash Flow Management
- Financial Modeling
- Strategic Financial Planning
- Internal Controls & Risk Management
- Management Accounting
- QuickBooks Online (Level 1 Certified)
- Advanced Microsoft Excel & Power BI
- SAP, Oracle, ERP Systems
- Google Sheets, Odoo

EDUCATION: Bachelor's — International Economic Relations, Azerbaijan State Economic University (2004–2009)
CERTIFICATIONS: DiplIFR (ACCA) in progress, QuickBooks Online Level 1
LANGUAGES: Azerbaijani (Native), English (B2)
"""
