import asyncio
import aiohttp
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, URLInputFile


TOKEN = "6361419585:AAFSJwZxG7WOp96PazxiibAt48J5STMmy3A"

dp = Dispatcher()
bot = Bot(token=TOKEN)


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Отримано")
    print(message.chat.id)


@dp.message(Command(commands="show"))
async def get_data_from_api(message: Message):

    # тут треба реалізувати запит до апі django проекту
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/api/') as response:
            data = await response.json()

    for item in data:
        await message.answer(f"<b>Товар</b>: {item['name']}\n"
                             f"<b>Вартість</b>: {item['price']}\n"
                             f"<b>Опис</b>: {item['discription']}\n")
        await bot.send_photo(message.chat.id, photo=URLInputFile(f"{item['img']}", filename="img"))


async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
