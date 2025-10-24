from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType
from create_bot import admins

def main_kb(user_telegram_id: int):
    kb_list = [
        [KeyboardButton(text='📖О нас'), KeyboardButton(text='🖊️Запись на пробное занятие')],
        [KeyboardButton(text='👤Профиль'), KeyboardButton(text='📅Расписание'), KeyboardButton(text='📚Учебник')]
    ]
    if user_telegram_id in admins:
        kb_list.append([KeyboardButton(text='Панель админа')])
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list, 
        resize_keyboard=True, 
        one_time_keyboard=True,
        input_field_placeholder='Воспользуйтесь меню:')
    return keyboard

def create_spec_kb():
    kb_list = [
        [KeyboardButton(text='поделиться локацией', request_location=True)],
        [KeyboardButton(text='поделиться номером', request_contact=True)],
        [KeyboardButton(text='Отправить викторину или опрос', request_poll=KeyboardButtonPollType())]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder='Воспользуйтесь специальной клавиатурой')
    return keyboard
    