# import os & cv file
import numpy as nb
import os
import csv
csvpath = os.path.join('budget_data.csv')

# Define Variables
total_months = 0
tot_revenue = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
biggest_decr = 0

# read csv 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read header 
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:

 #Total Number of Months Calculation
        total_months += 1
#Profit/Losses Total Revenue Calculation
        tot_revenue += int(row['Profit/Losses']) 

#Calulate average change 
prev_change = int(row["Profit/Losses"]) - prev_revenue
prev_revenue = int(row["Profit/Losses"])
revenue_change_list = revenue_change_list + [rev_change]
month_of_change = month_of_change + [row["Date"]]


# The greatest decrease in losses (date and amount) over the entire period

biggest_decr = np.min(int(row['Profit/Losses'])) 

#The greatest increase in profits (date and amount) over the entire period

biggest_decr = np.max(int(row['Profit/Losses']))
      



file_output = "results.txt"