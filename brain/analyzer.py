import anthropic
from config import ANTHROPIC_API_KEY, CANDIDATE_PROFILE

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

SYSTEM_PROMPT = f"""You are an elite remote accounting job-hunting AI.

{CANDIDATE_PROFILE}

SCORING RULES (0-100):
+20 QuickBooks mentioned
+20 Bookkeeping/bookkeeper role
+15 Excel or Google Sheets mentioned  
+15 Reconciliation mentioned
+15 Entry level / junior / no experience required
+10 Worldwide remote / open to all locations
+10 Pay rate mentioned and reasonable (>$8/hr)
-50 CPA required
-30 5+ years required
-40 US only / must be US citizen
-25 Native English only required
-20 Senior/Manager title

SCAM SIGNALS: vague description, unrealistic pay, "training fee", no company info, "pay to start"

Always respond in this EXACT format, plain text only, no JSON:
🎯 FIT SCORE: [number]/100
📋 JOB TITLE: [title]
✅ WHY FIT: [2 sentences why this matches candidate]
⚠️ RISKS: [concerns or None]
🚨 SCAM RISK: [LOW / MEDIUM / HIGH]
📊 DECISION: [APPLY ✅ or SKIP ❌]
📝 PROPOSAL:
[Write a 3-paragraph professional cover letter in English, personalized for this specific job. Mention QuickBooks certification, relevant skills, enthusiasm for remote work.]"""

def analyze_job(job: dict) -> str:
    """Send job to Claude for analysis and proposal generation."""
    try:
        prompt = f"""Analyze this job posting:

JOB TITLE: {job['title']}
SOURCE: {job['source']}
URL: {job['url']}

DESCRIPTION:
{job['description'][:1500]}

Provide full analysis and cover letter."""

        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1200,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}]
        )

        return message.content[0].text

    except Exception as e:
        return f"❌ AI Analysis failed: {str(e)}"

def should_send(analysis: str) -> bool:
    """Check if job scored high enough to send to Telegram."""
    try:
        # Extract score from analysis
        for line in analysis.split('\n'):
            if 'FIT SCORE:' in line:
                score_part = line.split('FIT SCORE:')[1].strip()
                score = int(score_part.split('/')[0].strip().replace('🎯', '').strip())
                return score >= 50  # Only send if score >= 50
        return True  # Send if can't parse score
    except:
        return True
