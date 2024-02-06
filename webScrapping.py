from bs4 import BeautifulSoup

import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)

table = soup.find_all('table')[1]

soup.find('table')

soup.find('table', class_ = 'wikitable sortable')

world_titles = table.find_all('th')

world_titles

world_titles_table = [title.text.strip() for title in world_titles]
print(world_titles_table)

import pandas as pd

df = pd.DataFrame(columns = world_titles_table)

df

column_data = table.find_all('tr')

for row in column_data[1:]:
  row_data = row.find_all('td')
  individual_row_data = [data.text.strip() for data in row_data]
  # print(individual_row_data)

  length = len(df)
  df.loc[length] = individual_row_data



df

import pandas as pd
import matplotlib.pyplot as plt

# Sort the DataFrame by revenue growth in descending order and select the top 10 companies
df_top10 = df.sort_values(by='Revenue growth', ascending=False).head(10)

# Convert 'Revenue growth' column from percentage strings to floats
df_top10['Revenue growth'] = df_top10['Revenue growth'].str.rstrip('%').astype(float)

# Create a pie chart for top 10 companies
plt.figure(figsize=(8, 8))
plt.pie(df_top10['Revenue growth'], labels=df_top10['Name'], autopct='%1.1f%%', startangle=140)
plt.title('Top 10 Companies by Revenue Growth')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.tight_layout()
plt.show()


import pandas as pd
import numpy as np
from scipy.stats import zscore


def handle_missing_values(df):
    return df.dropna()

def handle_duplicates(df):
    return df.drop_duplicates()

def standardize_data_formats(df):

    df['Revenue growth'] = df['Revenue growth'].str.rstrip('%').astype(float)
    return df


def perform_data_transformation(df):
    
    df['Revenue growth'] = np.log1p(df['Revenue growth']) 
    return df

df_cleaned = handle_missing_values(df)
df_cleaned = handle_duplicates(df_cleaned)
df_cleaned = standardize_data_formats(df_cleaned)
df_cleaned = perform_data_transformation(df_cleaned)


print(df_cleaned)
