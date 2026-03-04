from config import LOG_CHANNEL


def log_recharge(bot, user, amount):

    text = f"""
💰 عملية شحن

👤 الاسم: {user.first_name}
🔗 اليوزر: @{user.username}
🆔 الايدي: {user.id}

💵 المبلغ: {amount}
"""

    bot.send_message(LOG_CHANNEL, text)


def log_buy(bot, user, number, code, price):

    text = f"""
📱 شراء رقم جديد

👤 الاسم: {user.first_name}
🔗 اليوزر: @{user.username}
🆔 الايدي: {user.id}

📞 الرقم: {number}
🔐 الكود: {code}

💰 السعر: {price}
"""

    bot.send_message(LOG_CHANNEL, text)
