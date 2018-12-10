#import modules 

import csv
import os
from collections import OrderedDict
from operator import itemgetter

#import csv file 

election_data = os.path.join("election_data.csv")
output=  "election_analyst.txt"

#define variables and lists

votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}

#open and read csv file 

with open(election_data) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]       
        
#create table using candidates

        if row["Candidate"] not in candidate_options:
            
            candidate_options.append(row["Candidate"])
            candidate_votes[row["Candidate"]] = 1
            
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1
            
#print results             
    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")
    
#statistics calculations 

    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")

#export to text file

with open(file_to_output, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))