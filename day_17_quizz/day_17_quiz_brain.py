# Class to manage quiz game logic.
class QuizBrain:
    # Constructor that initializes the quiz with a list of questions, a question number, and a score.
    def __init__(self, q_list):
        self.question_number = 0  # Tracks the current question number.
        self.question_list = q_list  # List of question objects.
        self.score = 0  # Tracks the score of correctly answered questions.

    # Method to check if there are more questions left in the quiz.
    def still_has_questions(self):
        return self.question_number < len(self.question_list)  # Returns True if more questions remain.

    # Method to display the next question to the user and prompt for an answer.
    def next_question(self):
        current_question = self.question_list[self.question_number]  # Get the current question.
        self.question_number += 1  # Increment the question number.
        # Prompt the user for an answer and display the question number and text.
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # Check if the user's answer is correct.
        self.check_answer(user_answer, current_question.answer)

    # Method to check if the user's answer is correct, print a message, and update the score.
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():  # Convert answers to lowercase and compare.
            print("You got it right!")  # Inform the user their answer is correct.
            self.score += 1  # Increment the score for a correct answer.
        else:
            print("That's wrong")  # Inform the user their answer is incorrect.
        # Print the correct answer and the user's current score.
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")  # Print a newline for spacing.
