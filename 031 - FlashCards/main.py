from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import pandas
import pyperclip
import json


BACKGROUND_COLOR = "#B1DDC6"


def next_word():
    global current_word, timer
    window.after_cancel(timer)
    current_word = choice(words_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front)
    timer = window.after(3000, change_card)


def change_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back)


def remove_word():
    words_dict.remove(current_word)
    data = pandas.DataFrame(words_dict)
    data.to_csv(r"031 - FlashCards\data\words_to_learn.csv", index=False)
    next_word()


window = Tk()
window.title("FlashFrench!")
window.minsize(width=900, height=626)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    data = pandas.read_csv(r"031 - FlashCards\data\words_to_learn.csv")

except FileNotFoundError:
    data = pandas.read_csv(r"031 - FlashCards\data\french_words.csv")
    data.to_csv(r"031 - FlashCards\data\words_to_learn.csv", index=False)

finally:
    words_dict = data.to_dict(orient="records")
    current_word = {}
    timer = window.after(3000, change_card)

    canvas = Canvas(width=800, height=526)
    card_front = PhotoImage(file=r"031 - FlashCards\images\card_front.png")
    card_back = PhotoImage(file=r"031 - FlashCards\images\card_back.png")
    card_bg = canvas.create_image(400, 263, image=card_front)
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
    card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)

    right = PhotoImage(file=r"031 - FlashCards\images\right.png")
    wrong = PhotoImage(file=r"031 - FlashCards\images\wrong.png")
    button_right = Button(image=right, highlightthickness=0, command=remove_word)
    button_wrong = Button(image=wrong, highlightthickness=0, command=next_word)
    button_right.grid(column=1, row=1)
    button_wrong.grid(column=0, row=1)

next_word()

window.mainloop()
