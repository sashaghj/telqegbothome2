from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton


# ''''main menu'''
play_battons = KeyboardButton('Игры')
time_battons = KeyboardButton('Часовой пояс')
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(play_battons, time_battons)


# ''''other menu'''
random_battons = KeyboardButton('Рандомное число')
back_battons = KeyboardButton('Назад')
littlebig_battons = KeyboardButton('Больше меньше')
echo_battons = KeyboardButton('Эхо')
other_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(random_battons, littlebig_battons, echo_battons,
                                                           back_battons)


# ''''''times menu'''
times_battons = KeyboardButton('Узнать время')
data_battons = KeyboardButton('Узнать дату')
back_battons = KeyboardButton('Назад')
times_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(times_battons, back_battons, data_battons)