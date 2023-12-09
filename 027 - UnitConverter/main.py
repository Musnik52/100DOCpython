# from tkinter import *


# def button_clicked():
#     print("I got clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)


# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)

# #Label
# my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.config(text="New Text")
# my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)

# #Button
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)

# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)

# #Entry
# input = Entry(width=10)
# print(input.get())
# input.grid(column=3, row=2)


# window.mainloop()

from tkinter import *

window = Tk()
window.title("Miles2Kilometers")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)


def button_clicked():
    print(input.get())
    new_text = round(float(input.get()) * 1.609)
    converted_label.config(text=new_text)


input = Entry(width=20)
print(input.get())
input.insert(END, string="0")
input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=50, pady=50)

equal_label = Label(text="is equal to", font=("Arial", 24, "bold"))
equal_label.grid(column=0, row=1)
equal_label.config(padx=50, pady=50)

converted_label = Label(text="0", font=("Arial", 24, "bold"))
converted_label.grid(column=1, row=1)
converted_label.config(padx=50, pady=50)

km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=50, pady=50)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=2)
button.config(padx=50, pady=50)


window.mainloop()
