import json
import requests
from collections import Counter
from datetime import datetime, timezone, timedelta

# Path to Suricata's eve.json file
EVE_JSON_PATH = "/var/log/suricata/eve.json"

# Webhook URL for sending the weekly digest
WEBHOOK_URL = "https://your-tines-tenant.tines.com/path/secret"


def read_eve_json():
    """Reads Suricata's eve.json log and returns alert entries."""
    with open(EVE_JSON_PATH, "r") as file:
        events = [json.loads(line) for line in file]
    return [event for event in events if event.get("event_type") == "alert"]


def filter_weekly_alerts(events):
    """Filters alerts from the past week using timezone-aware datetime."""
    one_week_ago = datetime.now(timezone.utc) - timedelta(days=7)

    def parse_timestamp(timestamp):
        # Handle timestamps with 'Z' or missing timezone info by normalizing to UTC
        if timestamp.endswith("Z"):
            timestamp = timestamp.replace("Z", "+00:00")
        elif timestamp.endswith("+000"):
            timestamp += "0"  # Fix incomplete timezone notation
        return datetime.fromisoformat(timestamp)

    return [event for event in events if parse_timestamp(event["timestamp"]) >= one_week_ago]


def generate_summary(weekly_alerts):
    """Generates the weekly alert summary."""
    total_alerts = len(weekly_alerts)
    unique_signatures = len(set(alert["alert"]["signature"] for alert in weekly_alerts))
    top_signatures = Counter(alert["alert"]["signature"] for alert in weekly_alerts).most_common(3)
    return {
        "total_alerts": total_alerts,
        "unique_signatures": unique_signatures,
        "top_alert_signatures": [{"signature": sig, "count": count} for sig, count in top_signatures]
    }


def severity_breakdown(weekly_alerts):
    """Counts alerts by severity."""
    severities = Counter(alert["alert"]["severity"] for alert in weekly_alerts)
    return {
        "high": severities.get(4, 0) + severities.get(5, 0),
        "medium": severities.get(3, 0),
        "low": severities.get(1, 0) + severities.get(2, 0)
    }


def category_overview(weekly_alerts):
    """Counts alert categories by frequency."""
    categories = Counter(alert["alert"].get("category", "Uncategorized") for alert in weekly_alerts)
    return [{"category": cat, "count": count} for cat, count in categories.most_common()]


def generate_digest():
    """Generates the weekly digest in JSON format."""
    events = read_eve_json()
    weekly_alerts = filter_weekly_alerts(events)

    if not weekly_alerts:
        return {"message": "No alerts detected in the past week."}

    digest = {
        "time_period": {
            "start": (datetime.now(timezone.utc) - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "end": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        },
        "alert_summary": generate_summary(weekly_alerts),
        "severity_breakdown": severity_breakdown(weekly_alerts),
        "category_overview": category_overview(weekly_alerts)
    }
    return digest


def send_to_webhook(digest):
    """Sends the digest to the external webhook."""
    headers = {"Content-Type": "application/json"}
    response = requests.post(WEBHOOK_URL, headers=headers, data=json.dumps(digest))
    if response.status_code == 200:
        print("Weekly digest sent successfully.")
    else:
        print(f"Failed to send digest. Status code: {response.status_code}")


def main():
    digest = generate_digest()
    if "message" not in digest:  # only send if there are alerts
        send_to_webhook(digest)
    else:
        print(digest["message"])


if __name__ == "__main__":
    main()
