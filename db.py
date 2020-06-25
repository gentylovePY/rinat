import sqlite3



con = sqlite3.connect("databs.db")
c = con.cursor()


def check_if_exists(id):
    c.execute("SELECT * FROM user WHERE users = %d" % id)
    result = c.fetchone()
    if result is None:
        return False
    return True


def register_new_user(id ):
    c.execute("INSERT INTO user(users) VALUES (%d)" % id)
    con.commit()

def total_users():
    c.execute("SELECT COUNT(*) as count FROM user")
    res = c.fetchall()
    print(res)