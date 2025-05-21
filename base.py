import streamlit as st
import home
import about
import model

st.set_page_config(page_title="Water Potability Checker", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Model", "About"])

# Page router
if page == "Home":
    home.app()
elif page == "Model":
    model.app()
elif page == "About":
    about.app()
