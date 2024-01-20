import sqlite3 as sq

conn = sq.connect('users.db')
print("Users in Database.")
cursor = conn.cursor()
users = cursor.execute('SELECT * FROM users').fetchall()

for user in users:
    print(user)

conn.commit()