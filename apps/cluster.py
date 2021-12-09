import streamlit as st
#import leafmap.foliumap as leafmap
import datetime as dt
import pandas as pd
import numpy as np
import geopandas as gpd
from dateutil.relativedelta import relativedelta # to add days or years
#import matplotlib.pyplot as plt
import leafmap.deck as leafmap
import pydeck as pdk
#from pydeck.types import String
#import leafmap.kepler as leafmap
#import leafmap.colormaps as cm
#import plotly.express as px
#import plotly.graph_objects as go
import math

def calculate_elevation(val):
    return math.sqrt(val) * 10

COLOR_RANGE = [
    [65, 182, 196],
    [127, 205, 187],
    [199, 233, 180],
    [237, 248, 177],
    [255, 255, 204],
    [255, 237, 160],
    [254, 217, 118],
    [254, 178, 76],
    [253, 141, 60],
    [252, 78, 42],
    [227, 26, 28],
    [189, 0, 38],
    [128, 0, 38],
]

BREAKS = [-0.6, -0.45, -0.3, -0.15, 0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9, 1.05, 1.2]

def color_scale(val):
    for i, b in enumerate(BREAKS):
        if val < b:
            return COLOR_RANGE[i]
    return COLOR_RANGE[i]

def app():
    st.title("Visualizing Clusters of Covid-19 in the US")
    st.markdown(
        """
    This app is a demonstration of covid-19 geo-spatial clusters in US for a selected time
    """
    )

    row1_col1, row1_col2 = st.columns([2, 1])
    width = 550
    height = 400

    with row1_col2:
        selected = st.selectbox(
            "Select cluster weighting variable", ["Travel", "Genetic spread","Distance"], index=0
        
        )


    #url = "C:\\Users\\Rachel\\Google Drive\\StreaLitApps\\streamlit-geospatial\\data\\states\\Export_Output_2.shp"
    url = "https://github.com/giswqs/streamlit-geospatial/raw/master/data/us_states.geojson"
    df = pd.read_csv('https://raw.githubusercontent.com/rmbeard/data/main/us_covid_data_byState_over_Time.csv')
    #df1= df['date'] == '1/22/2020'
    #df = df[df1]
    df2 = gpd.read_file("https://github.com/giswqs/streamlit-geospatial/raw/master/data/us_states.geojson")
    gdf = df2.merge(df, on='STUSPS')
    file_path=url
    layer_name = "states"    
    container = st.container()
    slider= '11/1/2021'
    print(file_path)
    with row1_col1:
        #gdf = gpd.read_file(file_path)
        gdf1= gdf['date'] == slider
        sgdf=gdf[gdf1]
        lon = sgdf.centroid.iloc[0].x
        lat = sgdf.centroid.iloc[0].y
        #m = leafmap.Map(center=(lat, lon), draw_export=True)
        m = leafmap.Map(center=(lat, lon))
        df=sgdf[['STUSPS','new_case','geometry']]
        print(df)
        
        initial_view_state = pdk.ViewState(
        latitude=40, longitude=-100, zoom=3.2, max_zoom=16, pitch=0, bearing=0
        )
        #df["coordinates"] = url["features"].apply(lambda row: row["geometry"]["coordinates"])
        df["lon"] = df["geometry"].centroid.x
        df["lat"] = df["geometry"].centroid.y
        #df["elevation"] = url["features"].apply(lambda row: calculate_elevation(row["new_case"]["pop100k"]))
        #df["fill_color"] = url["features"].apply(lambda row: color_scale(row["new_case"]["tot_cases"]))
        #color_exp = f"[R, G, B]"
        layer1 = pdk.Layer(
            "GeoJsonLayer",
            df,
            pickable=True,
            opacity=0.5,
            stroked=True,
            filled=True,
            get_fill_color=[140, 10, 50],
            get_line_color=[0, 0, 0],
            get_line_width=2,
            line_width_min_pixels=2,
        )
        
        #m.add_gdf(df, layer_name=layer_name, fill_colors=["red", "green", "blue"])
        m=pdk.Deck(layers=layer1,initial_view_state=initial_view_state,
        map_style="light",)
   
        #m.to_streamlit(width=width, height=height)
        st.pydeck_chart(m)
    ## Range selector
    cols1,_ = st.columns((1,2)) # To make it narrower        
    #format = 'MMM DD, YYYY'  # format output
    format = 'MMM DD, YYYY'  # format output
    start_date = dt.date(year=2020,month=1,day=22)  #  I need some range in the past
    end_date = dt.date(year=2021,month=11,day=1) 
    max_days = end_date-start_date
        
    slider = cols1.slider('Select a date to view clustering present for that day', min_value=start_date, value=end_date ,max_value=end_date, format=format)
    ## check
   
    st.table(pd.DataFrame([[ slider]],
            columns=['selected'],
                    index=['Date']))

    #st.write("Select a date to view clustering present for that day")