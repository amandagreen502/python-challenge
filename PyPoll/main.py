# import os & cv file
import os
import csv
import numpy

csvpath = os.path.join('election_data.csv')

#define variables
candidates = []
number_votes = 0
vote_count = []


# read csv 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
# Read header 
    csv_header = next(csvreader)
    
# Read each row of data after the header
    for row in csvreader:

# Adding to vote number
        number_votes = number_votes + 1
#which candidate the voter id voted for
        candidate = row[2]
#index number of votes each canditate had: 
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_count[candidate_index] = vote_count[candidate_index] + 1

#when no more votes leff to count per canditate add to else create new spot in list for candidate
        else:
            candidates.append(candidate)
            vote_count.append(1)
percent_list = []

#Create list of percentages for each candidate 
for count in range(len(candidates)):
    vote_percent = vote_count[count]/number_votes*100
    percent_list.append(vote_percent)
    
 #variables for summary   
    total_votes = sum(vote_count)
    winner = max(vote_count)

# test print
print(total_votes)
print(vote_count)
print(candidates)
print(winner)

for count in range(len(candidates)):
    print(f"{candidates[count]}: {percent_list[count]}% ({vote_count[count]})")