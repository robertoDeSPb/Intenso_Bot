import asyncio
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from utils.classes import RegForm
from aiogram.utils.chat_action import ChatActionSender
from create_bot import bot
from keyboards.inline_keyboards import inline_check_userdata_kb
import db_handler.db_class as db_class

register_router = Router()

@register_router.message(F.text, RegForm.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await asyncio.sleep(2)
        await message.answer("Теперь укажи свою дату рождения:")
    await state.set_state(RegForm.birthday)

@register_router.message(F.text, RegForm.birthday)
async def get_date(message: Message, state: FSMContext):
    await state.update_data(date=message.text)
    
    data = await state.get_data()
    caption = f'Проверьте правильность данных\n\n' \
              f'<b>Полное имя</b>: {data.get("name")}\n' \
              f'<b>Дата рождения</b>: {data.get("date")}\n'
    await message.answer(caption, reply_markup=inline_check_userdata_kb())
    await state.set_state(RegForm.check_userdata)

@register_router.callback_query(F.data == "correct", RegForm.check_userdata)
async def add_to_db(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    db_class.add_user(username=data("username"), name=data("name"), lastname=data("name"), number=data("birthday"))
    await call.answer("Данные сохранены")
    await call.message.edit_reply_markup(reply_markup=None)
    await state.clear()
