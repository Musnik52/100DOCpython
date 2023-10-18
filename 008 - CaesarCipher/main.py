# def prime_checker(num):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#     print(f"{num} is prime? {is_prime}")


# n = 21
# prime_checker(num=n)

import logo


def caesar(text, shift, action):
    new_word = ""
    for char in text:
        if char in alphabet:
            shift_ammount = shift if action == "encode" else shift * -1
            new_position = alphabet.index(char) + shift_ammount
            if new_position < 0:
                new_position += 26
            elif new_position > 25:
                new_position -= 26
            new_word += alphabet[new_position]
        else:
            new_word += char
    print(new_word)


alphabet = [
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
]
using = True

while using:
    print(logo.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction not in ["encode", "decode"]:
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
        ).lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    retry = input("Want to reuse the app? y / n\n").lower()
    while retry not in ["y", "n"]:
        retry = input("Want to reuse the app? y / n\n").lower()
    using = True if retry == "y" else False
