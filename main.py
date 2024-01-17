from tkinter import *
import pandas

data_file = pandas.read_csv("data/japanese_data.csv")
data_file.set_index('expression')
new_df = data_file[["expression", "reading", "meaning"]].copy()
print(new_df)
new_df = new_df.to_dict(orient="list")
print(new_df)


def back_slide(meaning):
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(kanji_text, fill="white")
    canvas.itemconfig(kana_text, fill="white")
    print(meaning)
    canvas.itemconfig(meaning_text, text=meaning)


def knows_answer():
    next_question()


def front_slide():
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(kanji_text, fill="black")
    canvas.itemconfig(kana_text, fill="black")
    canvas.itemconfig(meaning_text, text="")


def next_question():
    global timer
    window.after_cancel(timer)
    # Random bir satırı elde etmek için kullanilir
    row = data_file.sample()
    # random_kanji = random.choice(data_file["expression"])
    # random_kana = data_file[data_file["expression"] == random_kanji]["reading"].iloc[0]
    # random_meaning = data_file[data_file["expression"] == random_kanji]["meaning"].iloc[0]
    front_slide()
    canvas.itemconfig(kanji_text, text=row["expression"].iloc[0])
    canvas.itemconfig(kana_text, text=row["reading"].iloc[0])
    timer = window.after(5000, back_slide, row["meaning"].iloc[0])


# -----------------------UI-----------------------------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Japonca Alıştırmalar")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Aninda yok olan
timer = window.after(1, back_slide)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)

tick_image = PhotoImage(file="./images/right.png")
tick_button = Button(width=100, height=100, image=tick_image, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR,
                     command=next_question)
tick_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(width=100, height=100, image=wrong_image, highlightthickness=0, borderwidth=0,
                      bg=BACKGROUND_COLOR, command=next_question)
wrong_button.grid(row=1, column=0)

kanji_text = canvas.create_text(400, 150, text="", font=("Ariel", 40))
kana_text = canvas.create_text(400, 263, text="", font=("Ariel", 60))
meaning_text = canvas.create_text(400, 350, text="deneme", font=("Ariel", 35), fill="white")

next_question()

window.mainloop()
