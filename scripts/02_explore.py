#
# Case number overlaid on a Folium map
#

# prepare country specific data
# recycle from week 1

import pandas as pd
from pyhere import here
import folium

df_country_raw = pd.read_csv(here("src", "cases_country.csv"))

# Change all column names to lower case
df_country = df_country_raw.rename(columns = {
    "Country/Region": "country_region", 
    "ISO3": "country_code", 
    "Long_": "long"})
df_country.columns = df_country.columns.str.lower()
# df_country.columns

# convert last_update to timestamp
df_country["last_update"] = pd.to_datetime(df_country["last_update"], 
        infer_datetime_format = True)

# Adjust the column order
df_country = df_country[["uid", "country_code", "country_region", "lat", "long", 
    "last_update", "confirmed", "deaths", "recovered", "active", 
    "incident_rate", "mortality_rate", 
    "people_tested", "people_hospitalized"]]


# Prepare for map

# df_country["active"].isna().sum()
# df_country["long"].isna().sum()
# df_country["lat"].isna().sum()
# There are two countries without location data. 

# missing = df_country[df_country["lat"].isna()]
# missing
# Two cruise ships do not have lat and long

# Only plot entries with a physical location
df_country_noship = df_country[~df_country["lat"].isna()]

# Create an empty map
m = folium.Map(tiles = 'Stamen Terrain', min_zoom=1.5)

# Add country data
for i in range(0, len(df_country_noship)):
    folium.Circle(
            location=[df_country_noship.iloc[i]['lat'], 
                df_country_noship.iloc[i]['long']], 
            popup=df_country_noship.iloc[i]['country_region'], 
            radius=df_country_noship.iloc[i]['active'], 
            color='crimson', 
            # fill=True, 
            # fill_color='crimson'
            ).add_to(m)

m.save(outfile = here("output", "country_active.html").__str__())
# without `.__str__()` part, would get a 'PosixPath' error

# In "country_active.html", 
# the number of active cases per country is represented by a circle, 
# with a corresponding size. 
# This plot is potentially misleading, 
# because countries with a larger population 
# may have a larger absolute number of active cases. 
# Next, will plot incident_rate. 

