from aiogram.dispatcher.filters.state import State, StatesGroup


class FSM_states(StatesGroup):
    state_main = State()
    # получение карты
    state_map = State()
    # выбор категории для поиска книг
    state_category = State()
    # выбор книги 
    state_booklist = State()
    # получение ссылки на нее
    state_link = State()
