from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

'''
question_bank=[
    Question(q1,a1),
    Question(q2,a2),
]
'''

question_bank = []

for question in question_data:
    questiontext = question["text"]
    questionanswer = question["answer"]

    new_question= Question(questiontext, questionanswer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")

