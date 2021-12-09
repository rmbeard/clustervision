import folium
import pandas as pd
import geopandas as gpd
import streamlit as st
import numpy as np
from streamlit_folium import folium_static
import datetime as dt


def app():
    st.title("Visualizing Clusters of Covid-19 in the US")
    st.subheader(
        """
    This app visualizes variables of interest along side a demonstration of covid-19 geo-spatial clusters in US for a selected time
    """
    )

    row1_col1, row1_col2 = st.columns([1, 1])
    width = 450
    height = 450

    with row1_col2:
        
        selected = st.selectbox(
            "Select cluster weighting variable to view Clustering", ["Travel", "Genetic spread","Distance"], index=0)
        st.image('https://github.com/rmbeard/data/raw/main/covid_res_2_23.png',width=450)
        st.write('Maybe a timerseries of the performance of the clustering, as well as another map here so can can view side by side')


    slider= '11/1/2021'
    covid_data = pd.read_csv('https://raw.githubusercontent.com/rmbeard/data/main/us_covid_data.csv')
    json1 = gpd.read_file("https://github.com/giswqs/streamlit-geospatial/raw/master/data/us_states.geojson")
    df1= covid_data['date'] == slider
    covid_data1=covid_data[df1]
    covid_data=covid_data1
    json2 = json1.merge(covid_data, on='STUSPS')
    print(json2.head())
    json=json2[['STUSPS','date','new_case','conf_cases','prob_cases', 'tot_death','geometry']]
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
    max_days = end_date-start_date
        
    slider = cols1.slider('Select a date to view clustering present for that day', min_value=start_date, value=end_date ,max_value=end_date, format=format)
    ## check
   
  #  st.table(pd.DataFrame([[ slider]],
  #          columns=['selected'],
  #                  index=['Date']))
    st.write("map displays not functional in current version")