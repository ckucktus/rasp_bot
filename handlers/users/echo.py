from aiogram import types
from loader import dp, bot


@dp.message_handler()
async def bot_echo(message: types.Message):
    chat_id = message.from_user.id
    text = message.text
    await bot.send_message(chat_id=chat_id, text=text)
