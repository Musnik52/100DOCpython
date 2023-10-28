class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.q_num = 0
        self.q_list = q_list

    def still_has_questions(self):
        return self.q_num < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_num]
        self.q_num += 1
        answer_given = input(f"Q{self.q_num}: {current_question.text} (True/False): ")
        print(self.check_answer(current_question.answer, answer_given))
        print(f"{self.score} / {self.q_num}\n")

    def check_answer(self, real_answer, user_answer):
        if user_answer.lower() == real_answer.lower():
            self.score += 1
            return "Correct!!!"
        return f"Incorrect - the right answer is: {real_answer}"
