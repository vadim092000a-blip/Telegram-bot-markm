import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
VIDEOGRAPH_USERNAME = "mark_em_wed"

bot = Bot(token=TOKEN)
dp = Dispatcher()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="🎬 Пакет 1 — Полный день (110 000₽)",
            url=f"https://t.me/{VIDEOGRAPH_USERNAME}?text=Здравствуйте!%20Я%20выбрал%20Пакет%201%20—%20Полный%20день%20(110%20000₽).%20Хочу%20забронировать%20дату."
        )
    ],
    [
        InlineKeyboardButton(
            text="🎞 Пакет 2 — Авторский фильм (85 000₽)",
            url=f"https://t.me/{VIDEOGRAPH_USERNAME}?text=Здравствуйте!%20Я%20выбрал%20Пакет%202%20—%20Авторский%20фильм%20(85%20000₽).%20Хочу%20забронировать%20дату."
        )
    ]
])

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Здравствуйте 👋\n"
        "Вы находитесь в официальном боте видеографа Mark Em Wed 🎥\n\n"
        "Выберите подходящий пакет съёмки ниже, "
        "и вы сразу сможете написать мне для бронирования даты 👇\n\n"
        "📌 Дата бронируется по предоплате 10 000₽",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
