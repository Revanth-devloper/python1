print("Welcome to the tip calculator")
bill = float(input("What was the total bill?"))
tip = int(input("how much tip do you want to give? 10, 12, or 15?"))
people = int(input("how many want to split the the bill: "))
total_bill = int(tip/100*bill + bill)
print(total_bill)