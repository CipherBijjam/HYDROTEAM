import pandas as pd
import numpy as np
import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def get_viz():
    dfs = pd.read_csv('metadata.csv')
    s_no = dfs['GEMS Station Number']
    latitudes = dfs['Latitude']
    longitudes = dfs['Longitude']
    dfs2 = pd.read_csv('input.csv')
    fig, ax = plt.subplots()
    ind_img = mpimg.imread('india-rivers-map.jpg')
    plt.imshow(ind_img,extent=[68.7, 96.25, 7.4, 37.6], alpha=0.75)
    labels = ["C1", "C2", "C3", "C4", "C3", "C2", "C1", "C2", "C3", "C4", "C3", "C2", "C1", "C2", "C3", "C4", "C3", "C2",
             "C1", "C2", "C3", "C4", "C3", "C2", "C1", "C2", "C3", "C4", "C3", "C2", "C1", "C2", "C3", "C4", "C3", "C2",
             "C1", "C2", "C3", "C4", "C3", "C2", "C1", "C2", "C3", "C4", "C3", "C2", "C1", "C2", "C3", "C4", "C3", "C2",
             "C1", "C2", "C3", "C4", "C3", "C2", "C1", "C2", "C3", "C4", "C3", "C2", "C1", "C2", "C3", "C4", "C3", "C2"]
    scatter = ax.scatter(longitudes, latitudes, c=labels)
    legend1 = ax.legend(*scatter.legend_elements(),
                loc="lower left", title="Classes")
    ax.add_artist(legend1)
    plt.show()

get_viz()