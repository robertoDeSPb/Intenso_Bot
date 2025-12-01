from aiogram.fsm.state import StatesGroup, State

class NavState(StatesGroup):
    navigation = State()

class RegForm(StatesGroup):
    birthday = State()
    name = State()
    number = State()
    check_userdata = State()
