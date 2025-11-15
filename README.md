# AI-Crop-Fertilizer-Recommendation-System


🌾 AI Crop & Fertilizer Recommendation System

An intelligent system that recommends the best crop and the right fertilizer based on soil conditions, weather parameters, and nutrient levels using Machine Learning.

🚀 Project Overview

This project uses machine learning models to help farmers and agricultural organizations make informed decisions about:

Which crop is most suitable for the current soil & climate

Which fertilizer will maximize crop yield

Improving sustainability

Reducing excessive fertilizer usage

Increasing overall crop productivity

The aim is to support modern agriculture with data-driven insights.

📂 Tech Stack

Python 3.x

NumPy, Pandas

Matplotlib / Seaborn

Scikit-learn

Flask / Streamlit (optional UI)

Jupyter Notebook


📁 Project Structure
AI-Crop-Fertilizer-Recommendation/
│── data/
│   ├── crop_recommendation.csv
│   ├── fertilizer.csv
│── notebook/
│   └── AI_Crop_&_Fertilizer_Recommendation_System.ipynb
│── models/
│   ├── crop_model.pkl
│   ├── fertilizer_model.pkl
│── app/
│   ├── app.py  (Flask/Streamlit UI)
│── README.md
│── requirements.txt



🧠 ML Models Used
✔ Crop Recommendation Model

Algorithm: Random Forest Classifier

Inputs:

Nitrogen (N)

Phosphorus (P)

Potassium (K)

Temperature

Humidity

pH

Rainfall

✔ Fertilizer Recommendation Model

Algorithm: Rule-based / Decision Tree

Inputs:

N, P, K values

Crop type

Soil condition

Nutrient deficiency levels
