import streamlit as st

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

st.write(uploaded_file.head())

