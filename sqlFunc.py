import datetime
import sqlite3, telebot

def createDB():
    db = sqlite3.connect('data.db')
    c = db.cursor()
    # c.execute('''CREATE TABLE users (
    # username text,
    # id integer,
    # isSubscribed integer,
    # lastGettingPhoto text
    # )''')

    # c.execute('''CREATE TABLE allIds (
    #     id integer,
    #     title text
    # )''')
    c.execute('SELECT * FROM users')
    # c.execute('DELETE FROM allids')
    users = c.fetchall()
    print(users)
    for user in users:
        c.execute(f'INSERT INTO allids VALUES({user[1]}, "@{user[0]}")')



    db.commit()
    db.close()
# createDB()
def test():
    db = sqlite3.connect('data.db')
    c = db.cursor()
    # c.execute('ALTER TABLE users DROP COLUMN isSubscribed')
    # c.execute('INSERT INTO users SET isSubscribed = 1')
    # c.execute('ALTER TABLE users ADD isSubscribed INTEGER(1) NOT NULL DEFAULT 1  ')
    db.commit()
    db.close()

def addUser(message: telebot.types.Message):
    db = sqlite3.connect('data.db')
    c = db.cursor()
    user = message.from_user
    c.execute(f'INSERT INTO users VALUES("{user.username}", {user.id}, 0, "")')
    db.commit()
    db.close()

def getUser(user)   :
    db = sqlite3.connect('data.db')
    c = db.cursor()

    c.execute(f'SELECT * FROM users WHERE id = {user.id}')

    fetched_user = c.fetchone()

    db.commit()
    db.close()

    return fetched_user

def isNewUser(message) -> bool:
    db = sqlite3.connect('data.db')
    c = db.cursor()
    user = message.from_user
    c.execute(f'SELECT * FROM users WHERE id = {user.id}')
    if len(c.fetchall()) == 1:
        db.close()
        return False
    db.close()
    return True



def getAllUsers() -> list:
    db = sqlite3.connect('data.db')
    c = db.cursor()
    c.execute('SELECT * FROM users')
    items = c.fetchall()
    db.close()
    return items

def subscribeToMailing(user) -> bool:
    db = sqlite3.connect('data.db')
    c = db.cursor()
    c.execute(f'SELECT * FROM users WHERE id = {user.id}')
    print(user)
    founded = c.fetchone()
    if founded[2] == 0:
        c.execute(f'UPDATE users SET isSubscribed = 1 WHERE id = {user.id}')
        db.commit()
        db.close()
        return True
    return False

def setGettedPhoto(user):
    db = sqlite3.connect('data.db')
    c = db.cursor()

    print(user, '-------')
    print(datetime.datetime.now())
    c.execute(f'UPDATE users SET lastGettingPhoto = "{datetime.datetime.now()}" WHERE id = {user.id}')

    fetched_user = c.fetchone()
    print(fetched_user)

    db.commit()
    db.close()


#   ids
def getAllIDs() -> list:
    db = sqlite3.connect('data.db')
    c = db.cursor()
    c.execute('SELECT * FROM allids')
    items = c.fetchall()
    db.close()
    return items
print(getAllIDs())
# setGettedPhoto({'id': 6732887031,
#                 'is_bot': False,
#                 'first_name': 'Хороший человек',
#                 'username': 'makarello11', 'last_name': None,
#                 'language_code': 'ru', 'can_join_groups': None,
#                 'can_read_all_group_messages': None, 'supports_inline_queries': None,
#                 'is_premium': None, 'added_to_attachment_menu': None, 'can_connect_to_business': None,
#                 'has_main_web_app': None})
# test()
# print(getAllUsers())