# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("python-challenge","PyBank", "Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("python-challenge","PyBank","analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data

net_change = 0
net_list = []
Gain = ["",0]
Loss = ["",9999999999]
time_passed = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list

    first_row = next(reader)
    total_months = (total_months + 1)
    

    # Track the total and net change

    total_net = (total_net + int(first_row[1]))
    saved_net = int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total
        profloss = int(row[1])
        date = row[0]
        
        total_months = (total_months + 1)
        total_net = (total_net + profloss)

        # Track the net change

        net_change = profloss - saved_net
        saved_net = profloss

        net_list = net_list + [net_change]
        time_passed = time_passed + [date]


        # Calculate the greatest increase in profits (month and amount)

        if net_change > Gain[1]:
            Gain[0] = date
            Gain[1] = net_change

        # Calculate the greatest decrease in losses (month and amount)

        if net_change < Loss[1]:
            Loss[0] = date
            Loss[1] = net_change



# Calculate the average net change across the months

average = sum(net_list)/len(net_list)

# Format averagae down to 2 decimal places
average = format(average, ".2f")


# Generate the output summary

output = ("Financial Analysis" + "\n" + "-------------------------" + "\n" +"Total Months: " + str(total_months) + "\n" + "Total: $" + str(total_net) + "\n" + "Average Change: $ " + str(average) + "\n" + "Greatest Increase in profit: " + Gain[0] + " ($" + str(Gain[1]) + ")" + "\n" + "Greatest Decrease in Profits: " + Loss[0] + " ($" + str(Loss[1]) + ")")

# Print the output

print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(str(output))
