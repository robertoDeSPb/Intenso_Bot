from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import keyboards.inline_keyboards as inline_keyboards
#from aiogram.exceptions import TelegramBadRequest
'''
async def check_file(bot: Bot, file_id: str) -> bool:
    try:
        print(file_id)
        await bot.get_file(file_id)
        print('File exist\n')
        return True
    except TelegramBadRequest as e:
        print('File does not exist')
        return False
'''

import os
from db_handler.json_management import read_credentials, add_credentials
from all_media.links import all_media_dir, INTENSO_STORAGE_CHAT_ID
from create_bot import bot
from aiogram.types import CallbackQuery

async def forward_library(level: str, call: CallbackQuery):
    """Переслать сообщение с необходимым файлом из файлового канала-хранилища"""
    all_chats_dict = read_credentials(filename=os.path.join(all_media_dir, "users_chats.json"))
    all_libs_dict = read_credentials(filename=os.path.join(all_media_dir, "libraries.json"))
    try:
        await bot.forward_message(
            chat_id=all_chats_dict[str(call.from_user.id)],
            from_chat_id=INTENSO_STORAGE_CHAT_ID,
            message_id=all_libs_dict["Prisma_" + level + ".pdf"]
        )
    except KeyError:
        print(f"Ошибка: Ключ Prisma_'{level}'.pdf не найден в словаре libraries.json.")
    try:
        await bot.forward_message(
            chat_id=all_chats_dict[str(call.from_user.id)],
            from_chat_id=INTENSO_STORAGE_CHAT_ID,
            message_id=all_libs_dict["Prisma_" + level + "_ejercicios.pdf"]
        )
    except KeyError:
        print(f"Ошибка: Ключ Prisma_'{level}'_ejercicios.pdf не найден в словаре libraries.json.")

async def open_screen(screen: str, message: Message):
    """Вернуть предыдущую клавиатуру"""
    print("inside open_screen")
    if screen == "main_menu":
        await message.edit_text('Меню', reply_markup=inline_keyboards.main_inline_kb())
    elif screen == "schedule":
        await message.edit_text('Расписание', reply_markup=inline_keyboards.inline_kb_schedule())
    elif screen == "profile":
        await message.edit_text('___User_Data___', reply_markup=inline_keyboards.inline_kb_profile())#
    elif screen == "library":
        await message.edit_text('Выбор литературы', reply_markup=inline_keyboards.inline_kb_library_level())
async def push(state: FSMContext, screen: str):
    """Пополнение стека состояний, путем получения текущего стека и возврата дополненного"""
    data = await state.get_data()
    stack = data.get("stack", [])
    stack.append(screen)
    await state.update_data(stack=stack)

async def pop(state: FSMContext) -> str:
    """Персонализированная функция pop для изымания последней страницы и возврата предпоследней"""
    data = await state.get_data()
    stack = data.get("stack", [])
    if len(stack) <= 1:
        return None
    stack.pop()
    await state.update_data(stack=stack)
    return stack[-1]
