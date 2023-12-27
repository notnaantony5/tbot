import asyncio
from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command
from aiogram.types import Message
from envparse import Env

env = Env()

env.read_envfile(".env")
TOKEN = env.str('TOKEN')

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message) -> None:
    username = message.from_user.username
    full_name = message.from_user.full_name
    await message.answer(
        text=f"Привет, {full_name}!\n"
             f"Твой username - {username}"
    )


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
