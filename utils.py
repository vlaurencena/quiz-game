# ------------------------------
def display_score(score):
    print(f"Your score is {score}.")
# ------------------------------
def check_answer(answer, question):
    return answer == question["correct"]
# ------------------------------
def print_separator():
    print("-*-*-*-*-*-*-")
# ------------------------------
def get_valid_answer():
    possible_answers = ["A", "B", "C", "D"]
    answer = input("What is your answer?: ").upper()
    while answer not in possible_answers:
        print(f"Invalid answer. Please choose from: {', '.join(possible_answers)}")
        answer = input("What is your answer?: ").upper()
    return answer
# ------------------------------