from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("No More Questions. GAME OVER!")
print(f"Your final score is: {quiz.score} / {len(question_bank)}")

# https://opentdb.com/ # For more questions