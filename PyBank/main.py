# import os & cv file
import os
import csv
csvpath = os.path.join('budget_data.csv')

# Define Variables
total_months = 0
tot_revenue = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []


# read csv 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read header 
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:

 #Total Number of Months
        total_months += 1
#Profit/Losses Total Revenue Calculation
        tot_revenue += int(row['Profit/Losses'])  


      



file_output = "results.txt"