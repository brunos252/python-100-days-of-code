"""
Number guessing game 1-100 with 5 or 10 tries.
"""
import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    tries = 10
elif difficulty == "hard":
    tries = 5
else:
    raise Exception("Difficulty should be either easy or hard")

number_to_guess = random.randint(1, 100)

while tries > 0:
    print(f"You have {tries} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    tries -= 1
    if guess == number_to_guess:
        print(f"You got it! The answer was {number_to_guess}")
        break
    elif guess < number_to_guess:
        print("Too Low")
    else:
        print("Too high")

    if tries == 0:
        print("You've run out of guesses, you lose")
    else:
        print("Guess again.")

    