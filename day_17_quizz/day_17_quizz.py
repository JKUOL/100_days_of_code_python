# Import the classes and the clear function
from day_17_question_model import Question
from day_17_data import question_data
from day_17_quiz_brain import QuizBrain
from clear_function import clear

# clear terminal
clear()

# Initialize an empty list to hold all the question objects.
question_bank = []

# Loop through each question in the question data.
for element in question_data:
    # Extract the question text from the current element.
    question_text = element['question']
    # Extract the correct answer from the current element.
    question_ans = element['correct_answer']
    # Create a new Question object with the extracted text and answer.
    new_question = Question(question_text,question_ans)
    # Append the new Question object to the question bank list.
    question_bank.append(new_question)

# Create a QuizBrain object with the question bank.
quiz = QuizBrain(question_bank)

# Loop to keep asking questions until there are no more left.
while quiz.still_has_questions():
    # Prompt the next question.
    quiz.next_question()

# Once there are no more questions, print the final score.
print(f"Your final score is {quiz.score}/{quiz.question_number}")