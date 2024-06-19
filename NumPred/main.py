from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too High!")
        return turns - 1
    elif guess < answer:
        print("Too Low!")
        return turns - 1
    else:
        print(f"You Got It! The answer was {answer}.")

#Make Function to check difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'Easy' or 'Hard' : ")
    if level == "Easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #choosing a random number between 1 and 100
    print("Welcome to the NumPred : The Number Guessing Game!")
    print("I'm Thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0
    #Repeat the guessing functionality if they get it wrong.
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user to guess a number
        guess = int(input("Make a Guess : "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've Run out of guesses You Lost!")
            return
        elif guess != answer:
            print("Guess Again!")
game()