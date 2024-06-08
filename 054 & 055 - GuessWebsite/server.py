from flask import Flask
import random

app = Flask(__name__)
number = random.randint(0, 9)


@app.route("/")
def intro():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHAyaGRnazI4N2VlM3cxNGVxMmFuemgzMXJrbXlxcGE0Z2V6eGZ5NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Rs2QPsshsFI9zeT4Kn/giphy.gif">'
    )


@app.route("/<int:guess>")
def check(guess):
    return (
        "<h1>correct</h1>"
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
        if guess == number
        else (
            "<h1>Too low!</h1>"
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
            if guess < number
            else "<h1>Too high!</h1>"
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
        )
    )


if __name__ == "__main__":
    app.run(debug=True)
