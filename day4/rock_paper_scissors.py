"""
Rock-paper-scissors game against computer
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

mapping = {0: rock, 1: paper, 2: scissors}

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

print("You chose:\n" + mapping[user_choice])

computer_choice = random.randint(0, 2)

print("Computer chose:\n" + mapping[computer_choice])

if user_choice == computer_choice:
    print("Draw")
elif (user_choice + 1) % 3 == computer_choice:
    print("You Lose")
else:
    print("You Win")
