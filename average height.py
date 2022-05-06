height = input("yes").split()
for i in range(0,len(height)):
    height[i] = int(height[i])
print(height)
total_height = 0
for n in height:
   total_height += n
print(total_height)
no_of_students = 0
for r in height:
    no_of_students += 1
print(no_of_students)
avg = total_height/no_of_students
print(avg)