# Live Weather Prediction App

This is a simple Python project that fetches live weather data using the OpenWeatherMap API and uses a machine learning model to predict climate conditions such as `sunny`, `rainy`, or `cloudy`. The app is built with Streamlit for an interactive web interface.

---

## Features

- Get real-time weather data (temperature and humidity) for any city
- Predict climate conditions using a trained decision tree model
- Clean and simple interface using Streamlit
- Lightweight and easy to run locally

---

## Project Files

- `app.py` – Streamlit web application
- `weather_api.py` – Python script to fetch live weather data
- `train_model.py` – Trains the ML model using historical data
- `historical_weather.csv` – Training dataset
- `weather_predictor.pkl` – Saved ML model after training

---

## Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weather-predictor-app.git
cd weather-predictor-app
2. Install Required Python Packages

pip install streamlit pandas scikit-learn requests joblib

How to Use
Step 1: Get Your API Key
Visit: https://home.openweathermap.org/api_keys

Create a free account and copy your API key

Open weather_api.py and replace:
API_KEY = "your_actual_api_key"

Step 2: Train the Model
This step generates a .pkl file that will be used in the app.

python train_model.py

Step 3: Run the Web App

streamlit run app.py
