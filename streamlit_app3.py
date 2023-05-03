# import streamlit as st
# import pandas as pd

# uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

# st.write(pd.read_excel(uploaded_file).head())

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Upload Excel file
uploaded_file = st.file_uploader("Choose a file", type=["xlsx", "xls"])

# Read Excel file and display first few rows
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
#     st.write(df.head())
    
    st.write('Filter by : ')
    
    options = ["Delivery_Associate", "Dropoff_Location","All","week"]
    selected_option = st.selectbox("Select an option", options)
    if selected_option == 'All':
        df2= df
        df2[['latitude', 'longitude']] = df2['Actual_Location'].str.split(',', expand=True)
        df2['latitude'] = df2['latitude'].str.replace('°', '').str.strip().astype(float)
        df2['longitude'] = df2['longitude'].str.replace('°', '').str.strip().astype(float)
        st.write(' Actual location ')
        df2['data']=df2['Delivery_Associate'] + '   ' + df2['Distance_between_Actual_and_Planned']+'   ' + df2['Dropoff_Location'] + '     ' + df2['Service_Area']  
        fig = px.scatter_mapbox(df2, lat='latitude', lon='longitude',hover_data={'latitude': False, 'longitude': False},text = df2['data'] ,zoom=6, height=500,size_max = 20, 
                                        color_discrete_sequence=['red'])
        fig.update_layout(mapbox_style='open-street-map', mapbox_zoom=6,
                      mapbox_center={'lat': 37.7749, 'lon': -122.4194})
        fig.show()
        st.plotly_chart(fig)
    elif selected_option == "week":
        range_slider = st.slider('Select a range of week', 10.0, 17.0, (10.0,17.0), 1.0)

        # Get the selected range
        start_value = range_slider[0]
        end_value = range_slider[1]
        df2 = df[(df['Week'] >= start_value) and (df['Week'] <= end_value)]
        df2[['latitude', 'longitude']] = df2['Actual_Location'].str.split(',', expand=True)
        df2['latitude'] = df2['latitude'].str.replace('°', '').str.strip().astype(float)
        df2['longitude'] = df2['longitude'].str.replace('°', '').str.strip().astype(float)
        
    #     df2[['latitude1', 'longitude1']] = df2['Planned_Location'].str.split(',', expand=True)
    #     df2['latitude1'] = df2['latitude1'].str.replace('°', '').str.strip().astype(float)
    #     df2['longitude1'] = df2['longitude1'].str.replace('°', '').str.strip().astype(float)
    #     fig = px.scatter_mapbox(df2,
    #                         lat='latitude',
    #                         lon= 'longitude',
    #                         hover_name=df2['Distance_between_Actual_and_Planned']+'\n'+df2['Dropoff_Location'],
    #                         zoom=2)

    #     # Customize plot as desired
    #     fig.update_layout(title="World Map with Latitude and Longitude Markers")

    #     fig.show()

    #     # Display plot in Streamlit app
    #     st.plotly_chart(fig)
    #     fig = make_subplots(rows=1, cols=2)

        # create a Plotly scatter plot
        st.write(' Actual location ')
        df2['data']=df2['Delivery_Associate'] + '   ' + df2['Distance_between_Actual_and_Planned']+'   ' + df2['Dropoff_Location'] + '     ' + df2['Service_Area']  
        fig = px.scatter_mapbox(df2, lat='latitude', lon='longitude',hover_data={'latitude': False, 'longitude': False},text = df2['data'] ,zoom=6, height=500,size_max = 20, 
                                        color_discrete_sequence=['red'])
        fig.update_layout(mapbox_style='open-street-map', mapbox_zoom=6,
                      mapbox_center={'lat': 37.7749, 'lon': -122.4194})
   
#     df2['data']= df2['Distance_between_Actual_and_Planned']+'\n'+df2['Dropoff_Location']
#     fig2 = px.scatter_mapbox(df2, lat='latitude1', lon='longitude1',text = df2['data'] ,zoom=6, height=500,size_max = 20, 
#                                     color_discrete_sequence=['blue'])
#     fig2.update_layout(mapbox_style='open-street-map', mapbox_zoom=6,
#                   mapbox_center={'lat': 37.7749, 'lon': -122.4194})
#     fig = go.Figure(go.Scattergeo(
#         lon = df2['longitude'],
#         lat = df2['latitude'],
#         mode = 'markers',
        
#     ))

#     # set the map layout and configuration
#     fig.update_layout(
#         geo_scope='usa-california',  # set the scope of the map to USA
#         geo=dict(
#             scope='usa-california',
#             showland=True,
#             landcolor='rgb(243, 243, 243)',
#             countrycolor='rgb(204, 204, 204)'
#         ),
#         height=600)
    
#     fig.update_layout(title="World Map with Latitude and Longitude Markers")
#     # show the plot
        fig.show()
        st.plotly_chart(fig)                         
        
    else:
        selected_option2 = st.selectbox("Select an option", df[selected_option].unique())
        df2 = df[df[selected_option] == selected_option2]

    #     st.write(df2.head())

    #     lat,long = df2['Actual_Location'].map(lambda x: x.split(','))
        df2[['latitude', 'longitude']] = df2['Actual_Location'].str.split(',', expand=True)
        df2['latitude'] = df2['latitude'].str.replace('°', '').str.strip().astype(float)
        df2['longitude'] = df2['longitude'].str.replace('°', '').str.strip().astype(float)
        
    #     df2[['latitude1', 'longitude1']] = df2['Planned_Location'].str.split(',', expand=True)
    #     df2['latitude1'] = df2['latitude1'].str.replace('°', '').str.strip().astype(float)
    #     df2['longitude1'] = df2['longitude1'].str.replace('°', '').str.strip().astype(float)
    #     fig = px.scatter_mapbox(df2,
    #                         lat='latitude',
    #                         lon= 'longitude',
    #                         hover_name=df2['Distance_between_Actual_and_Planned']+'\n'+df2['Dropoff_Location'],
    #                         zoom=2)

    #     # Customize plot as desired
    #     fig.update_layout(title="World Map with Latitude and Longitude Markers")

    #     fig.show()

    #     # Display plot in Streamlit app
    #     st.plotly_chart(fig)
    #     fig = make_subplots(rows=1, cols=2)

        # create a Plotly scatter plot
        st.write(' Actual location ')
        df2['data']=df2['Delivery_Associate'] + '   ' + df2['Distance_between_Actual_and_Planned']+'   ' + df2['Dropoff_Location'] + '     ' + df2['Service_Area']  
        fig = px.scatter_mapbox(df2, lat='latitude', lon='longitude',hover_data={'latitude': False, 'longitude': False},text = df2['data'] ,zoom=6, height=500,size_max = 20, 
                                        color_discrete_sequence=['red'])
        fig.update_layout(mapbox_style='open-street-map', mapbox_zoom=6,
                      mapbox_center={'lat': 37.7749, 'lon': -122.4194})
   
#     df2['data']= df2['Distance_between_Actual_and_Planned']+'\n'+df2['Dropoff_Location']
#     fig2 = px.scatter_mapbox(df2, lat='latitude1', lon='longitude1',text = df2['data'] ,zoom=6, height=500,size_max = 20, 
#                                     color_discrete_sequence=['blue'])
#     fig2.update_layout(mapbox_style='open-street-map', mapbox_zoom=6,
#                   mapbox_center={'lat': 37.7749, 'lon': -122.4194})
#     fig = go.Figure(go.Scattergeo(
#         lon = df2['longitude'],
#         lat = df2['latitude'],
#         mode = 'markers',
        
#     ))

#     # set the map layout and configuration
#     fig.update_layout(
#         geo_scope='usa-california',  # set the scope of the map to USA
#         geo=dict(
#             scope='usa-california',
#             showland=True,
#             landcolor='rgb(243, 243, 243)',
#             countrycolor='rgb(204, 204, 204)'
#         ),
#         height=600)
    
#     fig.update_layout(title="World Map with Latitude and Longitude Markers")
#     # show the plot
        fig.show()
        st.plotly_chart(fig)
#     st.write(' Planned location ')
#     fig2.show()
#     st.plotly_chart(fig2)
#     df_sub = df[]
    
#     unique_1 = df['Delivery_Associate'].unique()
#     unique_2 = df['Dropoff_Location'].unique()
    
#     df_group = df.group_by('Delivery_Associate')
#     st.write(df_group.head())
    
