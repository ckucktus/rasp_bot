from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
parse_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
                                          [
                                              KeyboardButton(
                                                  text='Начать'
                                              )
                                          ]
                                      ]
                                      )