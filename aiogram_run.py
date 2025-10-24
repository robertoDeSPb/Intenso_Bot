import asyncio
from create_bot import bot, dp, scheduler
from aiogram import Dispatcher
from handlers.start import start_router, set_commands
#from work_time.time_func import send_time_msg


async def start_bot():
    await set_commands()

async def main():
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()
    dp.include_router(start_router)
    dp.startup.register(start_bot)
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await set_commands()
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())