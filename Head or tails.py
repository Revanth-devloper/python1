import random
test_seed = int(input("enter an number"))
random.seed(test_seed)
random_side = random.randint(0, 1)
if random_side == 1:
    print("tails")
else:
    print("heads")