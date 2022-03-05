#######################################################################################
# Developer Name:            Wyatt Denham
# Program Name:              Denham_Chap5B_PE12.py
# Due Date:                  03/04/2022
# Program Description:       This program generates random numbers for a random number
#                            guessing game with the user.
#######################################################################################

import random

play_again = "y"


# Display program info function
def display_info():
    print("==================================================================================")
    print("  Developer Name:            Wyatt Denham")
    print("  Program Name:              Denham_Chap5_PE20.py")
    print("  Due Date:                  03/04/2022")
    print("  Program Description:       This program generates random numbers for a random")
    print("                             number guessing game with the user. ")
    print("==================================================================================")


def get_random_int():
    return random.randint(1, 100)


def get_user_guess():
    return int(input("Enter a whole number between 1-100, or 0 to quit: "))


def print_too_low():
    print("Too low, guess again")


def print_too_high():
    print("Too high, guess again")


def print_you_gave_up():
    print("You gave up too quickly.")


def print_attempted_guesses(user_attempts):
    print("Attempted Guesses: ", user_attempts)


def print_you_guessed_right():
    print("\nCongratulations! You guessed the correct number.")


def print_correct_number(random_int):
    print("The correct number was: ", random_int)


def ask_to_play_again():
    playAgain = input("Would you like to play again (y to continue)? ")
    if playAgain == "y":
        main()
    else:
        print("Goodbye.")


def main():
    random_int = get_random_int()
    user_guess = get_user_guess()
    attempts = 0

    while user_guess != random_int and user_guess != 0:
        if user_guess > random_int:
            print_too_high()
            attempts += 1
            user_guess = get_user_guess()
        else:
            print_too_low()
            attempts += 1
            user_guess = get_user_guess()

    if user_guess == 0:
        attempts += 1
        print_you_gave_up()
        print_correct_number(random_int)
        print_attempted_guesses(attempts)

    if user_guess == random_int:
        attempts += 1
        print_you_guessed_right()
        print_correct_number(random_int)
        print_attempted_guesses(attempts)

    ask_to_play_again()


# Main sequence
display_info()
main()
