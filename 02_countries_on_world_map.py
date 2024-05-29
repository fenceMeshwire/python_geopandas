#!/usr/bin/env python3

# Python 3.9.5

# 02_countries_on_world_map.py

# Dependencies
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import os

path = "/..."
os.chdir(path)

# Load the low resultion world map, check data:
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
world.head()

# Drop "Antarctica and "Seven Seas" from the DataFrame:
drop_idxs = world["continent"].isin(["Antarctica", "Seven seas (open ocean)"])
world = world.drop(world[drop_idxs].index)

def fix_missing_codes(world):
    # Replace country codes with the value of "-99": 
    world_fixed = world.copy()
    world_fixed.loc[world['name'] == 'France', 'iso_a3'] = 'FRA'
    world_fixed.loc[world['name'] == 'Norway', 'iso_a3'] = 'NOR'
    world_fixed.loc[world['name'] == 'Somaliland', 'iso_a3'] = 'SOM'
    world_fixed.loc[world['name'] == 'Kosovo', 'iso_a3'] = 'RKS'
    world_fixed.loc[world['name'] == 'N. Cyprus', 'iso_a3'] = 'CYP'
    return world_fixed

world_fixed = fix_missing_codes(world)
# Export CSV file to determine the country codes:
world_fixed_csv = world_fixed.drop(["pop_est", "gdp_md_est", "geometry"], axis=1)
world_fixed_csv.to_csv('world_df_fixed.csv')

total_iso_countries = world_fixed["iso_a3"].unique()
total_iso_countries.sort()
total_iso_countries = total_iso_countries.tolist()
iso_countries = ["ARG", "BRA", "COL", "ECU", "PER", "SUR", "VEN"]

colors = sns.color_palette(palette='Greens_d')

# Initialize a new figure:
fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot()

# Plot a boundary map of the world:
world.boundary.plot(
    ax=ax,
    edgecolor="black",
    linewidth=0.5
)

# Add the countries to the world map:
for iso_country in iso_countries:
    country = world_fixed[world_fixed["iso_a3"] == iso_country]
    country.plot(ax=ax, color=colors[5], alpha=0.5)

# Turn off axis ticks:
ax.set_xticks([])
ax.set_yticks([])

# Set final parameters:
plt.tight_layout()
plt.autoscale()
plt.axis('equal')
xmin, xmax, ymin, ymax = ax.axis()
plt.title("Countries on World Map")

plt.savefig("07_countries_on_world_map.png", dpi=300)
