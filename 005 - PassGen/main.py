# for num in range (1,101):
#     if num % 3 == 0:
#         if num % 5 == 0: print('FizzBuzz')
#         else: print('Fizz')
#     elif num % 5 == 0: print('Buzz')
#     else: print(num)

import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for i in range(1, num_letters + 1):
    password += random.choice(letters)
for i in range(1, num_symbols + 1):
    password += random.choice(symbols)
for i in range(1, num_numbers + 1):
    password += random.choice(numbers)
list_password = list(password)
random.shuffle(list_password)
password = "".join(list_password)
print(f"Your Password is: {password}")
