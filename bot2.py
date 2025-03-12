import os
import telebot
from telebot import types

# Замените на свой токен при необходимости.
TOKEN = '7625299955:AAFnicW1zahHB9cMZ5Te6xKP_bZsEUUaRGY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    count = len(os.listdir('databases'))
    menu = types.InlineKeyboardMarkup(row_width=2)
    profile = types.InlineKeyboardButton("👤 Информация", callback_data='info')
    shop = types.InlineKeyboardButton("🛒 Магазин", callback_data='shop')
    menu.add(profile, shop)
    bot.send_message(message.chat.id, "👋🏾 *Vapestore55 приветствует*", parse_mode="Markdown")
    bot.send_message(message.chat.id, f'👋🏾 *Vapestore55 приветствует вас!*, это бот от @SimpsonWave666🏴,для поиска данных🏴‍☠️.\nмой тгк с работами и отзывами💻📧\nКоличество баз данных: {count}.\nВведите свой запрос:', parse_mode="Markdown", reply_markup=menu)
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('info'))
def info(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    count = len(os.listdir('databases'))
    menu = types.InlineKeyboardMarkup(row_width=2)
    profile = types.InlineKeyboardButton("👤 Меню", callback_data='start')
    shop = types.InlineKeyboardButton("🛒 Создатель", callback_data='creator')
    menu.add(profile, shop)
    bot.send_message(user_id, "👋 *Информация!*", parse_mode="Markdown")
    bot.send_message(user_id, f'💫Соси хуй!', parse_mode="Markdown", reply_markup=menu)
@bot.callback_query_handler(lambda c: c.data and c.data.startswith('start'))
def start_config(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    count = len(os.listdir('databases'))
    menu = types.InlineKeyboardMarkup(row_width=2)
    profile = types.InlineKeyboardButton("👤 Информация", callback_data='info')
    shop = types.InlineKeyboardButton("🛒 Магазин", callback_data='shop')
    menu.add(profile, shop)
    bot.send_message(user_id, "👋 *Привет!*", parse_mode="Markdown")
    bot.send_message(user_id, f'💫🌟привет💫, это бот от @SimpsonWave666🏴,для поиска данных🏴‍☠️.\nмой тгк с работами и отзывами💻📧\nКоличество баз данных: {count}.\nВведите свой запрос:', parse_mode="Markdown", reply_markup=menu)
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
    bot.send_message(user_id, f'💫 Бота модифицировал: +79503383173!', parse_mode="Markdown", reply_markup=menu)
@bot.message_handler(func=lambda message: True)
def search_databases(message):
    data = message.text
    result = ''
    seen_lines = set()
    if not os.path.exists('databases'):
        bot.send_message(message.chat.id, "Не удается найти папку 'databases'\nПиши '/help🆘'")
        return

    for label in os.listdir('databases'):
        file_path = os.path.join('databases', label)
        try:
            with open(file_path, 'r', encoding='UTF-8') as f:
                for line in f:
                    if data in line:
                        formatted_line = line.replace(';', '\n').replace('.', '').replace('[', '').replace(']', '').replace('"', '').replace('NULL', '')
                        if formatted_line not in seen_lines:
                            seen_lines.add(formatted_line)
                            result += f"[{label}]\n{formatted_line}\n"
                        break
        except Exception as e:
            print(f"Ошибка при чтении файла {label}: {e}")
    
    if result:
        bot.send_message(message.chat.id, f'Все что я нашёл 💫:\n{result}\nНовый запрос -"/start"')
    else:
        bot.send_message(message.chat.id, 'Ничего не найдено \n "/start" для нового запроса.')
     

if __name__ == '__main__':
    print("   Бот запущен...\n   Если вы используете Pydroid 3 и у вас слетает бот\n   то  сделайте сессию, в этом меню справа сверху нажмите _")
    bot.polling(none_stop=True)
