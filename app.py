import datetime as dt
import yfinance as yf
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        stock = request.form.get('stock') or 'POWERGRID.NS'
        start = dt.datetime(2000, 1, 1)
        end = dt.datetime(2024, 10, 1)
        df = yf.download(stock, start=start, end=end)
        data_desc = df.describe()
        return render_template('index.html', data_desc=data_desc.to_html(classes='table table-bordered'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
