import sqlite3

conn = sqlite3.Connection('users.db')
cursor = conn.cursor()

create_users_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_users_table)

user = (1, "Kuba", "asd")
insert_user_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_user_query, user)

users = [(2, "Monika", "xxx"),
         (3, "Marcin", "abc")]
cursor.executemany(insert_user_query, users)

get_users_query = "SELECT * FROM users"
for row in cursor.execute(get_users_query):
    print(row)

conn.commit()
conn.close()