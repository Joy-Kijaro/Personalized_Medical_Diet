import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

df = pd.read_csv("data/Personalized_Diet_Recommendations.csv")

st.write("Gender, Disease & Meal Distributions")

fig, axes = plt.subplots(1, 3, figsize=(30, 10))

axes[0].set_title("Gender", fontsize=30)
sns.countplot(data=df, x="Gender", ax=axes[0])

axes[1].set_title("Disease Distribution", fontsize=30)
sns.countplot(data=df, x="Chronic_Disease", ax=axes[1])

axes[2].set_title("Recommended Meal Plans", fontsize=30)
sns.countplot(data=df, x="Recommended_Meal_Plan", ax=axes[2])
st.pyplot(fig)

st.write("BMI Vs. Exercise Frequency")
fig, ax = plt.subplots()
sns.boxplot(
    data = df,
    x = "Exercise_Frequency",
    y = "BMI",
    palette = "coolwarm")
plt.title("BMI vs. Exercise Frequency")
plt.xlabel("Exercise_Frequency")
plt.ylabel('BMI')

plt.tight_layout()
st.pyplot(fig)

st.write("Relationship between Dietary Habits, Caloric Intake, and BMI")

fig, axes = plt.subplots(1, 2, figsize=(30, 10))

axes[0].set_title("Caloric Intake vs. Dietary_Habits", fontsize=30)
sns.boxplot(
    data=df,
    x="Dietary_Habits",
    y="Caloric_Intake",
    palette="Dark2",
    ax=axes[0]
)

axes[1].set_title("BMI vs. Recommended_Meal_Plan", fontsize=30)
sns.boxplot(
    data=df,
    x="Recommended_Meal_Plan",
    y="BMI",
    palette="coolwarm",
    ax=axes[1]
)

st.pyplot(fig)

st.write("TO BE CONTINUED....")