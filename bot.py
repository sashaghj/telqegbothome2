from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.utils import executor
import logging
import os
import datetime
from config import token
import random
import buttoms as nav
from config import number, attamps

logging.basicConfig(level=logging.DEBUG, filename='mylog.log',
                    format='%(asctime)s | %(levelname)s | %(funcName)s: %(lineno)d | %(message)s',
                    datefmt='%H:%M:%S')

bot = Bot(token)
dp = Dispatcher(bot)
now_date = datetime.datetime.now()


@dp.message_handler(commands='start')
async def start_msg(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.full_name}', reply_markup=nav.main_menu)


@dp.message_handler(text='Больше меньше')
async def big_lit(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.full_name}, Пиши число')


@dp.message_handler(text='Эхо')
async def big_lit(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.full_name}, пиши любую фразу,я отправлю '
                                                 f'тебе ее в ответ')





@dp.message_handler()
async def reply_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)
    global number, attamps

    try:

        if message.text == "Рандомное число":
            await bot.send_message(message.from_user.id, 'Ваше число:' + str(random.randint(1, 99999)))

        elif message.text == 'Назад':
            await bot.send_message(message.from_user.id, 'Назад', reply_markup=nav.main_menu)

        elif message.text == 'Вперед':
            await bot.send_message(message.from_user.id, 'Вперед', reply_markup=nav.other_menu)

        elif message.text == 'Часовой пояс':
            await bot.send_message(message.from_user.id, 'Часовой пояс', reply_markup=nav.times_menu)

        elif message.text == 'Игры':
            await bot.send_message(message.from_user.id, 'Игры', reply_markup=nav.other_menu)

        elif message.text == 'Узнать время':
            await bot.send_message(message.from_user.id, f'{now_date.strftime("%H:%M:%S")}')

        elif message.text == 'Узнать дату':
            await bot.send_message(message.from_user.id, f'{now_date.strftime("%d,%m,%y")}')

        elif int(message.text) == number:
            await message.answer(f'Поздравляю. Вы угадали!\nКоличество попыток: {attamps}')
            attamps = 1

        elif int(message.text) < number:
            await message.answer(f'Ваше число меньше загаданного')
            attamps += 1

        else:
            await message.answer(f'Ваше число больше загаданного')
            attamps += 1

    except:
        await bot.send_message(message.from_user.id,
                               f'Будь внимательнее')


if __name__ == '__main__':
    print('bot polling started')
    executor.start_polling(dp)
