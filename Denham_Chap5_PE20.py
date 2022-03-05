######################################################################################
# Developer Name:            Wyatt Denham
# Program Name:              Denham_Chap5B_PE12.py
# Due Date:                  03/04/2022
# Program Description:       This program generates random numbers for a random number
#                            guessing game with the user.
#######################################################################################

import random

play_again = "y"


# Display program info function
#***************************************************************
#  Function:        display_info()
#  Description:     This function displays the project information
#                   before  the program runs.
#  Parameters:      none
#  Returns:         none               
#***************************************************************
def display_info():
    print("==================================================================================")
    print("  Developer Name:            Wyatt Denham")
    print("  Program Name:              Denham_Chap5_PE20.py")
    print("  Due Date:                  03/04/2022")
    print("  Program Description:       This program generates random numbers for a random")
    print("                             number guessing game with the user. ")
    print("==================================================================================")

#***************************************************************
#  Function:        get_random_int()
#  Description:     This function generates a random integer 
#                   between 1-100
#  Parameters:      none
#  Returns:         random.randint(1-100)               
#***************************************************************
def get_random_int():
    return random.randint(1, 100)

#***************************************************************
#  Function:        get_user_guess()
#  Description:     This function  returns the user guess for an
#                   integer 1-100 
#  Parameters:      none
#  Returns:         int(input("Enter a whole number between 1-100, or 0 to quit: "))               
#***************************************************************
def get_user_guess():
    return int(input("Enter a whole number between 1-100, or 0 to quit: "))

#***************************************************************
#  Function:        print_too_low()
#  Description:     This function prints a statement to be used when user 
#                   guess is too low
#  Parameters:      none
#  Returns:         none               
#***************************************************************
def print_too_low():
    print("Too low, guess again")

#***************************************************************
#  Function:        print_too_high()
#  Description:     This function prints a statement to be used when user 
#                   guess is too high
#  Parameters:      none
#  Returns:         none               
#***************************************************************
def print_too_high():
    print("Too high, guess again")

#***************************************************************
#  Function:        print_you_gave_up()
#  Description:     This function prints a statement to be used when user 
#                   quits before guessing the correct number
#  Parameters:      none
#  Returns:         none               
#***************************************************************
def print_you_gave_up():
    print("You gave up too quickly.")

#***************************************************************
#  Function:        print_attempted_guesses()
#  Description:     This function prints attempted guesses total
#                   guess is too high
#  Parameters:      user_attempts
#  Returns:         none               
#***************************************************************
def print_attempted_guesses(user_attempts):
    print("Attempted Guesses: ", user_attempts)

#***************************************************************
#  Function:        print_you_guessed_right
#  Description:     This function prints a statement to be used when user 
#                   guesses the number correctly
#  Parameters:      none
#  Returns:         none               
#***************************************************************
def print_you_guessed_right():
    print("\nCongratulations! You guessed the correct number.")

#***************************************************************
#  Function:        print_correct_number()
#  Description:     This function prints a statement to tell
#                   the user what the correct number is
#  Parameters:      random_int
#  Returns:         none               
#***************************************************************
def print_correct_number(random_int):
    print("The correct number was: ", random_int)

#***************************************************************
#  Function:        ask_to_play_again
#  Description:     This function asks the user if they would like 
#                   to play again. if yes, main function runs.
#  Parameters:      none
#  Returns:         none               
#***************************************************************
def ask_to_play_again():
    playAgain = input("Would you like to play again (y to continue)? ")
    if playAgain == "y":
        main()
    else:
        print("Goodbye.")

#***************************************************************
#  Function:        main
#  Description:     This  is the main function that runs the program
#  Parameters:      none
#  Returns:         none               
#***************************************************************
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


# Main sequence of program
display_info()
main()