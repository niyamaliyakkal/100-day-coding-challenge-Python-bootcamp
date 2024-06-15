
print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?$"))
tip=float(input("How much tip would you like to give?\n10, 12, or 15?"))
split=float(input("How many people to split the bill?"))
total= (bill+(bill*(tip/100)))/split
print(f"Each person should pay:${(round(total, 2)) }")
