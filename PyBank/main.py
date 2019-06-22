import os
import csv

#Define the variables
original_data="Original Data"
output_data="Output_Data"
csv_file="PyBank.csv"
new_file="financial_report.txt"

# Define path of csv file
path_csv_file=os.path.join(original_data,csv_file)

#Define new output file
new_file ="Output Data/fiancial_results.txt"


#Define the variable for what we will look for
total_months = 0
total_profit = 0
prev_profit = 0
month_of_change = []
profit_change_list = []
biggest_decr = ['', 99999999999]
biggest_incr = ['', 0]

with open(path_csv_file,newline="") as csvfile:  
    reader = csv.DictReader(csvfile)
    for row in reader:
        #The total number of months included in the dataset
        total_months += 1
        #The net total amount of "Profit/Losses" over the entire period
        total_profit += int(row['Profit/Losses'])
        
        #The average of the changes in "Profit/Losses" over the entire period
        prof_change = int(row["Profit/Losses"])- prev_profit
        prev_profit = int(row["Profit/Losses"])
        profit_change_list = profit_change_list + [prof_change]
        month_of_change = month_of_change + [row["Date"]]
        
        #The greatest increase in profits (date and amount) over the entire period
        if prof_change>biggest_incr[1]:
            biggest_incr[1]= prof_change
            biggest_incr[0] = row['Date']
            
        #The greatest decrease in losses (date and amount) over the entire period
        if prof_change<biggest_decr[1]:
            biggest_decr[1]= prof_change
            biggest_decr[0] = row['Date']


#print(prof_change_list)
prof_avg = sum(profit_change_list)/len(profit_change_list)


print('Average Change in profit: $ ' + str(prof_avg))
print("Total Months: " + str(total_months))
print("Total profit: $ " + str(total_profit))
print(biggest_incr)
print(biggest_decr)


with open(new_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total: $%d\n" % total_profit)
    file.write("Average Change $%d\n" % prof_avg)
    file.write("Greatest Increase in Profits: %s ($%s)\n" % (biggest_incr[0], biggest_incr[1]))
    file.write("Greatest Decrease in Profits: %s ($%s)\n" % (biggest_decr[0], biggest_decr[1]))
    
    