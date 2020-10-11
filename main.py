#imports
import os
import csv
import pandas as pd

#declaring variables
totalmonths = 0
nettotal = 0
netaverage = 0

#declaring CSV
dataset = pd.read_csv("PyBank/budget_data.csv",delimiter=",")

#giving values to variables
totalmonths= len(dataset.index)
nettotal = dataset["Profit/Losses"].sum()


print(netaverage)