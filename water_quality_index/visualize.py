import pandas as pd
import numpy as np
import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

def get_locations():
    dfs = pd.read_csv('metadata.csv')
    s_no = dfs['GEMS Station Number']
    latitudes = dfs['Latitude']
    longitudes = dfs['Longitude']
    latitude_map, longitude_map = {}, {}
    for i in range(len(s_no)):
        latitude_map[s_no[i]] = latitudes[i]
        longitude_map[s_no[i]] = longitudes[i]
    return latitude_map, longitude_map


def get_river_stretch_plot(stations, wqi_vals):
    lat_map, long_map = get_locations()
    fig = plt.figure(figsize=(14, 14))
    ax = plt.axes(projection=ccrs.PlateCarree())
    for i in range(len(stations)):
        ax.scatter(long_map[stations[i]], lat_map[stations[i]], s = wqi_vals[i]*10, transform=ccrs.PlateCarree())
    ax.coastlines()
    plt.show()

dfs = pd.read_csv('metadata.csv')
s_no = dfs['GEMS Station Number']
wqi = np.random.uniform(low = 10, high = 70, size = (len(s_no),))
get_river_stretch_plot(s_no, wqi)