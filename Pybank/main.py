#imports
import os
import csv
import pandas as pd

#declaring variables
totalmonths = 0
nettotal = 0
netaverage = 0

#declaring CSV
dataset = pd.read_csv("PyBank/budget_data.csv")
print(dataset.head())