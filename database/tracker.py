import json
import os
from datetime import datetime

DB_FILE = "memory/seen_jobs.json"

def load_seen():
    os.makedirs("memory", exist_ok=True)
    if not os.path.exists(DB_FILE):
        return set()
    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            return set(data.get("seen_ids", []))
    except:
        return set()

def save_seen(seen_ids: set):
    os.makedirs("memory", exist_ok=True)
    with open(DB_FILE, "w") as f:
        json.dump({
            "seen_ids": list(seen_ids),
            "last_updated": datetime.now().isoformat()
        }, f, indent=2)

def is_new_job(job_id: str) -> bool:
    seen = load_seen()
    return job_id not in seen

def mark_seen(job_id: str):
    seen = load_seen()
    seen.add(job_id)
    # Keep only last 1000 to avoid file bloat
    if len(seen) > 1000:
        seen = set(list(seen)[-1000:])
    save_seen(seen)
