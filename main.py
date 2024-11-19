from questions import questions
from utils import *
import random
import time

# -------------------
def new_game():
    # INITIAL SETUP
    current_score = 0
    total_questions = 10
    random.shuffle(questions) # randomize questions
    selected_questions = questions[:total_questions] # select 10 questions

    # START THE GAME
    for current_question, question in enumerate(selected_questions, start=1):
        print(f"QUESTION {current_question}/{total_questions}")
        print(question["question"])

        for choice in question["choices"]:
            print(choice)

        print_separator()

        answer = get_valid_answer()

        if check_answer(answer, question):
            print("You are right!")
            current_score += 1
        else:
            print(f"You are wrong! The correct answer is {question['correct']}.")

        display_score(current_score)
        print_separator()
        time.sleep(1)

    # GAME ENDED
    print(f"Thanks for playing! Your final score is {current_score}.")
    play_again()

def play_again():
    play = input("\nDo you want to play again? (yes/no): ").lower()
    while play not in ['yes', 'no']:
        print("Type a correct answer: yes or no?")
        play = input("\nDo you want to play again? (yes/no): ").lower()
    if play == "yes":
        new_game()  # Restart the game
    else:
        print("Thanks for playing! Goodbye!")

new_game()