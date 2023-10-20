import random

def difficulty():
    print("Welcome to the guessing game!")
    choice = input("Want to play HARD or EASY?\n").lower()
    while choice not in ["hard", "easy"]:
        choice = input("Want to play HARD or EASY?\n").lower()
    return 5 if choice == "hard" else 10

def replay():
    choice = input("Want to play again? y/n\n").lower()
    while choice not in ["y", "yes", "n", "no"]:
        choice = input("Want to play again? y/n\n").lower()
    return True if choice in ["y", "yes"] else False

attempts = 0
playing = True
while playing:
    guess = 0
    number = random.randint(1, 100)
    attempts = difficulty()
    print(f"{attempts} attempts")
    
    while guess != number and attempts != 0:
        guess = int(input("Try to guess the number: "))
        attempts -= 1
        print(f"Attempts left: {attempts}")
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low...")
    print(
        f"{number} is correct! Attempts left: {attempts}"
        if guess == number
        else "YOU LOSE..."
    )
    
    playing = replay()
