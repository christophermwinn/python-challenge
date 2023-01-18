# The first step is to import the OS module
# which enables paths to be created across multiple operating systems
import os
# Next, we need to import the module to read csv files
import csv
# Set the path for the csv file 
csvpath = os.path.join("Resources", "election_data.csv")
# Open the CSV with the CSV module
with open(csvpath) as csvfile:
    
    # specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header row
    next(csvreader, None)
    
    # Get the total number of votes cast
    data = list(csvreader)
    rowcount = len(data)
    
    #Create a new list to capture all the candidates
    candlist = list()
    votecount = list()
    
    for i in range (0, rowcount):
        candidate = data[i][2]
        votecount.append(candidate)
        if candidate not in candlist:
            candlist.append(candidate)
    candcount = len(candlist)
    
    #Determine the total number of votes for each candidate
    # and calculate the percentages
    
    votes = list()
    percentage = list()
    for j in range (0,candcount):
        name = candlist[j]
        votes.append(votecount.count(name))
        vprct = votes[j]/rowcount
        percentage.append(vprct)
        
    #Determine the election winner (most votes)
    winner = votes.index(max(votes))
    
    #Print the Election Results as Output
    print(f"Election Results\n--------------------\nTotal Votes:  {rowcount:,}\n--------------------)")
    for k in range (0, candcount):
        print(f"{candlist[k]}:  {percentage[k]:.3%} ({votes[k]:,})")      
    print("--------------------")
    print(f"Winner:  {candlist[winner]}\n--------------------")
    
    #Save the election results to a .txt file
    print("Election Results", file=open("Analysis/results.txt", "a"))
    print("--------------------", file=open("Analysis/results.txt", "a"))
    for k in range (0, candcount):
        print(f"{candlist[k]}:  {percentage[k]:.3%} ({votes[k]:,})", file=open("Analysis/results.txt", "a"))
    print("--------------------", file=open("Analysis/results.txt", "a"))
    print(f"Winner:  {candlist[winner]}", file=open("Analysis/results.txt", "a"))
    print("--------------------", file=open("Analysis/results.txt", "a"))
    
    