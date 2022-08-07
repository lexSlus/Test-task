from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup,\
    InlineKeyboardButton, InlineKeyboardMarkup


token = '5290879377:AAHAh3hRtHE1xrMNFE9gQ908rBF3yfDn-nk'
bot = Bot(token=token)
dp = Dispatcher(bot)

b = {'bogdan': 395519902, 'lovelas': 1836086969}


def keyb():
    button = KeyboardButton('Войти')
    keyb = ReplyKeyboardMarkup(resize_keyboard=True).add(button)
    return keyb


def inl():
    butinl = InlineKeyboardButton(text='Перейти', url='http://127.0.0.1:8000/login')
    keybin = InlineKeyboardMarkup().add(butinl)
    return keybin


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!")
    await message.answer(f"Ваш айди: {message.from_user.id}")
    if message.from_user.id in b.values():
        await message.reply('Ты в списке', reply_markup=keyb())
    else:
        await message.reply('Извини, твоего айди нет в списке')


@dp.message_handler(text='Войти')
async def ask(message: types.Message):
    await message.reply("Перейди по ссылке для авторизации", reply_markup=inl())


if __name__ == '__main__':
    executor.start_polling(dp)