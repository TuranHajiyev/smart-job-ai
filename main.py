import schedule
import time
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import CHECK_INTERVAL_MINUTES
from crawler.rss_crawler import crawl_all_feeds
from brain.analyzer import analyze_job, should_send
from telegram.sender import send_job_alert, send_startup_message, send_status
from database.tracker import is_new_job, mark_seen

def run_job_check():
    """Main job checking cycle."""
    print("\n" + "="*50)
    print("Starting job check cycle...")
    print("="*50)

    jobs = crawl_all_feeds()
    new_count = 0

    for job in jobs:
        # Skip if already seen
        if not is_new_job(job["id"]):
            print(f"Already seen: {job['title'][:50]}")
            continue

        print(f"\nAnalyzing: {job['title'][:60]}...")

        # Mark as seen immediately to avoid duplicates
        mark_seen(job["id"])

        # AI Analysis
        analysis = analyze_job(job)

        # Only send if score is good enough
        if should_send(analysis):
            print(f"Sending to Telegram: {job['title'][:50]}")
            send_job_alert(job, analysis)
            new_count += 1
            time.sleep(2)  # Small delay between messages
        else:
            print(f"Score too low, skipping: {job['title'][:50]}")

    print(f"\nCycle complete. Sent {new_count} job alerts.")

    if new_count == 0:
        print("No new relevant jobs found this cycle.")

def main():
    print("🤖 Smart Job AI — Starting up...")

    # Send startup message
    send_startup_message()

    # Run immediately on start
    run_job_check()

    # Schedule regular checks
    schedule.every(CHECK_INTERVAL_MINUTES).minutes.do(run_job_check)

    print(f"\n✅ Scheduler running — checking every {CHECK_INTERVAL_MINUTES} minutes")

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
