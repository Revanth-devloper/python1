print("Welcome to the love calculator")
name1 = input("Enter name")
name2 = input("enter name")
combine = name1+name2
lower_case = combine.lower()
t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
true = t + r + u + e
l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
love = l+o+v+e
love_score = str(true)+ str(love)
love_score = int(love_score)
print(love_score)
if love_score < 10 or love_score > 90:
    print(f"your score is{love_score},you go together like coke and mentos.")
elif 40<love_score<50:
    print(f"You score is{love_score},You are alright together.")
else:
    print(f"Your score is{love_score}")

