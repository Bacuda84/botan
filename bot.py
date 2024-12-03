import os.path

import sqlFunc, defs
import telebot, time, logging, datetime, json, funcs
token = ''

bot = telebot.TeleBot(token)
list = []
helpers = []
admins = []
spam_text = 'в этом чате не купили донат, страдайте'

@bot.message_handler(commands=['hi', 'start'])
def sendRaspisan(message):
    time.sleep(1)
    bot.reply_to(message, text='привет')
    bot.send_message(admins[0], text=f'{message}')

    time.sleep(1)

@bot.message_handler(commands=['date'])
def sendDate(message):
    date = datetime
    print('datetime', date.datetime.now())
    print('tome', date.time)
    print('date', date.date.today())
    print('date', date.timedelta)
    bot.reply_to(message, text='{}'.format(date.date.today()))
    if not os.path.isdir('test'):
        os.mkdir('test')
        bot.reply_to(message, text='direction created')

@bot.message_handler(commands=['bestSchool'])
def sendRaspisan(message):
    bot.reply_to(message, text='Номер лучшей школы в мире - 188')
    print(message.chat.id)


@bot.message_handler(content_types=['photo'])
def sendRaspisan(photo_message):
    id = photo_message.chat.id

    if id in admins:

        #сохраняем фото и говорим это
        os.chdir('photos')
        photo = photo_message.photo[-1]
        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        save_path = '{}.jpg'.format(datetime.date.today())
        with open(save_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        time.sleep(1)
        bot.reply_to(photo_message, text='Фотография сохранена.')
        os.chdir('..')

        if 'да' in photo_message.caption or 'Да' in photo_message.caption:
            for i in list:
                photo_id = photo_message.photo[-1].file_id

                bot.send_photo(i, photo_id)
        bot.send_message(chat_id=admins[0], text='✅Всё разослано ✅')





@bot.message_handler(commands=['schedule'])
def send_schedule(message):
    date = defs.needingDate()
    if sqlFunc.isNewUser(message):
        sqlFunc.addUser(message)
    os.chdir('photos')


    with open('{}.jpg'.format(date), 'rb') as file:
        bot.send_photo(message.chat.id, photo=file, caption='||_отправлено с любовью ❤️_||', parse_mode="MarkdownV2")
        bot.send_message(chat_id=admins[0], text='@{} просил расписание'.format(message.from_user.username))
        os.chdir('..')
        print(message.from_user)
        print(sqlFunc.setGettedPhoto(message.from_user), '--')

@bot.message_handler(commands=['delete'])
def delete_message(message):

    print(message.from_user.id)
    if message.from_user.id in admins:
        id_of_message = message.reply_to_message.id
        bot.delete_message(chat_id=message.chat.id, message_id=id_of_message)



@bot.message_handler(commands=['teqst'])
def test(message):
    for i in list:
        bot.send_message(i, 'test')
        time.sleep(1)

@bot.message_handler(commands=['essay'])
def send_essay(message):
    if sqlFunc.isNewUser(message.from_user):
        sqlFunc.addUser(message.from_user)
    print(message.from_user)
    user = message.from_user
    d = int(datetime.datetime.timestamp(datetime.datetime.now()))
    print("-------", d)
    info = '''О пользователе:
Id - {0}
userName - @{3}
Имя - {1} {2}
Премием - {4},
Время - {5}
    '''.format(str(user.id), user.first_name, user.last_name, user.username, user.is_premium, d)

    bot.forward_message(from_chat_id=message.chat.id, message_id=message.message_id, chat_id=admins[0])
    bot.send_message(chat_id=admins[0], text=info)

@bot.message_handler(commands=['subscribe'])
def subscribe_for_spending_photos():
    pass

#admin_панель
@bot.message_handler(commands=['admin'])
def admin_commands(message):
    if message.from_user.id in admins:
        bot.send_message(message.chat.id, reply_markup=funcs.markup_admin, text='Команды:')
        print(message.document)
        pass
    else:
        bot.reply_to(message, 'Вы не админ, не вызывайте эту команду пожалуйста')

@bot.message_handler(commands=['menu'])
def admin_commands(message):
    bot.send_message(message.chat.id, reply_markup=funcs.markup_user, text='Команды:')



#ответчик
@bot.callback_query_handler(func= lambda call: True)
def calls_answear(call):

    if call.data == 'scbLS' and sqlFunc.subscribeToMailing(call.from_user):
        bot.answer_callback_query(call.id, text='Вы подписаны!!!', show_alert=True)
    elif call.data == 'scbLS':
        bot.answer_callback_query(call.id, text='Не надо спамить, вы подписаны!', show_alert=True)


    if call.data == 'thks':
        bot.answer_callback_query(call.id, text='закинул')
        for i in list:
            bot.send_message(i, 'Спасибо что используете! 🥰😍😘')
    elif call.data == 'sorry':
        bot.answer_callback_query(call.id, text='Попросил прощения')
        for i in list:
            bot.send_message(i,
'Извиняемся что расписание могло кому-то не понравиться 😭\
Простите нас, мы не увидели что было там')
    elif call.data == 'users':
        users = sqlFunc.getAllUsers()
        textd = ''
        for user in users:
             textd += (f'Username: @{user[0]}, id: {user[1]},\n   подписан ли на рассылку: {user[2] == 1}, Последнее получение {user[3]} \n\n')
        textd = textd[:-2]
        bot.send_message(call.from_user.id, text=textd)
        bot.answer_callback_query(call.id, text="Скинул списком ниже")


@bot.message_handler(commands=['about'])
def send_about_bot(message):
    chat = message.chat
    text = 'Это бот, который сможет вам скинуть расписание. Пожалуйста не спамьте. Снизу находится основные кнопки'
    bot.send_message(chat_id=chat.id)

@bot.message_handler(commands=['get_users'])
def get_users(message):
    chat_id = message.chat.id
    members = bot.get_chat_administrators(chat_id)  # Получаем администраторов

    users = []
    for member in members:
        users.append(member.user.username or member.user.first_name)

    # Отправим список участников в чат
    bot.send_message(chat_id, "Список участников:\n" + "\n".join(users))


@bot.message_handler(content_types=['text'])
def free_commands_func(message):
    print("text")
    if message.from_user.id in admins :
        if message.text == 'ботик скинь всем':
            for i in list:
                today = datetime.date.today()
                os.chdir('photos')
                file = open('{}.jpg'.format(today), 'rb')

                bot.send_photo(i, photo=file, caption='||_отправлено с любовью ❤️_||',
                               parse_mode="MarkdownV2")
                os.chdir('..')
            bot.reply_to(message, text='Ну, скинул, где моя оценка 5? 🤓')
    if message.text == 'заспамь':
        i = 1
        while i!=11:
            txt = spam_text+' '+str(i)
            bot.send_message(chat_id=message.chat.id, text=txt)
            i+=1
    elif message.text == 'молодец':
        bot.reply_to(message, text='ты тоже 💖')
    elif message.text == 'пасхалко':
        bot.reply_to(message, text='1488?')
    time.sleep(1)
    bot.forward_message(chat_id=admins[0], message_id=message.message_id, from_chat_id=message.chat.id)


bot.infinity_polling()
