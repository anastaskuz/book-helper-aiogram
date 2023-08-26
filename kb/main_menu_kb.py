from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

from dop import get_btn_category

btn_category = get_btn_category()

# создание кнопок
btn_start = KeyboardButton('/start')

inline_btn_site = InlineKeyboardButton('Ссылка на сайт', url='https://www.chitai-gorod.ru')
inline_btn_map = InlineKeyboardButton('Карта', callback_data='map')
inline_btn_map_site = InlineKeyboardButton('Карта', url='https://www.chitai-gorod.ru/shops/samara-51/')
inline_btn_list_book = InlineKeyboardButton(text='Поиск книг', callback_data='poisk')
inline_btn_list_next = InlineKeyboardButton(text='Далее', callback_data='next')
inline_btn_list_back = InlineKeyboardButton(text='Назад', callback_data='back')
inline_btn_list_link = InlineKeyboardButton(text='Получить ссылку', callback_data='link')
inline_btn_list_in_cat = InlineKeyboardButton(text='К категориям', callback_data='cat')
inline_btn_list_in_book = InlineKeyboardButton(text='К книгам', callback_data='book')

inline_btn_cat1 = InlineKeyboardButton(text=btn_category[0][0], callback_data=btn_category[0][0])
inline_btn_cat2 = InlineKeyboardButton(text=btn_category[0][1], callback_data=btn_category[0][1])
inline_btn_cat3 = InlineKeyboardButton(text=btn_category[0][2], callback_data=btn_category[0][2])
inline_btn_cat4 = InlineKeyboardButton(text=btn_category[1][0], callback_data=btn_category[1][0])
inline_btn_cat5 = InlineKeyboardButton(text=btn_category[1][1], callback_data=btn_category[1][1])
inline_btn_cat6 = InlineKeyboardButton(text=btn_category[1][2], callback_data=btn_category[1][2])
inline_btn_cat7 = InlineKeyboardButton(text=btn_category[2][0], callback_data=btn_category[2][0])
inline_btn_cat8 = InlineKeyboardButton(text=btn_category[2][1], callback_data=btn_category[2][1])
inline_btn_cat9 = InlineKeyboardButton(text=btn_category[2][2], callback_data=btn_category[2][2])
inline_btn_cat10 = InlineKeyboardButton(text=btn_category[2][2], callback_data=btn_category[2][2])
inline_btn_cat11 = InlineKeyboardButton(text=btn_category[3][1], callback_data=btn_category[3][1])
inline_btn_cat12 = InlineKeyboardButton(text=btn_category[3][2], callback_data=btn_category[3][2])
inline_btn_cat13 = InlineKeyboardButton(text=btn_category[4][0], callback_data=btn_category[4][0])
inline_btn_cat14 = InlineKeyboardButton(text=btn_category[4][1], callback_data=btn_category[4][1])
inline_btn_cat15 = InlineKeyboardButton(text=btn_category[4][2], callback_data=btn_category[4][2])
inline_btn_cat16 = InlineKeyboardButton(text=btn_category[5][0], callback_data=btn_category[5][0])
inline_btn_cat17 = InlineKeyboardButton(text=btn_category[5][1], callback_data=btn_category[5][1])
inline_btn_cat18 = InlineKeyboardButton(text=btn_category[5][2], callback_data=btn_category[5][2])
inline_btn_cat19 = InlineKeyboardButton(text=btn_category[6][0], callback_data=btn_category[6][0])
inline_btn_cat20 = InlineKeyboardButton(text=btn_category[6][1], callback_data=btn_category[6][1])
inline_btn_cat21 = InlineKeyboardButton(text=btn_category[6][2], callback_data=btn_category[6][2])
inline_btn_cat22 = InlineKeyboardButton(text=btn_category[7][0], callback_data=btn_category[7][0])
inline_btn_cat23 = InlineKeyboardButton(text=btn_category[7][1], callback_data=btn_category[7][1])
inline_btn_cat24 = InlineKeyboardButton(text=btn_category[7][2], callback_data=btn_category[7][2])
inline_btn_cat25 = InlineKeyboardButton(text=btn_category[8][0], callback_data=btn_category[8][0])
inline_btn_cat26 = InlineKeyboardButton(text=btn_category[8][1], callback_data=btn_category[8][1])
inline_btn_cat27 = InlineKeyboardButton(text=btn_category[8][2], callback_data=btn_category[8][2])


# запись кнопок в клавиатуру
kb_start = ReplyKeyboardMarkup().add(btn_start)

inline_kb_start = InlineKeyboardMarkup().add(inline_btn_site, inline_btn_map, inline_btn_list_book)
inline_kb_map = InlineKeyboardMarkup().add(inline_btn_map_site).row(inline_btn_list_book)
inline_kb_next_back = InlineKeyboardMarkup().add(inline_btn_list_back, inline_btn_list_next).row(inline_btn_list_link).row(inline_btn_list_in_cat)
inline_kb_in_cat_book = InlineKeyboardMarkup().add(inline_btn_list_in_cat, inline_btn_list_in_book)


inline_kb_category = InlineKeyboardMarkup(row_width=1).add(
	inline_btn_cat1,
	inline_btn_cat2,
	inline_btn_cat3,
	inline_btn_cat4,
	inline_btn_cat5,
	inline_btn_cat6,
	inline_btn_cat7,
	inline_btn_cat8,
	inline_btn_cat9,
	inline_btn_cat10,
	inline_btn_cat11,
	inline_btn_cat12,
	inline_btn_cat13,
	inline_btn_cat14,
	inline_btn_cat15,
	inline_btn_cat16,
	inline_btn_cat17,
	inline_btn_cat18,
	inline_btn_cat19,
	inline_btn_cat20,
	inline_btn_cat21,
	inline_btn_cat22,
	inline_btn_cat23,
	inline_btn_cat24,
	inline_btn_cat25,
	inline_btn_cat26,
	inline_btn_cat27
	)
