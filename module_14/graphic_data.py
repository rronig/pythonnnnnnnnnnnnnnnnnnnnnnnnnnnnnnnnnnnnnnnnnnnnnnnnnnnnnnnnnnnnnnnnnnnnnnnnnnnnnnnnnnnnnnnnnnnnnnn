import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.distutils.system_info import numerix_info

#Bar Chart
# 1. Load the CSV
df = pd.read_csv('avgIQpercountry.csv')

#filtered_df = df[df["Average IQ"] >= 100]

#filtered_df = filtered_df.sort_values(by="Average IQ", ascending=False)

#print(filtered_df)

# 2. Create a bar chart
#plt.figure(figsize=(20, 8))  # Make the figure wider
#bar=plt.bar(filtered_df['Country'], filtered_df['Average IQ'], color='skyblue')
#plt.xlabel('Countries')
#plt.ylabel('Average IQ')
#plt.title('Average IQ per Country')
#plt.bar_label(bar, fmt='%.2f', fontsize=10, color='black', rotation=90)
#plt.grid(axis='y', linestyle='--', alpha=0.8)
#plt.xticks(rotation=90)  # Rotate labels vertically
#plt.tight_layout()       # Adjust layout to fit labels
#plt.show()

#line plot
#df=pd.read_csv('avgIQpercountry.csv')
#avg_iq_continent=df.groupby('Continent')['Average IQ'].mean()
#plt.figure(figsize=[8,8])
#avg_iq_continent.plot(kind='line', marker='o', color='skyblue')
#plt.title('Average IQ per continent')
#plt.xlabel('Continent')
#plt.ylabel('Average IQ')
#plt.grid(axis='both', linestyle='--', alpha=0.7)
#plt.show()
#scatter plot
#plt.figure(figsize=(10,6))
#plt.scatter(df['Country'], df['Mean years of schooling - 2021'], color='green', alpha=0.7)
#plt.title("Mean years of schooling per country")
#plt.xlabel("Country")
#plt.ylabel("Mean years of schooling")
#plt.grid(True, linestyle='--', alpha=0.7)
#plt.xticks(rotation=90)
#plt.show()

#pie chart
#nobel_prizes_total = df.groupby('Continent')['Nobel Prizes'].sum()
#colors = ['gold', 'limegreen', 'darkorange', 'cornflowerblue', 'lightskyblue', 'red', 'darkkhaki', 'purple']
#plt.figure(figsize=(10, 10))
#nobel_prizes_total.plot(kind='pie', colors=colors, autopct='%1.1f%%')
#plt.title("Nobel Prizes per Continent")
#plt.axis('equal')
#plt.show()
print(df.info())

#seaborn visualization
#plt.figure(figsize = (10,10))
#sns.histplot(df['Average IQ'])
#plt.title('Histogram of Average IQ')
#plt.xlabel('Average IQ')
#plt.ylabel('Frequency')
#plt.tight_layout()
#plt.show()
#df['Population - 2023'] = df['Population - 2023'].str.replace(',', '', regex=False).astype(float)
#print(df.info())
#numeric_iq_data_loc = df.select_dtypes(include=[np.number])
#sns.heatmap(numeric_iq_data_loc.corr(), annot=True, cmap="coolwarm", fmt=".2f")
#plt.show()

#box plot
plt.figure(figsize = (10,10))
sns.boxplot(data=df, x='Continent', y='Average IQ')
plt.title('Average IQ per Continent')
plt.xlabel('Continent')
plt.ylabel('Average IQ')
plt.show()