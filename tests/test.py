import pandas as pd
import numpy as np
import geopandas as gpd





df = pd.read_csv('https://raw.githubusercontent.com/rmbeard/data/main/us_covid_data.csv')
#df1= df['date'] == '1/22/2020'
#df = df[df1]
print(df.head())
df2 = gpd.read_file("https://github.com/giswqs/streamlit-geospatial/raw/master/data/us_states.geojson")
#df3 = pd.merge(df, df2, how='left', left_on='state', right_on='STUSPS')
df3 = df2.merge(df, on='STUSPS')
df4=df3[['STUSPS','date','new_case','conf_cases','prob_cases', 'tot_death','geometry']]
print(df4.head())
df4.to_csv("C:\\Users\\Rachel\\Google Drive\\StreaLitApps\\streamlit-geospatial\\data\\merge.csv")
