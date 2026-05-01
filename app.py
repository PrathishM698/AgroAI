import streamlit as st
import joblib
import pandas as pd
from profit import calculate_profit
from weather import get_weather
import matplotlib.pyplot as plt

# Load model
model = joblib.load("model.pkl")

# Page settings
st.set_page_config(page_title="AgroAI Guardian", layout="centered")

st.title("🌾 AgroAI Guardian")
st.subheader("AI-Based Smart Agriculture System")

# 🌦 Weather
weather = get_weather("Chennai")
st.markdown("### 🌦 Live Weather")
st.write("🌡 Temperature:", weather["temperature"])
st.write("💧 Humidity:", weather["humidity"])

st.markdown("---")

# 🎛 Inputs
st.markdown("### 🧪 Enter Soil & Climate Data")

N = st.number_input("Nitrogen (N)", 0, 150, 90)
P = st.number_input("Phosphorus (P)", 0, 150, 40)
K = st.number_input("Potassium (K)", 0, 150, 40)

temp = st.slider("Temperature (°C)", 0.0, 50.0, 25.0)
hum = st.slider("Humidity (%)", 0.0, 100.0, 80.0)
ph = st.slider("Soil pH", 0.0, 14.0, 6.5)
rain = st.slider("Rainfall (mm)", 0.0, 300.0, 200.0)

# 🚀 Prediction
if st.button("🔍 Predict Crop"):
    features = [[N, P, K, temp, hum, ph, rain]]

    pred = model.predict(features)[0]
    profit = calculate_profit(pred)

    st.success(f"🌱 Recommended Crop: {pred.upper()}")
    st.info(f"💰 Expected Profit: ₹ {profit}")

    # 📊 Prediction probabilities
    probs = model.predict_proba(features)[0]
    crops = model.classes_

    df = pd.DataFrame({
        "Crop": crops,
        "Confidence": probs
    }).sort_values(by="Confidence", ascending=False)

    # Show table
    st.markdown("### 📊 Top Crop Suggestions")
    st.dataframe(df.head(3))

    # 📈 Graph (FIXED VERSION)
    st.markdown("### 📈 Prediction Confidence Graph")

    plt.figure(figsize=(6,4))
    plt.bar(df["Crop"], df["Confidence"])
    plt.xticks(rotation=45)
    plt.xlabel("Crop")
    plt.ylabel("Confidence")
    plt.title("Crop Prediction Confidence")

    st.pyplot(plt)