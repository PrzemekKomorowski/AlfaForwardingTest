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

    data_manager.insert_data(currency_code, currency_name, rate_value, date_time)

    return jsonify({'message': 'Data added successfully'}), 200


def main():
    app.run(
        debug=True
    )


if __name__ == '__main__':
    main()
