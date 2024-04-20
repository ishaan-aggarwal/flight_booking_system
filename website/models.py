import sqlite3
import os

def create_database(db_path):
    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        uid INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password TEXT,
        name TEXT
    );
    ''')

    con.commit()
    con.close()