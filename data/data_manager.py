import sqlite3
from datetime import datetime

todays_date = datetime.now().date()
print(todays_date)


def create_table():
    conn = sqlite3.connect("C:\\Users\\Eteer\\Desktop\\AlfaForwading\\AlfaForwardingTest\\database\\ExchangeRate.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS RonExchangeRate (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency_code VARCHAR(3),
            currency_name VARCHAR(100),
            rate_value DECIMAL(10,4),
            date_time DATETIME
        )
    ''')
    cur.close()
    conn.close()


def clear_table():
    conn = sqlite3.connect("C:\\Users\\Eteer\\Desktop\\AlfaForwading\\AlfaForwardingTest\\database\\ExchangeRate.db")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE RonExchangeRate2;
    ''')
    cur.close()
    conn.close()


def insert_data(currency_code, currency_name, rate_value, date_time):
    conn = sqlite3.connect("C:\\Users\\Eteer\\Desktop\\AlfaForwading\\AlfaForwardingTest\\database\\ExchangeRate.db")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO RonExchangeRate (currency_code,currency_name, rate_value,date_time) VALUES (?, ?, ?, ?)
    ''', (currency_code, currency_name, rate_value, date_time))
    conn.commit()
    cur.close()
    conn.close()


def get_rate_by_date(date_time):
    conn = sqlite3.connect("C:\\Users\\Eteer\\Desktop\\AlfaForwading\\AlfaForwardingTest\\database\\ExchangeRate.db")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM RonExchangeRate
        WHERE date_time = ?
    ''', (date_time,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def fetch_data():
    conn = sqlite3.connect("C:\\Users\\Eteer\\Desktop\\AlfaForwading\\AlfaForwardingTest\\database\\ExchangeRate.db")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM RonExchangeRate
    ''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


if __name__ == "__main__":
    fetch_data()
