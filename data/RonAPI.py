from forex_python.converter import CurrencyRates
from datetime import datetime, timedelta


def aktualne_kursy_ron():
    c = CurrencyRates()
    kurs_ron = c.get_rate('RON', 'USD')  # Możesz zmienić 'USD' na inną walutę według potrzeb
    print(f'Bieżący kurs RON: 1 RON = {kurs_ron:.4f} USD')


def archiwalne_kursy_ron(start_date, end_date):
    c = CurrencyRates()

    current_date = start_date
    while current_date <= end_date:
        kurs_ron = c.get_rate('RON', 'PLN', date_obj=current_date)  # Możesz zmienić 'USD' na inną walutę według potrzeb
        print(f'Kurs RON na {current_date.date()}: 1 RON = {kurs_ron:.4f} PLN')
        current_date += timedelta(days=1)


if __name__ == "__main__":
    # Aktualne kursy RON
    aktualne_kursy_ron()

    # Archiwalne kursy RON (przykład dla ostatnich 7 dni)
    start_date = datetime.now() - timedelta(days=7)
    end_date = datetime.now()
    archiwalne_kursy_ron(start_date, end_date)