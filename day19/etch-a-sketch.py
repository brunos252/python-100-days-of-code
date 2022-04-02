"""
sketchy project
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.speed(100)


def move_forwards():
    tim.forward(5)


def move_backwards():
    tim.back(5)


def rotate_left():
    tim.left(10)


def rotate_right():
    tim.right(10)


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="a", fun=rotate_left)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=rotate_right)
screen.onkeypress(key="c", fun=tim.clear)
screen.exitonclick()
