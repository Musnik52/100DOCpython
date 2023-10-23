# Welcome to the HigherLower Game.
# You'll be presented with 2 items and your
# goal is to decide if the 2nd item has
# a larger ammount of IG followers than the 1st.

# If you're correct - a new item will be presented,
# for which you'll need to guss if it has
# a higher or lower number of followers, and so on.

# Upon a mistake, the game ands and your streak
# number will be presented

from data import data
from logo import *
import random
import os


def replay():
    print("You're amazing! you've finished the list!" if counter ==
          max_score else f'Game Over! Your streak was: {counter}')
    choice = input("Want to play again? y/n\n").lower()
    while choice not in ["y", "yes", "n", "no"]:
        choice = input("Want to play again? y/n\n").lower()
    return True if choice in ["y", "yes"] else False


def clear():
    os.system('cls')


def msg_format(item):
    return f"{item['name']} - a {item['description'].lower()} from {item['country']}"


def display(item1, item2):
    print(logo)
    print(
        'Compare the following - Who has more followers?\n' if not counter else f'Correct! Streak: {counter}. Next:\n')
    print(f"1: {msg_format(item1)}")
    print(f"followers: {item1['follower_count']}")
    print(vs)
    print(f"2: {msg_format(item2)}\n")


def compare(item1, item2):
    display(item1, item2)
    answers = [item1['follower_count'], item2['follower_count']]
    player_answer = int(input(
        'Who has a bigger number of IG followers? 1 or 2\n'))
    while player_answer not in [1, 2]:
        player_answer = int(input('WRONG INPUT! Choose 1 or 2\n'))
    correct_answer = max(answers[0], answers[1])
    return item2 if answers[player_answer - 1] == correct_answer else 0


playing = True
while playing:
    data_list = data.copy()
    max_score = len(data_list) - 1
    counter = 0
    answering_correct = True
    first_item = data_list.pop(random.randint(0, len(data_list)))

    while answering_correct and counter != (len(data_list) - 1):
        second_item = data_list.pop(random.randint(0, len(data_list)))
        first_item = compare(first_item, second_item)
        clear()
        if not first_item:
            answering_correct = False
        else:
            counter += 1

    playing = replay()
