from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Мы в ВК', url='https://vk.com/espanol.intenso')],
        [InlineKeyboardButton(text='Мой ВК', url='https://vk.com/alexandersaldana')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


def main_inline_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='📖О нас',callback_data='about_school')],
        [InlineKeyboardButton(text='📅Расписание', callback_data='schedule')],
        [InlineKeyboardButton(text='👤Профиль', callback_data='profile')],
        [InlineKeyboardButton(text='📚Учебник', callback_data='library')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def inline_kb_schedule():
    inline_kb_list = [
        [InlineKeyboardButton(text='Моя группа', callback_data='my_group')],
        [InlineKeyboardButton(text='Общее', callback_data='general_schedule')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def inline_kb_profile():
    inline_kb_list = [
        [InlineKeyboardButton(text='Учебник', callback_data='user_library')],
        [InlineKeyboardButton(text='Расписание', callback_data='my_group')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_menu')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
