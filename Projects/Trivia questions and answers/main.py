import random

# Trivia questions and answers
trivia_data = [
    {
        'question': 'What is the capital of France?',
        'answer': 'Paris'
    },
    {
        'question': 'Which planet is known as the "Red Planet"?',
        'answer': 'Mars'
    },
    {
        'question': 'Who wrote the play "Romeo and Juliet"?',
        'answer': 'William Shakespeare'
    },
    {
        'question': 'What is the largest mammal in the world?',
        'answer': 'Blue Whale'
    },
    {
        'question': 'What is the chemical symbol for water?',
        'answer': 'H2O'
    }
]

def get_random_question():
    return random.choice(trivia_data)

def ask_question(question):
    user_answer = input(question + ' ')
    return user_answer.strip()

def main():
    print("Welcome to the Trivia Quiz!")
    score = 0
    num_questions = 3  # Change this to set the number of questions you want to ask

    for _ in range(num_questions):
        question_data = get_random_question()
        question = question_data['question']
        correct_answer = question_data['answer']

        user_answer = ask_question(question)
        
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}")

    print(f"\nYou got {score} out of {num_questions} questions correct.")

if __name__ == "__main__":
    main()
