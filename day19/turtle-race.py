"""
Random speed 6-turtle race, betting is open
"""

from turtle import Turtle, Screen
from random import randint

colors = ["purple", "blue", "green", "yellow", "orange", "red"]

timmys = []
screen = Screen()
screen.setup(width=500, height=400)


for i in range(6):
    timmys.append(Turtle(shape="turtle"))
    timmys[i].color(colors[i])
    timmys[i].penup()
    timmys[i].goto(-230, 65 - 25*i)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in timmys:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_dist = randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
