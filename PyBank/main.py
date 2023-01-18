# The first step is to import the OS module
# which enables paths to be created across multiple operating systems

import os

# Next, we need to import the module to read csv files

import csv

# Set the path for the csv file 

csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV with the CSV module

with open(csvpath) as csvfile:


    # specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header row
    next(csvreader, None)
    #Set the initial value start values
    total_months = 0
    total_money = 0
    most_money = 0
    least_money = 0
    
    #Create the list to hold values
    profit_list = []
    profit_list2 = []
    date_list = []
    
    #Loop through the csv file
    for row in csvreader:
    
        #Find the total number of months 
        total_months += 1
        #Find the total profit/loss
        total_money += int(row[1])
        #Separate this data into individual lists
        profit_list.append(int(row[1]))
        date_list.append(str(row[0]))
    
    #Loop through the Profit/Loss list
    for x in range(len(profit_list)):
    
        # Generate a second list for the monthly delta
        profit_list2.append(profit_list[x] - profit_list [x - 1])
        
    #In order to compare properly, set first item to 0
    profit_list2[0] = 0
    
    #Loop through the list for amount delta
    for row in profit_list2:
        
        #Find the greatest incrase and index
        if (int(row)) > most_money:
            most_money = (int(row))
            date_inc_index = profit_list2.index(row)
        #Find the greatest decrease and index
        elif (int(row)) < least_money:
            least_money = (int(row))
            date_dec_index = profit_list2.index(row)
    
    #Calculate the average change
    for y in range(len(profit_list2)):
        
        avg_change = sum(profit_list2)/(total_months - 1)
        
    #Use date indices to store the date values
    date_inc = date_list[date_inc_index]
    date_dec = date_list[date_dec_index]

#Print the Financial Analysis
output_analysis = (f"Financial Analysis\n-----------------\nTotal Months:{total_months}\nTotal: ${total_money}\nAverage Change: ${avg_change:.2f}\nGreatest Increase in Profits: {date_inc} (${most_money})\nGreatest Decrease in Profits: {date_dec} (${least_money})")
print(output_analysis)  

#Create a text file with the output
with open('analysis/analysis.txt', 'w') as output:
    output.write(output_analysis)
    
                    
        