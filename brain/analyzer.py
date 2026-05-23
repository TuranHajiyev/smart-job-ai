import anthropic
from config import ANTHROPIC_API_KEY, CANDIDATE_PROFILE

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

SYSTEM_PROMPT = f"""You are an elite remote job-hunting AI for a senior finance professional.

{CANDIDATE_PROFILE}

SCORING RULES (0-100):
+25 Senior finance role (Financial Director, CFO, Controller, Finance Manager)
+20 IFRS or financial reporting mentioned
+20 Bookkeeping/accounting role with QuickBooks
+15 Excel, Power BI, financial modeling mentioned
+15 Reconciliation, budgeting, cash flow mentioned
+15 Entry to mid level (good for QuickBooks/bookkeeping roles)
+10 Worldwide remote / open to all locations
+10 Pay rate >$15/hr or good salary
-50 Must have US CPA license
-40 US only / must be US citizen / onsite only
-20 Junior only (0-1 year experience) — overqualified

SCAM SIGNALS: vague description, unrealistic pay, "training fee", no company info

Always respond in this EXACT format, plain text only, no JSON:
🎯 FIT SCORE: [number]/100
📋 JOB TITLE: [title]
🏢 COMPANY: [company name if available]
✅ WHY FIT: [2-3 sentences why Turan matches this role]
⚠️ RISKS: [concerns or None]
🚨 SCAM RISK: [LOW / MEDIUM / HIGH]
💰 PAY: [salary/rate if mentioned, else "Not specified"]
📊 DECISION: [APPLY ✅ or SKIP ❌]

📝 COVER LETTER:
[Write a 3-paragraph professional cover letter in English. 
Paragraph 1: Express interest, mention 17 years experience, current consulting work.
Paragraph 2: Match specific job requirements to Turan's real experience (IFRS, financial modeling, QuickBooks, Excel, team leadership).
Paragraph 3: Emphasize remote work experience, availability, and call to action.
Make it specific to THIS job, not generic.]"""

def analyze_job(job: dict) -> str:
    """Send job to Claude for analysis and proposal generation."""
    try:
        prompt = f"""Analyze this job posting:

JOB TITLE: {job['title']}
SOURCE: {job['source']}
URL: {job['url']}

DESCRIPTION:
{job['description'][:1500]}

Provide full analysis and tailored cover letter for Turan Hajiyev."""

        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1500,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}]
        )

        return message.content[0].text

    except Exception as e:
        return f"❌ AI Analysis failed: {str(e)}"

def should_send(analysis: str) -> bool:
    """Check if job scored high enough to send to Telegram."""
    try:
        for line in analysis.split('\n'):
            if 'FIT SCORE:' in line:
                score_part = line.split('FIT SCORE:')[1].strip()
                score = int(score_part.split('/')[0].strip().replace('🎯', '').strip())
                return score >= 45
        return True
    except:
        return True
