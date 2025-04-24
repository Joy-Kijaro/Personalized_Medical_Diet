import streamlit as st
import pandas as pd
import pickle

df = pd.read_csv("data/Personalized_Diet_Recommendations.csv")

with open("recommended_calories_model.pkl", "rb") as file:
    model = pickle.load(file)


def align_features_for_prediction(input_data: pd.DataFrame, expected_columns: list) -> pd.DataFrame:
    aligned_data = pd.DataFrame(columns=expected_columns)
    for col in expected_columns:
        if col in input_data.columns:
            aligned_data[col] = input_data[col]
        else:
            aligned_data[col] = 0
    return aligned_data


st.subheader("User Predictions")
if st.checkbox("Show Raw Data"):
    st.dataframe(df.head())

st.write("**Individual Details:**")
with st.expander("Enter Your Details"):
    Gender = st.radio("Select Gender", options=df["Gender"].unique())
    Age = st.number_input("(Age) : ", min_value=0, max_value=120, format="%d")
    Weight = st.number_input("Weight (kgs) : ")
    Height = st.number_input("Height (m) : ")
    Systolic_Pressure = st.number_input("Systolic Pressure:", min_value=0, max_value=240, format="%d")
    Diastolic_Pressure = st.number_input("Diastolic Pressure:", min_value=0, max_value=240, format="%d")
    Cholesterol_Level = st.number_input("Cholesterol Level (mg/dL):", min_value=50, max_value=300, format="%d")
    Blood_Sugar_Level = st.number_input("Blood Sugar Level (mg/dL):", min_value=50, max_value=300, format="%d")
    Submit = st.button("Submit")

st.write("**BMI Calculation:**")
if Height > 0:
    BMI = round(Weight / (Height ** 2), 1)
    st.write(f"Your BMI is {BMI}")
else:
    BMI = None
    st.warning("Please enter valid weight and height to calculate BMI.")

st.write("**Chronic Condition Assessment:**")
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

if Submit and BMI is not None:
    expected_features = model.feature_names_in_
user_inputs = {
    "Gender": Gender,
    "Age": Age,
    "Weight": Weight,
    "Height": Height,
    "Systolic_Pressure": Systolic_Pressure,
    "Diastolic_Pressure": Diastolic_Pressure,
    "Cholesterol_Level": Cholesterol_Level,
    "Blood_Sugar_Level": Blood_Sugar_Level,
    "BMI": BMI
}

input_data = pd.DataFrame([{
    feature: user_inputs.get(feature, 0) for feature in expected_features
}])
prediction = model.predict(input_data)[0]
st.success(f"✅ Your Recommended Caloric Intake is approximately: **{int(prediction)} calories/day**")
