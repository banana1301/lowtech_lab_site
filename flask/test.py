# import sqlite3

# connection = sqlite3.connect('database.db')

# cur = connection.cursor()

# # cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
# #             ('First Post', 'Content for the first post')
# #             )

# # cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
# #             ('Second Post', 'Content for the second post')
# #             )

# # cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
# #             ('3éme Post', 'Content for the second post')
# #             )

# cur.execute("SELECT * FROM users WHERE email = 'a@a.com' ;")

# account=cur.fetchone()
# print(account)

# connection.commit()
# connection.close()

from werkzeug.security import generate_password_hash,check_password_hash
mdp="a"

hmdp=(generate_password_hash(mdp, method='pbkdf2:sha1', salt_length=8))
print(hmdp)

print(check_password_hash(hmdp,"a"))
