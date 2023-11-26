
# Define a class Question to store information about a quiz question.
class Question:
    # Initialize method to create a new Question object with text and answer.
    def __init__(self, q_text, q_answer):
        self.text = q_text  # Assign the provided question text to the object.
        self.answer = q_answer  # Assign the provided answer to the object.
