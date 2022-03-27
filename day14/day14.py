from art import logo, vs
from game_data import data
import random
import os

cls = lambda: os.system("cls" if os.name == "nt" else "clear")

def game_state(score=0):
    cls()
    print(logo)

    if score:
        print(f"You're right! Current score: {score}")

    choices = random.sample(data, 2)
    print(f"Compare A: {choices[0]['name']}, a {choices[0]['description']}, from {choices[0]['country']}.")
    print(vs)
    print(f"Compare B: {choices[1]['name']}, a {choices[1]['description']}, from {choices[1]['country']}.")
    pick = input("Who has more followers? Type 'A' or 'B': ")

    has_more = "A" if choices[0]['follower_count'] > choices[1]['follower_count'] else "B"

    if pick == has_more:
        game_state(score + 1)
    else:
        cls()
        print(f"Sorry, that's wrong. Final score: {score}")
        return

game_state()
