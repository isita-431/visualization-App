# import streamlit as st
# import pandas as pd

# uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

# st.write(pd.read_excel(uploaded_file).head())

import streamlit as st
import pandas as pd
import plotly.express as px


# Upload Excel file
uploaded_file = st.file_uploader("Choose a file", type=["xlsx", "xls"])

# Read Excel file and display first few rows
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write(df.head())
    
    st.write('Filter by : ')
    
    options = ["Delivery_Associate", "Dropoff_Location"]
    selected_option = st.selectbox("Select an option", options)
    selected_option2 = st.selectbox("Select an option", df[selected_option].unique())
    df2 = df[df[selected_option] == selected_option2]
    
    st.write(df2.head())

#     lat,long = df2['Actual_Location'].map(lambda x: x.split(','))
    df2[['latitude', 'longitude']] = df2['Actual_Location'].str.split(',', expand=True)
    df2['latitude'] = df2['latitude'].str.replace('°', '').str.strip().astype(float)
    df2['longitude'] = df2['longitude'].str.replace('°', '').str.strip().astype(float)
    
    fig = px.scatter_mapbox(df2,
                        lat='latitude',
                        lon= 'longitude',
                        hover_name=df2['Distance_between_Actual_and_Planned']+'\n'+df2['Dropoff_Location'],
                        zoom=2)

    # Customize plot as desired
    fig.update_layout(title="World Map with Latitude and Longitude Markers")
    
    fig.show()

    # Display plot in Streamlit app
    st.plotly_chart(fig)
#     df_sub = df[]
    
#     unique_1 = df['Delivery_Associate'].unique()
#     unique_2 = df['Dropoff_Location'].unique()
    
#     df_group = df.group_by('Delivery_Associate')
#     st.write(df_group.head())
    
