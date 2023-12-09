import pandas

data = pandas.read_csv(r"026 - NatoAB\nato_phonetic_alphabet.csv")
phonetic_dict = {row["letter"]: row["code"] for row, row in data.iterrows()}


def gen_pho():
    word = input("Please entre the word: ").upper()
    try:
        print([phonetic_dict[f"{letter}"] for letter in word])
    except KeyError:
        print("Use Alphabetic Chars, please!")
        gen_pho()


gen_pho()
# print(phonetic_dict)
# {
#     "A": "Alfa",
#     "B": "Bravo",
#     "C": "Charlie",
#     "D": "Delta",
#     "E": "Echo",
#     "F": "Foxtrot",
#     "G": "Golf",
#     "H": "Hotel",
#     "I": "India",
#     "J": "Juliet",
#     "K": "Kilo",
#     "L": "Lima",
#     "M": "Mike",
#     "N": "November",
#     "O": "Oscar",
#     "P": "Papa",
#     "Q": "Quebec",
#     "R": "Romeo",
#     "S": "Sierra",
#     "T": "Tango",
#     "U": "Uniform",
#     "V": "Victor",
#     "W": "Whiskey",
#     "X": "X-ray",
#     "Y": "Yankee",
#     "Z": "Zulu",
# }
