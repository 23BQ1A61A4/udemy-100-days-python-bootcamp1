# Example Project: Tip Calculator

print("Welcome to the tip calculator!")
#asking for total bill amount in float data type
bill = float(input("What was the total bill? $"))
#details about tip
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
#Splitting the bill amount
num_people = int(input("How many people to split the bill between? "))
# tip and total bill amounts in percentages
tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tip_amount
bill_per_person = total_bill / num_people
# Using f-strings for formatted output:
final_amount = "{:.2f}".format(bill_per_person) #Formats to 2 decimal places.
print(f"Each person should pay: ${final_amount}")
