# line1 = ["o", "o", "o"]
# line2 = ["o", "o", "o"]
# line3 = ["o", "o", "o"]
# map = [line1, line2, line3]
# position = input("Where to go? first digit for the row, second digit for column.\n")
# while (
#     len(position) != 2
#     or position[0] not in ["1", "2", "3"]
#     or position[1] not in ["1", "2", "3"]
# ):
#     position = input(
#         "INVALID! Enter first digit for the row, second digit for column.\n"
#     )
# row_index = int(position[0]) - 1
# column_index = int(position[1]) - 1
# map[row_index][column_index] = "X"

# updated_layout = f"{line1}\n{line2}\n{line3}"
# print(updated_layout)

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
options = [rock, paper, scissors]
print("Welcome to another RPS challenge!")
player_choice = input("CHOOSE:\n1 -ROCK\n2 - PAPER\n3 - SCISSORS\n")
while player_choice not in ["1", "2", "3"]:
    player_choice = input("INVALID!\nCHOOSE:\n1 -ROCK\n2 - PAPER\n3 - SCISSORS\n")
bot_choice = random.randint(0, 2)
print(f"PLAYER:{options[int(player_choice) - 1]}\n")
print(f"COMPUTER:{options[bot_choice]}\n")
if player_choice == bot_choice:
    print("DRAW.")
elif (
    (player_choice == 0 and bot_choice == 1)
    or (player_choice == 1 and bot_choice == 2)
    or (player_choice == 2 and bot_choice == 0)
):
    print("You lost...")
else:
    print("WINNER!!!")
