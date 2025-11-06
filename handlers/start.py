from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand, BotCommandScopeDefault, CallbackQuery, FSInputFile
import create_bot
from create_bot import bot
from keyboards.all_keyboards import main_kb, create_spec_kb
import keyboards.inline_keyboards as inline_keyboards
from utils.my_utils import check_file
from all_media.links import all_media_dir, FILE_IDS, INTENSO_STORAGE_CHAT_ID, chat_ids
import os

start_router = Router()
#BotCommand(command='Links', description='Ссылки')
#BotCommand(command='hello', description='привет')
async def set_commands():
    commands = [BotCommand(command='start', description='Старт'),
                BotCommand(command='profile', description='Мой профиль'),
                BotCommand(command='links', description='Ссылки'),
                BotCommand(command='update_lib', description='Обновить библиотеку')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()',
                        reply_markup=main_kb(message.from_user.id))
@start_router.message()
async def get_chat_id(message: Message):
    chat_ids.append(Message.chat.id)

#@start_router.message(Command(commands=['start2']))
@start_router.message(Command("test"))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по команде /test используя фильтр Command()',
                        reply_markup=create_spec_kb())

    
@start_router.message(Command("update_lib"))
async def update_library(call: CallbackQuery):
    cur_book = FSInputFile(path=os.path.join(all_media_dir, 'Prisma_A2_ejercicios.pdf'))
    msg = await bot.send_document(chat_id=INTENSO_STORAGE_CHAT_ID, document=cur_book)
    FILE_IDS['Prisma_A2_ejercicios.pdf'] = msg.document.file_id
    await call.answer('LIbrary is updated')

@start_router.message(Command(commands=['links']))
async def get_inline_btn_link(message: Message):
    await message.answer('Ссылки на наши ресурсы', reply_markup=inline_keyboards.ease_link_kb())

@start_router.message(Command(commands=['menu']))
async def get_inline_btn_menu(message: Message):
    await message.answer('Меню', reply_markup=inline_keyboards.main_inline_kb())

@start_router.callback_query(F.data == 'back_to_menu')
async def get_inline_btn_back(call: CallbackQuery):
    '''
    prev = user_prev_menu.get(call.from_user.id)
    text, markup = prev
    '''
    #call.message.answer(text, reply_markup=markup)
    call.message.answer('back')

@start_router.callback_query(F.data == 'about_school')
async def get_inline_btn_about(call: CallbackQuery):
    await call.message.answer()

@start_router.callback_query(F.data == 'schedule')
async def get_inline_btn_shedule(call: CallbackQuery):
    await call.message.edit_text('Расписание', reply_markup=inline_keyboards.inline_kb_schedule())
    await call.answer()

@start_router.callback_query(F.data == 'general_schedule')
async def get_inline_btn_general(call: CallbackQuery):
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
    await call.message.edit_text(schedule)
    await call.answer()

@start_router.callback_query(F.data == 'profile')
async def get_inline_btn_profile(call: CallbackQuery):
    '''
    user_prev_menu[call.from_user.id] = (
        call.message.text,
        call.message.reply_markup
    )
    #print('*\n*\n*\n' + user_prev_menu(call.from_user.id).text + '*\n*\n*\n')
    print('*\n*\n*\n' + call.message.text + '*\n*\n*\n')
    '''
    await call.message.edit_text('___User_Data___', reply_markup=inline_keyboards.inline_kb_profile())
    await call.answer()

@start_router.callback_query(F.data == 'about_school')
async def get_inline_btn_about(call: CallbackQuery):
    await call.message.answer()

@start_router.callback_query(F.data == 'library')
async def get_inline_btn_book(call: CallbackQuery):
    '''
    await call.answer(text='Ищу на полке...')
    if await check_file(bot, FILE_IDS['Prisma_A1']):
        await call.message.answer_document(document=FILE_IDS['Prisma_A1'], caption='Моя <u>отформатированная</u> подпись к <b>файлу</b>')
    else:
        cur_book = FSInputFile(path=os.path.join(all_media_dir, 'Prisma_A2 ejercicios.pdf'))
        msg_id = await call.message.answer_document(document=cur_book)
        FILE_IDS['Prisma_A1'] = msg_id.document.file_id
        await check_file(bot, FILE_IDS['Prisma_A1'])
    '''
    await bot.forward_message(
        user_id = call.from_user.id,
        chat_id=chat_ids.pop,
        from_chat_id=INTENSO_STORAGE_CHAT_ID
        message_id=FILE_IDS['Prisma_A2_ejercicios']
    )

