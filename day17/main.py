from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    text = i["text"]
    answer = i["answer"]
    new_object = Question(text, answer)
    question_bank.append(new_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You\'ve completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")