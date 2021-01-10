from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import datetime
from keyboards.inline.inline_callback import data_pick_callback

def define_data():
    a = datetime.date.today()
    dt = datetime.timedelta(days=1.0)
    return a

parse_keyboard = InlineKeyboardMarkup(row_width=1,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(
                                                  text='Начать',
                                                  callback_data='refresh_time_and_start'
                                              )
                                          ]
                                      ]
                                      )
data_pick_keyboard = InlineKeyboardMarkup(row_width=1,
                                          inline_keyboard=[
                                                [InlineKeyboardButton(
                                                    text=f'{define_data()-datetime.timedelta(days=1.0)}',
                                                    callback_data=data_pick_callback.new(action='data_pick', def_data=f'{define_data()-datetime.timedelta(days=1.0)}')
                                                )],
                                                [InlineKeyboardButton(
                                                    text=f'{define_data()}',
                                                    callback_data=data_pick_callback.new(action='data_pick', def_data=f'{define_data()}')
                                                )],
                                                [InlineKeyboardButton(
                                                    text=f'{define_data()+datetime.timedelta(days=1.0)}',
                                                    callback_data=data_pick_callback.new(action='data_pick', def_data=f'{define_data()+datetime.timedelta(days=1.0)}')
                                                )],
                                                [InlineKeyboardButton(
                                                    text=f'{define_data()+datetime.timedelta(days=2.0)}',
                                                    callback_data=data_pick_callback.new(action='data_pick', def_data=f'{define_data()+datetime.timedelta(days=2.0)}')
                                                )],
                                                [InlineKeyboardButton(
                                                    text=f'{define_data()+datetime.timedelta(days=3.0)}',
                                                    callback_data=data_pick_callback.new(action='data_pick', def_data=f'{define_data()+datetime.timedelta(days=3.0)}')
                                                )],
                                                [InlineKeyboardButton(
                                                  text='Обновить даты',
                                                  callback_data=data_pick_callback.new(action='refresh_data', def_data='_')
                                                )]
                                          ]
                                          )
