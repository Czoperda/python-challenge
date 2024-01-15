import os
import csv

#Initialize Variables
totalmonths = 0
total_pl = 0
previous_period = 0
profit_loss_changes = []
profit_loss_change = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

#Change directory to C:\Users\czope\OneDrive\Desktop\Bootcamp\Module3\Starter_Code>
csv_file_path = 'PyBank\Resources\\budget_data.csv'

#Creating output text file path
output_file_path = 'PyBank\\analysis\\analysis.txt'
with open(output_file_path, "w") as output_file:

    with open(csv_file_path, 'r', encoding='UTF-8') as csvfile:
        # Create a CSV reader object
        csvreader = csv.reader(csvfile)

        #Skip the header row
        next(csvreader)

        # Iterate over each row in the CSV file
        for row in csvreader:
            # Each row is a list containing values from the CSV columns

            #TOTAL MONTH CALCULATION-------------------------------
            totalmonths = totalmonths + 1

            #NET PROFIT/LOSSES TOTAL AMOUNT CALCULATION------------
            profit_loss = int(row[1])
            total_pl = total_pl + profit_loss

            #AVERAGE CHANGE CALCULATION-----------------------------
            #If the total months are greater than one (Do not want to start at zero):
            if totalmonths > 1:
                #Calculate the profit/loss change from current period and past period
                profit_loss_change = profit_loss - previous_period
                #Append the profit/loss change to the profit loss list
                profit_loss_changes.append(profit_loss_change)

            #Assign previous period to the current profit loss for next calculation
            previous_period = profit_loss

            #If total months greater than 1 calculate solution
            if totalmonths > 1:
                #Calculate the average using the sum of profit/loss list and dividng total months
                average_change = sum(profit_loss_changes) / (totalmonths - 1)
            else:
                #Set to average change to zero (Can not divide by zero)
                average_change = 0
            
            average_change = round(average_change, 2)

            #GREATEST INCREASE IN PROFITS CALCULATION-------------------
            #Set the date to the first column
            date = row[0]
            #If the profit/loss change is greater than the current greatest increase then save row
            if profit_loss_change > greatest_increase:
                greatest_increase = profit_loss_change
                greatest_increase_date = date

            #GREATEST DECREASE IN PROFITS CALCULATION-------------------
            #Set the date to the first column
            date = row[0]
            #If the profit/loss change is less than the current greatest decrease then save row
            if profit_loss_change < greatest_decrease:
                greatest_decrease = profit_loss_change
                greatest_decrease_date = date

        #Printing results
        print("Financial Analysis")
        print("--------------------------------")
        print(f"Total Months: {totalmonths}")
        print(f"Total: ${total_pl}")
        print(f"Average Change: ${average_change}")
        print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
        print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

        #Printing results to analysis text file
        output_file.write("Financial Analysis\n")
        output_file.write("--------------------------------\n")
        output_file.write(f"Total Months: {totalmonths}\n")
        output_file.write(f"Total: ${total_pl}\n")
        output_file.write(f"Average Change: ${average_change}\n")
        output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
        output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")