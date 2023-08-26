from aiogram import executor

from create_bot import DP
from handlers import main_menu_h


# хэндлеры
main_menu_h.register_handlers_main(DP)


if __name__ == '__main__':

    # запуск бота
    # skip_updates - чтобы когда бот вышел из неактивного режима,
    # все пришедшие ему сообщения за это время на него не свалились
    executor.start_polling(DP, skip_updates=True)
