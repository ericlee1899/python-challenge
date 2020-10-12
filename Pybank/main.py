import os
import csv

#create variables for calculations
totalmonths = 0
nettotal = 0
netaverage = 0
budget_data = ['Date', 'Profit/Losses']

# Loop through files
for files in budget_data:

    # Open current CSV
    with open("C:\\Users\\ericl/Desktop/Course/python-challenge/PyBank/budget_data.csv") as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        # Skip headers
        next(csvReader, None)
