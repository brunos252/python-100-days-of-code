############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
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
