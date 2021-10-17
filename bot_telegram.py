from aiogram import Bot, types  # types - типы данных, чтобы мы могли писать аннотации в функциях
from aiogram.dispatcher import Dispatcher  # class Dispatcher - улавливает события в чате
from aiogram.utils import executor  # executor - чтобы запустить бота

import os  # чтобы прочитать токен из переменной среды окружения

# читаем токен
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


# декоратор обозначает события, когда в чат кто-то что-то пишет
@dp.message_handler()
# асинхронная функция для обработки сообщений ботом
async def echo_send(message: types.Message):  # указали аннотацию типа для параметра функции
    await message.answer(message.text)  # 1. Из события message получаем текст и отвечаем
    await message.reply(message.text)  # 2. То же + упоминаем сообщение на которое отвечаем
    await bot.send_message(message.from_user.id, message.text)  # 3. Получаем user_id и отвечаем в личку.


# запуск бота
executor.start_polling(dp, skip_updates=True)
