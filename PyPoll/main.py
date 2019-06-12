# import os & cv file
import os
import csv

#define variables
candidates = []
num_votes = 0
vote_counts = []


# read csv 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read header 
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader: