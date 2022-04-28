height = float(input("Enter your Weight in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight/height*height)
print(bmi)
if bmi == 18.5:
    print("underweight")
elif 18.5 < bmi < 25:
    print("normal weight")
elif 25 < bmi < 30:
    print("overweight")
elif 30 < bmi < 35:
    print("obese")
else:
    print("clinically obese")



