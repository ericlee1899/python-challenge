#import modules
import os
import csv

#create variables for calculations
totalmonths = 0
nettotal = 0
netaverage = 0
dataset = ['Date', 'Profit/Losses']

#looping through dataset
for data in dataset:

    #setting up CSV
    with open("C:\\Users\\ericl/Desktop/Course/python-challenge/PyBank/budget_data.csv") as csvFile:
        #seperate by comma
        csvReader = csv.reader(csvFile, delimiter=',')
        #skip header
        next(csvReader, None)
    
        #setting initial data
        line = next(csvReader,None)
        totalmonths = 1
        netaverage = 0
        minmonth = line[0]
        maxmonth = line[0]
        net = float(line[1])
        nettotal = float(line[1])
        minnet = net
        maxnet = net
        prevnet = net

        #removing decimals
        nettotal = int(nettotal)
        avgnetchange = int(avgnetchange)
        maxnet = int(maxnet)
        minnet = int(minnet)

        #reading one line at a time
        for line in csvReader:
            #declaring equations
            net = float(line[1])
            totalmonths = totalmonths + 1
            nettotal = nettotal + net
            netchange = net - prevnet
            netaverage = netaverage + netchange
            average_revenue = nettotal/totalmonths
            avgnetchange = netaverage/(totalmonths-1)

            #finding max/min changes
            if netchange > maxnet:
                maxmonth = line[0]
                maxnet = netchange

            if netchange < minnet:
                minmonth = line[0]
                minnet = netchange

            prevnet = net

        #print analysis in terminal
        print(f"Financial Analysis:")
        print("-------------------------------------------------------")
        print(f"Total Months: {totalmonths}")
        print(f"Total Revenue: {nettotal} ")
        print(f"Average Revenue Change: {avgnetchange}")
        print(f"Greatest Increase in Revenue: {maxmonth} ({maxnet})")
        print(f"Greatest Decrease in Revenue: {minmonth} ({minnet})")
