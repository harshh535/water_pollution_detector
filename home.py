import streamlit as st

def app():
    st.title("🏠 Welcome to Water Potability Checker")
    st.write("""
        This web app allows you to check whether water is potable based on various physical and chemical properties.

        Navigate to the **Model** page to try out predictions using pH, turbidity, solids, and conductivity values.
    """)
