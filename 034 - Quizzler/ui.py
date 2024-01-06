from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=FONT, fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quiz_text = self.canvas.create_text(
            150, 125, text="quizzTXT", fill=THEME_COLOR, font=FONT, width=280
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_pic = PhotoImage(file=r"034 - Quizzler\images\true.png")
        self.true_btn = Button(
            image=true_pic, highlightthickness=0, command=self.true_pressed
        )
        self.true_btn.grid(column=0, row=2)
        false_pic = PhotoImage(file=r"034 - Quizzler\images\false.png")
        self.false_btn = Button(
            image=false_pic, highlightthickness=0, command=self.false_pressed
        )
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=text)
        else:
            self.canvas.itemconfig(
                self.quiz_text, text="You've reached the end of the quiz!"
            )
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        self.feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.feedback(self.quiz.check_answer("false"))

    def feedback(self, is_correct):
        feedback_color = "green" if is_correct else "red"
        self.canvas.config(bg=feedback_color)
        self.window.after(1000, self.get_next_question)
