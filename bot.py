import telebot
from datetime import datetime

TOKEN = "PUT_BOT_TOKEN_HERE"

bot = telebot.TeleBot(TOKEN)

OWNER_ID = 6001517585
CHANNEL_ID = -1001983899376

users_balance = {}

@bot.message_handler(commands=['start'])
def start(msg):
    user = msg.from_user

    text = f"""
مرحبا بك في متجر الأرقام 📲

👤 الاسم : {user.first_name}
🆔 ايديك : {user.id}

اختر من القائمة
"""

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📱 شراء رقم")
    markup.add("💳 شحن رصيد")
    markup.add("👤 حسابي")

    bot.send_message(msg.chat.id, text, reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == "📱 شراء رقم")
def buy(msg):

    user = msg.from_user

    text = f"""
🟢 تم شراء رقم جديد

👤 الاسم : {user.first_name}
🔗 اليوزر : @{user.username}
🆔 الايدي : {user.id}

🌍 الدولة : روسيا
📱 الرقم : +79123456789

💰 السعر : 0.5$
🕒 الوقت : {datetime.now()}
"""

    bot.send_message(CHANNEL_ID, text)
    bot.send_message(msg.chat.id, "تم شراء الرقم بنجاح")


@bot.message_handler(func=lambda m: m.text == "💳 شحن رصيد")
def charge(msg):

    user = msg.from_user

    text = f"""
💳 عملية شحن جديدة

👤 الاسم : {user.first_name}
🆔 الايدي : {user.id}

💰 المبلغ : 10$
🏦 الطريقة : ZainCash
📅 الوقت : {datetime.now()}
"""

    bot.send_message(CHANNEL_ID, text)
    bot.send_message(msg.chat.id, "تم إرسال طلب الشحن")


@bot.message_handler(func=lambda m: m.text == "👤 حسابي")
def account(msg):

    bal = users_balance.get(msg.from_user.id, 0)

    bot.send_message(msg.chat.id, f"رصيدك : {bal}$")


bot.infinity_polling()
