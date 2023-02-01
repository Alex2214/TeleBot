from aiogram import Bot, Dispatcher, executor, types
import logging
from os import getenv
import Pars
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


bot = Bot(getenv('TOKEN'))
# Диспетчер для работы бота
Dp = Dispatcher(bot)
# Логирование бота
logging.basicConfig(level= logging.INFO)

@Dp.message_handler(commands='start')
async def star(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Курс доллара', 'Курс евро']
    keyboard.add(*buttons)
    await message.answer("Привет юный подован", reply_markup=keyboard)

@Dp.message_handler(lambda message: message.text == "Курс доллара")
async def dollar(message: types.Message):
    await message.answer(f'Курс доллара:  {Pars.dollar()}')

@Dp.message_handler(lambda message: message.text == "Курс евро")
async def euro(message: types.Message):
    await message.answer(f'Курс евро:  {Pars.euro()}')

# Запуск бота
executor.start_polling(Dp, skip_updates=True)