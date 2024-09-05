


import sqlite3
connection = sqlite3.connect('Products.db')
connection1 = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor1 = connection1.cursor()
def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')

    cursor1.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')
def get_all_products():
    initiate_db()
    products_list = cursor.execute("SELECT * FROM Products")
    connection.commit()
    return products_list
def add_user(username, email, age):
    cursor1.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",(f'{username}', f'{email}', f'{age}', '1000'))
    connection1.commit()

def is_included(username):
    check_user = cursor1.execute("SELECT * FROM Users WHERE username = ?", (username,))
    if check_user is None:
        return False
    else:
        return True
    connection1.commit()


connection.commit()
connection1.commit()
#connection.close()