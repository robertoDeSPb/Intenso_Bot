from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
async def check_file(bot: Bot, file_id: str) -> bool:
    try:
        print(file_id)
        await bot.get_file(file_id)
        print('File exist\n')
        return True
    except TelegramBadRequest as e:
        print('File does not exist')
        return False
    