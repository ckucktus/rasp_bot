from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import datetime
from keyboards.inline.inline_callback import data_pick_callback




'''    async with aiohttp.ClientSession() as session:
        delt = time.time()
        async with session.get('http://worldtimeapi.org/api/timezone/Asia/Yekaterinburg') as resp:
            json_answer = await resp.json()
            data_api = json_answer.get("datetime").split('T')[0]
            tuple_time = tuple(map(int, data_api.split('-')))
            define_datetime = datetime.date(*tuple_time)
            print(time.time()-delt)
            await session.close()
            return define_datetime'''


def data_pick_keyboard():
    day = datetime.date.today()
    buttons = InlineKeyboardMarkup(row_width=1,
       inline_keyboard=[
           [InlineKeyboardButton(

               text=f'{day-datetime.timedelta(days=1.0)}',
               callback_data=data_pick_callback.new(action='data_pick', def_data=f'{day-datetime.timedelta(days=1.0)}')
           )],
           [InlineKeyboardButton(
                text=f'{day}',
                callback_data=data_pick_callback.new(action='data_pick', def_data=f'{day}')
           )],
           [InlineKeyboardButton(
                 text=f'{day+datetime.timedelta(days=1.0)}',
                 callback_data=data_pick_callback.new(action='data_pick', def_data=f'{day + datetime.timedelta(days=1.0)}')
           )],
           [InlineKeyboardButton(
                  text=f'{day+datetime.timedelta(days=2.0)}',
                  callback_data=data_pick_callback.new(action='data_pick', def_data=f'{day+datetime.timedelta(days=2.0)}')
           )],
           [InlineKeyboardButton(
                  text=f'{day+datetime.timedelta(days=3.0)}',
                  callback_data=data_pick_callback.new(action='data_pick', def_data=f'{day+datetime.timedelta(days=3.0)}')
           )],
           [InlineKeyboardButton(
                  text='Обновить даты',
                  callback_data=data_pick_callback.new(action='refresh_data', def_data='_')
           )]
       ])
    return buttons
