import streamlit as st
import pandas as pd

st.subheader("User Predictions")

df = pd.read_csv("data/Personalized_Diet_Recommendations.csv")

st.write("**Individual Details**")
with st.expander("Enter Your Details"):
    Age = st.number_input("(Age) : ", min_value=0, max_value=120, format="%d")
    Weight = st.number_input("Weight (kgs) : ")
    Height = st.number_input("Height (m) : ")
    Systolic_Pressure = st.number_input("Systolic Pressure:", min_value=0, max_value=240, format="%d")
    Diastolic_Pressure = st.number_input("Diastolic Pressure:", min_value=0, max_value=240, format="%d")
    Cholesterol_Level = st.number_input("Cholesterol Level (mg/dL):", min_value=50, max_value=300, format="%d")
    Blood_Sugar_Level = st.number_input("Blood Sugar Level (mg/dL):", min_value=50, max_value=300, format="%d")

st.write("**BMI Calculation**")
if Height > 0:
    BMI = round(Weight / (Height ** 2), 1)
    st.write(f"Your BMI is: {BMI}")
else:
    BMI = None
    st.warning("Please enter valid weight and height to calculate BMI.")

st.write("**Chronic Condition Assessment**")
conditions = []

if Systolic_Pressure >= 180 and Diastolic_Pressure >= 120:
    conditions.append("Hypertension")
if Cholesterol_Level >= 160:
    conditions.append("Heart Disease")
if Blood_Sugar_Level >= 126:
    conditions.append("Diabetes")
if BMI and BMI >= 30:
    conditions.append("Obesity")

if conditions:
    st.warning("Potential Chronic Condition(s) Identified:")
    for cond in conditions:
        st.markdown(f"- {cond}")
else:
    st.success("No high-risk conditions detected based on input parameters.")
