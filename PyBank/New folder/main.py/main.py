# import required libraries
import csv
from pathlib import Path

#load file for part 1
load_file = Path("../Resources/budget_data.csv")

#Accessing CSV
with open(load_file) as FinancialData:
    reader = csv.reader(FinancialData)
    heading = next(reader)
    print(reader)

    #Financial Parameter Variables
    