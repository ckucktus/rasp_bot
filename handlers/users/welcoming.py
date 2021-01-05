from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.welcome import Welcome

@dp.message_handler(Command('form'), state=None)
async def start_form(message: types.Message):
    await message.answer('Добро пожаловать!\n'
                         'Пожалуйста,введите ваше имя')
    await Welcome.Name.set()

@dp.message_handler(state=Welcome.Name)
async def enter_name(message:types.Message, state: FSMContext):
    name = message.text
    await state.update_data({'Name': name})
    await message.answer('Введите ваш email')

    await Welcome.next()

@dp.message_handler(state=Welcome.Email)
async def enter_name(message:types.Message, state: FSMContext):
    email = message.text
    await state.update_data({'Email': email})
    await message.answer('Введите ваш номер телефона')

    await Welcome.next()

@dp.message_handler(state=Welcome.Phone_number)
async def enter_surname(message:types.Message, state: FSMContext):
    data = await state.get_data()
    name = data['Name']
    email = data['Email']
    phone_number = message.text
    await message.answer('Привет! Ты ввел следующие данные:\n'
                        f'Имя - {name}\n'
                        f'Email - {email}\n'
                        f'Телефон: - {phone_number}')
    await state.finish()

