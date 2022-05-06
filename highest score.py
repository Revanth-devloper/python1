score = input("yes").split()
for i in range(0,len(score)):
    score[i] = int(score[i])
print(score)
highest_score = 0
for n in score:
    if n > highest_score:
     highest_score = n
print(highest_score)