import sqlite3

conn = sqlite3.connect("C:\\Users\\Eteer\\Desktop\\AlfaForwading\\AlfaForwardingTest\\database\\ExchangeRate.db")
cur = conn.cursor()


def create_table():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS RonExchangeRate (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency_code VARCHAR(3),
            currency_name VARCHAR(100),
            rate_value DECIMAL(10,4),
            date_time DATETIME
        )
    ''')


def insert_data(currency_code, currency_name, rate_value, date_time):
    cur.execute('''
        INSERT INTO RonExchangeRate (currency_code,currency_name, rate_value,date_time) VALUES (?, ?, ?, ?)
    ''', (currency_code, currency_name, rate_value, date_time))
    conn.commit()


def fetch_data():
    cur.execute('''
        SELECT * FROM RonExchangeRate
    ''')
    data = cur.fetchall()
    for row in data:
        print(row)


def close_connection():
    cur.close()
    conn.close()


if __name__ == "__main__":
    fetch_data()
    close_connection()
