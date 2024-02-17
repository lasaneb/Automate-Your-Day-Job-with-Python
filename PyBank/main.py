# %%
#Initial Imports
import pandas as pd
import csv
from pathlib import Path

# %%
# Files to load and output 
file_to_load = Path("/Users/xbook/Desktop/FinTechRepos/GitHub/PyBank - Python/PyBank/Resources/budget_data.csv")
file_to_output = Path("/Users/xbook/Desktop/FinTechRepos/GitHub/Pybank - Python/Pybank/Final Results.txt")


# %%
# Read the CSV into a dataframe using Pandas and print the first 5 rows
budget_df = pd.read_csv(file_to_load)
budget_df.head()

# %%
# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0 


# %%
#Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# %%
# Calculate the Average Net Change
net_monthly_avg = round(sum(net_change_list) / len(net_change_list),2)

# %%
# Export the results as text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Final Results\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average  Change: ${net_monthly_avg}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")


