from flask import request
import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


def receive_sms():

    number = request.form.get("From")
    body = request.form.get("Body")

    text = f"""
📩 رسالة جديدة

📞 الرقم: {number}

💬 الرسالة:
{body}
"""

    bot.send_message(ADMIN_ID, text)
