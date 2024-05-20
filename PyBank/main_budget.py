import csv

# Initialize variables
total_months = 0
net_total = 0
changes = []
previous_profit = None
greatest_increase = {'date': None, 'amount': float('-inf')}
greatest_decrease = {'date': None, 'amount': float('inf')}

# Read the CSV file
with open('PyBank/Resources/budget_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        date, profit = row
        profit = int(profit)

        # Count the number of months
        total_months += 1

        # Calculate the net total amount of "Profit/Losses"
        net_total += profit

        # Calculate the changes in "Profit/Losses"
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)

            # Find the greatest increase in profits
            if change > greatest_increase['amount']:
                greatest_increase['amount'] = change
                greatest_increase['date'] = date

            # Find the greatest decrease in profits
            if change < greatest_decrease['amount']:
                greatest_decrease['amount'] = change
                greatest_decrease['date'] = date

        previous_profit = profit

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else 0

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
