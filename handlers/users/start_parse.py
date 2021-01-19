from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message

from keyboards.default.start_text_button import parse_keyboard
from keyboards.inline.inline_callback import data_pick_callback
from keyboards.inline.parse import data_pick_keyboard

from loader import dp
from aiohhttp_testing import main

@dp.message_handler(Command('start'))
async def start_command(message:Message):
    await message.answer(text='Привет, чтобы узнать расписание нажми на кнопку ниже и затем выбери дату', reply_markup = parse_keyboard)

@dp.callback_query_handler(data_pick_callback.filter(action='refresh_data'))
async def refresh_data(call: CallbackQuery):
    await call.answer()
    await call.answer(text='Теперь выбери дату')
    await call.message.edit_reply_markup(reply_markup=data_pick_keyboard())


@dp.message_handler(text='Начать')
async def start_data_query(message: Message):
    await message.answer(text='Теперь выбери дату', reply_markup=data_pick_keyboard())

@dp.callback_query_handler(data_pick_callback.filter(action='data_pick'))
async def data_query(call: CallbackQuery, callback_data: dict):
    data_time = callback_data['def_data']
    answer = await main.main(data_time)
    await call.answer()
    await call.message.answer(text=f'Расписание за {data_time}:\n{answer}')#text=f'{answer}'