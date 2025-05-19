import streamlit as st
from model.predictor import predict_outcomes
from utils.explain import explain_prediction

st.set_page_config(page_title="Life Path Simulator", layout="wide")
st.title("🔮 Life Path Simulator")
st.write("Fill in your life choices and see what your future might look like!")


# Basic Inputs
age = st.slider("Your Age", 18, 65, 25)
education = st.selectbox("Highest Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
career = st.selectbox("Career Path", ["Engineer", "Artist", "Doctor", "Entrepreneur", "Educator", "Other"])
sleep = st.slider("Average Sleep Hours", 4, 10, 7)
exercise = st.selectbox("Exercise Frequency", ["Rarely", "1-2x/week", "3-5x/week", "Daily"])
risk = st.slider("Risk Tolerance (0 = low, 10 = high)", 0, 10, 5)
location = st.selectbox("Region", ["Urban", "Suburban", "Rural"])

if st.button("🚀 Predict My Future"):
    inputs = {
        "age": age, "education": education, "career": career, "sleep": sleep,
        "exercise": exercise, "risk": risk, "location": location
    }
    prediction = predict_outcomes(inputs)
    st.subheader("📈 Predicted Future Stats:")
    st.metric("Estimated Income (2040)", f"${prediction['income']:,.0f}")
    st.metric("Life Satisfaction", f"{prediction['happiness']}/10")
    st.metric("Health Score", prediction['health'])
    st.metric("Relationship Stability", f"{prediction['love']}%")

    st.write("---")
    st.subheader("🔍 Explanation")
    explanation = explain_prediction(inputs)
    st.write(explanation)
