from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(
    KeyboardButton("🇺🇸 USD"),
    KeyboardButton("🇪🇺 EUR"),
    KeyboardButton("🇨🇳 CNY"),
)
menu.add(
    KeyboardButton("🇰🇿 KZT"),
    KeyboardButton("🇹🇷 TRY"),
    KeyboardButton("🇧🇾 BYN"),
)
