
"""
Blackjack game
"""

import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

cls = lambda: os.system("cls" if os.name == "nt" else "clear")

def deal_card():
    return random.choice(cards)

def check_for_ace(cards):
    for i in range(len(cards)):
        if cards[i] == 11:
            cards[i] -= 10
            return True
    
    return False

while True:
    if input("Want to play a game of blackjack? [y/n] ") != "y":
        break

    cls()

    player_cards = []
    computer_cards = []
    for i in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    player_sum = sum(player_cards)
    computer_sum = sum(computer_cards)

    if computer_sum == 21:
        print("You lose! Computer has a blackjack!")
        continue
    elif player_sum == 21:
        print("Blackjack! You win!")
        continue

    if computer_sum > 21:
        if check_for_ace(computer_cards):
            computer_sum -= 10

    if player_sum > 21:
        if check_for_ace(player_cards):
            player_sum -= 10

    print(f"Computer's first card: {computer_cards[0]}")

    player_bust = False
    computer_bust = False

    while True:
        print(f"Your cards: {player_cards}, current_score: {player_sum}")

        resp = input("type 'y' to get another card, type 'n' to pass: ")
        if resp != "y":
            break
        
        new_card = deal_card()
        player_cards.append(new_card)
        player_sum += new_card

        if player_sum > 21:
            if check_for_ace(player_cards):
                player_sum -= 10
            else:
                print(f"You draw {new_card}. You bust! You lose!")
                player_bust = True
                break
        
    if player_bust: continue
    

    while computer_sum <= 16:
        print(f"Computer's cards: {computer_cards}, current_score: {computer_sum}")
        new_card = deal_card()
        computer_cards.append(new_card)
        computer_sum += new_card
        
        if computer_sum > 21:
            if check_for_ace(computer_cards):
                computer_sum -= 10
            else:
                print(f"Computer draws {new_card} and busts! You win")
                computer_bust = True
                break

    if computer_bust: continue

    print(f"Your final hand: {player_cards}, final score: {player_sum}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}")

    if computer_sum == player_sum:
        print("It's a draw!")
    elif computer_sum > player_sum:
        print("Computer wins!")
    else:
        print("You win!")
