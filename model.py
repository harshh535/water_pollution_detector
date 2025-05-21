import streamlit as st
import numpy as np
from catboost import CatBoostClassifier

def load_model():
    model = CatBoostClassifier()
    model.load_model("catboost_model.cbm")  # Make sure this file is in the same directory
    return model

def app():
    st.title("💧 Water Potability Prediction Model")

    st.write("Enter the following values to check water potability:")

    # Inputs
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1)
    turbidity = st.number_input("Turbidity (NTU)", min_value=0.0)
    solids = st.number_input("Solids (ppm)", min_value=0.0)
    conductivity = st.number_input("Conductivity (μS/cm)", min_value=0.0)

    if st.button("Check Potability"):
        model = load_model()
        features = np.array([[ph, turbidity, solids, conductivity]])
        prediction = model.predict(features)

        if prediction[0] == 1:
            st.success("✅ The water is **potable**.")
        else:
            st.error("❌ The water is **not potable**.")

