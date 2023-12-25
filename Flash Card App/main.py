from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
lang_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    lang_dict = original_data.to_dict(orient="records")
else:
    lang_dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(lang_dict)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    lang_dict.remove(current_card)
    data = pandas.DataFrame(lang_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()




window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


button_right_photo = PhotoImage(file="images/right.png")
button_right = Button(image=button_right_photo, highlightthickness=0, command=is_known)
button_right.grid(column=1, row=1)

button_wrong_photo = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=button_wrong_photo, highlightthickness=0, command=next_card)
button_wrong.grid(column=0, row=1)


next_card()



window.mainloop()