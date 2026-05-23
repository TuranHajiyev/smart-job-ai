import feedparser
import requests
import hashlib
from config import RSS_FEEDS, PRIORITY_KEYWORDS, REJECT_KEYWORDS

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def fetch_feed(feed_info: dict) -> list:
    """Fetch and parse a single RSS feed."""
    jobs = []
    try:
        response = requests.get(feed_info["url"], headers=HEADERS, timeout=15)
        feed = feedparser.parse(response.content)

        for entry in feed.entries[:15]:  # Max 15 per feed
            title = getattr(entry, "title", "")
            summary = getattr(entry, "summary", "") or getattr(entry, "description", "")
            link = getattr(entry, "link", "")
            published = getattr(entry, "published", "")

            if not title or not link:
                continue

            # Create unique ID
            job_id = hashlib.md5(link.encode()).hexdigest()

            jobs.append({
                "id": job_id,
                "title": title,
                "description": summary[:2000],  # Limit length
                "url": link,
                "published": published,
                "source": feed_info["name"]
            })

    except Exception as e:
        print(f"Error fetching {feed_info['name']}: {e}")

    return jobs

def quick_filter(job: dict) -> tuple:
    """Quick keyword filter before sending to AI. Returns (pass, reason)."""
    title_lower = job["title"].lower()
    desc_lower = job["description"].lower()
    combined = title_lower + " " + desc_lower

    # Hard reject
    for kw in REJECT_KEYWORDS:
        if kw.lower() in combined:
            return False, f"Rejected: contains '{kw}'"

    # Check if relevant
    has_priority = any(kw.lower() in combined for kw in PRIORITY_KEYWORDS)
    if not has_priority:
        return False, "Not relevant to accounting/bookkeeping"

    return True, "Passed keyword filter"

def crawl_all_feeds() -> list:
    """Crawl all RSS feeds and return filtered jobs."""
    all_jobs = []

    for feed_info in RSS_FEEDS:
        print(f"Fetching: {feed_info['name']}...")
        jobs = fetch_feed(feed_info)
        print(f"  Found {len(jobs)} entries")

        for job in jobs:
            passed, reason = quick_filter(job)
            if passed:
                all_jobs.append(job)
            else:
                print(f"  Filtered out: {job['title'][:50]} — {reason}")

    print(f"Total relevant jobs after filter: {len(all_jobs)}")
    return all_jobs
