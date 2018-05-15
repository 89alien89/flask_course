import sqlite3
import os

if os.path.exists('users.db'):
    os.remove('users.db')

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
cursor.execute(query)

query = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, price REAL)"
cursor.execute(query)

conn.commit()
conn.close()
