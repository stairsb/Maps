import pandas as pd
import folium
import geopandas
import numpy as np


#Dataset with list of countries and other associated variables
Rhiz_countries = pd.read_csv('Reduced_data.csv')
print(Rhiz_countries)


#geo data by country
Global_countries = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

#print(Global_countries)

#Check the contents of the natural earth low res dataset
#np.savetxt('out.txt', Global_countries, fmt='%s')

#merge datasets
Rhiz_countries = Global_countries.merge(Rhiz_countries, how="left", left_on=['name'], right_on=['Country'])
print(Rhiz_countries)

#for missing data
Rhiz_countries = Rhiz_countries.dropna()

print(Rhiz_countries)
# Create a map
my_map = folium.Map()
# Add the data
folium.Choropleth(
    geo_data=Rhiz_countries,
    name='choropleth',
    data=Rhiz_countries,
 #   columns=['Country', 'Ecology'],
    columns=['Country', 'Number_found'],
    key_on='feature.properties.Country',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Rhizopus microsporus strains collected in each country',
    zoom_control=False
).add_to(my_map)
my_map.save('Global_Rhizopus.html')


