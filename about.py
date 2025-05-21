import streamlit as st

def app():
    st.title("About")
    st.write("""
        This app was built using **Streamlit** and a pre-trained ML model to predict water potability.

        ### Features:
        - Input: pH, Turbidity, Solids, Conductivity
        - Output: Potable (Yes/No)
        - Model trained and tested for accuracy
    """)
