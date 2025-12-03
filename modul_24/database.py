import sqlite3

connection = sqlite3.connect('hahseadsrsdgf.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        position TEXT,
        department TEXT,
        salary REAL
    )
''')
connection.commit()
cursor.execute('''
    INSERT INTO employis (name, position, department, salary) VALUES (?, ?, ?, ?)
''', ('Nick', 'random dude', 'Food', 2000000000000))
cursor.execute('''SELECT * FROM employis''')
employis = cursor.fetchall()
for emp in employis:
    print(emp)
cursor.execute('''
UPDATE employis SET salary = ? WHERE id = ?
''', (67, 1))
connection.commit()
cursor.execute('''
DELETE FROM employis WHERE id = ?
''', (1,))
connection.commit()
cursor.close()
connection.close()