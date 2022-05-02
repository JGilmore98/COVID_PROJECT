import pandas as pd
import geopandas
import folium
import json
import streamlit
from folium.plugins import HeatMap
from streamlit_folium import folium_static

streamlit.title("NC COVID DATA")
nc_county_data = geopandas.read_file('NC_Counties.geojson')
nc_COVID_data = pd.read_csv("NC_Counties_COVID_Cases.csv")
nc_COVID_data = nc_COVID_data.astype({"County":'string'})

us_map = folium.Map(location=[36.075254969740975, -79.78813799573425], zoom_start=10)
NorthCarolinaMap = folium.Map([36.07370945953413, -79.79215873797281], zoom_start=10,tiles='OpenStreetMap')

nc = folium.Choropleth(geo_data=nc_county_data,
                  data=nc_COVID_data,
                  columns=['County','Total Cases'],
                  key_on='feature.properties.coty_name',
                  fill_color='YlGn',
                  fill_opacity=0.7,
                  line_opacity=0.2).add_to(us_map)


folium.GeoJsonTooltip(['coty_name']).add_to(nc.geojson)


folium_static(us_map)

COVID_DATASET = pd.read_csv("COUNTY_COVID_DATA/NC_County_COVID_CASES_180_DAYS.csv")
COVID_DATASET = COVID_DATASET.drop(axis=1, columns=['RowNumber'])
chosen_county = County_Name = streamlit.text_input("Enter County Name to return Covid Cases.")
county = COVID_DATASET['County']

if(streamlit.button('Search')):
    streamlit.dataframe(COVID_DATASET.loc[COVID_DATASET['County']==chosen_county])







