import random
nameasCSV = input("give some names")
names = nameasCSV.split(", ")
print(names)
for i in range(4):
    print(random.choice(names))
person_bill = random.choice(names)
print(person_bill + "is going to pay bill")
