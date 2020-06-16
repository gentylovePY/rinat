import asyncio

from aiogram import executor

from config import ADMIN_ID
from bd import create_db
from main import Bot


async def on_shutdown(dp):
    await Bot.close()


async def on_startup(dp):
    await create_db()
    await Bot.send_message(ADMIN_ID, "Я запущен!")


if __name__ == '__main__':
    from admin_panel import dp


    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)