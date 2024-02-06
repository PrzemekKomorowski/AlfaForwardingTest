# from forex_python.converter import CurrencyRates
# from datetime import datetime, timedelta
#
#
# # def actual_ron(currency_code):
# #     c = CurrencyRates()
# #     rate_ron = c.get_rate('RON', currency_code)
# #     print(f'Actual RON: 1 RON = {rate_ron:.4f}' currency_code)
#
#
# def exchange_rate_ron(start_date, end_date, currency_code):
#     c = CurrencyRates()
#
#     current_date = start_date
#     while current_date <= end_date:
#         rate_ron = c.get_rate('RON', currency_code, date_obj=current_date)  # currency code to kod waluty. Np. PLN
#         # print(f'exchange rate RON for {current_date.date()}: 1 RON = {rate_ron:.4f} ' + currency_code)
#         print(f'{rate_ron:.4f} {currency_code}')
#         current_date += timedelta(days=1)
#
#
# if __name__ == "__main__":
#     # Aktualne kursy RON
#     # actual_ron()
#
#     # Archiwalne kursy RON (przykład dla ostatnich 7 dni)
#     start_date = datetime.now() - timedelta(days=7)
#     end_date = datetime.now()
#
#     # exchange_rate_ron(start_date, end_date, 'PLN')
#     # exchange_rate_ron(start_date, end_date, 'USD')
#     # exchange_rate_ron(start_date, end_date, 'CZK')
