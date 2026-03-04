from flask import Flask, request
import requests

app = Flask(__name__)

# معلومات البوت
BOT_TOKEN = "8594021815:AAGnCeQlSpK3urvQVbzzMdJXYX73t7nD-K8"
OWNER = 6001517585

# استقبال رسائل SMS من Twilio
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

# الصفحة الرئيسية للسيرفر
@app.route("/")
def home():
    return "SMS BOT RUNNING"

# تشغيل السيرفر
app.run(host="0.0.0.0", port=10000)
