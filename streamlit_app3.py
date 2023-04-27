# import streamlit as st
# import pandas as pd

# uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

# st.write(pd.read_excel(uploaded_file).head())

import streamlit as st
import pandas as pd

# Upload Excel file
uploaded_file = st.file_uploader("Choose a file", type=["xlsx", "xls"])

# Read Excel file and display first few rows
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write(df.head())
