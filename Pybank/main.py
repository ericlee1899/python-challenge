#import modules
import os
import csv

#create variables for calculations
totalmonths = 0
nettotal = 0
netaverage = 0
dataset = ["data"]

#looping through dataset
for data in dataset:

    #setting up csv
    with open("C:\\Users\\ericl/Desktop/Course/python-challenge/PyBank/Resources/budget_data.csv") as csvFile:
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

            #removing decimals
            nettotal = int(nettotal)
            avgnetchange = int(avgnetchange)
            maxnet = int(maxnet)
            minnet = int(minnet)

        #print analysis in terminal
        print(f"Financial Analysis:")
        print("-------------------------------------------------------")
        print(f"Total Months: {totalmonths}")
        print(f"Total: ${nettotal} ")
        print(f"Average Change: ${avgnetchange}")
        print(f"Greatest Increase in Profits: {maxmonth} (${maxnet})")
        print(f"Greatest Decrease in Profits: {minmonth} (${minnet})")
        
        #print analysis in txt
        newtxtCSV = "analysis.txt"
        newtxt = open(newtxtCSV, mode = 'w')
        newtxt.write(f"Financial Analysis:\n")
        newtxt.write("-------------------------------------------------------\n")
        newtxt.write(f"Total Months: {totalmonths}\n")
        newtxt.write(f"Total: ${nettotal} \n")
        newtxt.write(f"Average Change: ${avgnetchange} \n")
        newtxt.write(f"Greatest Increase in Profits: {maxmonth} (${maxnet}) \n")
        newtxt.write(f"Greatest Decrease in Profits: {minmonth} (${minnet}) \n")
        newtxt.close()