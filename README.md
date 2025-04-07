# StockSight – Stock Trend Prediction

StockSight is a Flask-based web application that predicts future trends in stock prices using deep learning and historical stock data. It allows users to enter a stock ticker symbol, visualize trends with Exponential Moving Averages (EMAs), and compare predicted prices with actual prices.

## 🚀 Features

- 📈 Download stock data from Yahoo Finance
- 📊 Visualize 20/50 and 100/200 days EMAs
- 🤖 Predict stock price trends using a trained deep learning model
- 🧾 View descriptive statistics of the stock
- 📥 Download the dataset used for predictions

## 🛠️ Tech Stack

- **Frontend**: HTML5, Bootstrap 5
- **Backend**: Flask (Python)
- **ML/DL**: TensorFlow/Keras, LSTM model
- **Data**: yFinance API
- **Visualization**: Matplotlib

## 🔧 Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/namaniisc/StockSight.git
    cd StockSight
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your trained model to the root folder:
    - File name: `stock_dl_model.h5`

4. Run the application:
    ```bash
    python app.py
    ```

5. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```


