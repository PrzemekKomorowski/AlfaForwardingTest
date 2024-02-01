import sqlite3

conn = sqlite3.connect("C:\\Users\\Eteer\\Desktop\\AlfaForwading\\AlfaForwardingTest\\database\\test.db")

cur = conn.cursor()

conn.execute('''
    CREATE TABLE IF NOT EXISTS test (fp TEXT, lm TEXT)
''')

cur.execute('''
    INSERT INTO test (fp,lm) VALUES("Przemek","Piotrek")
''')
conn.commit()

cur.execute('''
    SELECT * FROM test
''')

for data in cur:
    print(data)

cur.close()
conn.close()
