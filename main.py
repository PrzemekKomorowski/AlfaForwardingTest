from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime

actual_date = datetime.now()

app = Flask('RON_EXCHANGE_RATE')


@app.route('/')
def index():
    day_date = actual_date.strftime("%Y-%m-%d")
    return render_template('index.html', day_date=day_date)

def main():
    app.run(
        debug=True
    )


if __name__ == '__main__':
    main()
