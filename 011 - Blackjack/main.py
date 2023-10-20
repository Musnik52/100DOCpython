## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import logo
import random


def random_card():
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card_list)

def ace_change(cards, player):
    if sum(cards) > 21 and 11 in cards:
        location = cards.index(11)
        cards[location] = 1
    print(f"{player}'s hand: {cards}")


def player_turn(cards):
    hit_me = input("Want to take another card? y/n\n")
    while hit_me not in ["y", "yes", "n", "no"]:
        hit_me = input("Want to take another card? y/n y/n\n").lower()
    if hit_me in ["y", "yes"]:
        cards.append(random_card())
        return hit_me


def replay():
    choice = input("Want to play again? y/n\n").lower()
    while choice not in ["y", "yes", "n", "no"]:
        choice = input("Want to play again? y/n\n").lower()
    return True if choice in ["y", "yes"] else False


playing = True
print(logo.logo)
while playing:
    print("#" * 50)
    drawing_card = True
    player_cards = [random_card(), random_card()]
    player_value = sum(player_cards)
    dealer_cards = [random_card()]
    dealer_value = sum(dealer_cards)
    player_playing = player_value < 21
    print(f"Player's cards: {player_cards}")
    print(f"Dealer's cards: {dealer_cards}")

    while player_playing:
        hit_me = player_turn(player_cards)
        ace_change(player_cards, "Player")
        player_value = sum(player_cards)
        player_playing = True if player_value < 21 and hit_me in ["y", "yes"] else False

    if player_value == 21:
        print(f"Player wins! You scored 21")
    elif player_value > 21:
        print(f"Player BUST: {player_value} - Dealer Wins!")
    else:
        while dealer_value < 17:
            dealer_cards.append(random_card())
            ace_change(dealer_cards, "Dealer")
            dealer_value = sum(dealer_cards)
        if dealer_value == 21:
            print(f"Dealer wins! Dealer scored 21")
        elif dealer_value > 21:
            print(f"Dealer BUST: {dealer_value} - Player Wins!")
        elif dealer_value > player_value:
            print(f"Dealer wins: {dealer_value} > {player_value}")
        elif player_value > dealer_value:
            print(f"Player wins: {player_value} > {dealer_value}")
        else:
            print(f"DRAW! {player_cards} = {dealer_cards} = {player_value}")

    playing = replay()
