# importing Earthquake.py as eq
import Earthquake as eq
import sqlite3
import numpy as np
import pandas as pd

# connect to the output database and name it earthquakes.sqlite 
conn = sqlite3.connect('earthquakes.sqlite')

# forces database to return strings for TEXT attributes 
conn.text_factory = str 

# get the cursor for the connection 
cur = conn.cursor()

# run select query on database to get data for statistics
cur.execute('''SELECT magnitude, time, depth, place, title, felt, region 
           FROM earthquakes''')

# create an empty list to hold objects
eq_obj_list = []

# for loop to iterate through earthquake db and store into empty list
for quake in cur:
    eq_obj_list.append(eq.Earthquake(quake[0],quake[1],quake[2],quake[3],quake[4],quake[5],quake[6]))

# put the list of objs into a dataframe
df = pd.DataFrame([x.eq_dict() for x in eq_obj_list])

# printing first 5 earthquakes using .head()
print('First 5 Earthquakes in Dataset:')
print(df.head())

# basic statistics
print('\nSummary of Earthquake Data:')
print(df.describe())

# top two regions by earthquake count
print('\nTop 2 Regions by Earthquake Count:')
print(df['Region'].value_counts().head(2))

# filter for California region
cafilter = df[df['Region'] == 'California']

# statistics for the California region
print('\nStatistics for California Region:')
print(cafilter.describe())

# filter for Alaska region
akfilter = df[df['Region'] == 'Alaska']

# statistics for the Alaska region
print('\nStatistics for Alaska Region:')
print(akfilter.describe())

# filter for felt > 0
f_filter = df[df['Felt'] > 0]

# locations for felt > 0
print('\nEarthquakes Where Felt > 0:')
print(f_filter.sort_values('Felt', ascending=False))

# statistics for felt > 0 
print('\nStatistics for Earthquakes Where Felt > 0:')
print(f_filter.describe())

# filter for depth < 50
d_filter = df[df['Depth'] < 50]

# locations for depth < 50, too many locations so printing first 10
print('\nFirst 10 Earthquakes Where Depth < 50:')
print(d_filter.sort_values('Depth', ascending=False).head(10))

# statistics for depth < 50 
print('\nStatistics for Earthquakes Where Depth < 50:')
print(d_filter.describe())