
import streamlit as st
import joblib
from response_agent import response_agent
from report_generator import generate_report

# Load model
model = joblib.load("models/risk_model.pkl")


st.set_page_config(page_title="FloodGuard AI", layout="wide")

st.title("🌊 FloodGuard AI — Disaster Prediction & Response System")
st.write("AI-powered Flood Risk Prediction + Emergency Response Planning")

st.sidebar.header("Enter Live Weather Conditions")

rainfall = st.sidebar.slider("Rainfall (mm)", 50, 500, 200)
temperature = st.sidebar.slider("Temperature (°C)", 20, 45, 30)
humidity = st.sidebar.slider("Humidity (%)", 40, 100, 70)
river_level = st.sidebar.slider("River Level (m)", 1, 10, 5)

# Predict
sample = [[rainfall, temperature, humidity, river_level]]
risk_level = model.predict(sample)[0]

st.subheader("⚠️ Predicted Flood Risk Level:")
st.success(risk_level)

# Response Plan
plan = response_agent(risk_level)

st.subheader("🚨 Autonomous Emergency Response Plan")
st.json(plan)

# Report Generator
st.subheader("📄 Emergency Report for Authorities")

zone = st.text_input("Enter Affected Zone Name", "Bihar - Patna Region")

if st.button("Generate Report"):
    report = generate_report(zone, risk_level, plan)
    st.text(report)
