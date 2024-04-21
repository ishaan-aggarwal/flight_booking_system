from flask_login import UserMixin
import sqlite3
import os
from . import db_path

def create_database():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        uid INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password TEXT,
        name TEXT,
        contact TEXT
    );
    ''')

    conn.commit()
    conn.close()

class User(UserMixin):
    def __init__(self, uid, email, password, name, contact):
        self.id = uid
        self.email = email
        self.password = password
        self.name = name
        self.contact = contact

    @staticmethod
    def get(user_id):
        with sqlite3.connect(db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM user WHERE uid = ?;', (user_id,))
            user = cursor.fetchone()
            if user:
                return User(user['uid'], user['email'], user['password'], user['name'], user['contact'])
            else:
                return None