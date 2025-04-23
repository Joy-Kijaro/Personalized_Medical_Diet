import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

st.header("Models")

st.subheader("Data Preparation and Splitting")

df = pd.read_csv("data/Personalized_Diet_Recommendations.csv")
x = df.drop(columns=['Patient_ID', 'Recommended_Meal_Plan'])
y = df['Recommended_Meal_Plan']

categorical_cols = ['Gender', 'Chronic_Disease', 'Genetic_Risk_Factor', 'Allergies',
                    'Alcohol_Consumption', 'Smoking_Habit', 'Preferred_Cuisine',
                    'Dietary_Habits', 'Food_Aversions', 'Physical_Activity_Level',
                    'Stress_Level', 'Alcohol_Consumption', 'Obese', 'Diabetic',
                    'Hypertensive', 'Exercise_Level']

for col in categorical_cols:
    if col in x.columns:
        le = LabelEncoder()
        x[col] = le.fit_transform(x[col])

numerical_cols = x.select_dtypes(include=['int64', 'float64']).columns

scaler = StandardScaler()
x[numerical_cols] = scaler.fit_transform(x[numerical_cols])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

st.write("Sample of preprocessed training data:")
st.dataframe(x_train.head())

st.subheader("Regression - Predicting Recommended Calories")
with st.expander("Model Training & Evaluation", expanded=True):

    x = df.drop(columns=['Patient_ID', 'Recommended_Calories'])
    y = df['Recommended_Calories']

    regression_categorical = categorical_cols + ["Recommended_Meal_Plan"]

    for col in regression_categorical:
        if col in x.columns:
            le = LabelEncoder()
            x[col] = le.fit_transform(x[col])

numerical_cols = x.select_dtypes(include=['int64', 'float64']).columns
scaler = StandardScaler()
x[numerical_cols] = scaler.fit_transform(x[numerical_cols])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(random_state=42),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Support Vector Regressor": SVR(),
        "Gradient Boosting": GradientBoostingRegressor(random_state=42)
    }

results = []

for name, model in models.items():
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)

        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)

        results.append({
            "Model": name,
            "R² Score": round(r2, 4),
            "MAE": round(mae, 2),
            "MSE": round(mse, 2),
            "RMSE": round(rmse, 2)
        })

st.write("Model Performance Summary")

st.dataframe(pd.DataFrame(results).sort_values("R² Score", ascending=False))

st.write("Assessing Model Performance")
y_pred = model.predict(x_test[:5])

results = pd.DataFrame({
    'Predicted Calories': y_pred,
    'Actual Calories': y_test[:5].values
})

st.dataframe(results)
