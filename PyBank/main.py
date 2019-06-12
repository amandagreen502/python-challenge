# import os & cv file
import decimal
import os
import csv
csvpath = os.path.join('budget_data.csv')

# Define Variables
total_months = 0
tot_revenue = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []

revenue_list=[]


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
        tot_revenue += float(row[1]) 
        revenue_list.append(row[1])

#Calulate average change 
#rev_change = int(row[1]) - prev_revenue
#prev_change = int(row[1]) - prev_revenue
#prev_revenue = int(row[1])
#revenue_change_list = revenue_change_list + [rev_change]
#month_of_change = month_of_change + [row[0]]

rev_avg = float(round(tot_revenue/total_months,2))

# The greatest decrease in losses (date and amount) over the entire period
 
biggest_decr = min(revenue_list) 

#The greatest increase in profits (date and amount) over the entire period

biggest_incr = max(revenue_list)
      
#print(rev_change_list)
#rev_avg = sum(revenue_change_list)/len(revenue_change_list)


print('Average Change in Revenue: $ ' + str(rev_avg))
print("Total Months: " + str(total_months))
print("Total Revenue: $ " + str(tot_revenue))
print(biggest_incr)
print(biggest_decr)
