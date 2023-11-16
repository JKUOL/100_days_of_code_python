# Print a welcome message for the user
print("Welcome to the tip calculator")

# Get the total bill amount from the user and convert it to a float
bill = float(input("What was the total bill?\n"))

# Get the number of people to split the bill and convert it to an integer
ppl = int(input("How many people to split the bill?\n"))

# Get the tip percentage the user wishes to give and convert it to a float
tipp = float(input("What percentage tip would you like to give?\n"))

# Calculate the base amount per person by dividing the total bill by the number of people
pp = bill / ppl

# Calculate the final amount each person needs to pay including the tip
# The tip is calculated as a percentage of the base amount and then added to it
fin_amount = round(pp + pp * (tipp / 100), 2)

# Print the final amount each person should pay
print(f"Each person should pay: {fin_amount}")



