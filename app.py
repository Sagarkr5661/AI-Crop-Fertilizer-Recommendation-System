import streamlit as st
import numpy as np
import pickle

st.title("🌾 AI Crop & Fertilizer Recommendation System")

N = st.number_input("Nitrogen (N)", 0, 150)
P = st.number_input("Phosphorus (P)", 0, 150)
K = st.number_input("Potassium (K)", 0, 150)
temperature = st.number_input("Temperature (°C)", 0.0, 50.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0)
ph = st.number_input("pH", 0.0, 14.0)
rainfall = st.number_input("Rainfall (mm)", 0.0, 500.0)

@st.cache_resource
def load_model():
    with open("crop_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

def recommend_fertilizer(N, P, K):
    if N < 50:
        return "Add Nitrogen-rich fertilizer (Urea)"
    elif P < 50:
        return "Add Phosphorus-rich fertilizer (DAP)"
    elif K < 50:
        return "Add Potassium-rich fertilizer (MOP)"
    else:
        return "Balanced fertilizer (NPK 10:10:10)"

if st.button("Recommend Crop & Fertilizer"):
    crop = model.predict([[N, P, K, temperature, humidity, ph, rainfall]])[0]
    fert = recommend_fertilizer(N, P, K)
    st.success(f"🌱 Recommended Crop: **{crop}**")
    st.info(f"💧 Fertilizer Suggestion: **{fert}**")

