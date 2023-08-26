from aiogram.dispatcher import FSMContext
from fsm_states import FSM_states

from aiogram import types, Dispatcher
from create_bot import BOT
from parser import get_categorys, get_books
from kb import *
from dop import get_btn_category
from itertools import chain


cat_lst = list(chain.from_iterable(get_btn_category()))


def for_send_photo(callback_query, step):
    name = book_list[step][0]
    price = book_list[step][2]
    photo = types.InputFile(book_list[step][3])
    msg = name + '\n' + price
    
    return [photo, msg]


# ответ на запуск бота
# @DP.message_handler(commands=['start'])
async def command_start(message: types.Message, state: FSMContext):
    await FSM_states.state_main.set()
    await BOT.send_message(message.chat.id,\
                           'Приветствую!',
                           reply_markup=kb_start)
    await BOT.send_message(message.chat.id,\
                           'Я помогу тебе найти книгу на сайте книжного магазина "Читай Город"',
                           reply_markup=inline_kb_start)


# ответ на кнопку карта
# @DP.callback_query_handler(text='map')
async def callback_button_map(callback_query: types.CallbackQuery,  state: FSMContext):
    await FSM_states.state_map.set()
    await BOT.send_location(callback_query.from_user.id, latitude=53.186835, longitude=50.126106)
    await BOT.send_message(callback_query.from_user.id,
     'Для подробной информации пройдите по ссылке\nИли переходите к выбору категории',
     reply_markup=inline_kb_map)


# ответ на кнопку поиск книг
# @DP.callback_query_handler(text='poisk')
async def callback_button_poisk(callback_query: types.CallbackQuery,  state: FSMContext):
    await FSM_states.state_category.set()
    await BOT.send_message(callback_query.from_user.id,
     'Выбери категорию, в которой нужно найти книги:\n',
     reply_markup=inline_kb_category)


# ответ на кнопку с категорией
# @DP.callback_query_handler(text='cat')
async def callback_button_cat(callback_query: types.CallbackQuery,  state: FSMContext):
    await FSM_states.state_booklist.set()
    temporary_msg = await BOT.send_message(callback_query.from_user.id, 'Немного терпения. Идет загрузка...')

    global categorys
    global categorys_name
    global book_list
    global step
    categorys = get_categorys()
    categorys_name = callback_query.data
    book_list = get_books(category_link=categorys[categorys_name])
    step = 0

    for_send_photo_list = for_send_photo(callback_query, step=step)

    await BOT.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await temporary_msg.delete()
    await BOT.send_photo(chat_id=callback_query.from_user.id,
        photo=for_send_photo_list[0],
        caption=for_send_photo_list[1],
        reply_markup=inline_kb_next_back)


# ответ на кнопку далее
# @DP.callback_query_handler(text='next')
async def callback_button_next(callback_query: types.CallbackQuery,  state: FSMContext):
    global step
    step += 1

    for_send_photo_list = for_send_photo(callback_query, step=step)

    await BOT.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await BOT.send_photo(chat_id=callback_query.from_user.id,
        photo=for_send_photo_list[0],
        caption=for_send_photo_list[1],
        reply_markup=inline_kb_next_back)

# ответ на кнопку назад
# @DP.callback_query_handler(text='back')
async def callback_button_back(callback_query: types.CallbackQuery,  state: FSMContext):
    global step
    step -= 1

    for_send_photo_list = for_send_photo(callback_query, step=step)

    await BOT.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await BOT.send_photo(chat_id=callback_query.from_user.id,
        photo=for_send_photo_list[0],
        caption=for_send_photo_list[1],
        reply_markup=inline_kb_next_back)


# ответ на кнопку получить ссылку
# @DP.callback_query_handler(text='link')
async def callback_button_link(callback_query: types.CallbackQuery,  state: FSMContext):
    await FSM_states.state_link.set()
    await BOT.send_message(callback_query.from_user.id,
     f'{book_list[step][1]}',
     reply_markup=inline_kb_in_cat_book)


# ответ на кнопку к категориям
# @DP.callback_query_handler(text='cat')
async def callback_button_in_cat(callback_query: types.CallbackQuery,  state: FSMContext):
    await FSM_states.state_category.set()
    await BOT.send_message(callback_query.from_user.id,
     'Выбери категорию, в которой нужно найти книги:\n',
     reply_markup=inline_kb_category)


# ответ на кнопку к книгам
# @DP.callback_query_handler(text='book')
async def callback_button_in_book(callback_query: types.CallbackQuery,  state: FSMContext):
    await FSM_states.state_booklist.set()

    for_send_photo_list = for_send_photo(callback_query, step=step)

    await BOT.send_photo(chat_id=callback_query.from_user.id,
        photo=for_send_photo_list[0],
        caption=for_send_photo_list[1],
        reply_markup=inline_kb_next_back)


# регистрация всех хэндлеров в отдельной ф-ии
# чтобы потом передать именно ее в нужное место
def register_handlers_main(DP: Dispatcher):
    DP.register_message_handler(command_start, commands=['start'], state='*')
    DP.register_callback_query_handler(callback_button_map, text='map', state='*')
    DP.register_callback_query_handler(callback_button_poisk, text='poisk', state=[FSM_states.state_main, FSM_states.state_map])
    DP.register_callback_query_handler(callback_button_cat, text=cat_lst, state=FSM_states.state_category)
    DP.register_callback_query_handler(callback_button_next, text='next', state=FSM_states.state_booklist)
    DP.register_callback_query_handler(callback_button_back, text='back', state=FSM_states.state_booklist)
    DP.register_callback_query_handler(callback_button_link, text='link', state=FSM_states.state_booklist)
    DP.register_callback_query_handler(callback_button_in_cat, text='cat', state='*')
    DP.register_callback_query_handler(callback_button_in_book, text='book', state='*')
