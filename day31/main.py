"""
Flip card program for learning languages (French)
"""

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")
timer = None
current_card = None


def flip_card():
    global timer, current_card
    window.after_cancel(timer)
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def next_card():
    global timer, current_card
    window.after_cancel(timer)
    canvas.itemconfig(language_text, text="French", fill="black")
    current_card = random.choice(words)
    canvas.itemconfig(word_text, text=current_card['French'], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    timer = window.after(3000, flip_card)


def guessed_word():
    words.remove(current_card)
    next_card()

# ================= UI ==============================================

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# images must be created outside of functions, because the references would be gone
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)

language_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=guessed_word, highlightthickness=0)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card, highlightthickness=0)
wrong_button.grid(row=1, column=1)

timer = window.after(3000, flip_card)
next_card()

window.mainloop()

data = pandas.DataFrame(words)
data.to_csv("data/words_to_learn.csv", index=False)
