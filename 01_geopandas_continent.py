#!/usr/bin/env python3

# Python 3.9.5

# 01_geopandas_continent.py

# Dependencies
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import os

path = ".../output"
os.chdir(path)

# Load low resolution world map (type: geopandas.geodataframe.GeoDataFrame)
# _________________________________________________________________________
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
world.head()

# Select all countries of e.g. North America:
north_america = world[world["continent"] == "North America"]

# Initialize figure, plot and save the data:
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot()

north_america.plot(
    ax=ax,
    cmap="Greens",
    edgecolor="black",
    alpha=0.5
)

ax.set_xticks([])
ax.set_yticks([])

plt.title("Continent and countries of North America")
plt.savefig("01_continent.png", dpi=300)
