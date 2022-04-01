import turtle

from extract_colors import extract
from turtle import Turtle, Screen

colors = extract("Hirst_dots.png")

timmy = Turtle()
timmy.speed(100)
turtle.colormode(255)

for i in range(100):
    timmy.pendown()
    timmy.dot(20, colors[i % len(colors)])
    timmy.penup()
    timmy.forward(40)

    if i % 10 == 9:
        timmy.left(90)
        timmy.forward(40)
        timmy.left(90)
        timmy.forward(400)
        timmy.left(180)

screen = Screen()
screen.exitonclick()
