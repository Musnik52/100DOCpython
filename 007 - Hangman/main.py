import random
import words
import hangman
import logo

wrong_letters = []
lives_remaining = len(hangman.stages) - 1
word = random.choice(words.words_list)
displayed_word = list("_" * len(word))
playing = True
print(logo.logo)

while playing:
    print(
        f"\nThe word is: {displayed_word}\n{hangman.stages[lives_remaining]}\n Wrong letters: {wrong_letters}\n"
    )

    letter = input("Try to guess a letter.\n").lower()
    while (
        len(letter.strip()) != 1 or letter in wrong_letters or letter in displayed_word
    ):
        letter = input("Try to guess a NEW and SINGLE letter!\n")

    for i, char in enumerate(word):
        if char == letter:
            displayed_word[i] = letter
        elif i == len(word) - 1 and letter not in displayed_word:
            lives_remaining -= 1
            wrong_letters.append(letter)

        if "_" not in displayed_word or lives_remaining == 0:
            winner = True if "_" not in displayed_word else False
            playing = False

print(word)
print("WINNER!" if winner else f"{hangman.stages[lives_remaining]}\nYou lose...")
