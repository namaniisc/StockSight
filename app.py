import datetime as dt
import yfinance as yf
import pandas as pd
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

plt.style.use("fivethirtyeight")

app = Flask(__name__)

# Load the pre-trained deep learning model (ensure 'stock_dl_model.h5' is in the correct path)
model = load_model('stock_dl_model.h5')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        stock = request.form.get('stock') or 'POWERGRID.NS'
        start = dt.datetime(2000, 1, 1)
        end = dt.datetime(2024, 10, 1)
        df = yf.download(stock, start=start, end=end)
        
        # Calculate Exponential Moving Averages (EMA)
        ema20 = df.Close.ewm(span=20, adjust=False).mean()
        ema50 = df.Close.ewm(span=50, adjust=False).mean()
        ema100 = df.Close.ewm(span=100, adjust=False).mean()
        ema200 = df.Close.ewm(span=200, adjust=False).mean()
        
        # Plot 1: 20 & 50 Days EMA
        fig1, ax1 = plt.subplots(figsize=(12, 6))
        ax1.plot(df.Close, 'y', label='Closing Price')
        ax1.plot(ema20, 'g', label='EMA 20')
        ax1.plot(ema50, 'r', label='EMA 50')
        ax1.set_title("Closing Price vs Time (20 & 50 Days EMA)")
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Price")
        ax1.legend()
        ema_chart_path = "static/ema_20_50.png"
        fig1.savefig(ema_chart_path)
        plt.close(fig1)
        
        # Plot 2: 100 & 200 Days EMA
        fig2, ax2 = plt.subplots(figsize=(12, 6))
        ax2.plot(df.Close, 'y', label='Closing Price')
        ax2.plot(ema100, 'g', label='EMA 100')
        ax2.plot(ema200, 'r', label='EMA 200')
        ax2.set_title("Closing Price vs Time (100 & 200 Days EMA)")
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Price")
        ax2.legend()
        ema_chart_path_100_200 = "static/ema_100_200.png"
        fig2.savefig(ema_chart_path_100_200)
        plt.close(fig2)
        
        # --- Begin Deep Learning Model Integration ---
        # Data splitting
        data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
        data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70):])
        
        # Scaling data
        scaler = MinMaxScaler(feature_range=(0, 1))
        data_training_array = scaler.fit_transform(data_training)
        
        # Prepare data for prediction using last 100 days of training data
        past_100_days = data_training.tail(100)
        final_df = pd.concat([past_100_days, data_testing], ignore_index=True)
        input_data = scaler.fit_transform(final_df)
        
        x_test, y_test = [], []
        for i in range(100, input_data.shape[0]):
            x_test.append(input_data[i - 100:i])
            y_test.append(input_data[i, 0])
        x_test, y_test = np.array(x_test), np.array(y_test)
        
        # Make predictions
        y_predicted = model.predict(x_test)
        
        # Inverse scaling for predictions
        scale_factor = 1 / scaler.scale_[0]
        y_predicted = y_predicted * scale_factor
        y_test = y_test * scale_factor
        
        # Plot 3: Prediction vs Original Trend
        fig3, ax3 = plt.subplots(figsize=(12, 6))
        ax3.plot(y_test, 'g', label="Original Price", linewidth=1)
        ax3.plot(y_predicted, 'r', label="Predicted Price", linewidth=1)
        ax3.set_title("Prediction vs Original Trend")
        ax3.set_xlabel("Time")
        ax3.set_ylabel("Price")
        ax3.legend()
        prediction_chart_path = "static/stock_prediction.png"
        fig3.savefig(prediction_chart_path)
        plt.close(fig3)
        # --- End Deep Learning Model Integration ---
        
        # Save dataset as CSV
        csv_file_path = f"static/{stock}_dataset.csv"
        df.to_csv(csv_file_path)
        
        return render_template('index.html', 
                               plot_path_ema_20_50=ema_chart_path, 
                               plot_path_ema_100_200=ema_chart_path_100_200, 
                               plot_path_prediction=prediction_chart_path,
                               data_desc=df.describe().to_html(classes='table table-bordered'),
                               dataset_link=csv_file_path)
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    from flask import send_file
    return send_file(f"static/{filename}", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
