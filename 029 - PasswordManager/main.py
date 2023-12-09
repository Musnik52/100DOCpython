from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def rand_pass():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    pass_letters = [choice(letters) for i in range(randint(7, 9))]
    pass_numbers = [choice(numbers) for i in range(randint(5, 8))]
    pass_symbols = [choice(symbols) for i in range(randint(3, 5))]
    list_password = pass_letters + pass_numbers + pass_symbols
    shuffle(list_password)
    password = "".join(list_password)
    if password_entry.get():
        password_entry.delete(0, "end")
    password_entry.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    is_blank = (
        True
        if not website.strip() or not username.strip() or not password.strip()
        else False
    )
    if is_blank:
        messagebox.showwarning(
            title="Invalid", message="Please do not leave empty fields!"
        )
    else:
        is_ok = messagebox.askokcancel(
            title="Confirm",
            message=f"Website: {website.strip()}\nUsername: {username.strip()}\nPassword: {password.strip()}\nIs it OK to save?",
        )
        if is_ok:
            with open("file.txt", "a") as file:
                file.write(
                    f"{website.strip()} || {username.strip()} || {password.strip()}\n"
                )
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPassMan!")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file=r"029 - PasswordManager\logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

generate_button = Button(text="Generate Password", command=rand_pass)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

website_entry = Entry(width=35)
website_entry.focus()
# website_entry.insert(END, string="Some text to begin with.")
# print(website_entry.get())
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=35)
username_entry.insert(0, string="@gmail.com")
# print(username_entry.get())
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=19)
# password_entry.insert(END, string="Some text to begin with.")
# print(password_entry.get())
password_entry.grid(column=1, row=3)

window.mainloop()
