import json
import hashlib
import requests
import time
from collections import OrderedDict

# Configuration
EVE_JSON_PATH = '/var/log/suricata/eve.json'
TINES_WEBHOOK_URL = 'https://your-tines-tenant.tines.com/path/secret'
MAX_SEEN_ALERTS = 10000  # Maximum number of unique alerts to track in memory
seen_alerts = OrderedDict()


def get_alert_hash(alert: dict) -> str:
    """Generate a unique hash for the alert.

    Args:
        alert (dict): Alert data received from Suricata

    Returns:
        str: A unique hash for the alert.
    """
    unique_id = f"{alert.get('flow_id')}-{alert.get('src_ip')}-{alert.get('src_port')}-" \
                f"{alert.get('dest_ip')}-{alert.get('dest_port')}-{alert.get('alert', {}).get('signature_id')}"
    return hashlib.md5(unique_id.encode('utf-8')).hexdigest()


def relay_alert(alert: dict):
    """Relay the alert to Tines.

    Args:
        alert (dict): Alert data received from Suricata.
    """
    try:
        response = requests.post(TINES_WEBHOOK_URL,
                                 json=alert,
                                 timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        pass


def add_to_seen(alert_hash: str):
    """Add the alert hash to the seen_alerts dictionary.

    Args:
        alert_hash (str): The hash of the alert.
    """
    seen_alerts[alert_hash] = None

    if len(seen_alerts) > MAX_SEEN_ALERTS:
        seen_alerts.popitem(last=False)  # Remove the oldest item


def follow(file: object):
    """Follow a file and yield new lines as they are written.

    Args:
        file (object): The file to follow.

    Yields:
        _type_: _description_
    """

    file.seek(0, 2)  # Move to the end of the file
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def main():
    with open(EVE_JSON_PATH, 'r') as f:
        loglines = follow(f)
        for line in loglines:
            try:
                event_data = json.loads(line)
                if event_data.get("event_type") == "alert":
                    alert_hash = get_alert_hash(event_data)
                    if alert_hash not in seen_alerts:
                        relay_alert(event_data)
                        add_to_seen(alert_hash)
                # Else, it's a duplicate alert; do nothing
            except json.JSONDecodeError:
                # Skip lines that aren't valid JSON
                continue


if __name__ == "__main__":
    main()
