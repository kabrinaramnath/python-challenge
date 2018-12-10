import os
import csv

#importing file
budget_data = os.path.join("budget_data.csv")

#open and read csv file 

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
#skip header row
    print(f"Header: {csv_header}")

#assign list/variables

    Profit = []
    Months = []

#read through each row of data

    for rows in csvreader:
        Profit.append(int(rows[1]))
        Months.append(rows[0])

#calculate changes in revenue
    revenue_change = []

    for x in range(1, len(P)):
        revenue_change.append((int(Profit[x]) - int(Profit[x-1])))
    
#calculate average change in revenue
    revenue_average = sum(revenue_change) / len(revenue_change)
    #calculate total length of months
    total_months = len(months)

#greatest increase in revenue
    greatest_increase = max(revenue_change)
#greatest decrease in revenue
    greatest_decrease = min(revenue_change)

#print the Results
    print("Financial Analysis")
    print(".........................")
    print("Total Number of Months: " + str(total_months))
    print("Total: " + "$" + str(sum(Profit)))
    print("Average change: " + "$" + str(revenue_average))
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))


#print to a text file

    file = open("output.txt","w")
    file.write("Financial Analysis" + "\n")
    file.write("..........................." + "\n")
    file.write("total months: " + str(total_months) + "\n")
    file.write("Total: " + "$" + str(sum(Profit)) + "\n")
    file.write("Average change: " + "$" + str(revenue_average) + "\n")
    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")
    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")
    file.close()