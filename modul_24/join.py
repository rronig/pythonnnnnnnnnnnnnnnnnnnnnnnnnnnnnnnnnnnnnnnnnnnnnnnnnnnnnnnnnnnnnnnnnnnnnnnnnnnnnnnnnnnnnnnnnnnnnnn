import sqlite3

connection = sqlite3.connect('hahseadsrsdgf.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    student_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id)
)
''')
cursor.execute('''INSERT INTO students (name) VALUES (?)''', ('weasdfi',))
cursor.execute('''INSERT INTO students (name) VALUES (?)''', ('weasdfi the second',))
cursor.execute('''INSERT INTO students (name) VALUES (?)''', ('weasdfi the third',))

cursor.execute(""" INSERT INTO courses (name, student_id) VALUES (?, ?)""", ("fghdfgdhg", 1))
cursor.execute(""" INSERT INTO courses (name, student_id) VALUES (?, ?)""", ("hgdghfghdfdgfhfgdh", 2))
cursor.execute(""" INSERT INTO courses (name, student_id) VALUES (?, ?)""", ("larry", 3))
connection.commit()
cursor.execute('''SELECT s.*, c.* FROM courses c JOIN students s ON s.id = c.student_id''')
lakh=cursor.fetchall()
for police in lakh:
    print(police)
cursor.close()
connection.close()