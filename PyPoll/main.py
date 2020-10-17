#import modules
import os
import csv

#create variables for calculations
candidates = []
totalvotes = 0
votecounter = []
dataset = ["data"]

#looping through dataset
for data in dataset:

    #setting up csv
    with open("C:\\Users\\ericl/Desktop/Course/python-challenge/PyPoll/Resources/election_data.csv") as csvFile:
        #seperate by comma
        csvReader = csv.reader(csvFile, delimiter=',')
        line = next(csvReader,None)

        #main loop
        for line in csvReader:
            #declaring equations
            totalvotes = totalvotes + 1
            candidate = line[2]

            #candidate ticker
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                votecounter[candidate_index] = votecounter[candidate_index] + 1
            else:
                candidates.append(candidate)
                votecounter.append(1)

    #create more variables for calculations
    percentages = []
    maxvote = votecounter[0]
    winnercount = 0

    #candidate calculation
    for count in range(len(candidates)):
        votepercent = votecounter[count]/totalvotes*100
        percentages.append(votepercent)
        if votecounter[count] > maxvote:
            maxvote = votecounter[count]
            print(maxvote)
            winnercount = count
    winner = candidates[winnercount]

    #rounding decimals
    percentages = [round(i,2) for i in percentages]

    #print analysis in terminal
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {totalvotes}")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({votecounter[count]})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")

    #print analysis in txt
    newtxtCSV = "analysis.txt"
    newtxt = open(newtxtCSV, mode = 'w')
    newtxt.write("Election Results\n")
    newtxt.write("--------------------------\n")
    newtxt.write(f"Total Votes: {totalvotes}\n")
    for count in range(len(candidates)):
        newtxt.write(f"{candidates[count]}: {percentages[count]}% ({votecounter[count]})\n")
    newtxt.write("---------------------------\n")
    newtxt.write(f"Winner: {winner}\n")
    newtxt.write("---------------------------\n")
    newtxt.close()