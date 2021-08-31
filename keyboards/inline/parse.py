from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import datetime
from keyboards.inline.inline_callback import data_pick_callback




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
