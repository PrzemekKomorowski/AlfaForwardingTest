from flask import Flask, render_template, url_for, request, redirect, jsonify
from datetime import datetime
from data import data_manager

today_date = datetime.now().date()
print("Data z Maina")
print(today_date)

app = Flask('RON_EXCHANGE_RATE')


@app.route('/')
def index():
    return render_template('index.html', day_date=today_date)


@app.route('/api/actual_RON_rate')
def api_table_actual_rate():
    return data_manager.fetch_data()


@app.route('/api/add_to_database', methods=['POST'])
def add_to_database():
    data = request.json
    currency_code = data.get('currency_code')
    currency_name = data.get('currency_name')
    rate_value = data.get('rate_value')
    date_time = data.get('date_time')

    # Sprawdź, czy rekord już istnieje w bazie danych
    existing_data = data_manager.get_rate_by_currency_and_date(currency_code, date_time)

    if existing_data:
        pass
    else:
        data_manager.insert_data(currency_code, currency_name, rate_value, date_time)
        return jsonify({'message': 'Data added successfully'}), 200

    return jsonify({'message': 'Data already exists in the database'}), 400


@app.route('/api/fill_table_based_on_date', methods=['POST'])
def fill_table_based_on_date():
    data = request.json
    selected_date = data.get('date')

    exchange_rates = data_manager.get_rate_by_date(selected_date)

    # Przygotuj dane do zwrócenia w formie odpowiedzi JSON
    response_data = []
    for rate in exchange_rates:
        response_data.append({
            'currency_code': rate[1],
            'currency_name': rate[2],
            'rate_value': rate[3],
            'date_time': rate[4]
        })

    return jsonify(response_data), 200


def main():
    app.run(
        debug=True
    )


if __name__ == '__main__':
    main()
