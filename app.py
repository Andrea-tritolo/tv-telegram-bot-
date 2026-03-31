from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/", methods=["GET"])
def home():
    return "Webhook online", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True)

    if not data:
        return "No data received", 400

    text = f"""📊 SEGNALE TRADING

Asset: {data.get('asset', 'N/A')}
Direzione: {data.get('direction', 'N/A')}
Timeframe: {data.get('timeframe', 'N/A')}
Score: {data.get('score', 'N/A')}
Grade: {data.get('grade', 'N/A')}

Bias H4: {data.get('bias_h4', 'N/A')}
Trend M30: {data.get('trend_m30', 'N/A')}
Pullback M30: {data.get('pullback_m30', 'N/A')}
Trigger M15: {data.get('trigger_m15', 'N/A')}

Freshness: {data.get('freshness', 'N/A')}
Base Quality: {data.get('basing_quality', 'N/A')}
Impulse Quality: {data.get('impulse_quality', 'N/A')}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })

    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
