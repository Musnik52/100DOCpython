from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import pyperclip
import json


# ------------------------------- FIND PROFILE ---------------------------------- #
def find():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Invalid", message="No profiles registered, yet.")
    else:
        if website.lower() in data:
            profile = data[website.lower()]
            messagebox.showinfo(
                title=f"{website.title()}",
                message=f"USER: {profile['username']}\nPASSWORD: {profile['password']}",
            )
        else:
            messagebox.showerror(title="Invalid", message="No such profile!")


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
    new_data = {website.lower(): {"username": username.lower(), "password": password}}
    is_blank = (
        True
        if not website.lower().strip()
        or not username.lower().strip()
        or not password.strip()
        else False
    )
    if is_blank:
        messagebox.showwarning(
            title="Invalid", message="Please do not leave empty fields!"
        )
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPassMan!")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file=r"029 & 030 - PasswordManager\logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

generate_button = Button(text="Generate Password", width=14, command=rand_pass)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find)
search_button.grid(column=2, row=1)

website_entry = Entry(width=31)
website_entry.focus()
website_entry.grid(column=1, row=1)

username_entry = Entry(width=49)
username_entry.insert(0, string="@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=31)
password_entry.grid(column=1, row=3)

window.mainloop()
