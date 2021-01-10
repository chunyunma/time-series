import pandas as pd
from pyhere import here

# Import six data sets
df_globalconf_raw = pd.read_csv(here("src", "time_series_covid19_confirmed_global.csv"))
df_globaldeat_raw = pd.read_csv(here("src", "time_series_covid19_deaths_global.csv"))
df_globalreco_raw = pd.read_csv(here("src", "time_series_covid19_recovered_global.csv"))
df_usconf_raw = pd.read_csv(here("src", "time_series_covid19_confirmed_US.csv"))
df_usdeat_raw = pd.read_csv(here("src", "time_series_covid19_deaths_US.csv"))
df_country_raw = pd.read_csv(here("src", "cases_country.csv"))


# 
# global confirmed cases
# 

# df_globalconf_raw.head(3)
# df_globalconf_raw.shape

# Change all column names to lower case
df_globalconf = df_globalconf_raw.rename(columns = {
    "Province/State": "province_state", 
    "Country/Region": "country_region", 
    "Lat": "lat", 
    "Long": "long"})

# wide to long
df_globalconfl = pd.melt(df_globalconf, 
    id_vars=["country_region", "province_state", "lat", "long"], 
    var_name="day", value_name="n_globalconf")

# Separate year, month, and date into three columns
df_globalconfl[["month", "date", "year"]] = df_globalconfl.day.str.split("/", expand=True)
# Drop the original day column
df_globalconfl = df_globalconfl.drop(columns="day")
# convert to int type
df_globalconfl[["year", "month", "date"]] = df_globalconfl[["year", "month", "date"]].apply(pd.to_numeric)
# Adjust the column order
df_globalconfl = df_globalconfl[["country_region", "province_state", "lat", "long", 
    "year", "month", "date", "n_globalconf"]]
print("# global_confirmed:\n", df_globalconfl.head(3))


# 
# Global death
# 

# df_globaldeat_raw.head(2)
# df_globaldeat_raw.shape

# Change all column names to lower case
df_globaldeat = df_globaldeat_raw.rename(columns = {
    "Province/State": "province_state", 
    "Country/Region": "country_region", 
    "Lat": "lat", 
    "Long": "long"})

# wide to long
df_globaldeatl = pd.melt(df_globaldeat, 
    id_vars=["country_region", "province_state", "lat", "long"], 
    var_name="day", value_name="n_globaldeat")

# Separate year, month, and date into three columns
df_globaldeatl[["month", "date", "year"]] = df_globaldeatl.day.str.split("/", expand=True)
# Drop the original day column
df_globaldeatl = df_globaldeatl.drop(columns="day")
# convert to int type
df_globaldeatl[["year", "month", "date"]] = df_globaldeatl[["year", "month", "date"]].apply(pd.to_numeric)
# Adjust the column order
df_globaldeatl = df_globaldeatl[["country_region", "province_state", "lat", "long", 
    "year", "month", "date", "n_globaldeat"]]
print("global_deaths:\n", df_globaldeatl.head(3))

# 
# Global recovered
# 

# df_globalreco_raw.head(2)
# df_globalreco_raw.shape

# Change all column names to lower case
df_globalreco = df_globalreco_raw.rename(columns = {
    "Province/State": "province_state", 
    "Country/Region": "country_region", 
    "Lat": "lat", 
    "Long": "long"})

# wide to long
df_globalrecol = pd.melt(df_globalreco, 
    id_vars=["country_region", "province_state", "lat", "long"], 
    var_name="day", value_name="n_globalreco")

# Separate year, month, and date into three columns
df_globalrecol[["month", "date", "year"]] = df_globalrecol.day.str.split("/", expand=True)
# Drop the original day column
df_globalrecol = df_globalrecol.drop(columns="day")
# convert to int type
df_globalrecol[["year", "month", "date"]] = df_globalrecol[["year", "month", "date"]].apply(pd.to_numeric)
# Adjust the column order
df_globalrecol = df_globalrecol[["country_region", "province_state", "lat", "long", 
    "year", "month", "date", "n_globalreco"]]
print("global_recovered:\n", df_globalrecol.head(3))

# 
# US confirmed cases
# 


# Rename columns with meaningful words, all lowercase
df_usconf = df_usconf_raw.rename(columns = {
    "UID": "uid", 
    "iso3": "country_code", 
    "FIPS": "county_code", 
    "Admin2": "county_name", 
    "Province_State": "province_state", 
    "Country_Region": "country_region", 
    "Lat": "lat", 
    "Long_": "long"
    })
# df_usconf.head(2)

# Drop columns deemed redundant
# df_usconf_raw.iso2 is just the first two letters of df_usconf.iso3
# df_usconf_raw.Combined_Key is just county + state + country
# df_usconf_raw.code3 unclear what it is used for; dropped for now
df_usconf = df_usconf.drop(columns=["iso2", "Combined_Key", "code3"], axis=1)

# wide to long
df_usconfl = pd.melt(df_usconf, 
    id_vars=["uid", "country_code", "country_region", 
        "province_state", "county_code", "county_name", 
        "lat", "long"], 
    var_name="day", value_name="n_case")

# Separate day into year, month and date
df_usconfl[["month", "date", "year"]] = df_usconfl.day.str.split("/", expand=True)
# Drop the original day column
df_usconfl = df_usconfl.drop(columns="day")
df_usconfl[["year", "month", "date"]] = df_usconfl[["year", "month", "date"]].apply(pd.to_numeric)
# Adjust column order
df_usconfl = df_usconfl[["uid", "country_code", "country_region", 
    "province_state", "county_code", "county_name", 
    "lat", "long", 
    "year", "month", "date", "n_case"]]
print("US_confirmed:\n", df_usconfl.head(3))



# 
# US death
# 

# df_usdeat_raw.head(2)
# df_usdeat_raw.shape


# Rename columns with meaningful words, all lowercase
df_usdeat = df_usdeat_raw.rename(columns = {
    "UID": "uid", 
    "iso3": "country_code", 
    "FIPS": "county_code", 
    "Admin2": "county_name", 
    "Province_State": "province_state", 
    "Country_Region": "country_region", 
    "Lat": "lat", 
    "Long_": "long", 
    "Population": "population"
    })
# df_usdeat.head(2)

# Drop columns deemed redundant
# df_usdeat_raw.iso2 is just the first two letters of df_usdeat.iso3
# df_usdeat_raw.Combined_Key is just county + state + country
# df_usdeat_raw.code3 unclear what it is used for; dropped for now
df_usdeat = df_usdeat.drop(columns=["iso2", "Combined_Key", "code3"], axis=1)
# df_usdeat[["county_code"]] = df_usdeat[["county_code"]].astype(int)

# wide to long
df_usdeatl = pd.melt(df_usdeat, 
    id_vars=["uid", "country_code", "country_region", 
        "province_state", "county_code", "county_name", 
        "lat", "long", "population"], 
    var_name="day", value_name="n_usdeat")

# Separate day into year, month and date
df_usdeatl[["month", "date", "year"]] = df_usdeatl.day.str.split("/", expand=True)
# Drop the original day column
df_usdeatl = df_usdeatl.drop(columns="day")
# Convert year month date to int type
df_usdeatl[["year", "month", "date"]] = df_usdeatl[["year", "month", "date"]].apply(pd.to_numeric)

# df_usdeatl.dtypes
# df_usdeatl.head(2)
df_usdeatl[["county_code"]] = df_usdeatl[["county_code"]].fillna(0).astype(int)


# Adjust column order
df_usdeatl = df_usdeatl[["uid", "country_code", "country_region", 
    "province_state", "county_code", "county_name", 
    "lat", "long", "population", 
    "year", "month", "date", "n_usdeat"]]
print("US_deaths:\n", df_usdeatl.head(3))


# 
# Country specific
# 

# df_country_raw.head(2)
# df_country_raw.shape


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
print("country_specific:\n", df_country.head(3))

#
# Descriptives
# 

# df_globalconfl["country_region"].nunique()
# 191
# df_globalconfl["country_region"].isna().sum()
# no missing data in country_region column

# convert country_region to categorical
df_globalconfl["country_region"] = df_globalconfl["country_region"].astype("category")
# <https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html>

# Countries that have data at province or state level
df_globalconfl_province = df_globalconfl[~df_globalconfl["province_state"].isna()]
# df_globalconfl_province.shape
# df_globalconfl_province["country_region"].unique()
# Australia, Canada, China, Denmark, France, Netherlands, UK

print("Global confirmed average by month:\n", 
        df_globalconfl[["year", "month", "n_globalconf"]].groupby(["year", "month"]).mean().astype(int))
print("Global confirmed median by month:\n", 
        df_globalconfl[["year", "month", "n_globalconf"]].groupby(["year", "month"]).median())
# mean > median, indicating positive skewness

df_globaldeatl[["year", "month", "n_globaldeat"]].groupby(["year", "month"]).mean().astype(int)
df_globaldeatl[["year", "month", "n_globaldeat"]].groupby(["year", "month"]).median()

print("# Similar descriptives can be applied to the US_confirmed, US_deaths, \n \
# and global_recovered. \n \
# There are many other summary statistics, \n \
# such as the incident_rate per country grouped by month, \n \
# mortality_rate per country grouped by month, etc. \n \
# Also need to use the population size in the UID_lookup_table.")
