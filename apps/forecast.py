import folium
import pandas as pd
import geopandas as gpd
import streamlit as st
import numpy as np
from streamlit_folium import folium_static
import datetime as dt

def app():
    st.title("Forecasting Clusters of Covid-19 in the US")
    st.markdown(
        """
    This app is a demonstration of covid-1 forecasing of clusters
    """
    )

    row1_col1, row1_col2 = st.columns([1, 1])
    width = 450
    height = 450

    with row1_col2:
        
    #    selected = st.selectbox(
    #        "something", ["Travel", "Genetic spread","Distance"], index=0)
    #    st.image('https://github.com/rmbeard/data/raw/main/covid_res_2_23.png',width=450)
       st.write('Maybe a timerseries of the performance of the forecasting ')


    slider= '11/1/2021'
    covid_data = pd.read_csv('https://raw.githubusercontent.com/rmbeard/data/main/us_covid_data.csv')
    json1 = gpd.read_file("https://github.com/giswqs/streamlit-geospatial/raw/master/data/us_states.geojson")
   
    df1= covid_data['date'] == slider
    covid_data1=covid_data[df1]
    covid_data=covid_data1
    json = json1.merge(covid_data, on='STUSPS')
    json1=json
    with row1_col1:
        choice = ['conf_cases','prob_cases', 'tot_death']
        choice_selected = st.selectbox("Select Variable of interest to view ", choice,index=0)
        #print('covid data', covid_data.head(49))
        m = folium.Map(location=[39, -97], tiles='CartoDB positron',name="Light Map",
                zoom_start=4,
                attr='My')

        #print(choice_selected)
        folium.Choropleth(
            geo_data=json1,
            name="choropleth",
            #data=json1,
            columns=["STUSPS", choice_selected],
            key_on="feature.properties.STUSPS",
            fill_color="YlOrRd",
            fill_opacity=0.7,
            line_opacity=.1,
            legend_name=choice_selected+"(%)",
        ).add_to(m)
        folium.features.GeoJson(json1, name="STUSPS",
                                popup=folium.features.GeoJsonPopup(fields=['STUSPS'])).add_to(m)
        folium_static(m, width=700, height=350)
    ## Range selector
    cols1,_ = st.columns((1,2)) # To make it narrower        
    #format = 'MMM DD, YYYY'  # format output
    format = 'MMM DD, YYYY'  # format output
    start_date = dt.date(year=2020,month=1,day=22)  #  I need some range in the past
    end_date = dt.date(year=2021,month=11,day=1) 
    slider = cols1.slider('Select a date to view clustering present for that day', min_value=start_date, value=end_date ,max_value=end_date, format=format)
    ## check
   
    st.table(pd.DataFrame([[ slider]],
            columns=['selected'],
                    index=['Date']))   
    slider = cols1.slider('Select the number of weeks into the future to view clustering forecast', min_value=1, value=4 ,max_value=4)
   