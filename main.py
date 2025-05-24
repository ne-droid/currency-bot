import telebot
from telebot import types
import requests

# Замените на ваш токен
TOKEN = '7913358838:AAEtggRt8nzvvlzPLpVVUVLYExA86tu9-fw'
bot = telebot.TeleBot(TOKEN)

# Список валют и флаги
currency_flags = {
    "USD": "🇺🇸 Доллар",
    "EUR": "🇪🇺 Евро",
    "RUB": "🇷🇺 Рубль",
    "GBP": "🇬🇧 Фунт",
    "CNY": "🇨🇳 Юань",
    "JPY": "🇯🇵 Иена",
    "KZT": "🇰🇿 Тенге",
}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for code, name in currency_flags.items():
        markup.add(types.KeyboardButton(name))
    bot.send_message(message.chat.id, "Привет! Выберите валюту, чтобы узнать курс к рублю:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def send_rate(message):
    code = None
    for c, name in currency_flags.items():
        if name == message.text:
            code = c
            break

    if not code:
        bot.send_message(message.chat.id, "Пожалуйста, выберите валюту из списка.")
        return

    url = f"https://api.exchangerate.host/latest?base={code}&symbols=RUB"
    try:
        response = requests.get(url).json()
        rate = response['rates']['RUB']
        bot.send_message(message.chat.id, f"Курс {currency_flags[code]} к рублю: {rate:.2f} ₽")
    except:
        bot.send_message(message.chat.id, "Ошибка при получении курса валют.")

bot.infinity_polling()
