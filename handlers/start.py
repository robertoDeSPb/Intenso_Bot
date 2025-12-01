import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand, BotCommandScopeDefault, CallbackQuery, FSInputFile
import create_bot
from create_bot import bot
from keyboards.all_keyboards import main_kb, create_spec_kb
import keyboards.inline_keyboards as inline_keyboards
from utils.my_utils import push, pop, open_screen
from all_media.links import all_media_dir, INTENSO_STORAGE_CHAT_ID
import os
from db_handler.json_management import read_credentials, add_credentials
from utils.classes import NavState, RegForm
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.utils.chat_action import ChatActionSender

start_router = Router()
#BotCommand(command='Links', description='Ссылки')
#BotCommand(command='hello', description='привет')
async def set_commands():
    commands = [BotCommand(command='start', description='Старт'),
                BotCommand(command='profile', description='Мой профиль'),
                BotCommand(command='links', description='Ссылки')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    chats = {}
    chats[str(message.from_user.id)] = message.chat.id
    add_credentials(chats, filename=os.path.join(all_media_dir, "users_chats.json"))
    await state.update_data(user_id=message.chat.id)
    await state.update_data(username=message.from_user.username)
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await asyncio.sleep(2)
        await message.answer('¡Hola! Укажи свое имя и фамилию на латинице:')
    await state.set_state(RegForm.name)

@start_router.message(Command(commands=['links']))
async def get_inline_btn_link(message: Message, state: FSMContext):
    await message.answer('Ссылки на наши ресурсы', reply_markup=inline_keyboards.ease_link_kb())

@start_router.message(Command(commands=['menu']))
async def get_inline_btn_menu(message: Message, state: FSMContext):
    await state.set_state(NavState.navigation)
    await state.update_data(stack=["main_menu"])
    user_id = await message.chat.id
    await message.answer('Меню', reply_markup=inline_keyboards.main_inline_kb(user_id))

@start_router.callback_query(F.data == 'back')
async def get_inline_btn_back(call: CallbackQuery, state: FSMContext):
    print('\n\nSOMETHING\n\n')
    prev_screen = await pop(state)
    if not prev_screen:
        print('\n\nНЕТ ПУТИ НАЗАД\n\n')
        await call.answer("Назад некуда")
        return None
    print('\n\n', prev_screen, '\n\n')
    await open_screen(prev_screen, call.message)
    await call.answer('back')

@start_router.callback_query(F.data == 'about_school')
async def get_inline_btn_about(call: CallbackQuery, state: FSMContext):
    await push(state,call.data)
    stack = await state.get_data()
    stack_dict = stack.get("stack", [])
    print(stack_dict)
    await call.answer()

@start_router.callback_query(F.data == 'schedule')
async def get_inline_btn_shedule(call: CallbackQuery, state: FSMContext):
    await push(state, call.data)
    await call.message.edit_text('Расписание', reply_markup=inline_keyboards.inline_kb_schedule())
    await call.answer()

@start_router.callback_query(F.data == 'general_schedule')
async def get_inline_btn_general(call: CallbackQuery, state: FSMContext):
    schedule = ('📕Расписание занятий на осенний период:\n'
    '🎉Уровень А0 (с нуля) - по понедельникам и средам в 18:00;\n'
    '🎉Уровень А1.1 - по понедельникам и средам в 18:00;\n'
    '🎉Уровень А1.2 - по вторникам и четвергам в 20:00;\n'
    '🎉Уровень А2.1 - по вторникам и четвергам в 20:00;\n'
    '🎉Уровень А2.2 - по понедельникам и средам в 20:00;\n'
    '🎉Уровень B1- по понедельникам и средам в 20:00;\n'
    '🎉Уровень В1.2 - по субботам в 14:00;\n'
    '🎉Уровень B2.1- по субботам в 14:00;\n'
    '🎉Уровень В2.2 - по вторникам и четвергам в 18:00\n'
    '🎉Уровень С1 - по вторникам и четвергам в 18:00\n'
    'ОНЛАЙН\n'
    '🎉Уровень B2.2- по вторникам и четвергам в 20:00 (онлайн);\n'
    '🎉Уровень С2 - по понедельникам и средам в 20:00 (онлайн).')
    await push(state, call.data)
    await call.message.edit_text(schedule, reply_markup=inline_keyboards.inline_kb_back())
    await call.answer()

@start_router.callback_query(F.data == 'profile')
async def get_inline_btn_profile(call: CallbackQuery, state: FSMContext):
    '''
    user_prev_menu[call.from_user.id] = (
        call.message.text,
        call.message.reply_markup
    )
    #print('*\n*\n*\n' + user_prev_menu(call.from_user.id).text + '*\n*\n*\n')
    print('*\n*\n*\n' + call.message.text + '*\n*\n*\n')
    '''
    await push(state, call.data)
    await call.message.edit_text('___User_Data___', reply_markup=inline_keyboards.inline_kb_profile())
    await call.answer()

@start_router.callback_query(F.data == 'about_school')
async def get_inline_btn_about(call: CallbackQuery, state: FSMContext):
    await push(state, call.data)
    await call.message.answer()

@start_router.callback_query(F.data == 'library')
async def get_inline_btn_book(call: CallbackQuery, state: FSMContext):
    print("inline_kb_library_level keyboard selected")
    #call.answer('A1', reply_markup=inline_keyboards.inline_kb_library_level())
    await push(state, call.data)
    await call.message.edit_text('Выбор литературы', reply_markup=inline_keyboards.inline_kb_library_level())
    await call.answer()
    
from keyboards.inline_keyboards import CourseCallBack
from utils.my_utils import forward_library
@start_router.callback_query(CourseCallBack.filter())
async def get_needed_library(call: CallbackQuery, callback_data: CourseCallBack):
    current_case = callback_data.level
    if (current_case == "A1"):
        await forward_library(callback_data.level, call)
        await call.answer()
    elif (current_case == "A2"):
        await forward_library(callback_data.level, call)
        await call.answer()
    elif (current_case == "B1"):
        await forward_library(callback_data.level, call)
        await call.answer()
    elif (current_case == "B2"):
        await forward_library(callback_data.level, call)
        await call.answer()
    elif (current_case == "C1"):
        await forward_library(callback_data.level, call)
        await call.answer()
    else:
        print (current_case)
