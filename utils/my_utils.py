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

import os
from db_handler.json_management import read_credentials, add_credentials
from all_media.links import all_media_dir, INTENSO_STORAGE_CHAT_ID
from create_bot import bot
from aiogram.types import CallbackQuery

async def forward_library(level: str, call: CallbackQuery):
    all_chats_dict = read_credentials(filename=os.path.join(all_media_dir, "users_chats.json"))
    all_libs_dict = read_credentials(filename=os.path.join(all_media_dir, "libraries.json"))
    await bot.forward_message(
        chat_id=all_chats_dict[str(call.from_user.id)],
        from_chat_id=INTENSO_STORAGE_CHAT_ID,
        message_id=all_libs_dict["Prisma_" + level + ".pdf"]
    )
    await bot.forward_message(
        chat_id=all_chats_dict[str(call.from_user.id)],
        from_chat_id=INTENSO_STORAGE_CHAT_ID,
        message_id=all_libs_dict["Prisma_" + level + "_ejercicios.pdf"]
    )