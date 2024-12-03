import telebot, json, os

# thks - спасибо что используете нас
#
# chatWithDev
# scb and scbLS
#
#
#

#  markups
markup_admin = telebot.types.InlineKeyboardMarkup(row_width=2)
markup_user = telebot.types.InlineKeyboardMarkup(row_width=2)
#  кнопки
admin_send_thanks_message_button = telebot.types.InlineKeyboardButton(text='Поблагодорить всех за использование',
                                                                      callback_data='thks')
admin_send_sorry_message_button = telebot.types.InlineKeyboardButton(text='Извиниться из-за плохого расписания',
                                                                      callback_data='sorry')
admin_send_list_of_users_button = telebot.types.InlineKeyboardButton(text='Список всех пользователей',
                                                                      callback_data='users')

chat_with_dev_button = telebot.types.InlineKeyboardButton(text='Написать админу',
                                                          callback_data='chatWithDev', url='t.me/@makarello11')
subscribe_for_channel_button = telebot.types.InlineKeyboardButton(text='Подписаться на канал',
                                                          callback_data='scb', url='t.me/@schedule188')
subscribe_for_malling_button = telebot.types.InlineKeyboardButton(text='Подписаться на рассылку',
                                                          callback_data='scbLS')

# addding to markups
markup_admin.add(admin_send_thanks_message_button)
markup_admin.add(admin_send_sorry_message_button)
markup_admin.add(admin_send_list_of_users_button)

markup_user.add(chat_with_dev_button)
markup_user.add(subscribe_for_channel_button)
markup_user.add(subscribe_for_malling_button)
#

