import streamlit as st

st.set_page_config(page_title="Home")
st.title("PERSONALIZED DIET APP")
col1, col2, = st.columns(2)
with col1:
    st.image("Screenshot (70).png", width=500)
with col2:
    st.caption("You are what you eat, so don't be fast, cheap or fake")

st.subheader("WELCOME ABOARD!")
st.write("""
*"The doctor of the future will give no medicine but will interest his patients in the care of the human frame, in diet and in the cause and prevention of disease."*
 — **Thomas Edison**

This explains the incorporation of preventive care, nutrition, and lifestyle in healthcare, over just prescribing medication.
""")
st.subheader("APP OFFERING")
st.write("This app allows for **personalized diet recommendations** for Individuals living with chronic conditions i.e Diabetes, Hypertension, Heart Disease, and Obesity based on their unique health parameters and lifestyle habits.")

