from telebot import types
from config import ADMIN_ID


def admin_menu():

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add("➕ إضافة رصيد", "➖ خصم رصيد")
    markup.add("📢 نشر عرض")
    markup.add("📊 الاحصائيات")

    return markup
