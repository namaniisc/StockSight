# StockSight – Stock Trend Prediction

A Flask-based web application for downloading stock data, performing exploratory data analysis (EDA), visualizing price trends (including candlestick charts and moving averages), and predicting future stock prices using LSTM (Long Short-Term Memory) neural networks.

## 🎬 Demo

![Demo](StockSight.gif)

## 🔍 Overview

This project demonstrates a full end-to-end pipeline for stock trend prediction:

1. **Data Acquisition**: Download historical price data from Yahoo Finance using `yfinance`.
2. **Exploratory Data Analysis**: Display raw data, descriptive statistics, and visualize:
   - Line charts of Open, High, Low, Close, Volume
   - Candlestick plots
   - Simple Moving Averages (SMA) and Exponential Moving Averages (EMA)
3. **Modeling**: Prepare data with `MinMaxScaler`, split into training/testing sets, then train an LSTM model to forecast future prices.
4. **Web Interface**: Use Flask to build a front-end where users enter a stock ticker to:
   - View EDA charts
   - Download the raw CSV
   - See predictions overlaid with actual prices


## 💡 Key Features

- **Download & Preview Data**: Fetch any public stock by ticker symbol.
- **Descriptive Statistics**: Summary statistics (mean, std, percentiles).
- **Interactive Visualizations**: 
  - Candlestick charts with Plotly
  - Line plots for OHLC & Volume
  - SMA & EMA overlays
- **LSTM-based Forecasting**: Predict next-day or multi-day prices.
- **Model Persistence**: Save/load trained model (`.h5` file) to avoid retraining.
- **CSV Export**: Download the processed dataset.


## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Web Framework**: Flask
- **Data Handling**: Pandas, NumPy
- **Visualization**: Matplotlib, Plotly
- **Finance API**: yfinance
- **Machine Learning**:
  - Preprocessing: Scikit-learn (`MinMaxScaler`)
  - Deep Learning: TensorFlow / Keras (Sequential API, LSTM layers)
- **Template Rendering**: Jinja2 (Flask)


## 🚀 Installation & Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/namaniisc/StockSight.git
   cd StockSight
   ```

2. **Create & Activate a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate        # Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download Pretrained Model (optional)**

   If you wish to skip training, download `stock_dl_model.h5` into the project root.


## 📂 Project Structure

```
├── app.py                   # Flask application
├── models/                  # Saved Keras model (.h5)
├── static/                  # Generated plots & downloaded CSVs
├── templates/
│   └── index.html           # Main UI template
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── notebooks/               # Jupyter notebooks used for prototyping
```


## ⚙️ Usage

1. **Run the Flask App**

   ```bash
   flask run      # or python app.py
   ```

2. **Interact**

   - Open your browser to `http://127.0.0.1:5000`
   - Enter a stock ticker (e.g., `AAPL`, `POWERGRID.NS`)
   - View EDA charts, download CSV, and see LSTM forecasts.


## 📊 Model Training (Optional)

If you want to retrain the LSTM model:

1. Open `notebooks/train_model.ipynb`.
2. Adjust hyperparameters (e.g., lookback window, epochs).
3. Run all cells to preprocess data, train the model, and save `stock_dl_model.h5`.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a Pull Request.


