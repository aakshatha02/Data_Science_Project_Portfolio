import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
import numpy as np
from sklearn.cluster import KMeans

APP_TITLE = 'Crime Analysis in Chicago City'
APP_SUB_TITLE = 'Source: Chicago Data Portal'

def display_crime_facts(data, year, metric_title, types,days):
    data.drop_duplicates(inplace = True)
    if (types == 'All' and days != 'All'):
        data = data[(data['Year'] == year) & (data['day'] == days)]
    elif types == 'All' and days == 'All': 
        data = data[(data['Year'] == year)]
    elif types != 'All' and days == 'All':
        data = data[(data['Year'] == year) & (data['Primary Type'] == types)]
    else:
        data = data[(data['Year'] == year) & (data['Primary Type'] == types) & (data['day'] == days)]
    total = data.groupby(['Year'])['ID'].transform('count').iloc[0]
    st.metric(metric_title, '{:,}'.format(total))


def display_map(data,year,types,days):
    #data = data[(data['Year'] == year)] 
    if (types == 'All' and days != 'All'):
        data = data[(data['Year'] == year) & (data['day'] == days)]
    elif types == 'All' and days == 'All': 
        data = data[(data['Year'] == year)]
    elif types != 'All' and days == 'All':
        data = data[(data['Year'] == year) & (data['Primary Type'] == types)]
    else:
        data = data[(data['Year'] == year) & (data['Primary Type'] == types) & (data['day'] == days)]
    map = folium.Map(location=[41.8781, -87.6298], title= 'Number of Crimes reported by area', scrollWheelZoom= False,zoom_start=10,tiles='cartodb positron')
    choropleth = folium.Choropleth(
        geo_data = 'Data/Boundaries - Neighborhoods.geojson',
        df = data,
        columns=('pri_neigh', 'total_crime'),
        #key_on='properties.pri_neigh',
        key_on='feature.properties.pri_neigh',
        line_opacity = 0.7,
        fill_color='lightblue',
        highlight= True)
    choropleth.add_to(map)

    #data = data.set_index('pri_neigh')
    for feature in choropleth.geojson.data['features']:
        pri_neigh = feature['properties']['pri_neigh']
        if pri_neigh in data['pri_neigh'].unique():
            feature['properties']['total_crime'] = 'Total_Crimes :' + str('{: ,}'.format(data.loc[data['pri_neigh']== pri_neigh]['total_crime'].count())) 
        else:
            feature['properties']['total_crime'] = 'Total_Crimes : 0' 

    choropleth.geojson.add_child(
    #choropleth.geojson.add_child(new_tooltip)
        folium.features.GeoJsonTooltip([ 'pri_neigh','total_crime'], labels = False)
    )

    st_map = st_folium(map, width=700, height=450)

def display_time_filters(data):

    year_list = list(data['Year'].unique())
    year_list.sort()
    year = st.sidebar.selectbox('Year',year_list,)
    return year

def display_primary_type_filters(data):
    type_list = ['All'] + list(data['Primary Type'].unique())
    type_list.sort()
    types = st.sidebar.selectbox('Primary Type', type_list)
    return types

def display_days_filters(data):
    day_list = ['All'] + list(data['day'].unique())
    day_list.sort()
    days =st.sidebar.selectbox('day',day_list)
    return days

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
##Load Data
    df = pd.read_csv("Data/Crimes_-_2001_to_Present_modified.csv", delimiter= ',',low_memory=False)
    year = display_time_filters(df)
    data = df[(df['Year'] == year)]
    metric_title = f'No. of Crimes for the year {year}'

    types = display_primary_type_filters(data)
    days = display_days_filters(data)
    display_crime_facts(df, year, metric_title,types,days)
    
##Display Filters and Map
    display_map(data,year,types,days)
if __name__ == "__main__":
    main()


    
