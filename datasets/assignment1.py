import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
#%matplotlib inline
from bs4 import BeautifulSoup
#scrape elements
COLUMNS = ['Rank', 'Player', 'MMR', 'Games']
dataframes = []
i = 1
url = "https://r6.tracker.network/leaderboards/pvp-season/pc/Mmr?page={}&region=-1&season=12"
while(i<10):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table") # Find the "table" tag in the page
    rows = table.find_all("tr") # Find all the "tr" tags in the table
    cy_data = []
    for row in rows:
        cells = row.find_all("td") #  Find all the "td" tags in each row
        cells = cells[0:4] # Select the correct columns
        cy_data.append([cell.text for cell in cells]) # For each "td" tag, get the text inside it

    dataframes.append(pd.DataFrame(cy_data, columns=COLUMNS).drop(0, axis=0))
    i= i+1;
    print(i)
data = pd.concat(dataframes)

print(data.head())