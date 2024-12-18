import random
def game():
    print("Welcome to the number guessing game!")
    print("i'm thinking of a number between 1- 100")
    answer = random.randint(1, 100)

    def check_ans(guessed_ans, actual_ans):
        if guessed_ans>actual_ans:
            return "Too high"
        elif guessed_ans<actual_ans:
            return "Too low"
        else:
            return "You won!"


    easy_level = 10
    hard_level = 5
    def set_diff():
        set_difff = input("Choose a difficulty. Type 'easy' or 'hard':")
        if set_difff == "hard":
            return "fYou have {hard_level} attempts to guess the number"
        else:
            return "You have 10 attempts to guess the number"

    print(set_diff())
    guess = 0
    while guess != answer:
        guess = int(input("Guess the number:"))
        print(check_ans(guess, answer))





