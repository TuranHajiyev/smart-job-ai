import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_message(text: str, parse_mode: str = None) -> bool:
    """Send message to Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    # Telegram has 4096 char limit per message
    # Split if needed
    messages = split_message(text)

    success = True
    for msg in messages:
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": msg,
        }
        if parse_mode:
            payload["parse_mode"] = parse_mode

        try:
            response = requests.post(url, json=payload, timeout=10)
            if not response.ok:
                print(f"Telegram error: {response.text}")
                success = False
        except Exception as e:
            print(f"Telegram send failed: {e}")
            success = False

    return success

def split_message(text: str, max_len: int = 4000) -> list:
    """Split long messages for Telegram."""
    if len(text) <= max_len:
        return [text]

    parts = []
    while len(text) > max_len:
        # Split at newline if possible
        split_at = text[:max_len].rfind('\n')
        if split_at == -1:
            split_at = max_len
        parts.append(text[:split_at])
        text = text[split_at:]
    parts.append(text)
    return parts

def send_job_alert(job: dict, analysis: str) -> bool:
    """Send formatted job alert to Telegram."""
    header = f"🔔 NEW JOB ALERT — {job['source']}\n{'─'*30}\n\n"
    footer = f"\n\n🔗 {job['url']}"
    full_message = header + analysis + footer
    return send_message(full_message)

def send_startup_message():
    """Send startup notification."""
    send_message(
        "🤖 Smart Job AI started!\n"
        "Monitoring remote accounting jobs 24/7\n"
        "Will alert you when relevant jobs are found ✅"
    )

def send_status(checked: int, found: int):
    """Send periodic status update."""
    send_message(
        f"📊 Status Update\n"
        f"Feeds checked: {checked}\n"
        f"New jobs found: {found}"
    )
