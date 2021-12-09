import pandas as pd
import geopandas as gpd



#read in data and display basics
def display (input):
    df = input
    # Basic info
    print("Shape: /n", df.shape) 
    print('Total unique states:',len(df.STUSPS.unique()))
    print('Date span:',df.date.min(),df.date.max())
    print(df.head(5))
    print(df.tail(5))
    # column info
    print(df.info())
    ## describe the data , min, max, std dev, count,  50, 70 %
    print(df. describe())
    return df



## Find Rows containing duplicate data, or null data
def null_dupe(df):
    duplicate_rows_df = df[df.duplicated()]
    print('number of duplicate rows:' , duplicate_rows_df.shape)
    print('duplicates sums by column:\n', duplicate_rows_df.sum())
    #affter reviewin data, nulls can safely be set to zero
    df.fillna(0, inplace=True)
    print('is there null data: \n', df.isnull().sum())
    return df

def get_indexes(x):
    # identifies indexes where no data points exist yet and we will want to fill with a value other than null
    index_fill_1 = [i for i in range(x.index[0], x.dropna().index[0])]
    # identifies indexes where there is data however some missing points exist and we will want to apply interpolation
    index_interpolate = [i for i in range(x.dropna().index[0], x.index[-1])]
    return index_fill_1, index_interpolate

def update_series(x):
    
    # if there are all nulls in series replace with 1 - this is needed for legends to be visible in Plotly animations
    if len(x.dropna()) == 0:
        x = x.fillna(1)
        return x
    # otherwise apply either the null logic as above or interpolate genuine missing values
    else:
        index_fill_1, index_interpolate = get_indexes(x)
        x_fill_1 = x[x.index.isin(index_fill_1)]
        x_interpolate = x[x.index.isin(index_interpolate)]
        x_fill_1 = x_fill_1.fillna(1)
        x_interpolate = x_interpolate.interpolate()
        return pd.concat([x_fill_1, x_interpolate])

transform_cols = ['date','state','Confirmed','Deaths','Population']


if __name__ == "__main__":
    #df = pd.read_csv('C:\\Users\\Rachel\\Google Drive\\StreaLitApps\\streamlit-geospatial\\data\\us_covid_data_byState_over_Time.csv')      
    df =  pd.read_csv('C:\\Users\Rachel\\Google Drive\\StreaLitApps\\streamlit-geospatial\\data\\us_covid_data_byState_over_Time.csv')
    display(df)
    output=null_dupe(df)
    output.to_csv("C:\\Users\\Rachel\\Google Drive\\StreaLitApps\\streamlit-geospatial\\data\\us_covid_data.csv")
