# pip install requests
import json
import os
import requests

def main():
    webhook = os.getenv("DISCORD_WEBHOOK_URL", "").strip()
    if not webhook:
        raise SystemExit("DISCORD_WEBHOOK_URL が未設定です")

    with open("model.json", "r", encoding="utf-8") as f:
        payload = json.load(f)

    r = requests.post(webhook, json=payload, timeout=10)
    r.raise_for_status()
    print("Posted:", r.status_code)

if __name__ == "__main__":
    main()
