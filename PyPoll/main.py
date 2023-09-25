#import required libries
import csv
import os
from pathlib import Path

#load file for part 2
file_to_load = os.path.join("Resources","election_data.csv")

#variables to access row
total_votes = 0
votes_diana = 0
votes_charles = 0
votes_raymon = 0 
most_votes = winner
candidate_name = "Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane" 


with open(file_to_load) as ElectionResults:
    reader = csv.reader(ElectionResults)
    header = next(reader)
    total_votes += 1 
    

    for row in reader:
         print(row)
         # Add votes in list
         total_votes += 1 
         
         
         # Add individual candidate votes
         if row[2] == "Charles Casper Stockham":
              votes_charles +=1
         elif row[2] == "Diana DeGette":
              votes_diana +=1
         else:
              votes_raymon+=1


              charles = votes_charles /total_votes*100
              diana = votes_diana /total_votes*100
              raymon = votes_raymon /total_votes*100
              most_votes = ("Winner", "Diana DeGette" )  




              
                   



  



     
print(total_votes)
print(candidate_name)
print(votes_charles)
print(votes_diana)
print(votes_raymon)
print(charles)
print(diana)
print(raymon)
print(most_votes)










    


         
        