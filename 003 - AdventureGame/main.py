print(
    '''
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
    '''
)
print("Welcome to the Treasure Journey Game.")
playing = True
while playing:
    print("You wake up in a cave. there are 2 ways in front f you.")
    left_right = input("Do you want to go left or right?\n").lower()
    while left_right not in [
        "right",
        "r",
        "left",
        "l",
    ]:
        left_right = input("INVALID INPUT! - left or right?\n").lower()
    if left_right in ["right", "Right", "RIGHT", "R", "r"]:
        dive_jump = input(
            "You stumbled into a hole that is filling up with water - do you jump or dive?\n"
        ).lower()
        while dive_jump not in [
            "jump",
            "j",
            "dive",
            "d",
        ]:
            dive_jump = input("INVALID INPUT! - jump or dive?\n").lower()
        if dive_jump in ["jump", "Jump", "JUMP", "J", "j"]:
            move_wait = input(
                "You got out and hear a noise coming towards you, do you move or wait?\n"
            ).lower()
            while move_wait not in [
                "move",
                "m",
                "wait",
                "w",
            ]:
                move_wait = input("INVALID INPUT! - move or wait?\n").lower()
            if move_wait in ["move", "m"]:
                print(
                    "You escaped a trap! A boulder rolled by you.\nYou see a treasure chest in the back room."
                )
                break
            else:
                print("You got crushed by a rolling boulder and died.")
                playing = False
        else:
            print("You drowned and died.")
            playing = False
    else:
        print("You fell into a hole and died.")
        playing = False
if playing:
    print("You found the treasure! WINNER!!!")
else:
    print("GAME OVER...")
