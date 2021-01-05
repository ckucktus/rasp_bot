from aiogram.dispatcher.filters import Command, Text
from keyboards.default import menu
from aiogram import types
from loader import dp


@dp.message_handler(Command('menu'))
async def menu_start(message: types.Message):
    await message.answer('выбирайте', reply_markup=menu)

@dp.message_handler(Text(equals=['soap', 'Пюре']))
async def menu_choose(message: types.Message):
    await message.answer(f'Вы выбрали {message.text}')

@dp.message_handler(text='close')
async def menu_close(message: types.Message):
    await message.answer('спасибо', reply_markup=types.ReplyKeyboardRemove())
