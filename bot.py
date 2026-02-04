import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8518754654:AAGjSkLYl1fo892mP_BNuy_cmrF4dB3t4xQ"
VIDEOGRAPH_USERNAME = "yourusername"  # без @

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Кнопки прайса
price_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="🎬 Reels — 15 000₽",
            url=f"https://t.me/{VIDEOGRAPH_USERNAME}?text=Здравствуйте!%20Я%20выбрал%20тариф%20Reels%20—%2015%20000₽"
        )
    ],
    [
        InlineKeyboardButton(
            text="📢 Рекламное видео — 30 000₽",
            url=f"https://t.me/{VIDEOGRAPH_USERNAME}?text=Здравствуйте!%20Я%20выбрал%20рекламное%20видео%20—%2030%20000₽"
        )
    ],
    [
        InlineKeyboardButton(
            text="💍 Свадебная съёмка — 70 000₽",
            url=f"https://t.me/{VIDEOGRAPH_USERNAME}?text=Здравствуйте!%20Я%20выбрал%20свадебную%20съёмку%20—%2070%20000₽"
        )
    ]
])

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет 👋\n"
        "Я видеограф 🎥\n\n"
        "Ниже ты можешь выбрать формат съёмки и сразу написать мне 👇",
        reply_markup=price_keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
