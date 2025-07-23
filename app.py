# app.py
import streamlit as st
from weather_api import get_weather
import plotly.graph_objects as go

st.set_page_config(page_title="Live Weather Dashboard", page_icon="☁️", layout="centered")

st.title("🌦️ Live Weather Dashboard")
city = st.text_input("Enter a city name:")

if city:
    weather = get_weather(city)
    if weather:
        st.subheader(f"Weather in {weather['city']}")
        st.write(f"**Temperature:** {weather['temp']}°C")
        st.write(f"**Humidity:** {weather['humidity']}%")
        st.write(f"**Condition:** {weather['description'].capitalize()}")

        # Weather condition message
        condition = weather["main"].lower()
        if "rain" in condition:
            st.info("☔ It's raining. Don't forget your umbrella!")
        elif "cloud" in condition:
            st.info("☁️ It's cloudy today.")
        elif "clear" in condition:
            st.info("☀️ It's a clear sky!")
        elif "snow" in condition:
            st.info("❄️ Snowy weather outside.")
        else:
            st.info("🌈 Mixed weather conditions.")

        # Temperature graph (past 6 hours as mock)
        temps = [weather["temp"] - 2, weather["temp"] - 1, weather["temp"], weather["temp"] + 1, weather["temp"] + 0.5]
        hours = ["-4h", "-3h", "-2h", "-1h", "Now"]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=hours, y=temps, mode='lines+markers', name='Temp'))
        fig.update_layout(title="📈 Temperature Trend (Mock)", xaxis_title="Time", yaxis_title="Temp (°C)")
        st.plotly_chart(fig)
    else:
        st.error("City not found or error fetching data.")
