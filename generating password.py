import random
letters = ['a', 'b', 'c']
numbers = ['0', '1', '2', '3']
symbols = ['!','#','$']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("how many letters to have\n"))
nr_symbols = int(input("\n"))
nr_numbers = int(input("\n"))
password = ''
for char in range(1,nr_letters+1):
    random_char = random.choice(letters)
    print(random_char)
    password += random_char
    print(password)
for char in range(1,nr_numbers+1):
    password += random.choice(numbers)
for char in range(1,nr_symbols+1):
    password += random.choice(symbols)
print(password)