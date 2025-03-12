import os
import telebot
from telebot import types

# Замените на свой токен при необходимости.
TOKEN = '7625299955:AAFnicW1zahHB9cMZ5Te6xKP_bZsEUUaRGY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    menu = types.InlineKeyboardMarkup(row_width=2)
    profile = types.InlineKeyboardButton("👤 Информация", callback_data='info')
    shop = types.InlineKeyboardButton("🛒 Магазин", callback_data='shop')
    menu.add(profile, shop)
    bot.send_message(message.chat.id, f'👋🏾 *Vapestore55 приветствует вас!*, это бот от @vapestorewisting, для покупки наших принадлежностей\nНажмите на кнопку, для выбора:', parse_mode="Markdown", reply_markup=menu)
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('info'))
def info(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    menu = types.InlineKeyboardMarkup(row_width=2)
    profile = types.InlineKeyboardButton("👤 Меню", callback_data='start')
    shop = types.InlineKeyboardButton("🛒 Создатель", callback_data='creator')
    menu.add(profile, shop)
    bot.send_message(user_id, "👋 *Наш ассортимент!*", parse_mode="Markdown")
    bot.send_message(user_id, f'Похуй сам напишешь!', parse_mode="Markdown", reply_markup=menu)
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('start'))
def start_config(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    menu = types.InlineKeyboardMarkup(row_width=2)
    profile = types.InlineKeyboardButton("👤 Информация", callback_data='info')
    shop = types.InlineKeyboardButton("🛒 Магазин", callback_data='shop')
    menu.add(profile, shop)
    bot.send_message(message.chat.id, f'👋🏾 *Vapestore55 приветствует вас!*, это бот от @vapestorewisting, для покупки наших принадлежностей\nНажмите на кнопку, для выбора:', parse_mode="Markdown", reply_markup=menu)
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('shop'))
def start_config(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    count = len(os.listdir('databases'))
    menu = types.InlineKeyboardMarkup(row_width=2)
    profile = types.InlineKeyboardButton("👤 Меню", callback_data='start')
    shop = types.InlineKeyboardButton("🛒 Создатель", callback_data='creator')
    menu.add(profile, shop)
    bot.send_message(user_id, "👋 *Привет!*", parse_mode="Markdown")
    bot.send_message(user_id, f'💫Тут сам свои цены ставь:', parse_mode="Markdown", reply_markup=menu)
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('creator'))
def info(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    count = len(os.listdir('databases'))
    menu = types.InlineKeyboardMarkup(row_width=2)
    profile = types.InlineKeyboardButton("👤 Меню", callback_data='start')
    shop = types.InlineKeyboardButton("🛒 Магазин", callback_data='shop')
    menu.add(profile, shop)
    bot.send_message(user_id, "👋 *Информация!*", parse_mode="Markdown")
    bot.send_message(user_id, f'💫 Бот ОТ ВЕЙПСТОР 55 РОССИЯ!', parse_mode="Markdown", reply_markup=menu)
if __name__ == '__main__':
    print("   Бот запущен...\n   Если вы используете Pydroid 3 и у вас слетает бот\n   то  сделайте сессию, в этом меню справа сверху нажмите _")
    bot.polling(none_stop=True)
