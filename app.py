import telebot
from flask import Flask, request

from config import BOT_TOKEN
from database import add_user
from user_panel import main_menu, recharge_message
from admin_panel import admin_menu
from twilio_sms import receive_sms

bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):

    add_user(message.chat.id)

    bot.send_message(
        message.chat.id,
        "مرحبا بك في بوت الارقام",
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda m: m.text == "شحن رصيد")
def recharge(message):

    bot.send_message(message.chat.id, recharge_message())


@bot.message_handler(commands=['admin'])
def admin(message):

    from config import ADMIN_ID

    if message.chat.id == ADMIN_ID:

        bot.send_message(
            message.chat.id,
            "لوحة المالك",
            reply_markup=admin_menu()
        )


@app.route("/sms", methods=['POST'])
def sms():

    receive_sms()

    return "ok"


@app.route("/telegram", methods=["POST"])
def telegram():

    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))

    bot.process_new_updates([update])

    return "ok"


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=10000)
