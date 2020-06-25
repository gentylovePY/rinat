import sqlite3
from aiogram.dispatcher.filters.state import StatesGroup, State
con = sqlite3.connect("databs.db")
c = con.cursor()

def check_if_exists(id):

    c.execute("SELECT * FROM user WHERE users = %d" % id)
    result = c.fetchone()
    if result is None:
        return False
    return True

def register_new_user(id):
    c.execute("INSERT INTO user(users) VALUES (%d)" % id)
    con.commit()


def get_user_wish():
    c.execute("SELECT * FROM user")
    result = c.fetchall()
    for row in result:
        a =row[0]


        print(a)


class Mailing(StatesGroup):
    Text = State()


