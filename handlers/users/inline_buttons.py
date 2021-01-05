from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp

@dp.message_handler(Command('inline'))
async def start_inl_buttons(message: types.Message):
    await message.answer(text='klick on down button', reply_markup=inline_klick)

