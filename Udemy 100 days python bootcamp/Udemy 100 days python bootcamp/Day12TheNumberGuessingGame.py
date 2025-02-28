# ASCII logo for the game
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

from random import randint  # Import randint function to generate a random number

# Constants for difficulty levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1  # Reduce the remaining turns by 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1  # Reduce the remaining turns by 1
    else:
        print(f"You got it! The answer was {actual_answer}")
        return 0  # User won, no more turns needed

# Function to set difficulty level
def set_difficulty():
    """Asks user for difficulty level and returns the number of turns."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid choice, defaulting to 'easy' mode.")
        return EASY_LEVEL_TURNS

# Main game function
def game():
    """Runs the number guessing game."""
    print(logo)  # Display game logo
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)  # Generate a random number between 1 and 100
    # Uncomment below for debugging (it shows the correct answer)
    # print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()  # Get number of turns based on difficulty

    guess = None  # Initialize guess variable
    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")

        try:
            guess = int(input("Make a guess: "))  # Convert input to integer
        except ValueError:  # Handle non-integer inputs
            print("Invalid input! Please enter a number.")
            continue

        turns = check_answer(guess, answer, turns)  # Compare guess with answer

        if turns == 0 and guess != answer:  # If no turns left and guess is incorrect
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

# Start the game
game()
