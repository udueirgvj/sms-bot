from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "PUT_BOT_TOKEN_HERE"
OWNER = 6001517585

@app.route("/sms", methods=["POST"])
def sms():

    body = request.form.get("Body")
    sender = request.form.get("From")

    text = f"""
📩 وصول كود جديد

📱 الرقم : {sender}

🔐 الكود :
{body}
"""

    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": OWNER,
            "text": text
        }
    )

    return "OK"


@app.route("/")
def home():
    return "SMS BOT RUNNING"


app.run(host="0.0.0.0", port=10000)
