"""
Hangman game
"""
import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
print(logo)

display = []
lives = 6

for letter in chosen_word:
    display.append("_")

guessed = set()

while "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("Already guessed that!")
        continue

    guessed.add(guess)

    if guess in display:
        print("Already guessed that!")

    letter_guessed = False
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            letter_guessed = True
            display[i] = guess

    if not letter_guessed:
        lives -= 1

    print(''.join(display))

    print(stages[lives])

    if lives == 0:
        print("You lose")
        break

if lives > 0:
    print("You win!")
