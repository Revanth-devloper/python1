year = int(input("enter your year: "))
if year%400==0 and year%100==0:
    print("it's a Leap Year")
elif year%4==0 and year%100!=0:
    print("it's a Leap Year")
else:
    print("It's not a Leap Year")