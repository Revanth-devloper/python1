import random

user_choice = int(input("what do you choose?Type 0 for rock,1 for Paper or 2 for scissors.\n"))
computer_choice = random.randint(0, 2)
print(f"comp chose{computer_choice}")
if user_choice>=3 or user_choice <0:
    print("you typed an invalid no")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")
elif computer_choice == user_choice:
    print("its draw")
elif computer_choice > user_choice:
    print("you lose")
elif user_choice> computer_choice:
    print("you win")