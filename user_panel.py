from telebot import types
from config import QI_NUMBER


def main_menu():

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("شراء رقم", "شحن رصيد")
    markup.add("عدادات الرقم", "رقم VIP")
    markup.add("القوانين", "الخصوصية")
    markup.add("قناة التحديث", "السيرفرات")
    markup.add("حسابي")

    return markup


def recharge_message():

    text = f"""
💳 شحن رصيد

قم بالتحويل إلى الرقم:

{QI_NUMBER}

ثم اضغط تم التحويل.
"""

    return text
