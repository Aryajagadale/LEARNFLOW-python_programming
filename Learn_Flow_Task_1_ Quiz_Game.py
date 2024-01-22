#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

# Quiz data structure
quiz_questions = {
    "easy": [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct_answer": "4"
        },
        {
            "question": "Which of the following is a primary color?",
            "options": ["Green", "Orange", "Red", "Purple"],
            "correct_answer": "Red"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            "correct_answer": "Blue Whale"
        },
    ],
    "medium": [
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Mars", "Jupiter", "Venus", "Saturn"],
            "correct_answer": "Mars"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
            "correct_answer": "William Shakespeare"
        },
        {
            "question": "In which year did World War II end?",
            "options": ["1943", "1945", "1947", "1950"],
            "correct_answer": "1945"
        },
        {
            "question": "What is the currency of Japan?",
            "options": ["Yuan", "Won", "Yen", "Ringgit"],
            "correct_answer": "Yen"
        },
    ],
    "hard": [
        {
            "question": "What is the capital of Mongolia?",
            "options": ["Ulaanbaatar", "Astana", "Kuala Lumpur", "Manila"],
            "correct_answer": "Ulaanbaatar"
        },
        {
            "question": "In which year did the French Revolution begin?",
            "options": ["1776", "1789", "1801", "1820"],
            "correct_answer": "1789"
        },
        {
            "question": "What is the chemical symbol for the element gold?",
            "options": ["Au", "Ag", "Fe", "Cu"],
            "correct_answer": "Au"
        },
        {
            "question": "Who is the author of 'The Catcher in the Rye'?",
            "options": ["J.D. Salinger", "F. Scott Fitzgerald", "Ernest Hemingway", "George Orwell"],
            "correct_answer": "J.D. Salinger"
        },
    ],
}



def quiz_game(difficulty):
    questions = quiz_questions[difficulty]
    random.shuffle(questions)  # Shuffle the questions for variety

    score = 0

    for idx, question_data in enumerate(questions, start=1):
        print(f"\nQuestion {idx}: {question_data['question']}")

        # Display answer choices
        for i, option in enumerate(question_data['options'], start=1):
            print(f"{i}. {option}")

        # Get user's answer
        user_answer = input("Your answer (enter the corresponding number): ").strip()

        # Check the answer
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question_data['options']):
            user_answer = question_data['options'][int(user_answer) - 1]
            if user_answer == question_data['correct_answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {question_data['correct_answer']}")
        else:
            print("Invalid input. Please enter a valid number.")

    print(f"\nQuiz complete! Your score is: {score}/{len(questions)}")

if __name__ == "__main__":
    print("Welcome to the Quiz Game!")

    # Choose difficulty level
    difficulty_level = input("Choose difficulty (easy/medium/hard): ").lower()

    if difficulty_level in quiz_questions:
        quiz_game(difficulty_level)
    else:
        print("Invalid difficulty level. Please choose from easy, medium, or hard.")


# In[ ]:




