import streamlit as st
import pandas as pd

st.subheader("Data Header")
df = pd.read_csv("data/Personalized_Diet_Recommendations.csv")

st.dataframe(df.head())

st.subheader("Description")
st.write(df.describe())

st.subheader("Columns")
st.write(df.columns)
