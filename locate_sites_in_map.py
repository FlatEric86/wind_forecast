import numpy as np
import geopandas as gpd
import pandas as pd
import sys
import matplotlib.pyplot as plt
import matplotlib


### we load the relevant data of the weather observation sites from the 
### corresponding JSON file
df_site_def = pd.read_json('./OWM/site_sample.json').T


### we transform the DataFrame to a GeoPandas DataFrame
gdf_site_def = gpd.GeoDataFrame(
    df_site_def, geometry = gpd.points_from_xy(df_site_def.lon, df_site_def.lat))


### we set the city ID as index before we cast the ID's to integer
### we actually do not need them, but it is more handy to do so

# cast column data to integer
gdf_site_def.open_weather_city_id = gdf_site_def.open_weather_city_id.astype('int32')

# set a new column that is including the city/observation site names
gdf_site_def['city_names'] = gdf_site_def.index.values

# set the site ID's as index column
gdf_site_def.set_index('open_weather_city_id', inplace=True)




### we plot all the sites into a map


## we load the shape file of the border

# hatch across all contries
shp_path            = './SHP_files/border_data/hatch/CNTR_RG_10M_2020_4326.shp'
contries_hatch      = gpd.read_file(shp_path)

# coastlines
shp_path            = './SHP_files/border_data/coastlines/CNTR_BN_10M_2020_4326_COASTL.shp'
contries_coastlines = gpd.read_file(shp_path)

# inland borders
shp_path            = './SHP_files/border_data/inland_borders/CNTR_BN_10M_2020_4326_INLAND.shp'
inland_borders      = gpd.read_file(shp_path)




###############################################################################


size_fac = 8

fig, ax = plt.subplots(1, 2)




### first plot as overview

# plot the locations of the sites
gdf_site_def[~gdf_site_def.city_names.isin(['Zwenkau', 'Neu Fahrland', 'Rheinsberg'])].plot(
    ax = ax[0], markersize = 20, 
    color = 'red', 
    marker = 'o', 
    label = 'observation site\n of the weather stations',
    zorder=1
    )


# plot the locations of the 3 surf spots
gdf_site_def[gdf_site_def.city_names.isin(['Zwenkau', 'Neu Fahrland', 'Rheinsberg'])].plot(
    ax = ax[0], 
    markersize = 30, 
    color = 'blue', 
    marker = 'x', 
    label = 'surfe spots that to be investigated',
    zorder=1
    )

# plot the borders and hatch
contries_hatch.plot(color='green', alpha=0.3, ax=ax[0], zorder=0)
contries_coastlines.plot(color='k', alpha=0.8, linewidth=1, ax=ax[0])
inland_borders.plot(color='k', alpha=0.8, linewidth=1, ax=ax[0])



## we want only plot the map area of the scope of interesting
ax[0].set_xlim([min(gdf_site_def.lon.values)*1.2, max(gdf_site_def.lon.values)*1.2])
ax[0].set_ylim([min(gdf_site_def.lat.values)*0.8, max(gdf_site_def.lat.values)*1.2])



ax[0].set_title('Map the surfe spot as well the weatherstations')
ax[0].set_xlabel('Longitude')
ax[0].set_ylabel('Latitude')
ax[0].legend()



## zoom in



for x, y, label in zip(gdf_site_def.geometry.x, gdf_site_def.geometry.y, gdf_site_def.city_names):
    ax[1].annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points", size=6)



# plot the locations of the sites
gdf_site_def[~gdf_site_def.city_names.isin(['Zwenkau', 'Neu Fahrland', 'Rheinsberg'])].plot(
    ax = ax[1], markersize = 20, 
    color = 'red', 
    marker = 'o', 
    label = 'observation site\n of the weather stations',
    zorder= 2
    )


# plot the locations of the 3 surf spots
gdf_site_def[gdf_site_def.city_names.isin(['Zwenkau', 'Neu Fahrland', 'Rheinsberg'])].plot(
    ax = ax[1], 
    markersize = 30, 
    color = 'blue', 
    marker = 'x', 
    label = 'weather stations near by surfe spots to be investigated',
    zorder= 2
    )

# plot the borders and hatch
contries_hatch.plot(color='green', alpha=0.3, ax=ax[1], zorder=0)
contries_coastlines.plot(color='k', alpha=0.8, linewidth=1, ax=ax[1])
inland_borders.plot(color='k', alpha=0.8, linewidth=1, ax=ax[1])





## we want only plot the map area of the scope of interesting
ax[1].set_xlim([6.6, 19.5])
ax[1].set_ylim([48, 56])



ax[1].set_title('Map the surfe spot as well the weatherstations in a smaller scope')
ax[1].set_xlabel('Longitude')
ax[1].set_ylabel('Latitude')
ax[1].legend()


plt.show()