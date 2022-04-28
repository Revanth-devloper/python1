size = input("what size yu want to have small,medium,large_pizza")
pepperoni = input("Y or N")
chesse = input("Y or N")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if chesse == "Y":
    bill += 1
print(f"your final bill is:{bill}")
