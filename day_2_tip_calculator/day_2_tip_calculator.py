print("Welcome to the tip calculator")
bill = float(input("What was the total bill?\n"))
ppl = int(input("How many people to split the bill?\n"))
tipp = float(input("What percentage tip would you like to give?\n"))

pp = bill/ppl
fin_amount = round(pp + pp * (float(tipp)/100), 2)

print(f"Each person should pay: {fin_amount}")


