from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from create_bot import admins

def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Мы в ТГ', url='https://t.me/espanol_intenso')],
        [InlineKeyboardButton(text='Мы в ВК', url='https://vk.com/espanol.intenso')],
        [InlineKeyboardButton(text='Мой ВК', url='https://vk.com/alexandersaldana')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
#доделать меню регистрации пользователя
def inline_register_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Моя группа', callback_data='my_group')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def inline_check_userdata_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Подтвердить', callback_data='confirm')],
        [InlineKeyboardButton(text='Попробовать начала', callback_data='restart')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def main_inline_kb(user_id):
    inline_kb_list = [
        [InlineKeyboardButton(text='📖О нас',callback_data='about_school')],
        [InlineKeyboardButton(text='📅Расписание', callback_data='schedule')],
        [InlineKeyboardButton(text='👤Профиль', callback_data='profile')],
        [InlineKeyboardButton(text='📚Учебник', callback_data='library')]
    ]
    if user_id in admins:
        inline_kb_list.append([InlineKeyboardButton(text='Панель админа', callback_data="administator")])
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def inline_kb_schedule():
    inline_kb_list = [
        [InlineKeyboardButton(text='Моя группа', callback_data='my_group')],
        [InlineKeyboardButton(text='Общее', callback_data='general_schedule')],
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def inline_kb_profile():
    inline_kb_list = [
        [InlineKeyboardButton(text='Учебник', callback_data='user_library')],
        [InlineKeyboardButton(text='Расписание', callback_data='my_group')],
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def inline_kb_back():
    inline_kb_list = [
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

class CourseCallBack(CallbackData, prefix="course"):
    level: str
    action: str

def inline_kb_library_level():
    inline_kb_list = [
        #[InlineKeyboardButton(text='Для моей группы', callback_data='user_library')],
        [InlineKeyboardButton(text='A1', callback_data=CourseCallBack(level="A1", action="library").pack())],
        [InlineKeyboardButton(text='A2', callback_data=CourseCallBack(level="A2", action="library").pack())],
        [InlineKeyboardButton(text='B1', callback_data=CourseCallBack(level="B1", action="library").pack())],
        [InlineKeyboardButton(text='B2', callback_data=CourseCallBack(level="B2", action="library").pack())],
        [InlineKeyboardButton(text='С1', callback_data=CourseCallBack(level="C1", action="library").pack())],
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def inline_kb_library_choice():
    inline_kb_list = [
        [InlineKeyboardButton(text='Prisma', callback_data='prisma')],
        [InlineKeyboardButton(text='Libro del ejercicios', callback_data='ejercicios')],
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ]
