import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('avgIQpercountry.csv')
df['Population - 2023'] = df['Population - 2023'].str.replace(',', '', regex=False).astype(float)
#plot 1
#fig = px.scatter_geo(df, locations='Country', locationmode='country names', hover_name='Country',
#                     size='Average IQ', color='Continent', projection='natural earth',
#                     title='Average IQ by Country', size_max=20, template='plotly_dark')
#fig.show()

#plot 2
fig = px.choropleth(df, locations='Country', locationmode='country names', color='Average IQ', hover_name='Country', hover_data=['Literacy Rate', 'Nobel Prizes'], color_continuous_scale='agsunset', projection='natural earth', title='Average IQ by Country')
fig.show()