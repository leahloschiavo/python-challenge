# import required libraries
import csv
from pathlib import Path

#load file for part 1
load_file = Path("Resources/budget_data.csv")

#Variables to access row
total_months = 0
profit_loss_total = 0
profit_loss_change = []
month_list = [] 


#Accessing CSV
with open(load_file) as FinancialData:
    reader = csv.reader(FinancialData)
    heading = next(reader)
    next_line = next(reader)
    profit_initial = int(next_line[1])  
    total_months += 1
    profit_loss_total += profit_initial 
    month_list.append(next_line[0])  
    for row in reader:
        print(row) 
        total_months += 1
    
    # get the profit/loss value from the row
        profit_loss = int(row[1])
        profit_total = int(row[1])
        # get average of changes in profit_loss
        profit_loss_change.append(profit_loss - profit_initial)
    
        month_list.append(row[0])
        profit_initial = profit_loss 
       

        # add the profit/loss value to net profit/loss
        profit_loss_total += profit_loss

        #for  csv.reader:
            #print(total_months + [1])
              
    # get max/min of profit loss list
    max_increase_value = max(profit_loss_change)
    max_decrease_value = min(profit_loss_change)

    #months of increase/decrease 

    max_increase_month = profit_loss_change.index(max_increase_value) +1    
    max_decrease_month = profit_loss_change.index(max_decrease_value) +1  
 
    average_change = profit_loss_change.index(max_increase_value) + 1

    #average of profit/losses over time

    
    

print(total_months)
print(profit_loss_total)
print(month_list[max_increase_month])
print(month_list[max_decrease_month])
print(sum(profit_loss_change)/len(profit_loss_change))


















            


    
      
        



  
    
    

 




    

