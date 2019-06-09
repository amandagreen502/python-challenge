# import os & cv file
import os
import csv
csvpath = os.path.join('budget_data.csv')

# read csv 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read header 
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
   

           

      


           