from tkinter import *
import pandas
import random
import os
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CREATE FLASH CARDS ------------------------------- #

current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    try:
        data = pandas.read_csv("words_to_learn.csv")
    except FileNotFoundError:
        data = pandas.read_csv("data/french_words.csv")

    to_learn = data.to_dict(orient="records")
    current_card = random.choice(to_learn)
    french_word = current_card['French']
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- FLIP FLASH CARDS ------------------------------- #


def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")

# ---------------------------- PROGRESS SAVING ------------------------------- #


try:
    words_data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    french_list = original_data["French"].to_list()
    english_list = original_data["English"].to_list()
else:
    french_list = words_data["French"].to_list()
    english_list = words_data["English"].to_list()

words_to_learn = pandas.DataFrame({
    "French": french_list,
    "English": english_list,
})


def save_progress():
    next_card()
    global current_card
    french_list.remove(current_card["French"])
    english_list.remove(current_card["English"])
    global words_to_learn
    words_to_learn = pandas.DataFrame({
        "French": french_list,
        "English": english_list,
    })
    words_to_learn.to_csv("words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=save_progress)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
