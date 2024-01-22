# import json
# import country_converter as coco
# from datetime import datetime, timedelta
# import requests
# import pandas as pd
# import geopandas as gpd
# import matplotlib.pyplot as plt

# """
# Hello World
# """

# """
# .shp -> Spatial vector data -> points, lines and polygons
# .shx -> Index file -> AutoCAD shape index positions
# .dbf -> Mandatory shape file -> Stores attribute data and object IDs
# .prj -> Optional Projection file -> stores metadata associated with coordinates in shapefile
# .cpg -> Plain text file -> explains what encoding is used to create shapefile. In this case UTF-8


# """

# SHAPEFILE = 'D:\Downloads\\ne_10m_admin_0_countries\\ne_10m_admin_0_countries.shp'
# geo_df = gpd.read_file(SHAPEFILE)[['ADMIN', 'ADM0_A3', 'geometry']]
# geo_df.columns = ['country', 'country_code', 'geometry']
# # Drop row for 'Antarctica'. It takes a lot of space in the map and is not of much use
# geo_df = geo_df.drop(geo_df.loc[geo_df['country'] == 'Antarctica'].index)
# # Print the map
# geo_df.plot(figsize=(20, 20), edgecolor='white', linewidth=1, color='lightblue')

import folium as f

myshpfile = geopandas.read_file('ne_10m_admin_0_countries\\ne_10m_admin_0_countries.shp')
myshpfile.to_file('myJson.geojson', driver='GeoJSON')