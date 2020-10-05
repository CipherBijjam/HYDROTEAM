import pandas as pd
import numpy as np
import cartopy
import cartopy.crs as ccrs
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def get_viz():
    dfs = pd.read_csv('metadata.csv')
    s_no = dfs['GEMS Station Number']
    latitudes = dfs['Latitude']
    longitudes = dfs['Longitude']

    dfs2 = pd.read_csv('input.csv')
    wqi_array = []
    for i in range(len(s_no)):
        stn = s_no[i]
        dfs3 = dfs2.loc[dfs2['Station'] == stn]
        stn_wqi = np.mean(dfs3['WQI'].to_numpy())
        wqi_array.append(stn_wqi)

    print(wqi_array)
    wqi_array = np.array(wqi_array)

    m = np.mean(wqi_array)
    std = np.std(wqi_array)
    wqi_array = wqi_array - m
    wqi_array = (wqi_array/std)*100

    fig, ax = plt.subplots()
    ind_img = mpimg.imread('india-rivers-map.jpg')
    plt.imshow(ind_img,extent=[68.7, 96.25, 7.4, 37.6], alpha=0.75)
    labels = []
    colors = ['red', 'yellow', 'blue', 'purple', 'green']
    ct = [0,0,0,0,0]
    for val in wqi_array:
        if val >=0 and val <25:
            labels.append(0)
        elif val>=25 and val <50:
            labels.append(1)
        elif val>=50 and val <70:
            labels.append(2)
        elif val>=70 and val<90:
            labels.append(3)
        else:
            labels.append(4)
    # print(ct)

    scatter = ax.scatter(longitudes, latitudes, c=labels, cmap=matplotlib.colors.ListedColormap(colors))
    legend1 = ax.legend(*scatter.legend_elements(), loc="lower left")
    ax.add_artist(legend1)
    ax.set_title('In the scale, 0 denotes worst quality, 4 denotes excellent')
    plt.show()

get_viz()