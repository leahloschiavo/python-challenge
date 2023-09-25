#import required libries
import csv
import os
from pathlib import Path

#load file for part 2
file_to_load = os.path.join("Resources","election_data.csv")

#variables to access row
total_votes = 0
votes_per_candidate = []
percent_per_candidate = []
politicians = ["Charles Casper Stockham", "Diane DeGette"
 "Raymon Anthony Doane"]

candidates = list(zip(politicians, total votes, 
percent per candidate))


with open(file_to_load) as ElectionResults:
    reader = csv.reader(ElectionResults)
    header = next(reader)
    next_line = next(reader)
    candidate_name.append(row[2])
    for row in reader:
         print(row)

         # Add votes in list
         total_votes += 1 

         # List each candidate individually 



         # Add individual candidate votes


         #Determine percentage of votes each winner

         # Determine name of winner 
         






print(total_votes)


    

