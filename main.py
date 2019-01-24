import pandas as pd
import numpy as np

shots = pd.read_csv('datasets/shots.csv')

# get the data dictionary for the dataset
ddurl = "http://peter-tanner.com/moneypuck/downloads/MoneyPuck_Shot_Data_Dictionary.csv"
dd = pd.read_csv(ddurl)

## only keep the first two columns, looks like a rogue entry in the csv
dd_clean = dd[['Variable', 'Definition']]

## quick peak to make sure its what we expected
dd_clean.head()

print(shots.head())
