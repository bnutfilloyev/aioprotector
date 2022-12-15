import asyncio
import logging

from aiogram import Bot, Dispatcher
from bot.handlers import setup_routers

from bot.config import config


async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s",
    )

    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    router = setup_routers()
    dp.include_router(router)

    try:
        await bot.delete_webhook()
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


asyncio.run(main())
