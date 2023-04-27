import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

st.write(pd.DataFrame(uploaded_file).head())

