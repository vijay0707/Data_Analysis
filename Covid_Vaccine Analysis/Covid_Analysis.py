

# importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




#Importing the dataset

df = pd.read_csv('.../Covid_Vaccine Analysis/country_vaccinations.csv')
df.head()




# Statistical Info
df.describe()





# Count of Countries
df.country.value_counts()





pd.to_datetime(df.date)





# Vaccine counts:
df.vaccines.value_counts()




# Create a new Dataframe by only selecting the vaccine and the country columns to find which country is taken by which country

data = df[['vaccines', 'country']]
data.head(10)
# data[data['country']=='India']


# ### let’s see how many countries are taking each of the vaccines mentioned in this data:




dict_ = {}
for i in df.vaccines.unique():
    dict_[i]=[df["country"][j] for j in df[df["vaccines"]==i].index]
    
vaccines = {}
for key, value in dict_.items():
      vaccines[key] = set(value)
for i, j in vaccines.items():
      print(f"{i}:>>{j}")


# ### Visualizing this data to look at what combination of vaccines every county is using:



# using Plotly
import plotly.express as px
import plotly.offline as py




vaccine_map = px.choropleth(data, locations = 'country', color = 'vaccines')
vaccine_map.update_layout(height=300, margin={"r":0, "t":0, "l":0, "b":0})
vaccine_map.show()







