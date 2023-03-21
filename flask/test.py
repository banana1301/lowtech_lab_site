# mdp = 'azertyuiop'
# print(hash(mdp))

# amdp = 'azertyuiop'
# print(hash(amdp))


import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('3éme Post', 'Content for the second post')
            )

connection.commit()
connection.close()