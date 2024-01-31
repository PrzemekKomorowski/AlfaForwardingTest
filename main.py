from flask import Flask, render_template, url_for, request, redirect
from data import queries
from urllib import parse

app = Flask('RON_EXCHANGE_RATE')


@app.route('/')
def index():
    return render_template('index.html')


def main():
    app.run(
        debug=True
    )


if __name__ == '__main__':
    main()
