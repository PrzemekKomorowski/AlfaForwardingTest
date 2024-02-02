import sqlite3

conn = sqlite3.connect("C:\\Users\\Eteer\\Desktop\\AlfaForwading\\AlfaForwardingTest\\database\\ExchangeRate.db")

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS RonExchangeRate (
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        currency_code VARCHAR(3),
        rate_value DECIMAL(10,4),
        country_name VARCHAR(100),
        date_time DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

cur.execute('''
    INSERT INTO RonExchangeRate (currency_code,rate_value) VALUES("PWM",2.25)
''')
conn.commit()

cur.execute('''
    SELECT * FROM RonExchangeRate
''')

for data in cur:
    print(data)

cur.close()
conn.close()
