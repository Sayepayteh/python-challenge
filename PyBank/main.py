# Open csv file
file = open('Resources/budget_data.csv', 'r')

# Set File Contents
content = file.read()

#close file
file.close()

# Split the content into lines
lines = content.splitlines()

total_months = 0
total_amount = 0

last_period = 0

total_average_change = 0
number_of_change = 0

greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""

# Iterate over each line
for line in lines:
    if not line.startswith("Date"): 
        total_months = total_months + 1

        split_line = line.split(",")

        profit_losses = int(split_line[1])
        total_amount = total_amount + profit_losses

        if last_period != 0:
            changes = (profit_losses - last_period)

            total_average_change = total_average_change + changes
            number_of_change = number_of_change + 1

            if changes > greatest_increase:
                greatest_increase = changes
                greatest_increase_month = split_line[0]

            if changes < greatest_decrease:
                greatest_decrease = changes
                greatest_decrease_month = split_line[0]


        last_period = profit_losses

average_change = total_average_change/number_of_change

print("Financial Analysis \n")
print("----------------------\n")

print("Total Months: " + str(total_months))
print("Total: $" + str(total_amount))
print("Average Change: $" + str(round(average_change, 2)))
print("Greatest Increase in Profits: " + greatest_increase_month + " $" + str(greatest_increase))
print("Greatest Decrease in Profits: " + greatest_decrease_month + " $" + str(greatest_decrease))

new_file = open("analysis/results.txt", "w")


new_file.write("Financial Analysis \n")
new_file.write("----------------------\n")

new_file.write("Total Months: " + str(total_months))
new_file.write("Total: $" + str(total_amount))
new_file.write("Average Change: $" + str(round(average_change, 2)))
new_file.write("Greatest Increase in Profits: " + greatest_increase_month + " $" + str(greatest_increase))
new_file.write("Greatest Decrease in Profits: " + greatest_decrease_month + " $" + str(greatest_decrease))

#close new_file
new_file.close()